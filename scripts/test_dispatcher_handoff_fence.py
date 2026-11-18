#!/usr/bin/env python3
"""Offline crash/reselection contract for the per-Intent handoff fence."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("dispatcher_handoff_fence.py")


class HandoffFenceTest(unittest.TestCase):
    def call(self, state, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--state-dir", str(state), *args],
                              capture_output=True, text=True)

    def reserve(self, state, run="run-1", task="task-1", ids=("intent-a",)):
        return self.call(state, "reserve", "--run-id", run, "--task-id", task,
                         "--canonical-sha", "a" * 40, *ids)

    def test_pending_survives_forced_parent_exit_and_new_cycle_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp)
            child = subprocess.run([sys.executable, "-c", "import os,sys; from pathlib import Path; from dispatcher_handoff_fence import reserve; reserve(sys.argv[1], 'run-1', 'task-1', 'a'*40, ['intent-a']); Path(sys.argv[2]).write_text('mock child entered'); os._exit(137)", str(state), str(state / "child-entered")],
                                   env={**os.environ, "PYTHONPATH": str(SCRIPT.parent)}, capture_output=True)
            self.assertEqual(child.returncode, 137)
            self.assertEqual((state / "child-entered").read_text(), "mock child entered")
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 3)

    def test_busy_nonstart_releases_but_timeout_and_missing_receipt_do_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp)
            self.assertEqual(self.reserve(state).returncode, 0)
            receipt = state / "receipt.json"
            self.assertNotEqual(self.call(state, "resolve", "--run-id", "run-1", "--outcome", "nonstarted", "--receipt", str(receipt), "--exit-code", "4").returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 3)
            receipt.write_text(json.dumps({"task_id": "task-1", "state": "expired"}))
            self.assertNotEqual(self.call(state, "resolve", "--run-id", "run-1", "--outcome", "nonstarted", "--receipt", str(receipt), "--exit-code", "5").returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 3)
            receipt.write_text(json.dumps({"task_id": "task-1", "state": "busy"}))
            self.assertEqual(self.call(state, "resolve", "--run-id", "run-1", "--outcome", "nonstarted", "--receipt", str(receipt), "--exit-code", "4").returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 0)

    def test_completed_child_requires_remote_proof_before_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp)
            self.assertEqual(self.reserve(state).returncode, 0)
            receipt, post = state / "receipt.json", state / "post.json"
            receipt.write_text(json.dumps({"task_id": "task-1", "state": "completed"}))
            post.write_text(json.dumps({"canonical_sha": "a" * 40, "resume_candidates": [], "handoff_candidates": []}))
            cmd = ("resolve", "--run-id", "run-1", "--outcome", "verified", "--receipt", str(receipt), "--exit-code", "0", "--post-plan", str(post), "--remote-sha", "b" * 40)
            self.assertNotEqual(self.call(state, *cmd).returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 3)
            post.write_text(json.dumps({"canonical_sha": "b" * 40, "resume_candidates": [], "handoff_candidates": []}))
            self.assertEqual(self.call(state, *cmd).returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2").returncode, 0)

    def test_verified_followup_creation_releases_even_when_source_report_persists(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state"; state.mkdir()
            repo = Path(tmp) / "repo"; repo.mkdir()
            def git(*args):
                return subprocess.run(["git", "-C", str(repo), "-c", "user.name=Fixture", "-c", "user.email=fixture@localhost", *args],
                                      capture_output=True, text=True, check=True).stdout.strip()
            git("init", "-q")
            registry = repo / "INTENTS.yaml"
            registry.write_text("lanes:\n  archive:\n  - id: source-1\n")
            git("add", "INTENTS.yaml"); git("commit", "-qm", "intake")
            before = git("rev-parse", "HEAD")
            reserve = self.call(state, "reserve", "--run-id", "run-1", "--task-id", "task-1",
                                "--canonical-sha", before, "source-1")
            self.assertEqual(reserve.returncode, 0, reserve.stderr)
            registry.write_text(registry.read_text() + "  inbox:\n  - id: next-1\n")
            git("add", "INTENTS.yaml"); git("commit", "-qm", "new followup")
            after = git("rev-parse", "HEAD")
            receipt, post = state / "receipt.json", state / "post.json"
            receipt.write_text(json.dumps({"task_id": "task-1", "state": "completed"}))
            post.write_text(json.dumps({"canonical_sha": after, "resume_candidates": [], "handoff_candidates": [],
                                        "follow_up_candidates": [{"intent_id": "source-1", "follow_up_intent_ids": "next-1"}]}))
            unproved = self.call(state, "resolve", "--run-id", "run-1", "--outcome", "verified",
                                 "--receipt", receipt, "--exit-code", "0", "--post-plan", post,
                                 "--remote-sha", after)
            self.assertEqual(unproved.returncode, 3)
            resolved = self.call(state, "resolve", "--run-id", "run-1", "--outcome", "verified",
                                 "--receipt", receipt, "--exit-code", "0", "--post-plan", post,
                                 "--remote-sha", after, "--repo", repo)
            self.assertEqual(resolved.returncode, 0, resolved.stderr)
            self.assertEqual(self.reserve(state, "run-2", "task-2", ("source-1",)).returncode, 0)

    def test_reserve_is_atomic_for_multiple_intents(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp)
            self.assertEqual(self.reserve(state, ids=("intent-a", "intent-b")).returncode, 0)
            self.assertEqual(self.reserve(state, "run-2", "task-2", ("intent-b", "intent-c")).returncode, 3)
            self.assertEqual(self.reserve(state, "run-3", "task-3", ("intent-c",)).returncode, 0)


if __name__ == "__main__":
    unittest.main()
