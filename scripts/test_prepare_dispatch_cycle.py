#!/usr/bin/env python3
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("prepare", Path(__file__).with_name("prepare_dispatch_cycle.py"))
prepare = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(prepare)

def block(intent_id, status, extra=""):
    return f"### [{intent_id}] task\n- status: {status}\n- target_agent: genie\n{extra}"

class PlanTests(unittest.TestCase):
    def test_metadata_is_not_an_intent_count(self):
        text = "## Inbox\n" + block("work-1", "inbox") + "\n## Active\n" + block("work-2", "active", "- goal: x\n" * 23) + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", Path(tempfile.mkdtemp()))
        self.assertEqual(plan["counts"]["active"], 1)
        self.assertEqual(len(plan["promote_candidates"]), 1)

    def test_slots_are_capped_at_three(self):
        text = "## Inbox\n" + "\n".join(block(f"work-{n}", "inbox") for n in range(4)) + "\n## Active\n" + "\n".join(block(f"active-{n}", "active") for n in range(2)) + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", Path(tempfile.mkdtemp()))
        self.assertEqual(len(plan["promote_candidates"]), 1)

    def test_lane_status_mismatch_is_not_dispatched(self):
        text = "## Inbox\n" + block("work-1", "inbox") + "\n## Active\n" + block("bad-1", "archived") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", Path(tempfile.mkdtemp()))
        self.assertEqual(plan["invalid_state"][0]["intent_id"], "bad-1")
        self.assertNotIn("bad-1", [item["intent_id"] for item in plan["handoff_candidates"]])

    def test_timestamp_handoff_is_live_evidence(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "traces").mkdir()
        (repo / "traces" / "work-1.json").write_text('{"events":[{"type":"dispatcher_handoff","timestamp":"2026-09-02T09:41:00Z","status":"accepted"}]}')
        reference = prepare.dt.datetime(2026, 9, 2, 9, 42, tzinfo=prepare.dt.timezone.utc)
        self.assertIsNotNone(prepare.fresh_trace("work-1", repo, reference))

if __name__ == "__main__":
    unittest.main()
