#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("record", Path(__file__).with_name("record_intent_trace.py"))
record = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(record)
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validator", Path(__file__).with_name("validate_intent_trace.py"))
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
VALIDATOR_SPEC.loader.exec_module(validator)

class LegacyTraceTest(unittest.TestCase):
    def test_exploratory_archive_records_required_red_evidence(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "repo"
            root.mkdir()
            for relative in ("report.html", "red-review.md", "remote-proof.txt"):
                (root / relative).write_text("evidence", encoding="utf-8")
            previous_root, previous_traces = record.ROOT, record.TRACES
            try:
                record.ROOT = root
                record.TRACES = root / "data" / "traces"
                record.TRACES.mkdir(parents=True)
                target = record.trace_path("exploratory-red")
                target.write_text(json.dumps({"intent_id": "exploratory-red", "status": "active", "events": []}), encoding="utf-8")
                args = type("Args", (), {
                    "intent_id": "exploratory-red", "report_path": "report.html",
                    "red_report_path": "red-review.md", "remote_proof_path": "remote-proof.txt",
                    "research_mode": "exploratory_research", "evidence": [], "artifact": [],
                    "at": "2026-09-10T00:02:00Z", "decision_status": "implemented",
                    "next_decision": "done",
                })()
                record.archive(args)
                archived = json.loads(target.read_text(encoding="utf-8"))
            finally:
                record.ROOT, record.TRACES = previous_root, previous_traces
        event = archived["events"][-1]
        self.assertEqual(event["verification"]["red_status"], "pass")
        self.assertEqual(event["verification"]["red_report_path"], "red-review.md")
        self.assertIn("red-review.md", event["evidence_paths"])

    def test_exploratory_archive_rejects_missing_red_evidence(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "repo"
            root.mkdir()
            (root / "report.html").write_text("report", encoding="utf-8")
            (root / "remote-proof.txt").write_text("proof", encoding="utf-8")
            previous_root, previous_traces = record.ROOT, record.TRACES
            try:
                record.ROOT = root
                record.TRACES = root / "data" / "traces"
                record.TRACES.mkdir(parents=True)
                record.trace_path("exploratory-no-red").write_text(json.dumps({"intent_id": "exploratory-no-red", "events": []}), encoding="utf-8")
                args = type("Args", (), {
                    "intent_id": "exploratory-no-red", "report_path": "report.html",
                    "red_report_path": "missing-red.md", "remote_proof_path": "remote-proof.txt",
                    "research_mode": "exploratory_research", "evidence": [], "artifact": [],
                    "at": "2026-09-10T00:02:00Z", "decision_status": "implemented",
                    "next_decision": "done",
                })()
                with self.assertRaises(SystemExit):
                    record.archive(args)
            finally:
                record.ROOT, record.TRACES = previous_root, previous_traces

    def test_new_intake_records_user_intent_contract(self):
        with tempfile.TemporaryDirectory() as raw:
            previous = record.TRACES
            try:
                record.TRACES = Path(raw) / "traces"
                args = type("Args", (), {
                    "intent_id": "new-contract", "status": "inbox",
                    "raw": "사용자 원문", "query": "정규화된 작업",
                    "user_intent": "사용자의 목적", "desired_outcome": "받을 결과",
                    "out_of_scope": "하지 않을 범위", "success_evidence": "성공 증거",
                    "context_pack": "intents/context/infinity-trace-contract-01.json",
                    "evidence": ["README.md"], "next_decision": "다음 단계",
                    "at": "2026-09-10T00:00:00Z",
                })()
                record.intake(args)
                data = json.loads((record.TRACES / "new-contract.json").read_text())
            finally:
                record.TRACES = previous
        self.assertEqual(data["schema_version"], 2)
        self.assertEqual(data["request"]["user_intent"]["value"], "사용자의 목적")
        self.assertEqual(data["request"]["success_evidence"]["value"], "성공 증거")

    def test_bare_handoff_list_is_normalized(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "sample.json"
            path.write_text(json.dumps([{"event": "dispatcher_handoff", "run_id": "r", "canonical_sha": "a" * 40, "agent": "genie", "session_key": "s", "timestamp": "2026-09-10T00:00:00Z", "status": "accepted"}]))
            data = record.load(path)
        self.assertEqual(data["intent_id"], "sample")
        self.assertEqual(data["events"][0]["type"], "intake")
        self.assertEqual(data["events"][1]["type"], "dispatcher_handoff")
        self.assertEqual(data["request"]["raw"]["status"], "missing")

    def test_legacy_task_event_becomes_backfill(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "sample.json"
            path.write_text(json.dumps({"schema_version": 1, "intent_id": "sample", "status": "active", "trace_completeness": "partial", "events": [{"type": "task_completed", "at": "2026-09-10T00:00:00Z"}]}))
            data = record.load(path)
        self.assertEqual(data["events"][0]["type"], "intake")
        self.assertEqual(data["events"][1]["type"], "backfill")

    def test_handoff_only_object_is_backfilled_without_invented_context_pack(self):
        with tempfile.TemporaryDirectory() as raw:
            previous = record.TRACES
            try:
                record.TRACES = Path(raw) / "traces"
                record.TRACES.mkdir()
                target = record.TRACES / "handoff-only.json"
                target.write_text(json.dumps({
                    "schema_version": 1, "intent_id": "handoff-only", "status": "active",
                    "events": [{"type": "dispatcher_handoff", "run_id": "run-1", "canonical_sha": "a" * 40,
                                "agent": "genie", "session_key": "agent:genie:infinity-dispatcher",
                                "timestamp": "2026-09-10T00:00:00Z", "status": "accepted"}],
                }))
                args = type("Args", (), {
                    "intent_id": "handoff-only", "run_id": "run-2", "canonical_sha": "b" * 40,
                    "agent": "genie", "session_key": "agent:genie:infinity-dispatcher", "at": "2026-09-10T00:01:00Z",
                })()
                record.dispatcher_handoff(args)
                data = json.loads(target.read_text())
                errors = validator.validate(target)
            finally:
                record.TRACES = previous
        self.assertEqual(data["trace_completeness"], "partial")
        self.assertEqual(data["backfill_source"], "dispatcher_missing_trace")
        self.assertEqual(data["events"][0]["context_pack_status"], "missing")
        self.assertFalse(errors)

    def test_recovery_marker_cannot_bypass_context_or_archive_gates(self):
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw) / "invalid-recovery.json"
            target.write_text(json.dumps({
                "schema_version": 1, "intent_id": "invalid-recovery", "status": "archived",
                "trace_completeness": "partial", "backfill_source": "dispatcher_missing_trace",
                "request": {"raw": {"status": "recorded", "value": "invented"}, "normalized_query": {"status": "missing", "reason": "missing"}},
                "events": [
                    {"type": "intake", "at": "2026-09-10T00:00:00Z", "context_pack": "fake.json", "context_pack_status": "missing", "context_pack_reason": "missing", "evidence_paths": []},
                    {"type": "dispatcher_handoff", "run_id": "run-1", "canonical_sha": "a" * 40, "agent": "genie", "session_key": "agent:genie:test", "timestamp": "2026-09-10T00:01:00Z", "status": "accepted"},
                    {"type": "archive", "at": "2026-09-10T00:02:00Z", "report_path": "missing.html", "verification": {"red_status": "pass", "remote_verified": "pass"}},
                ], "artifacts": [], "verifications": [], "next_decision": {"status": "done", "value": "bad"},
            }))
            errors = validator.validate(target)
        self.assertTrue(errors)
        self.assertTrue(any("context_pack" in item for item in errors))
        self.assertTrue(any("execution before archive" in item for item in errors))

    def test_missing_trace_is_backfilled_for_dispatcher_handoff(self):
        with tempfile.TemporaryDirectory() as raw:
            previous = record.TRACES
            try:
                record.TRACES = Path(raw) / "traces"
                args = type("Args", (), {
                    "intent_id": "missing-trace", "run_id": "run-1",
                    "canonical_sha": "a" * 40, "agent": "genie",
                    "session_key": "agent:genie:infinity-dispatcher", "at": "2026-09-10T00:00:00Z",
                })()
                record.dispatcher_handoff(args)
                target = record.TRACES / "missing-trace.json"
                data = json.loads(target.read_text())
                errors = validator.validate(target)
            finally:
                record.TRACES = previous
        self.assertEqual(data["trace_completeness"], "partial")
        self.assertEqual(data["request"]["raw"]["status"], "missing")
        self.assertEqual(data["events"][0]["context_pack_status"], "missing")
        self.assertEqual([event["type"] for event in data["events"]], ["intake", "dispatcher_handoff"])
        self.assertFalse(errors)

if __name__ == "__main__":
    unittest.main()
