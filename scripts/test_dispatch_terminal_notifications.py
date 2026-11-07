#!/usr/bin/env python3
"""Controlled regression fixture for terminal notification reconciliation."""
from __future__ import annotations

import json
import fcntl
import os
import sys
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

from PIL import Image


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
            first_payload, second_payload = (json.loads(line) for line in lines)
            self.assertTrue(first_payload["message"].startswith("✅ 완료 카드\n"))
            self.assertIn("Infinity 완료", first_payload["message"])
            self.assertTrue(second_payload["message"].startswith("⚠️ 승인 카드\n"))
            self.assertIn("Infinity 승인/결정 필요", second_payload["message"])
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

    def test_explicit_unknown_origin_is_silent_and_retires_old_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True).replace("notification_channel: mock", "notification_channel: delivery_unknown").replace("notification_target: original-thread", "notification_target: missing-at-intake"))
            state.write_text(json.dumps({"version": 2, "deliveries": {"old": {"intent_id": "fixture-1", "state": "failed_before_acceptance"}}}))
            result = self.run_dispatch(intents, state, outbox)
            self.assertEqual(result, {"sent": 0, "skipped_missing_destination": 1, "delivery_uncertain": 0})
            self.assertEqual(json.loads(state.read_text())["deliveries"]["old"]["state"], "superseded")
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

    def test_telegram_origin_thread_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            source = registry(archived=True).replace(
                "notification_channel: mock\n- notification_target: original-thread",
                "notification_channel: telegram\n- notification_target: telegram:433493318\n- notification_thread: 77",
            )
            intents.write_text(source)
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            self.assertEqual(json.loads(outbox.read_text())["destination"], {
                "channel": "telegram", "target": "telegram:433493318", "thread": "77",
            })

    def test_waiting_approval_required_is_not_hidden_and_has_buttons(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(waiting=True).replace("- waiting_on: user\n", "- approval_required: true\n- permission_level: approval_required\n"))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            payload = json.loads(outbox.read_text())
            self.assertTrue(payload["message"].startswith("⚠️ 승인 카드\n"))
            self.assertIn("Infinity 승인/결정 필요", payload["message"])
            self.assertEqual(payload["presentation"]["tone"], "warning")
            values = [button["action"]["value"] for button in payload["presentation"]["blocks"][-1]["buttons"]]
            self.assertIn("infinity:approve:fixture-2", values)
            self.assertIn("infinity:reject:fixture-2", values)

    def test_terminal_destination_ignores_legacy_override_and_preserves_origin(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            source = registry(archived=True).replace(
                "notification_channel: mock\n- notification_target: original-thread",
                "notification_channel: telegram\n- notification_target: telegram:111111\n- notification_thread: 77",
            )
            intents.write_text(source)
            result = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--terminal-channel", "telegram", "--terminal-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["sent"], 1)
            payload = json.loads(outbox.read_text())
            self.assertEqual(payload["destination"], {
                "channel": "telegram", "target": "telegram:111111", "thread": "77",
            })
            self.assertEqual(payload["presentation"]["tone"], "success")
            self.assertEqual(payload["presentation"]["blocks"][0]["type"], "text")
            media = Path(payload["media"])
            self.assertTrue(media.exists())
            with Image.open(media) as image:
                self.assertEqual(image.size, (1200, 675))

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
            failed = subprocess.run([sys.executable, str(SCRIPT), "--intents", str(intents), "--state", str(state), "--deliver", "--openclaw-bin", str(root / "missing-cli")], capture_output=True, text=True)
            self.assertEqual(failed.returncode, 2)
            receipt = next(iter(json.loads(state.read_text())["deliveries"].values()))
            self.assertEqual(receipt["state"], "failed_before_acceptance")
            self.assertEqual(receipt["failure_class"], "command_start_failed")
            event = json.loads(failed.stderr.splitlines()[0])
            self.assertEqual(event["outcome"], "retryable_pre_acceptance")
            self.assertNotIn("/tmp/", failed.stderr)
            retried = self.run_dispatch(intents, state, outbox)
            self.assertEqual(retried["sent"], 1)
            self.assertEqual(len(outbox.read_text().splitlines()), 1)

    def test_legacy_unclassified_preacceptance_receipt_is_not_replayed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text(registry(archived=True))
            self.assertEqual(self.run_dispatch(intents, state, outbox)["sent"], 1)
            ledger = json.loads(state.read_text())
            receipt = next(iter(ledger["deliveries"].values()))
            receipt["state"] = "failed_before_acceptance"
            receipt["attempt_started_at"] = receipt.get("sent_at", "legacy-attempt")
            receipt.pop("failure_class", None)
            state.write_text(json.dumps(ledger))
            replay = subprocess.run(
                [sys.executable, str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox)],
                capture_output=True, text=True,
            )
            self.assertEqual(replay.returncode, 2)
            self.assertEqual(len(outbox.read_text().splitlines()), 1)
            updated = next(iter(json.loads(state.read_text())["deliveries"].values()))
            self.assertEqual(updated["state"], "delivery_unknown")
            self.assertEqual(updated["failure_class"], "legacy_unverified_pre_acceptance")

    def make_cli(self, root: Path, *, stdout: str, stderr: str = "", exit_code: int = 0, sleep_seconds: float = 0) -> Path:
        script = root / "mock-openclaw"
        script.write_text(
            "#!/usr/bin/env python3\n"
            "import json,sys,time\n"
            "args=sys.argv[1:]\n"
            "body=args[args.index('--message')+1] if '--message' in args else ''\n"
            "with open(" + repr(str(root / "calls.jsonl")) + ", 'a') as f: f.write(json.dumps({'body':body})+'\\n')\n"
            "sys.stderr.write(" + repr(stderr) + ".replace('__BODY__', body))\n"
            "time.sleep(" + repr(sleep_seconds) + ")\n"
            "sys.stdout.write(" + repr(stdout) + ")\n"
            "sys.exit(" + str(exit_code) + ")\n"
        )
        script.chmod(0o755)
        return script

    def run_cli_dispatch(self, intents: Path, state: Path, cli: Path, *, send_timeout: float = 1) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--intents", str(intents), "--state", str(state),
             "--deliver", "--openclaw-bin", str(cli), "--send-timeout-seconds", str(send_timeout)],
            capture_output=True, text=True,
        )

    def test_nonzero_cli_exit_is_ambiguous_redacted_and_never_replayed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"
            intents.write_text(registry(archived=True))
            cli = self.make_cli(root, stdout="", stderr="secret=do-not-log Authorization: Bearer bearersecret123 https://user:pass@example.test/private __BODY__", exit_code=7)
            failed = self.run_cli_dispatch(intents, state, cli)
            self.assertEqual(failed.returncode, 2)
            receipt = next(iter(json.loads(state.read_text())["deliveries"].values()))
            self.assertEqual(receipt["state"], "delivery_unknown")
            self.assertEqual(receipt["failure_class"], "nonzero_exit")
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 1)
            self.assertNotIn("do-not-log", failed.stderr)
            self.assertNotIn("bearersecret123", failed.stderr)
            self.assertNotIn("user:pass", failed.stderr)
            self.assertNotIn("example.test", failed.stderr)
            self.assertNotIn("✅ 완료 카드", failed.stderr)
            self.assertIn("[redacted]", failed.stderr)
            replay = self.run_cli_dispatch(intents, state, cli)
            self.assertEqual(replay.returncode, 2)
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 1)

    def test_malformed_cli_response_is_ambiguous_and_never_replayed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"
            intents.write_text(registry(archived=True))
            cli = self.make_cli(root, stdout="not-json")
            failed = self.run_cli_dispatch(intents, state, cli)
            self.assertEqual(failed.returncode, 2)
            receipt = next(iter(json.loads(state.read_text())["deliveries"].values()))
            self.assertEqual(receipt["state"], "delivery_unknown")
            self.assertEqual(receipt["failure_class"], "malformed_response")
            self.run_cli_dispatch(intents, state, cli)
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 1)

    def test_send_timeout_is_bounded_ambiguous_and_never_replayed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"
            intents.write_text(registry(archived=True))
            cli = self.make_cli(root, stdout='{"ok":true}', sleep_seconds=1)
            started = time.monotonic()
            failed = self.run_cli_dispatch(intents, state, cli, send_timeout=0.05)
            self.assertLess(time.monotonic() - started, 0.8)
            self.assertEqual(failed.returncode, 2)
            receipt = next(iter(json.loads(state.read_text())["deliveries"].values()))
            self.assertEqual(receipt["state"], "delivery_unknown")
            self.assertEqual(receipt["failure_class"], "timeout")
            self.run_cli_dispatch(intents, state, cli, send_timeout=0.05)
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 1)

    def test_git_timeout_and_whole_run_budget_are_structured(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); fakebin = root / "bin"; fakebin.mkdir()
            fake_git = fakebin / "git"
            fake_git.write_text("#!/bin/sh\nsleep 1\n")
            fake_git.chmod(0o755)
            env = dict(os.environ, PATH=f"{fakebin}:{os.environ['PATH']}")
            started = time.monotonic()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--repo", str(root), "--state", str(root / "state.json"),
                 "--git-timeout-seconds", "1", "--run-timeout-seconds", "0.05"],
                capture_output=True, text=True, env=env,
            )
            self.assertLess(time.monotonic() - started, 0.8)
            self.assertEqual(result.returncode, 1)
            events = [json.loads(line) for line in result.stderr.splitlines() if line.startswith("{")]
            self.assertEqual(events[0]["phase"], "git")
            self.assertEqual(events[0]["failure_class"], "timeout")

    def test_whole_run_deadline_bounds_receipt_lock_wait(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.md"; state = root / "state.json"; lock_path = root / "held.lock"
            intents.write_text(registry(archived=True))
            with lock_path.open("w") as held:
                fcntl.flock(held, fcntl.LOCK_EX)
                started = time.monotonic()
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "--intents", str(intents), "--state", str(state),
                     "--lock", str(lock_path), "--run-timeout-seconds", "0.05", "--mock-outbox", str(root / "outbox.jsonl")],
                    capture_output=True, text=True,
                )
                self.assertLess(time.monotonic() - started, 0.8)
                self.assertEqual(result.returncode, 1)
                event = json.loads(result.stderr.splitlines()[0])
                self.assertEqual(event["phase"], "lock")
                self.assertEqual(event["failure_class"], "run_timeout")
                self.assertFalse((root / "outbox.jsonl").exists())

    def test_cron_setup_failure_is_nonzero_structured(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); nvm = root / "nvm"; bindir = root / "bin"
            nvm.mkdir(); bindir.mkdir()
            (nvm / "nvm.sh").write_text("nvm() { return 0; }\n")
            openclaw = bindir / "openclaw"
            openclaw.write_text("#!/bin/sh\nexit 0\n")
            openclaw.chmod(0o755)
            state_dir = root / "not-a-directory"
            state_dir.write_text("collision")
            env = dict(os.environ, NVM_DIR=str(nvm), NVM_BIN=str(bindir),
                       INFINITY_NOTIFICATION_STATE_DIR=str(state_dir),
                       INFINITY_NOTIFICATION_CARD_DIR=str(state_dir / "cards"))
            result = subprocess.run(["bash", str(SCRIPT.with_name("run_notification_cron.sh"))],
                                    capture_output=True, text=True, env=env)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stderr.splitlines()[-1])["failure_class"], "state_directory_unavailable")

    def test_yaml_new_intent_and_status_change_are_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "INTENTS.yaml"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            base = """version: 1
format: infinity-intents-yaml
lanes:
  backlog: []
  inbox:
    - id: fixture-1
      title: 첫 태스크
      task_name: 첫 태스크
      status: inbox
      notification_channel: telegram
      notification_target: telegram:111111
      notification_thread: "77"
  active: []
  waiting: []
"""
            intents.write_text(base)
            first = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--change-channel", "telegram", "--change-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(first.stdout)["sent"], 0)
            changed = """version: 1
format: infinity-intents-yaml
lanes:
  backlog: []
  inbox:
    - id: fixture-1
      title: 첫 태스크
      task_name: 첫 태스크
      status: inbox
    - id: fixture-2
      title: 새 태스크
      task_name: 새 태스크
      status: inbox
      notification_channel: telegram
      notification_target: telegram:222222
      notification_thread: "88"
  active: []
  waiting: []
"""
            intents.write_text(changed)
            created = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--change-channel", "telegram", "--change-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(created.stdout)["sent"], 1)
            created_payload = json.loads(outbox.read_text().splitlines()[0])
            self.assertTrue(created_payload["message"].startswith("🆕 새 태스크\n"))
            self.assertEqual(created_payload["destination"], {
                "channel": "telegram", "target": "telegram:222222", "thread": "88",
            })
            # Move the original item Inbox → Active, then Active → Waiting.
            changed = """version: 1
format: infinity-intents-yaml
lanes:
  backlog: []
  inbox:
    - id: fixture-2
      title: 새 태스크
      task_name: 새 태스크
      status: inbox
      notification_channel: telegram
      notification_target: telegram:222222
      notification_thread: "88"
  active:
    - id: fixture-1
      title: 첫 태스크
      task_name: 첫 태스크
      status: active
      notification_channel: telegram
      notification_target: telegram:111111
      notification_thread: "77"
  waiting: []
"""
            intents.write_text(changed)
            result = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--change-channel", "telegram", "--change-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["sent"], 1)
            changed_payload = json.loads(outbox.read_text().splitlines()[1])
            self.assertEqual(changed_payload["destination"], {
                "channel": "telegram", "target": "telegram:111111", "thread": "77",
            })
            changed = changed.replace("  active:\n    - id: fixture-1\n      title: 첫 태스크\n      task_name: 첫 태스크\n      status: active\n      notification_channel: telegram\n      notification_target: telegram:111111\n      notification_thread: \"77\"\n  waiting: []", "  active: []\n  waiting:\n    - id: fixture-1\n      title: 첫 태스크\n      task_name: 첫 태스크\n      status: waiting\n      notification_channel: telegram\n      notification_target: telegram:111111\n      notification_thread: \"77\"")
            intents.write_text(changed)
            result = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--change-channel", "telegram", "--change-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["sent"], 1)
            replay = subprocess.run(["python3", str(SCRIPT), "--intents", str(intents), "--state", str(state), "--mock-outbox", str(outbox), "--change-channel", "telegram", "--change-target", "telegram:433493318"], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(replay.stdout)["sent"], 0)
            self.assertEqual(len(outbox.read_text().splitlines()), 3)

    def test_yaml_archive_terminal_is_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); intents = root / "2026-10.yaml"; state = root / "state.json"; outbox = root / "outbox.jsonl"
            intents.write_text("""version: 1
period: 2026-10
archive:
  - id: fixture-archive
    title: 종료 태스크
    task_name: 종료 태스크
    status: archived
    remote_verified: pass
    notification_channel: mock
    notification_target: original-thread
    result: 원격 검증 완료
""")
            first = self.run_dispatch(intents, state, outbox)
            self.assertEqual(first["sent"], 1)
            second = self.run_dispatch(intents, state, outbox)
            self.assertEqual(second["sent"], 0)
            self.assertEqual(len(outbox.read_text().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
