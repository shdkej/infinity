#!/usr/bin/env python3
"""Execute validated Infinity commands emitted by an AI planner.

The planner may be expansive: assumptions, alternatives, dissent, questions and
evidence are preserved in the plan. Only the small, registered command surface
can mutate Infinity state.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import re
from pathlib import Path
from typing import Any

import yaml

from intent_registry import append_archive, find_open, load_registry, normalize_entry, save_registry

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_LAB = ROOT.parent
CONTEXT_PACK_BUILDER = KNOWLEDGE_LAB / "scripts" / "build_context_pack.py"
TRACE_WRITER = ROOT / "scripts" / "record_intent_trace.py"
REGISTRY = ROOT / "data" / "command-registry.yaml"
RUN_LOG = ROOT / "data" / "command-runs.jsonl"
LANES = ("inbox", "active", "waiting")
ROLES = ("planner", "developer", "marketer", "operator")
SAFE_ID = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)+$")
PERMISSION_RANK = {"L0": 0, "L1": 1, "L2": 2, "L3": 3}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_commands() -> dict[str, Any]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    if data.get("version") != 1 or not isinstance(data.get("commands"), dict):
        raise ValueError("invalid command registry")
    return data["commands"]


def load_runs() -> dict[str, dict[str, Any]]:
    if not RUN_LOG.exists():
        return {}
    result = {}
    for line in RUN_LOG.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            result[str(item["command_id"])] = item
    return result


def validate_plan(plan: dict[str, Any], commands: dict[str, Any]) -> list[str]:
    errors = []
    if plan.get("version") != 1:
        errors.append("plan.version must be 1")
    plan_intent_id = str(plan.get("intent_id") or "").strip()
    if not plan_intent_id:
        errors.append("plan.intent_id is required")
    elif not SAFE_ID.fullmatch(plan_intent_id):
        errors.append("plan.intent_id must be a safe kebab-case id")
    if not isinstance(plan.get("judgment"), dict):
        errors.append("plan.judgment is required; AI reasoning belongs here")
    if not isinstance(plan.get("commands"), list) or not plan["commands"]:
        errors.append("plan.commands must be a non-empty list")
    plan_permission = str(plan.get("permission", "L1")).upper()
    if plan_permission not in PERMISSION_RANK:
        errors.append("plan.permission must be L0, L1, L2 or L3")
    seen_command_ids: set[str] = set()
    for index, command in enumerate(plan.get("commands", [])):
        name = command.get("name") if isinstance(command, dict) else None
        spec = commands.get(name or "")
        if not spec:
            errors.append(f"commands[{index}]: unregistered command {name!r}")
            continue
        command_id = str(command.get("command_id") or "").strip()
        if not command_id:
            errors.append(f"commands[{index}]: command_id is required")
        elif command_id in seen_command_ids:
            errors.append(f"commands[{index}]: duplicate command_id {command_id!r} in plan")
        else:
            seen_command_ids.add(command_id)
        required_permission = str(spec.get("permission", "L3")).upper()
        if plan_permission in PERMISSION_RANK and required_permission in PERMISSION_RANK and PERMISSION_RANK[required_permission] > PERMISSION_RANK[plan_permission]:
            errors.append(f"commands[{index}]: {name} requires {required_permission}, plan allows {plan_permission}")
        args = command.get("args") or {}
        for field in spec.get("required", []):
            if field not in args or args[field] in (None, "", []):
                errors.append(f"commands[{index}]: missing args.{field}")
        if "intent_id" in args and not SAFE_ID.fullmatch(str(args["intent_id"])):
            errors.append(f"commands[{index}]: args.intent_id must be a safe kebab-case id")
    return errors


def intent_register(args: dict[str, Any]) -> dict[str, Any]:
    data = load_registry()
    intent_id = str(args["intent_id"])
    if not SAFE_ID.fullmatch(intent_id):
        raise ValueError("intent_id must be a safe kebab-case id")
    if find_open(data, intent_id):
        return {"status": "noop", "reason": "already_open", "intent_id": intent_id}
    item = normalize_entry({
        "id": intent_id, "title": args["title"], "task_name": args["task_name"],
        "goal": args["goal"], "user_intent": args["user_intent"],
        "desired_outcome": args["desired_outcome"], "out_of_scope": args["out_of_scope"],
        "success_evidence": args["success_evidence"],
        "status": "inbox", "target_agent": args.get("target_agent", "genie"),
        "priority": args.get("priority", "normal"), "projects": args.get("projects", []),
        "task_type": args.get("task_type", "implementation"),
        "ai_judgment": args.get("ai_judgment", {}),
        "notification_channel": args.get("notification_channel", "slack"),
        "notification_target": args.get("notification_target", ""),
    }, "inbox")
    data["lanes"]["inbox"].append(item)
    save_registry(data)
    return {"status": "changed", "intent_id": intent_id, "lane": "inbox"}


def intent_move(args: dict[str, Any]) -> dict[str, Any]:
    data = load_registry()
    intent_id, source, target = str(args["intent_id"]), args["from_lane"], args["to_lane"]
    if source not in LANES or target not in LANES:
        raise ValueError("from_lane and to_lane must be inbox, active or waiting")
    found = find_open(data, intent_id)
    if not found:
        raise ValueError(f"intent not open: {intent_id}")
    actual_source, item = found
    if actual_source != source:
        raise ValueError(f"intent is in {actual_source}, not {source}")
    data["lanes"][source] = [x for x in data["lanes"][source] if x.get("id") != intent_id]
    moved = normalize_entry(dict(item), target)
    moved["transitioned_at"] = now()
    if args.get("reason"):
        moved["transition_reason"] = args["reason"]
    data["lanes"][target].append(moved)
    save_registry(data)
    return {"status": "changed", "intent_id": intent_id, "from": source, "to": target}


def intent_archive(args: dict[str, Any]) -> dict[str, Any]:
    data = load_registry()
    found = find_open(data, str(args["intent_id"]))
    if not found:
        return {"status": "noop", "reason": "already_archived_or_missing", "intent_id": args["intent_id"]}
    lane, item = found
    data["lanes"][lane] = [x for x in data["lanes"][lane] if x.get("id") != args["intent_id"]]
    item = dict(item)
    item.update({"status": "archived", "completed_at": args.get("completed_at", now()), "archive_reason": args["reason"]})
    save_registry(data)
    archive_path = append_archive(item)
    return {"status": "changed", "intent_id": args["intent_id"], "archive": str(archive_path.relative_to(ROOT))}


def role_fanout(args: dict[str, Any]) -> dict[str, Any]:
    if not SAFE_ID.fullmatch(str(args["intent_id"])):
        raise ValueError("intent_id must be a safe kebab-case id")
    roles = args.get("roles", list(ROLES))
    if tuple(roles) != ROLES:
        raise ValueError(f"role.fanout requires exactly {ROLES} in order")
    contract = args["shared_contract"]
    if not isinstance(contract, dict) or not contract.get("goal") or not contract.get("success_evidence"):
        raise ValueError("shared_contract requires goal and success_evidence")
    path = ROOT / "artifacts" / str(args["intent_id"]) / "work" / "role-fanout.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"version": 1, "intent_id": args["intent_id"], "mode": "parallel", "roles": list(roles), "shared_contract": contract, "created_at": now()}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "changed", "artifact": str(path.relative_to(ROOT)), "roles": list(roles), "mode": "parallel"}


def trace_record(args: dict[str, Any]) -> dict[str, Any]:
    if not SAFE_ID.fullmatch(str(args["intent_id"])):
        raise ValueError("intent_id must be a safe kebab-case id")
    path = ROOT / "data" / "traces" / f"{args['intent_id']}.json"
    payload = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"version": 1, "intent_id": args["intent_id"], "events": []}
    payload.setdefault("events", []).append({"type": args["event"], "at": now(), "data": args.get("data", {})})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "changed", "trace": str(path.relative_to(ROOT)), "event": args["event"]}


def safe_repo_path(value: str, *, required_prefix: str) -> Path:
    """Resolve a command path without allowing writes outside Infinity."""
    candidate = Path(str(value))
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError("path must be relative and stay inside Infinity")
    if not str(candidate).startswith(required_prefix):
        raise ValueError(f"path must be under {required_prefix}")
    return ROOT / candidate


def context_pack_build(args: dict[str, Any]) -> dict[str, Any]:
    intent_id = str(args["intent_id"])
    if not SAFE_ID.fullmatch(intent_id):
        raise ValueError("intent_id must be a safe kebab-case id")
    output = safe_repo_path(str(args["output_path"]), required_prefix="intents/context/")
    output.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        [sys.executable, str(CONTEXT_PACK_BUILDER), "--route", str(args["route"]), "--request", str(args["request"]), "--output", str(output)],
        cwd=KNOWLEDGE_LAB, text=True, capture_output=True,
    )
    if completed.returncode:
        detail = (completed.stdout or completed.stderr).strip()
        raise RuntimeError(f"context pack build failed: {detail}")
    payload = json.loads(output.read_text(encoding="utf-8"))
    preflight = payload.get("preflight", {})
    selected_paths = [item.get("path") for item in payload.get("selected_context", []) if item.get("path")]
    return {
        "status": "changed", "context_pack": str(output.relative_to(ROOT)),
        "tool": preflight.get("tool"), "query": preflight.get("query"),
        "result_count": preflight.get("result_count", 0), "selected_paths": selected_paths,
    }


def trace_execution_record(args: dict[str, Any]) -> dict[str, Any]:
    intent_id = str(args["intent_id"])
    if not SAFE_ID.fullmatch(intent_id):
        raise ValueError("intent_id must be a safe kebab-case id")
    context_pack = safe_repo_path(str(args["context_pack"]), required_prefix="intents/context/")
    if not context_pack.is_file():
        raise ValueError(f"context pack does not exist: {args['context_pack']}")
    command = [sys.executable, str(TRACE_WRITER), "execution", "--intent-id", intent_id,
               "--context-pack", str(args["context_pack"]), "--next-decision", str(args["next_decision"])]
    for value in args["evidence_paths"]: command += ["--evidence", str(value)]
    for value in args["searches"]: command += ["--search", str(value)]
    for value in args.get("wiki_pages", []): command += ["--wiki-page", str(value)]
    for value in args.get("operational_log_sections", []): command += ["--operational-log", str(value)]
    if args.get("note"): command += ["--note", str(args["note"])]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if completed.returncode:
        raise RuntimeError(f"trace execution record failed: {(completed.stderr or completed.stdout).strip()}")
    return {"status": "changed", "trace": f"data/traces/{intent_id}.json", "context_pack": str(args["context_pack"]), "searches": args["searches"], "wiki_pages": args.get("wiki_pages", []), "evidence_paths": args["evidence_paths"]}


def git_verify(_: dict[str, Any]) -> dict[str, Any]:
    local = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    remote = subprocess.check_output(["git", "ls-remote", "origin", "refs/heads/main"], cwd=ROOT, text=True).split()[0]
    return {"status": "pass" if local == remote else "fail", "local_sha": local, "remote_sha": remote}


HANDLERS = {"intent_register": intent_register, "intent_move": intent_move, "intent_archive": intent_archive, "role_fanout": role_fanout, "trace_record": trace_record, "context_pack_build": context_pack_build, "trace_execution_record": trace_execution_record, "git_verify": git_verify}


def run(plan: dict[str, Any], apply: bool) -> dict[str, Any]:
    commands = load_commands()
    errors = validate_plan(plan, commands)
    if errors:
        return {"status": "rejected", "errors": errors}
    prior = load_runs()
    results = []
    for command in plan["commands"]:
        command_id = command["command_id"]
        if command_id in prior:
            results.append({"command_id": command_id, "status": "noop", "reason": "already_run"})
            continue
        if not apply:
            results.append({"command_id": command_id, "status": "dry_run", "name": command["name"]})
            continue
        result = HANDLERS[commands[command["name"]]["handler"]](command.get("args") or {})
        record = {"command_id": command_id, "name": command["name"], "at": now(), "result": result}
        RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
        with RUN_LOG.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        results.append({"command_id": command_id, **result})
    return {"status": "pass", "intent_id": plan["intent_id"], "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", nargs="?", help="JSON plan path; stdin when omitted")
    parser.add_argument("--apply", action="store_true", help="apply commands; default is validation/dry-run")
    args = parser.parse_args()
    raw = Path(args.plan).read_text(encoding="utf-8") if args.plan else sys.stdin.read()
    result = run(json.loads(raw), args.apply)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"pass", "dry_run"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
