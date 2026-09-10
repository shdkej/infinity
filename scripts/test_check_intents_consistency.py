#!/usr/bin/env python3
"""Regression tests for the Infinity lane and notification contract."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def registry(card: str) -> str:
    return f"## Inbox\n{card}\n## Active\n\n## Waiting\n\n## Archive\n"


class NotificationContractTests(unittest.TestCase):
    def check(self, card: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "INTENTS.md"
            path.write_text(registry(card))
            return subprocess.run(
                ["python3", str(ROOT / "scripts/check_intents_consistency.py"), str(path)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_open_intent_requires_destination(self) -> None:
        result = self.check("### [work-1] 누락\n- status: inbox\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing terminal notification", result.stderr)

    def test_open_intent_with_destination_passes(self) -> None:
        result = self.check(
            "### [work-1] 수신 대상\n- status: inbox\n- notification_channel: telegram\n- notification_target: 433493318\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
