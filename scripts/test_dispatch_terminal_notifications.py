#!/usr/bin/env python3
"""Controlled regression fixture for terminal notification reconciliation."""
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("dispatch_terminal_notifications.py")


def registry(waiting: bool = False, archived: bool = False) -> str:
    if archived:
        body = """## Inbox\n\n## Active\n\n## Waiting\n\n## Archive\n### [fixture-1] 완료 카드\n- status: archived\n- remote_verified: pass\n- notification_channel: mock\n- notification_target: original-thread\n- result: 원격 검증 완료\n- remote_commit: abc123\n- report: reports/fixture.md\n"""
    elif waiting:
        body = """## Inbox\n\n## Active\n\n## Waiting\n### [fixture-2] 승인 카드\n- status: waiting\n- notification_channel: mock\n- notification_target: original-thread\n- waiting_on: user\n- blocker: 선택이 필요함\n- next_action: A 또는 B를 고르기\n\n## Archive\n"""
    else:
        body = "## Inbox\n\n## Active\n\n## Waiting\n\n## Archive\n"
    return body


class TerminalNotificationTest(unittest.TestCase):
    def run_dispatch(self, intents: Path, state: Path, outbox: Path) -> dict:
        result = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox)], check=True, capture_output=True, text=True)
        return json.loads(result.stdout)

    def test_archive_once_replay_waiting_and_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 0)
            intents.write_text(registry(waiting=True))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            intents.write_text(registry())
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 0)
            lines = outbox.read_text().splitlines()
            self.assertEqual(len(lines), 2)
            self.assertIn("Infinity 완료", lines[0])
            self.assertIn("Infinity 승인/결정 필요", lines[1])
            receipts = json.loads(state.read_text())["deliveries"]
            self.assertEqual({receipt["state"] for receipt in receipts.values()}, {"sent"})
            self.assertTrue(all(receipt["remote_sha"].startswith("fixture:") for receipt in receipts.values()))

    def test_missing_origin_is_silent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True).replace("- notification_channel: mock\n- notification_target: original-thread\n", ""))
            result = self.run_dispatch(intents, state, outbox)
            self.assertEqual(result, {"sent": 0, "skipped_missing_destination": 1, "delivery_uncertain": 0})
            self.assertFalse(outbox.exists())

    def test_unverified_archive_is_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True).replace("- remote_verified: pass\n", ""))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 0)
            self.assertFalse(outbox.exists())

    def test_slack_reply_uses_reply_to_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True).replace("notification_channel: mock", "notification_channel: slack").replace("notification_target: original-thread", "notification_target: channel:C123\n- notification_reply_to: 1788296972.847769"))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            self.assertEqual(json.loads(outbox.read_text())["destination"]["reply_to"], "1788296972.847769")

    def test_concurrent_replay_emits_one_message(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True))
            command = ["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox)]
            first = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            second = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            first.communicate()
            second.communicate()
            self.assertEqual(first.returncode, 0)
            self.assertEqual(second.returncode, 0)
            self.assertEqual(len(outbox.read_text().splitlines()), 1)

    def test_known_preacceptance_failure_retries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True))
            failed = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--deliver", "--openclaw-bin", "/bin/false"], capture_output=True, text=True)
            self.assertEqual(failed.returncode, 2)
            retried = self.run_dispatch(intents, state, outbox)
            self.assertEqual(retried["sent"], 1)
            self.assertEqual(len(outbox.read_text().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
