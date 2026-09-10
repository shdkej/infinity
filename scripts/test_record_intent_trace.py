#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("record", Path(__file__).with_name("record_intent_trace.py"))
record = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(record)

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

if __name__ == "__main__":
    unittest.main()
