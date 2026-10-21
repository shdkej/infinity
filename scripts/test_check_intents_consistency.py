#!/usr/bin/env python3
"""Regression tests for the canonical YAML lifecycle and dashboard ledger contract."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def registry(*, notification: bool = False, manifest: str = "") -> str:
    destination = (
        "    notification_channel: telegram\n"
        "    notification_target: 433493318\n"
        if notification
        else ""
    )
    files = f"  files:\n  - {manifest}\n" if manifest else "  files: []\n"
    return (
        "version: 1\n"
        "format: infinity-intents-yaml\n"
        "lanes:\n"
        "  inbox:\n"
        "  - id: work-1\n"
        "    title: 테스트 작업\n"
        "    task_name: 테스트 작업\n"
        "    status: inbox\n"
        "    user_intent: 테스트\n"
        "    desired_outcome: 테스트\n"
        "    out_of_scope: 테스트\n"
        "    success_evidence: 테스트\n"
        + destination
        + "  active: []\n"
        + "  waiting: []\n"
        + "archive:\n"
        + files
    )


class CanonicalYamlContractTests(unittest.TestCase):
    def check(self, content: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "INTENTS.yaml"
            path.write_text(content, encoding="utf-8")
            return subprocess.run(
                ["python3", str(ROOT / "scripts/check_intents_consistency.py"), str(path)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_open_intent_requires_destination(self) -> None:
        result = self.check(registry())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing terminal notification", result.stderr)

    def test_open_intent_with_destination_passes(self) -> None:
        result = self.check(registry(notification=True))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_archive_manifest_rejects_detail_markdown(self) -> None:
        result = self.check(registry(notification=True, manifest="intents/archive/work-1.md"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not a monthly YAML ledger", result.stderr)


if __name__ == "__main__":
    unittest.main()
