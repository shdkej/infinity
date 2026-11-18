#!/usr/bin/env python3
"""Safety contract for the paused Hermes Infinity migration entrypoint."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_hermes_infinity_cron.sh"


class HermesCronEntrypointTest(unittest.TestCase):
    def invoke(self, role, *args, home, script=SCRIPT):
        env = os.environ.copy()
        env["INFINITY_HERMES_STATE_DIR"] = str(home)
        env.pop("INFINITY_HERMES_CUTOVER_READY", None)
        return subprocess.run(["bash", str(script), role, *args], cwd=ROOT, env=env,
                              text=True, capture_output=True)

    def fixture(self, temp):
        home = Path(temp) / "state"
        home.mkdir()
        scripts = Path(temp) / "scripts"
        scripts.mkdir()
        payload = '{"version":2,"deliveries":{},"observed_intents":{}}\n'
        digest = hashlib.sha256(payload.encode()).hexdigest()
        (home / "ubuntu-consumer-stopped.confirmed").write_text("confirmed-ubuntu-consumer-stopped\n")
        (home / "receipt-bootstrap.sha256").write_text(digest + "\n")
        (home / "notification-ledger-intake-baseline.json").write_text(payload)
        (home / "dispatcher-terminal-notifications.json").write_text(payload)
        (scripts / "verify_hermes_receipt.py").write_bytes((ROOT / "scripts/verify_hermes_receipt.py").read_bytes())
        script = scripts / "run_hermes_infinity_cron.sh"
        script.write_text(SCRIPT.read_text().replace(
            "a33b0be96db917069d3b66761ab7dc8aa92aacb3a06e6e1a64d761028c724666", digest))
        return home, script

    def test_checks_are_local_and_report_not_ready_without_state(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "uncreated"
            for role in ("dispatcher", "consumer", "notifier"):
                with self.subTest(role=role):
                    result = self.invoke(role, "--check", home=home)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    report = json.loads(result.stdout)
                    self.assertEqual(report["role"], role)
                    self.assertFalse(report["ready"])
                    self.assertFalse(home.exists(), "a read-only check must not create state")

    def test_normal_entry_refuses_before_any_state_or_external_call(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "uncreated"
            for role in ("dispatcher", "consumer", "notifier"):
                with self.subTest(role=role):
                    result = self.invoke(role, home=home)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(home.exists())

    def test_bootstrap_proof_allows_a_mutated_runtime_ledger(self):
        # Isolated fixture only: no queue access, no real transport or receipt content.
        with tempfile.TemporaryDirectory() as temp:
            home, script = self.fixture(temp)
            current = home / "dispatcher-terminal-notifications.json"
            data = json.loads(current.read_text())
            data["deliveries"]["new"] = {"state": "sent"}
            current.write_text(json.dumps(data))
            result = self.invoke("consumer", "--check", home=home, script=script)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["reason"], "ok")

    def test_dispatcher_hermes_handoff_retains_original_safety_pipeline(self):
        source = (ROOT / "scripts/run_dispatcher_cycle.sh").read_text()
        self.assertIn('INFINITY_EXECUTOR', source)
        self.assertIn('route_hermes_task.py', source)
        self.assertIn('--task-id "$GUARD_TASK_ID" --end-at "$GUARD_END_AT"', source)
        self.assertIn('Canonical revision: {plan["canonical_sha"]}', source)
        self.assertIn('git -C "$ROOT" push origin main', source)
        self.assertNotIn('`/home/ubuntu/workspace/infinity`', source)

    def test_notification_wrapper_selects_telegram_bridge_without_openclaw(self):
        source = (ROOT / "scripts/run_notification_cron.sh").read_text()
        self.assertIn('INFINITY_NOTIFICATION_TRANSPORT', source)
        self.assertIn('hermes_telegram_send.py', source)
        self.assertIn('notification-receipt-checkpoint.sqlite3', source)
        self.assertIn('--receipt-checkpoint', source)
        self.assertIn('--state "$STATE_FILE" --deliver', source)

    def test_all_roles_share_canonical_git_lock(self):
        source = SCRIPT.read_text()
        self.assertIn('canonical-git.lock', source)
        self.assertIn('flock -n 8', source)
        self.assertLess(source.index('flock -n 8'), source.index('run_dashboard_actions_cron.sh'))

    def test_shared_lock_contention_prevents_consumer_from_reaching_queue(self):
        import fcntl
        with tempfile.TemporaryDirectory() as temp:
            home, script = self.fixture(temp)
            with (home / "canonical-git.lock").open("w") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                result = self.invoke("consumer", home=home, script=script)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(list(home.glob("dashboard-actions*")))

    def test_invalid_role_never_succeeds(self):
        with tempfile.TemporaryDirectory() as temp:
            result = self.invoke("old-evaluator", "--check", home=Path(temp))
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
