#!/usr/bin/env python3
"""Offline monotonic notification receipt checkpoint regressions."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("notification_receipt_guard.py")


class ReceiptCheckpointTest(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)

    def test_post_intake_sent_and_unknown_cannot_disappear_or_revert(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline, ledger, guard = root / "baseline.json", root / "ledger.json", root / "checkpoint.sqlite3"
            intake = {"deliveries": {"old": {"state": "sent", "destination": "i|telegram:1"}}, "observed_intents": {}}
            baseline.write_text(json.dumps(intake))
            ledger.write_text(baseline.read_text())
            sha = hashlib.sha256(baseline.read_bytes()).hexdigest()
            self.assertEqual(self.call("init", guard, baseline, ledger, sha).returncode, 0)
            evolving = json.loads(ledger.read_text())
            evolving["deliveries"].update({
                "new-sent": {"state": "sent", "destination": "j|telegram:1", "attempt_started_at": "a"},
                "new-unknown": {"state": "delivery_unknown", "destination": "k|telegram:1", "attempt_started_at": "b"},
            })
            ledger.write_text(json.dumps(evolving))
            self.assertEqual(self.call("record", guard, ledger).returncode, 0)
            for missing in ("new-sent", "new-unknown"):
                stale = json.loads(ledger.read_text())
                del stale["deliveries"][missing]
                ledger.write_text(json.dumps(stale))
                self.assertNotEqual(self.call("verify", guard, ledger).returncode, 0)
                ledger.write_text(json.dumps(evolving))
            ledger.write_text(baseline.read_text())
            self.assertNotEqual(self.call("verify", guard, ledger).returncode, 0)
            guard.unlink()
            self.assertNotEqual(self.call("verify", guard, ledger).returncode, 0)

    def test_attempt_checkpoint_prevents_replay_after_older_ledger_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline, ledger, guard = root / "baseline.json", root / "ledger.json", root / "checkpoint.sqlite3"
            baseline.write_text(json.dumps({"deliveries": {}, "observed_intents": {}}))
            ledger.write_text(baseline.read_text())
            self.assertEqual(self.call("init", guard, baseline, ledger, hashlib.sha256(baseline.read_bytes()).hexdigest()).returncode, 0)
            started = {"deliveries": {"new": {"state": "claimed", "destination": "a|telegram:1", "attempt_started_at": "t"}}, "observed_intents": {}}
            ledger.write_text(json.dumps(started))
            self.assertEqual(self.call("record", guard, ledger).returncode, 0)
            ledger.write_text(baseline.read_text())
            self.assertNotEqual(self.call("verify", guard, ledger).returncode, 0)
            started["deliveries"]["new"]["state"] = "sent"
            ledger.write_text(json.dumps(started))
            self.assertEqual(self.call("verify", guard, ledger).returncode, 0)
            self.assertEqual(self.call("record", guard, ledger).returncode, 0)


if __name__ == "__main__":
    unittest.main()
