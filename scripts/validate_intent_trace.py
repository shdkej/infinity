#!/usr/bin/env python3
"""Validate durable Infinity intent trace records without third-party deps."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VALID_STATES = {"inbox", "active", "waiting", "archived"}
VALID_EVENTS = {"intake", "execution", "archive", "backfill", "dispatcher_handoff"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def error(errors: list[str], trace: Path, message: str) -> None:
    errors.append(f"{trace}: {message}")


def parse_time(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
        return parsed if parsed.tzinfo is not None else None
    except ValueError:
        return None


def valid_capture(value: object) -> bool:
    if not isinstance(value, dict) or value.get("status") not in {"recorded", "missing"}:
        return False
    if value["status"] == "recorded":
        return isinstance(value.get("value"), str) and bool(value["value"].strip())
    return isinstance(value.get("reason"), str) and bool(value["reason"].strip())


def local_path_ok(value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    return (ROOT / value).is_file()


def non_empty_strings(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )


def validate(trace: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(trace.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{trace}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{trace}: root must be an object"]
    if data.get("schema_version") != 1:
        error(errors, trace, "schema_version must be 1")
    intent_id = data.get("intent_id")
    if not isinstance(intent_id, str) or trace.stem != intent_id:
        error(errors, trace, "intent_id must match filename")
    status = data.get("status")
    if status not in VALID_STATES:
        error(errors, trace, "status must be inbox, active, waiting, or archived")
    completeness = data.get("trace_completeness")
    if completeness not in {"complete", "partial"}:
        error(errors, trace, "trace_completeness must be complete or partial")
    request = data.get("request")
    if not isinstance(request, dict):
        error(errors, trace, "request must be an object")
    else:
        for key in ("raw", "normalized_query"):
            if not valid_capture(request.get(key)):
                error(errors, trace, f"request.{key} must be recorded value or missing reason")
        if completeness == "complete" and any(request.get(k, {}).get("status") != "recorded" for k in ("raw", "normalized_query") if isinstance(request.get(k), dict)):
            error(errors, trace, "complete trace cannot have missing request fields")
    events = data.get("events")
    if not isinstance(events, list) or not events:
        error(errors, trace, "events must be a non-empty list")
        events = []
    prior: datetime | None = None
    types: list[str] = []
    for index, event in enumerate(events):
        if not isinstance(event, dict) or event.get("type") not in VALID_EVENTS:
            error(errors, trace, f"events[{index}] has invalid type")
            continue
        types.append(event["type"])
        time_key = "timestamp" if event.get("type") == "dispatcher_handoff" else "at"
        at = parse_time(event.get(time_key))
        if not at:
            error(errors, trace, f"events[{index}].{time_key} must be ISO-8601 UTC")
        elif prior and at < prior:
            error(errors, trace, "events must be chronological")
        if at:
            prior = at
        if event["type"] == "intake" and not local_path_ok(event.get("context_pack")):
            error(errors, trace, f"events[{index}].context_pack must name an existing file")
        for path in event.get("evidence_paths", []):
            if not local_path_ok(path):
                error(errors, trace, f"events[{index}] missing evidence path: {path}")
    if types.count("intake") != 1:
        error(errors, trace, "exactly one intake event is required")
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            continue
        if event.get("type") == "execution":
            if not local_path_ok(event.get("context_pack")):
                error(errors, trace, f"events[{index}].context_pack must name an existing file")
            if not non_empty_strings(event.get("evidence_paths")):
                error(errors, trace, f"events[{index}].evidence_paths must be a non-empty list")
            if not non_empty_strings(event.get("searches")):
                error(errors, trace, f"events[{index}].searches must be a non-empty list")
        if event.get("type") == "archive":
            if not local_path_ok(event.get("report_path")):
                error(errors, trace, f"events[{index}].report_path must name an existing final report")
            verification = event.get("verification")
            if not isinstance(verification, dict) or verification.get("red_status") != "pass":
                error(errors, trace, f"events[{index}].verification.red_status must be pass")
            if not isinstance(verification, dict) or verification.get("remote_verified") != "pass":
                error(errors, trace, f"events[{index}].verification.remote_verified must be pass")
            if completeness == "complete" and (not isinstance(verification, dict) or not local_path_ok(verification.get("red_report_path"))):
                error(errors, trace, f"events[{index}].verification.red_report_path must name Red evidence")
            if completeness == "complete" and (not isinstance(verification, dict) or not local_path_ok(verification.get("remote_proof_path"))):
                error(errors, trace, f"events[{index}].verification.remote_proof_path must name remote proof")
        if event.get("type") == "dispatcher_handoff":
            required = ("run_id", "canonical_sha", "agent", "session_key")
            if any(not isinstance(event.get(key), str) or not event[key].strip() for key in required):
                error(errors, trace, f"events[{index}] dispatcher_handoff needs run_id, canonical_sha, agent, and session_key")
            if event.get("status") != "accepted":
                error(errors, trace, f"events[{index}].status must be accepted")
            if not isinstance(event.get("canonical_sha"), str) or not SHA40.fullmatch(event["canonical_sha"]):
                error(errors, trace, f"events[{index}].canonical_sha must be a 40-character lowercase SHA")
    if status == "archived" and types.count("archive") != 1:
        error(errors, trace, "archived trace requires exactly one archive event")
    if status != "archived" and "archive" in types:
        error(errors, trace, "non-archived trace cannot include archive event")
    for group in ("artifacts", "verifications"):
        values = data.get(group)
        if not isinstance(values, list):
            error(errors, trace, f"{group} must be a list")
            continue
        for entry in values:
            if not isinstance(entry, dict) or not isinstance(entry.get("label"), str):
                error(errors, trace, f"{group} entries need label")
            elif "path" in entry and not local_path_ok(entry["path"]):
                error(errors, trace, f"{group} references missing path: {entry['path']}")
    decision = data.get("next_decision")
    if not isinstance(decision, dict) or not isinstance(decision.get("status"), str) or not isinstance(decision.get("value"), str):
        error(errors, trace, "next_decision needs status and value")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("trace", nargs="?", type=Path)
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    traces = sorted((ROOT / "traces").glob("*.json")) if args.all else [args.trace]
    if not args.all and args.trace is None:
        parser.error("trace or --all is required")
    errors: list[str] = []
    for trace in traces:
        errors.extend(validate(trace if trace.is_absolute() else ROOT / trace))
    if errors:
        print("TRACE VALIDATION FAILED", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"TRACE VALIDATION PASSED ({len(traces)} trace(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
