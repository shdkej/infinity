#!/usr/bin/env python3
"""Static contract checks for the split Infinity cron entrypoints."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CronSeparationTest(unittest.TestCase):
    def test_dispatcher_no_longer_owns_buttons_or_notifications(self):
        source = (ROOT / "scripts/run_dispatcher_cycle.sh").read_text()
        self.assertNotIn("process_action_requests.py", source)
        self.assertNotIn("dispatch_terminal_notifications.py", source)

    def test_dashboard_cron_owns_action_processing_and_remote_proof(self):
        source = (ROOT / "scripts/run_dashboard_actions_cron.sh").read_text()
        self.assertIn("process_action_requests.py", source)
        self.assertIn("git -C \"$ROOT\" push origin HEAD:main", source)
        self.assertIn("ls-remote origin refs/heads/main", source)

    def test_notification_cron_owns_delivery_and_card_arguments(self):
        source = (ROOT / "scripts/run_notification_cron.sh").read_text()
        self.assertIn("dispatch_terminal_notifications.py", source)
        self.assertIn("--deliver", source)
        self.assertIn("--card-dir", source)


if __name__ == "__main__":
    unittest.main()
