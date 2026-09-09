#!/usr/bin/env python3
"""Normalize a pre-contract trace without inventing missing intake facts."""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def when(event: dict) -> str:
    return event.get("at") or event.get("timestamp") or "1970-01-01T00:00:00Z"


def main() -> int:
    intent_id = sys.argv[1]
    path = ROOT / "traces" / f"{intent_id}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    context = f"intents/context/{intent_id}.json"
    if not (ROOT / context).is_file():
        raise SystemExit(f"missing context pack: {context}")

    request = data.get("request") if isinstance(data.get("request"), dict) else {}
    raw = request.get("raw") if isinstance(request.get("raw"), dict) else None
    query = request.get("normalized_query") if isinstance(request.get("normalized_query"), dict) else None
    missing = {"status": "missing", "reason": "legacy trace predates the capture contract; original intake value was not recoverable."}
    events = [event for event in data.get("events", []) if isinstance(event, dict)]
    intake = next((event for event in events if event.get("type") == "intake"), None)
    intake_at = when(intake or {})
    normalized = [{"type": "intake", "at": intake_at, "context_pack": context, "evidence_paths": ["INTENTS.md"]}]
    for event in events:
        if event is intake or event.get("type") == "archive":
            continue
        event_at = when(event)
        if event.get("type") == "dispatcher_handoff":
            normalized.append({key: event[key] for key in ("type", "run_id", "canonical_sha", "agent", "session_key", "timestamp", "status") if key in event})
        else:
            normalized.append({"type": "backfill", "at": event_at, "note": event.get("summary", event.get("type", "legacy event")), "source_type": event.get("type", "unknown")})
    archive = next((event for event in events if event.get("type") == "archive"), None)
    if archive:
        normalized.append(archive)
    normalized.sort(key=when)
    data = {
        "schema_version": 1,
        "intent_id": intent_id,
        "status": "archived" if archive else data.get("status", "waiting"),
        "trace_completeness": "partial",
        "request": {"raw": raw if raw and raw.get("status") == "recorded" else missing, "normalized_query": query if query and query.get("status") == "recorded" else missing},
        "events": normalized,
        "artifacts": data.get("artifacts", []) if isinstance(data.get("artifacts"), list) else [],
        "verifications": data.get("verifications", []) if isinstance(data.get("verifications"), list) else [],
        "next_decision": data.get("next_decision") if isinstance(data.get("next_decision"), dict) else {"status": "archived", "value": "legacy trace normalized for archive verification"},
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
