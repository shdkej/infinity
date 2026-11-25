"""Read-only experiment decisions: python3 -m unittest discover -s scripts -p test_miniapp_experiment.py."""
import base64
import copy
import io
import json
import subprocess
import unittest
from unittest.mock import patch

import miniapp_experiment as helper


def run_fixture():
    return {
        "run_id": "miniapp-20261125-2h", "status": "scheduled",
        "metrics": {"user_page_views": None, "target": 10},
        "tasks": [],
        "windows": [
            {"id": f"r{i}", "start_at": f"2026-11-25T{hour:02d}:00:00+09:00",
             "end_at": f"2026-11-25T{hour+2:02d}:00:00+09:00",
             "observation_due_at": f"2026-11-25T{hour+1:02d}:45:00+09:00",
             "report_status": "pending", "metrics": {"user_page_views": i}}
            for i, hour in enumerate((17, 19, 21), 1)
        ],
    }


def task(status="running", **extra):
    item = {
        "id": "t1", "window_id": "r1", "start_at": "2026-11-25T17:00:00+09:00",
        "end_at": "2026-11-25T19:00:00+09:00", "status": status,
        "handoff_status": "sent", "handoff_message_id": "m1", "status_check_at": None,
        "result_summary": None, "product_changes": [], "release_runs": [],
        "guard": {"state": "running", "exit_code": None, "finished_at": None,
                  "lock_free_verified_at": None},
    }
    item.update(extra)
    return item


def finished(**extra):
    return task("completed", result_summary="done", guard={
        "state": "completed", "exit_code": 0,
        "finished_at": "2026-11-25T17:20:00+09:00",
        "lock_free_verified_at": "2026-11-25T17:21:00+09:00"}, **extra)


