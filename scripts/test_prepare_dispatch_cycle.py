#!/usr/bin/env python3
import importlib.util
import json
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
        self.assertTrue(plan["dispatch_required"])

    def test_deadline_active_card_requires_observability_fields(self):
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", "- deadline: 2026-09-05T06:00:00Z\n") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", Path(tempfile.mkdtemp()))
        invalid = [item for item in plan["invalid_state"] if item["intent_id"] == "work-1"]
        self.assertEqual(invalid[0]["reason"], "missing_card_contract")
        self.assertIn("task_plan", invalid[0]["missing_fields"])

    def test_deadline_active_card_with_observability_fields_is_valid(self):
        extra = "".join([
            "- deadline: 2026-09-05T06:00:00Z\n", "- deadline_local: 2026-09-05 08:00 Europe/Rome (CEST)\n",
            "- task_plan: artifacts/work-1/task-plan.json\n", "- trace: traces/work-1.json\n",
            "- notification_channel: slack\n", "- notification_target: channel:C0\n", "- notification_reply_to: 1.2\n",
        ])
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", extra) + "\n## Waiting\n\n## Archive\n"
        repo = Path(tempfile.mkdtemp())
        (repo / "artifacts" / "work-1").mkdir(parents=True)
        (repo / "artifacts" / "work-1" / "task-plan.json").write_text(json.dumps({"tasks": [{"id": "T1", "status": "active"}]}))
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertFalse(plan["invalid_state"])

    def test_pending_task_is_explicitly_activated_before_handoff(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "artifacts" / "work-1").mkdir(parents=True)
        (repo / "artifacts" / "work-1" / "task-plan.json").write_text(json.dumps({"tasks": [{"id": "T1", "title": "검증", "status": "pending"}]}))
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", "- task_plan: artifacts/work-1/task-plan.json\n") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertEqual(plan["plan_activation_candidates"][0]["task_state"]["task_id"], "T1")
        self.assertEqual(plan["handoff_candidates"][0]["intent_id"], "work-1")

    def test_dependencies_gate_pending_task_activation(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "artifacts" / "work-1").mkdir(parents=True)
        tasks = {"tasks": [
            {"id": "T1", "title": "선행", "status": "pending"},
            {"id": "T2", "title": "후행", "status": "pending", "depends_on": ["T1"]},
        ]}
        (repo / "artifacts" / "work-1" / "task-plan.json").write_text(json.dumps(tasks))
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", "- task_plan: artifacts/work-1/task-plan.json\n") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertEqual(plan["plan_activation_candidates"][0]["task_state"]["task_id"], "T1")

    def test_timebox_expiry_requires_reassessment(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "artifacts" / "work-1").mkdir(parents=True)
        tasks = {"tasks": [{
            "id": "T1", "title": "시간 제한 작업", "status": "active",
            "started_at": "2020-01-01T00:00:00Z", "max_minutes": 10,
        }]}
        (repo / "artifacts" / "work-1" / "task-plan.json").write_text(json.dumps(tasks))
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", "- task_plan: artifacts/work-1/task-plan.json\n") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertEqual(plan["timebox_reassessment_candidates"][0]["task_state"]["task_id"], "T1")

    def test_cycle_contract_rejects_unbounded_leaf(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "artifacts" / "work-1").mkdir(parents=True)
        tasks = {"cycle_contract_version": 1, "tasks": [{"id": "T1", "title": "기능", "status": "pending", "max_minutes": 45}]}
        (repo / "artifacts" / "work-1" / "task-plan.json").write_text(json.dumps(tasks))
        text = "## Inbox\n\n## Active\n" + block("work-1", "active", "- task_plan: artifacts/work-1/task-plan.json\n") + "\n## Waiting\n\n## Archive\n"
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertEqual(plan["invalid_state"][0]["reason"], "cycle_contract_violation")

    def test_timestamp_handoff_is_live_evidence(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "traces").mkdir()
        (repo / "traces" / "work-1.json").write_text('{"events":[{"type":"dispatcher_handoff","timestamp":"2026-09-02T09:41:00Z","status":"accepted"}]}')
        reference = prepare.dt.datetime(2026, 9, 2, 9, 42, tzinfo=prepare.dt.timezone.utc)
        self.assertIsNotNone(prepare.fresh_trace("work-1", repo, reference, "fixture"))

    def test_archive_followup_fields_are_exposed(self):
        repo = Path(tempfile.mkdtemp())
        (repo / "reports").mkdir()
        (repo / "reports" / "done.md").write_text(
            "follow_up_intent_ids: next-1\nfollow_up_not_created_reasons: approval: publish\n"
        )
        text = "## Inbox\n\n## Active\n\n## Waiting\n\n## Archive\n" + block(
            "done-1", "archived", "- report: reports/done.md\n"
        )
        plan = prepare.build_plan(text, "fixture", repo)
        self.assertEqual(plan["follow_up_candidates"][0]["follow_up_intent_ids"], "next-1")
        self.assertEqual(plan["follow_up_candidates"][0]["follow_up_not_created_reasons"], "approval: publish")
        self.assertTrue(plan["dispatch_required"])

if __name__ == "__main__":
    unittest.main()
