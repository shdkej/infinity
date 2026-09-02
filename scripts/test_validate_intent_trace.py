#!/usr/bin/env python3
"""Controlled validator fixtures for the trace contract."""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate_intent_trace.py")
spec = importlib.util.spec_from_file_location("trace_validator", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)

writer_spec = importlib.util.spec_from_file_location("trace_writer", Path(__file__).with_name("record_intent_trace.py"))
writer = importlib.util.module_from_spec(writer_spec)
assert writer_spec.loader
writer_spec.loader.exec_module(writer)


def record(status: str = "active") -> dict:
    events = [{"type": "intake", "at": "2026-09-02T00:00:00Z", "context_pack": "intents/context/infinity-trace-contract-01.json"}]
    events.append({"type": "execution", "at": "2026-09-02T00:00:30Z", "context_pack": "intents/context/infinity-trace-contract-01.json", "evidence_paths": ["README.md"], "searches": ["fixture search"]})
    if status == "archived":
        events.append({"type": "archive", "at": "2026-09-02T00:01:00Z", "report_path": "README.md", "verification": {"red_status": "pass", "red_report_path": "README.md", "remote_verified": "pass", "remote_proof_path": "README.md"}})
    return {"schema_version": 1, "intent_id": "fixture", "status": status, "trace_completeness": "complete", "request": {"raw": {"status": "recorded", "value": "raw"}, "normalized_query": {"status": "recorded", "value": "query"}}, "events": events, "artifacts": [], "verifications": [], "next_decision": {"status": "continue", "value": "next"}}


def run_case(name: str, data: dict, expected_ok: bool) -> None:
    with tempfile.TemporaryDirectory() as directory:
        trace = Path(directory) / "fixture.json"
        trace.write_text(json.dumps(data), encoding="utf-8")
        errors = validator.validate(trace)
        assert bool(errors) is not expected_ok, f"{name}: {errors}"
    print(f"PASS {name}")


run_case("active-valid", record(), True)
run_case("archive-valid", record("archived"), True)
broken = record("archived")
broken["events"] = broken["events"][:-1]
run_case("archive-requires-event", broken, False)
duplicate = record()
duplicate["events"].insert(1, duplicate["events"][0].copy())
run_case("exactly-one-intake", duplicate, False)
execution_missing_search = record()
execution_missing_search["events"][1].pop("searches")
run_case("execution-needs-context-search-evidence", execution_missing_search, False)
archive_missing_proof = record("archived")
archive_missing_proof["events"][-1]["verification"].pop("remote_verified")
run_case("archive-needs-report-and-remote-proof", archive_missing_proof, False)
archive_missing_evidence = record("archived")
archive_missing_evidence["events"][-1]["verification"].pop("red_report_path")
run_case("archive-pass-needs-red-evidence", archive_missing_evidence, False)
try:
    writer.parser().parse_args(["archive", "--intent-id", "fixture", "--report-path", "README.md", "--next-decision", "next"])
except SystemExit as exc:
    assert exc.code == 2
else:
    raise AssertionError("archive writer accepted a pass without evidence paths")
print("PASS archive-writer-requires-evidence-paths")
legacy = record("archived")
legacy["trace_completeness"] = "partial"
legacy["request"]["raw"] = {"status": "missing", "reason": "no original intake record"}
run_case("legacy-missing-is-explicit", legacy, True)
handoff = record()
handoff["events"].append({"type": "dispatcher_handoff", "timestamp": "2026-09-02T00:00:45Z", "run_id": "dispatch-fixture", "canonical_sha": "a" * 40, "agent": "genie", "session_key": "agent:genie:test", "status": "accepted"})
run_case("dispatcher-handoff-is-auditable", handoff, True)
naive_handoff = record()
naive_handoff["events"].append({"type": "dispatcher_handoff", "timestamp": "2026-09-02T00:00:45", "run_id": "dispatch-fixture", "canonical_sha": "a" * 40, "agent": "genie", "session_key": "agent:genie:test", "status": "accepted"})
run_case("dispatcher-handoff-rejects-naive-time", naive_handoff, False)
invalid_sha_handoff = record()
invalid_sha_handoff["events"].append({"type": "dispatcher_handoff", "timestamp": "2026-09-02T00:00:45Z", "run_id": "dispatch-fixture", "canonical_sha": "abc123", "agent": "genie", "session_key": "agent:genie:test", "status": "accepted"})
run_case("dispatcher-handoff-rejects-invalid-sha", invalid_sha_handoff, False)
print("TRACE VALIDATOR FIXTURES PASSED (12)")
