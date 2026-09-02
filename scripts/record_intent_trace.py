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
TRACES = ROOT / "traces"


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
    if not isinstance(data, dict):
        raise SystemExit("trace root must be an object")
    return data


def intake(args: argparse.Namespace) -> None:
    path = trace_path(args.intent_id)
    if path.exists():
        raise SystemExit(f"trace already exists: {path.relative_to(ROOT)}")
    data = {
        "schema_version": 1,
        "intent_id": args.intent_id,
        "status": args.status,
        "trace_completeness": "complete",
        "request": {
            "raw": {"status": "recorded", "value": args.raw},
            "normalized_query": {"status": "recorded", "value": args.query},
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
    data["events"].append({"type": "execution", "at": timestamp(args.at), "context_pack": args.context_pack, "evidence_paths": args.evidence, "searches": args.search, "note": args.note})
    data["next_decision"] = {"status": args.decision_status, "value": args.next_decision}
    write_atomic(path, data)


def dispatcher_handoff(args: argparse.Namespace) -> None:
    """Record dispatcher custody before the delegated executor starts work."""
    path = trace_path(args.intent_id)
    data = load(path)
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
    for evidence_path, label in ((args.red_report_path, "Red evidence"), (args.remote_proof_path, "remote proof")):
        if not (ROOT / evidence_path).is_file():
            raise SystemExit(f"{label} path must name an existing file: {evidence_path}")
    data["events"].append({"type": "archive", "at": timestamp(args.at), "report_path": args.report_path, "evidence_paths": args.evidence + [args.report_path, args.red_report_path, args.remote_proof_path], "verification": {"red_status": "pass", "red_report_path": args.red_report_path, "remote_verified": "pass", "remote_proof_path": args.remote_proof_path}})
    data["artifacts"].extend({"label": label, "path": path} for label, path in (item.split("=", 1) for item in args.artifact))
    data["verifications"].extend(({"label": "Red verification evidence", "path": args.red_report_path, "status": "pass"}, {"label": "Remote verification evidence", "path": args.remote_proof_path, "status": "pass"}))
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
    p.add_argument("--context-pack", required=True); p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--status", choices=("inbox", "active", "waiting"), default="inbox")
    p.add_argument("--next-decision", required=True); p.set_defaults(func=intake)
    p = commands.add_parser("execution", parents=[common])
    p.add_argument("--context-pack", required=True); p.add_argument("--evidence", action="append", required=True)
    p.add_argument("--search", action="append", required=True); p.add_argument("--note", default="")
    p.add_argument("--status", choices=("active", "waiting"), default="active")
    p.add_argument("--decision-status", default="in_progress"); p.add_argument("--next-decision", required=True); p.set_defaults(func=execution)
    p = commands.add_parser("dispatcher-handoff", parents=[common])
    p.add_argument("--run-id", required=True); p.add_argument("--canonical-sha", required=True)
    p.add_argument("--agent", default="genie"); p.add_argument("--session-key", default="agent:genie:infinity-dispatcher")
    p.set_defaults(func=dispatcher_handoff)
    p = commands.add_parser("archive", parents=[common])
    p.add_argument("--report-path", required=True); p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--artifact", action="append", default=[], metavar="LABEL=PATH")
    p.add_argument("--red-report-path", required=True); p.add_argument("--remote-proof-path", required=True)
    p.add_argument("--decision-status", default="implemented"); p.add_argument("--next-decision", required=True); p.set_defaults(func=archive)
    return top


if __name__ == "__main__":
    args = parser().parse_args()
    args.func(args)