class Decisions(unittest.TestCase):
    def setUp(self):
        self.run = run_fixture()

    def snap(self, time="17:30:00", date="2026-11-25"):
        return helper.snapshot(self.run, helper.parse_time(f"{date}T{time}+09:00"))

    def test_first_task_and_date_boundaries(self):
        self.assertTrue(self.snap("17:00:00")["dispatch_allowed"])
        for time, date in [("16:59:59", "2026-11-25"), ("23:00:00", "2026-11-25"),
                           ("18:00:00", "2026-11-26")]:
            self.assertFalse(self.snap(time, date)["fire"])

    def test_next_task_proposal_is_concrete_but_does_not_write_or_bypass_lock(self):
        self.run["tasks"] = [finished(id="miniapp-20261125-r1-t01")]
        before = copy.deepcopy(self.run)
        proposed = self.snap().get("proposed_task")
        self.assertIsNotNone(proposed)
        self.assertEqual(proposed["id"], "miniapp-20261125-r1-t02")
        self.assertEqual(proposed["window_id"], "r1")
        self.assertEqual(proposed["status"], "prepared")
        self.assertEqual(proposed["guard"]["state"], "not_started")
        self.assertEqual(helper.parse_time(proposed["end_at"]), helper.parse_time(self.run["windows"][0]["end_at"]))
        self.assertEqual(self.run, before)
        self.run["tasks"][0]["guard"]["state"] = "running"
        self.assertIsNone(self.snap()["proposed_task"])

    def test_proposal_moves_to_current_window_without_resending_old_task(self):
        self.run["tasks"] = [finished(id="miniapp-20261125-r1-t01")]
        result = self.snap("21:51:00")
        self.assertIsNotNone(result.get("proposed_task"))
        self.assertEqual(result["proposed_task"]["id"], "miniapp-20261125-r3-t01")
        self.assertEqual(helper.parse_time(result["proposed_task"]["end_at"]), helper.parse_time(helper.END))
        self.assertIsNone(result["reuse_task_id"])
        self.assertIsNone(self.snap("23:00:00")["proposed_task"])

    def test_running_waits_without_model_even_after_ten_minutes(self):
        self.run["tasks"] = [task()]
        self.assertFalse(self.snap()["fire"])

    def test_result_and_released_guard_are_both_required(self):
        self.run["tasks"] = [finished()]
        self.assertTrue(self.snap()["dispatch_allowed"])
        self.run["tasks"][0]["guard"]["lock_free_verified_at"] = None
        self.assertFalse(self.snap()["dispatch_allowed"])
        self.run["tasks"][0]["guard"]["lock_free_verified_at"] = "2026-11-25T17:19:00+09:00"
        self.assertFalse(self.snap()["dispatch_allowed"])

    def test_failed_expired_or_timeout_can_advance_after_guard_releases(self):
        for status in ("failed", "timed_out", "expired"):
            item = finished()
            item["status"] = status
            item["guard"]["state"] = status
            self.run["tasks"] = [item]
            self.assertTrue(self.snap()["dispatch_allowed"], status)

    def test_sent_unconfirmed_checks_once_after_ten_minutes(self):
        self.run["tasks"] = [task("sent", guard={})]
        self.assertFalse(self.snap("17:09:59")["fire"])
        result = self.snap("17:10:00")
        self.assertEqual(result["status_check_task_id"], "t1")
        self.assertFalse(result["dispatch_allowed"])
        self.run["tasks"][0]["status_check_at"] = "2026-11-25T17:10:00+09:00"
        self.assertIsNone(self.snap()["status_check_task_id"])
        self.assertFalse(self.snap()["dispatch_allowed"])

    def test_posted_result_missing_parent_receipt_wakes_reconciliation(self):
        self.run["tasks"] = [task("posted_guard_pending", result_summary="published",
                                  guard={"state": "pending_parent_after_child_exit"},
                                  status_check_at="2026-11-25T17:15:00+09:00")]
        self.assertFalse(self.snap("17:24:59")["fire"])
        result = self.snap("17:25:00")
        self.assertTrue(result["fire"])
        self.assertEqual(result.get("reconcile_task_id"), "t1")
        self.assertIn("receipt_reconciliation_due", result["reasons"])
        self.assertFalse(result["dispatch_allowed"])
        self.assertIsNone(result["status_check_task_id"])

    def test_receipt_rechecks_are_spaced_and_never_release_a_live_guard(self):
        self.run["tasks"] = [task(status_check_at="2026-11-25T17:15:00+09:00",
                                  receipt_checked_at="2026-11-25T17:25:00+09:00")]
        self.assertFalse(self.snap("17:39:59")["fire"])
        result = self.snap("17:40:00")
        self.assertEqual(result.get("reconcile_task_id"), "t1")
        self.assertFalse(result["dispatch_allowed"])
        self.run["tasks"] = [finished(receipt_checked_at="2026-11-25T17:25:00+09:00")]
        self.assertTrue(self.snap("17:40:00")["dispatch_allowed"])
        self.assertIsNone(self.snap("17:40:00").get("reconcile_task_id"))

    def test_queried_previous_window_cannot_go_silent_until_end_of_day(self):
        self.run["tasks"] = [task("posted_guard_pending", guard={},
                                  status_check_at="2026-11-25T17:15:00+09:00")]
        for window in self.run["windows"][:2]:
            window["report_status"] = "sent"
        result = self.snap("21:51:00")
        self.assertTrue(result["fire"])
        self.assertEqual(result.get("reconcile_task_id"), "t1")
        self.assertFalse(result["dispatch_allowed"])
        self.assertFalse(self.snap("23:00:00")["fire"])

    def test_prepared_unsent_reuses_id_but_uncertain_send_never_dispatches(self):
        self.run["tasks"] = [task("prepared", handoff_status="prepared",
                                  handoff_message_id=None, guard={})]
        result = self.snap()
        self.assertTrue(result["dispatch_allowed"])
        self.assertEqual(result["reuse_task_id"], "t1")
        self.run["tasks"][0]["handoff_status"] = "uncertain"
        self.assertFalse(self.snap()["dispatch_allowed"])

    def test_boundary_reports_even_if_previous_window_still_running(self):
        self.run["tasks"] = [task()]
        result = self.snap("19:00:00")
        self.assertTrue(result["fire"])
        self.assertEqual(result["reports_due"], ["r1"])
        self.assertEqual(result["window_id"], "r2")
        self.assertFalse(result["dispatch_allowed"])
        self.run["windows"][0]["report_status"] = "sent"
        self.run["tasks"][0]["status_check_at"] = "2026-11-25T19:00:00+09:00"
        self.assertFalse(self.snap("19:03:00")["fire"])

    def test_running_past_deadline_gets_one_status_check_without_dispatch(self):
        self.run["tasks"] = [task()]
        self.run["windows"][0]["report_status"] = "sent"
        result = self.snap("19:00:00")
        self.assertTrue(result["fire"])
        self.assertEqual(result["status_check_task_id"], "t1")
        self.assertIn("task_deadline_status_check", result["reasons"])
        self.assertFalse(result["dispatch_allowed"])
        self.run["tasks"][0]["status_check_at"] = "2026-11-25T19:00:00+09:00"
        self.assertFalse(self.snap("19:03:00")["fire"])

    def test_task_deadline_must_match_its_window(self):
        for deadline in ("2026-11-25T19:01:00+09:00", "2026-11-25T17:45:00+09:00",
                         "2026-11-26T19:00:00+09:00", "2026-11-25T19:00:00", None):
            self.run["tasks"] = [task(end_at=deadline)]
            with self.assertRaises(ValueError):
                self.snap()

    def test_task_start_is_required_and_inside_its_window(self):
        for start in (None, "2026-11-25T16:59:59+09:00", "2026-11-25T19:00:00+09:00",
                      "2026-11-26T17:00:00+09:00", "2026-11-25T17:00:00"):
            self.run["tasks"] = [task(start_at=start)]
            with self.assertRaises(ValueError):
                self.snap()

    def test_timezone_equivalent_deadline_is_accepted(self):
        self.run["tasks"] = [task(end_at="2026-11-25T10:00:00Z")]
        self.assertFalse(self.snap()["fire"])

    def test_observation_deadline_must_be_fifteen_minutes_before_window_end(self):
        self.run["windows"][0]["observation_due_at"] = "2026-11-25T18:44:00+09:00"
        with self.assertRaises(ValueError):
            self.snap()

    def test_observation_due_wakes_exhausted_window_once_and_keeps_zero(self):
        self.run["tasks"] = [finished()]
        self.run["windows"][0]["exhausted"] = True
        self.assertFalse(self.snap("18:44:59")["fire"])
        result = self.snap("18:45:00")
        self.assertTrue(result["dispatch_allowed"])
        self.assertIn("metrics_observation_due", result["reasons"])
        self.run["windows"][0]["metrics"].update({"observed_at": "2026-11-25T18:45:00+09:00", "user_page_views": 0})
        self.assertFalse(self.snap("18:48:00")["fire"])

    def test_observation_waits_for_running_guard_then_dispatches(self):
        self.run["tasks"] = [task()]
        self.run["windows"][0]["exhausted"] = True
        self.assertFalse(self.snap("18:45:00")["fire"])
        self.run["tasks"] = [finished()]
        self.assertIn("metrics_observation_due", self.snap("18:48:00")["reasons"])

    def test_failed_observation_attempt_prevents_infinite_retry(self):
        self.run["tasks"] = [finished()]
        self.run["windows"][0]["exhausted"] = True
        self.run["windows"][0]["metrics"].update({"observed_at": None, "obs_attempted_at": "2026-11-25T18:45:00+09:00"})
        self.assertFalse(self.snap("18:48:00")["fire"])

    def test_reports_at_twenty_one_and_finished_run_is_quiet(self):
        self.assertEqual(self.snap("21:00:00")["reports_due"], ["r1", "r2"])
        self.run["status"] = "finished"
        self.assertFalse(self.snap("21:00:00")["fire"])

    def test_exhausted_window_stops_completed_loop_but_reports(self):
        self.run["tasks"] = [finished()]
        self.run["windows"][0]["exhausted"] = True
        self.assertFalse(self.snap()["fire"])
        self.assertIn("r1", self.snap("19:00:00")["reports_due"])

    def test_pending_recovery_is_reused_only_without_active_guard(self):
        pending = task("pending", id="recovery", required=True, handoff_status="pending",
                       handoff_message_id=None, guard={})
        self.run["tasks"] = [finished(), pending]
        self.assertEqual(self.snap()["reuse_task_id"], "recovery")
        self.run["windows"][0]["exhausted"] = True
        self.assertEqual(self.snap()["reuse_task_id"], "recovery")
        self.run["tasks"][0]["guard"]["state"] = "running"
        self.assertFalse(self.snap()["dispatch_allowed"])

    def test_recent_send_uses_handoff_attempt_time_not_old_task_start(self):
        self.run["tasks"] = [task("sent", guard={}, handoff_attempt_at="2026-11-25T17:29:00+09:00")]
        self.assertFalse(self.snap()["fire"])

    def test_summaries_preserve_all_changes_releases_blockers_and_unknowns(self):
        self.run["tasks"] = [finished(product_changes=["홈 개선"], release_runs=["123"]),
                             finished(id="t2", changes=["콘텐츠 게시"], release_runs=["123", "124"]),
                             task("blocked", id="t3", result_summary="로그인 필요"),
                             task(id="t4")]
        result = self.snap()
        report = result["window_summaries"][0]
        self.assertEqual(report["product_changes"], ["홈 개선", "콘텐츠 게시"])
        self.assertEqual(report["release_runs"], ["123", "124"])
        self.assertEqual(report["blockers"], ["로그인 필요"])
        self.assertIn("t4", report["unknown_task_ids"])
        self.assertEqual(report["task_count"], 4)
        self.assertEqual(report["metrics"]["user_page_views"], 1)
        self.assertIsNone(result["metrics"]["user_page_views"])

    def test_zero_is_not_missing_and_input_is_not_mutated(self):
        self.run["metrics"]["user_page_views"] = 0
        before = copy.deepcopy(self.run)
        self.assertEqual(self.snap()["metrics"]["user_page_views"], 0)
        self.assertEqual(self.run, before)


