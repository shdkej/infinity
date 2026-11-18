#!/usr/bin/env python3
"""Offline transport compatibility tests: never contact Telegram."""
import json
import unittest
from unittest.mock import patch
import hermes_telegram_send as bridge


class TelegramBridgeTest(unittest.TestCase):
    def test_logical_target_only_normalized_at_transport(self):
        self.assertEqual(bridge.chat_id("telegram:433493318"), "433493318")
        with self.assertRaises(ValueError):
            bridge.chat_id("433493318")

    def test_image_and_approval_buttons_remain_in_one_message(self):
        card = {"blocks": [{"type": "buttons", "buttons": [
            {"label": "승인", "action": {"type": "callback", "value": "infinity:approve:fixture-2"}},
            {"label": "보류", "action": {"type": "callback", "value": "infinity:reject:fixture-2"}},
        ]}]}
        payload = bridge.photo_fields("telegram:433493318", "⚠️ · 검증", card, "19")
        self.assertEqual(payload["chat_id"], "433493318")
        self.assertEqual(payload["message_thread_id"], "19")
        buttons = json.loads(payload["reply_markup"])["inline_keyboard"]
        self.assertEqual(buttons[0][0]["callback_data"], "infinity:approve:fixture-2")
        self.assertEqual(buttons[0][1]["callback_data"], "infinity:reject:fixture-2")

    def test_transport_builds_single_photo_request_without_network(self):
        import io
        from contextlib import redirect_stdout
        from pathlib import Path
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            media = Path(tmp) / "card.png"
            media.write_bytes(b"\x89PNG\r\n\x1a\nfixture")
            response = io.BytesIO(b'{"ok":true,"result":{"message_id":42}}')
            with patch.dict("os.environ", {"TELEGRAM_BOT_TOKEN": "fixture-only"}), \
                 patch.object(bridge.urllib.request, "urlopen", return_value=response) as urlopen, \
                 redirect_stdout(io.StringIO()) as stdout:
                code = bridge.main(["message", "send", "--json", "--channel", "telegram",
                                    "--target", "telegram:433493318", "--message", "검증",
                                    "--media", str(media)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(stdout.getvalue())["message_id"], 42)
            request = urlopen.call_args.args[0]
            self.assertIn("/sendPhoto", request.full_url)
            self.assertIn(b"433493318", request.data)
            self.assertIn(b"photo", request.data)

    def test_unexpected_callback_and_long_body_fail_before_send(self):
        bad = {"blocks": [{"type": "buttons", "buttons": [
            {"label": "x", "action": {"type": "callback", "value": "other:bad"}},
        ]}]}
        with self.assertRaises(ValueError):
            bridge.photo_fields("telegram:433493318", "test", bad, None)
        with self.assertRaises(ValueError):
            bridge.photo_fields("telegram:433493318", "x" * 1025, None, None)


if __name__ == "__main__":
    unittest.main()
