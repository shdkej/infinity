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