class Loading(unittest.TestCase):
    def registry(self):
        return {"lanes": {"Active": [{"id": helper.INTENT_ID, "experiment_run": run_fixture()}]}}

    def test_extract_exact_intent_and_run(self):
        self.assertEqual(helper.extract_run(self.registry())["run_id"], helper.RUN_ID)
        registry = self.registry()
        registry["lanes"]["Active"][0]["experiment_run"]["run_id"] = "old-run"
        with self.assertRaises(ValueError):
            helper.extract_run(registry)

    @patch("miniapp_experiment.subprocess.run")
    def test_remote_is_read_only_timeout_bounded_and_in_memory(self, call):
        payload = json.dumps(self.registry()).encode()
        call.return_value = subprocess.CompletedProcess([], 0, json.dumps({
            "encoding": "base64", "content": base64.b64encode(payload).decode()}), "")
        self.assertEqual(helper.load_registry(remote=True), self.registry())
        self.assertEqual(call.call_args.kwargs["timeout"], 15)
        self.assertEqual(call.call_args.args[0], ["gh", "api", helper.REMOTE_ENDPOINT])

    @patch("miniapp_experiment.subprocess.run")
    def test_remote_failure_and_invalid_response_raise(self, call):
        call.return_value = subprocess.CompletedProcess([], 1, "", "private token")
        with self.assertRaisesRegex(ValueError, "remote registry read failed") as error:
            helper.load_registry(remote=True)
        self.assertNotIn("private token", str(error.exception))
        call.return_value = subprocess.CompletedProcess([], 0, "bad-json", "")
        with self.assertRaises(ValueError):
            helper.load_registry(remote=True)

    @patch("miniapp_experiment.subprocess.run", side_effect=subprocess.TimeoutExpired("gh", 15))
    def test_remote_timeout_fails(self, call):
        with self.assertRaisesRegex(ValueError, "timed out"):
            helper.load_registry(remote=True)

    @patch("miniapp_experiment.load_registry")
    def test_report_cli_returns_selected_whole_window_with_separate_metrics(self, load):
        load.return_value = self.registry()
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            code = helper.main(["report", "--window", "r2", "--remote", "--now", "2026-11-25T21:00:00+09:00"])
        self.assertEqual(code, 0)
        result = json.loads(output.getvalue())
        self.assertEqual(result["window"]["window_id"], "r2")
        self.assertEqual(result["window"]["metrics"]["user_page_views"], 2)
        self.assertIsNone(result["metrics"]["user_page_views"])

    def test_bad_dates_and_duplicate_tasks_fail_instead_of_waking_model(self):
        with self.assertRaises(ValueError):
            helper.parse_time("2026-11-25T17:00:00")
        run = run_fixture()
        run["tasks"] = [task(), task()]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            helper.snapshot(run, helper.parse_time("2026-11-25T17:30:00+09:00"))


if __name__ == "__main__":
    unittest.main()
