#!/usr/bin/env python3
"""Write the durable intake/execution/archive events used by Infinity cards.

This is intentionally local-only: callers pass paths relative to the Infinity
repository and then run the validator before committing the ledger update.
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACES = ROOT / "data" / "traces"


def timestamp(value: str | None) -> str:
    if value:
        return value
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def trace_path(intent_id: str) -> Path:
    if not intent_id or "/" in intent_id or ".." in intent_id:
        raise SystemExit("intent id must be a simple trace filename")
    return TRACES / f"{intent_id}.json"


def write_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def load(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"trace does not exist: {path.relative_to(ROOT)}")
    if isinstance(data, list):
        # Early dispatcher versions wrote a bare handoff list.  Leaving that
        # shape in place turns an agent-owned archive receipt into a false
        # Waiting state because the trace tool cannot append an archive event.
        events = []
        for item in data:
            if not isinstance(item, dict):
                continue
            event = dict(item)
            if "event" in event:
                event["type"] = event.pop("event")
            events.append(event)
        data = {
            "schema_version": 1,
            "intent_id": path.stem,
            "status": "active",
            "trace_completeness": "partial",
            "backfill_source": "dispatcher_missing_trace",
            "request": {
                "raw": {"status": "missing", "reason": "legacy dispatcher trace omitted intake request"},
                "normalized_query": {"status": "missing", "reason": "legacy dispatcher trace omitted normalized query"},
                "user_intent": {"status": "missing", "reason": "legacy dispatcher trace omitted user intent"},
                "desired_outcome": {"status": "missing", "reason": "legacy dispatcher trace omitted desired outcome"},
                "out_of_scope": {"status": "missing", "reason": "legacy dispatcher trace omitted out-of-scope boundary"},
                "success_evidence": {"status": "missing", "reason": "legacy dispatcher trace omitted success evidence"},
            },
            "events": events,
            "artifacts": [],
            "verifications": [],
            "next_decision": {"status": "in_progress", "value": "legacy trace normalized for agent-owned closeout"},
        }
    if not isinstance(data, dict):
        raise SystemExit("trace root must be an object or legacy event list")
    data.setdefault("schema_version", 1)
    data.setdefault("intent_id", path.stem)
    data.setdefault("status", "active")
    data.setdefault("trace_completeness", "partial")
    data.setdefault("request", {
        "raw": {"status": "missing", "reason": "legacy trace omitted intake request"},
        "normalized_query": {"status": "missing", "reason": "legacy trace omitted normalized query"},
        "user_intent": {"status": "missing", "reason": "legacy trace omitted user intent"},
        "desired_outcome": {"status": "missing", "reason": "legacy trace omitted desired outcome"},
        "out_of_scope": {"status": "missing", "reason": "legacy trace omitted out-of-scope boundary"},
        "success_evidence": {"status": "missing", "reason": "legacy trace omitted success evidence"},
    })
    data.setdefault("artifacts", [])
    data.setdefault("verifications", [])
    data.setdefault("next_decision", {"status": "in_progress", "value": "legacy trace normalized for agent-owned closeout"})
    normalized = []
    for event in data.get("events", []):
        if not isinstance(event, dict):
            continue
        event = dict(event)
        if "event" in event:
            event["type"] = event.pop("event")
        # Task-level events predate the durable trace schema.  A backfill is
        # intentionally lossless enough for chronology but never pretends to
        # be a fresh execution evidence record.
        if event.get("type") not in {"intake", "execution", "archive", "backfill", "dispatcher_handoff"}:
            event["type"] = "backfill"
        if event.get("type") == "backfill" and "at" not in event and event.get("timestamp"):
            event["at"] = event["timestamp"]
        normalized.append(event)
    if not any(event.get("type") == "intake" for event in normalized):
        # A handoff-only record proves neither the original request nor a
        # Context Pack.  Do not manufacture the conventional filename: it
        # might not exist and would make the recovery record look complete.
        first_at = next((event.get("timestamp") or event.get("at") for event in normalized if event.get("timestamp") or event.get("at")), "1970-01-01T00:00:00Z")
        data["trace_completeness"] = "partial"
        data["backfill_source"] = "dispatcher_missing_trace"
        normalized.insert(0, {
            "type": "intake",
            "at": first_at,
            "context_pack": "",
            "context_pack_status": "missing",
            "context_pack_reason": "legacy dispatcher trace omitted intake context pack",
            "evidence_paths": [],
        })
    data["events"] = normalized
    return data


def intake(args: argparse.Namespace) -> None:
    path = trace_path(args.intent_id)
    if path.exists():
        raise SystemExit(f"trace already exists: {path.relative_to(ROOT)}")
    data = {
        "schema_version": 2,
        "intent_id": args.intent_id,
        "status": args.status,
        "trace_completeness": "complete",
        "request": {
            "raw": {"status": "recorded", "value": args.raw},
            "normalized_query": {"status": "recorded", "value": args.query},
            "user_intent": {"status": "recorded", "value": args.user_intent},
            "desired_outcome": {"status": "recorded", "value": args.desired_outcome},
            "out_of_scope": {"status": "recorded", "value": args.out_of_scope},
            "success_evidence": {"status": "recorded", "value": args.success_evidence},
        },
        "events": [{"type": "intake", "at": timestamp(args.at), "context_pack": args.context_pack, "evidence_paths": args.evidence}],
        "artifacts": [],
        "verifications": [],
        "next_decision": {"status": "in_progress", "value": args.next_decision},
    }
    write_atomic(path, data)


def execution(args: argparse.Namespace) -> None:
    path = trace_path(args.intent_id)
    data = load(path)
    data["status"] = args.status
    data["events"].append({"type": "execution", "at": timestamp(args.at), "context_pack": args.context_pack, "evidence_paths": args.evidence, "searches": args.search, "wiki_pages": args.wiki_page, "operational_log_sections": args.operational_log, "note": args.note})
    data["next_decision"] = {"status": args.decision_status, "value": args.next_decision}
    write_atomic(path, data)


def role_review(args: argparse.Namespace) -> None:
    """Record Planner/Developer/Marketer/Operator role evidence for L3."""
    path = trace_path(args.intent_id)
    data = load(path)
    data.setdefault("verifications", []).append({
        "label": "workflow role review",
        "type": "role_review",
        "at": timestamp(args.at),
        "roles": args.role,
        "evidence_paths": args.evidence,
        "status": args.status,
        "next_role": args.next_role or None,
    })
    write_atomic(path, data)


def dispatcher_handoff(args: argparse.Namespace) -> None:
    """Record dispatcher custody before the delegated executor starts work."""
    path = trace_path(args.intent_id)
    # An older or manually-created Inbox card can legitimately predate its
    # trace.  Dispatcher custody must remain durable in that case: failing
    # here aborts the whole cycle before the executor can repair the card.
    # Create an explicitly partial backfill rather than pretending the intake
    # request was captured.
    if path.exists():
        data = load(path)
    else:
        data = {
            "schema_version": 2,
            "intent_id": args.intent_id,
            "status": "active",
            "trace_completeness": "partial",
            "backfill_source": "dispatcher_missing_trace",
            "request": {
                "raw": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
                "normalized_query": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
                "user_intent": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
                "desired_outcome": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
                "out_of_scope": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
                "success_evidence": {"status": "missing", "reason": "dispatcher backfill: intake trace was absent"},
            },
            "events": [{
                "type": "intake",
                "at": timestamp(args.at),
                "context_pack": "",
                "context_pack_status": "missing",
                "context_pack_reason": "dispatcher backfill: intake context pack was absent",
                "evidence_paths": [],
            }],
            "artifacts": [],
            "verifications": [],
            "next_decision": {"status": "in_progress", "value": "dispatcher created partial trace before executor handoff"},
        }
    event = {
        "type": "dispatcher_handoff",
        "run_id": args.run_id,
        "canonical_sha": args.canonical_sha,
        "agent": args.agent,
        "session_key": args.session_key,
        "timestamp": timestamp(args.at),
        "status": "accepted",
    }
    if any(existing == event for existing in data.get("events", []) if isinstance(existing, dict)):
        return
    data.setdefault("events", []).append(event)
    write_atomic(path, data)


def archive(args: argparse.Namespace) -> None:
    path = trace_path(args.intent_id)
    data = load(path)
    if any(event.get("type") == "archive" for event in data.get("events", []) if isinstance(event, dict)):
        raise SystemExit("archive event already exists")
    data["status"] = "archived"
    evidence = [(args.remote_proof_path, "remote proof")]
    if args.research_mode != "exploratory_research":
        evidence.insert(0, (args.red_report_path, "Red evidence"))
    for evidence_path, label in evidence:
        if not (ROOT / evidence_path).is_file():
            raise SystemExit(f"{label} path must name an existing file: {evidence_path}")
    verification = {"red_status": "not_required" if args.research_mode == "exploratory_research" else "pass", "remote_verified": "pass", "remote_proof_path": args.remote_proof_path}
    if args.research_mode != "exploratory_research":
        verification["red_report_path"] = args.red_report_path
    evidence_paths = args.evidence + [args.report_path, args.remote_proof_path]
    if args.research_mode != "exploratory_research":
        evidence_paths.append(args.red_report_path)
    data["events"].append({"type": "archive", "at": timestamp(args.at), "report_path": args.report_path, "evidence_paths": evidence_paths, "research_mode": args.research_mode, "verification": verification})
    # Older traces predate the top-level artifact/verification arrays.  Keep
    # terminalization backward-compatible instead of failing after the remote
    # archive transition has already been proven.
    data.setdefault("artifacts", []).extend(
        {"label": label, "path": path} for label, path in (item.split("=", 1) for item in args.artifact)
    )
    verifications = [{"label": "Remote verification evidence", "path": args.remote_proof_path, "status": "pass"}]
    if args.research_mode != "exploratory_research":
        verifications.insert(0, {"label": "Red verification evidence", "path": args.red_report_path, "status": "pass"})
    data.setdefault("verifications", []).extend(verifications)
    data["next_decision"] = {"status": args.decision_status, "value": args.next_decision}
    write_atomic(path, data)


def parser() -> argparse.ArgumentParser:
    top = argparse.ArgumentParser(description=__doc__)
    commands = top.add_subparsers(required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--intent-id", required=True)
    common.add_argument("--at")
    p = commands.add_parser("intake", parents=[common])
    p.add_argument("--raw", required=True); p.add_argument("--query", required=True)
    p.add_argument("--user-intent", required=True, help="사용자가 이 작업으로 이루려는 목적")
    p.add_argument("--desired-outcome", required=True, help="사용자가 받아야 하는 결과")
    p.add_argument("--out-of-scope", required=True, help="이번 작업에서 하지 않을 범위")
    p.add_argument("--success-evidence", required=True, help="성공을 판정할 직접 증거")
    p.add_argument("--context-pack", required=True); p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--status", choices=("inbox", "active", "waiting"), default="inbox")
    p.add_argument("--next-decision", required=True); p.set_defaults(func=intake)
    p = commands.add_parser("execution", parents=[common])
    p.add_argument("--context-pack", required=True); p.add_argument("--evidence", action="append", required=True)
    p.add_argument("--search", action="append", required=True); p.add_argument("--wiki-page", action="append", default=[]); p.add_argument("--operational-log", action="append", default=[]); p.add_argument("--note", default="")
    p.add_argument("--status", choices=("active", "waiting"), default="active")
    p.add_argument("--decision-status", default="in_progress"); p.add_argument("--next-decision", required=True); p.set_defaults(func=execution)
    p = commands.add_parser("role-review", parents=[common])
    p.add_argument("--role", action="append", required=True, choices=("planner", "developer", "marketer", "operator"))
    p.add_argument("--evidence", action="append", required=True)
    p.add_argument("--status", choices=("pass", "warn", "blocked"), default="pass")
    p.add_argument("--next-role", default="")
    p.set_defaults(func=role_review)
    p = commands.add_parser("dispatcher-handoff", parents=[common])
    p.add_argument("--run-id", required=True); p.add_argument("--canonical-sha", required=True)
    p.add_argument("--agent", default="genie"); p.add_argument("--session-key", default="agent:genie:infinity-dispatcher")
    p.set_defaults(func=dispatcher_handoff)
    p = commands.add_parser("archive", parents=[common])
    p.add_argument("--report-path", required=True); p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--artifact", action="append", default=[], metavar="LABEL=PATH")
    p.add_argument("--red-report-path", default=""); p.add_argument("--remote-proof-path", required=True)
    p.add_argument("--research-mode", choices=("exploratory_research", "decision_research"), default="exploratory_research")
    p.add_argument("--decision-status", default="implemented"); p.add_argument("--next-decision", required=True); p.set_defaults(func=archive)
    return top


if __name__ == "__main__":
    args = parser().parse_args()
    args.func(args)
