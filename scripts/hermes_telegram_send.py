#!/usr/bin/env python3
"""Bounded Telegram transport for Infinity's existing OpenClaw-style send boundary.

The logical destination (including telegram:) remains in Infinity receipts. This
adapter translates it only at the outbound API call. Callback ingress is NOT
provided here; do not enable the notifier until the receiving bot's callback
consumer has been independently verified.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import urllib.request
import uuid


_TARGET = re.compile(r"telegram:(-?[0-9]+)\Z")
_CALLBACK = re.compile(r"infinity:(approve|reject):[A-Za-z0-9._-]+\Z")


def chat_id(logical_target: str) -> str:
    match = _TARGET.fullmatch(logical_target)
    if not match:
        raise ValueError("Telegram logical target must retain its telegram: prefix")
    return match.group(1)


def photo_fields(target: str, body: str, card: dict | None, thread: str | None) -> dict[str, str]:
    if len(body) > 1024:
        raise ValueError("Telegram photo caption exceeds 1024 characters")
    fields = {"chat_id": chat_id(target), "caption": body}
    if thread:
        if not thread.isdigit():
            raise ValueError("Invalid Telegram topic")
        fields["message_thread_id"] = thread
    keyboard = []
    for block in (card or {}).get("blocks", []):
        if block.get("type") != "buttons":
            continue
        row = []
        for button in block.get("buttons", []):
            action = button.get("action", {})
            value = action.get("value", "")
            if action.get("type") != "callback" or not _CALLBACK.fullmatch(value) or len(value.encode()) > 64:
                raise ValueError("Unsupported Telegram callback")
            row.append({"text": str(button.get("label", "")), "callback_data": value})
        if row:
            keyboard.append(row)
    if keyboard:
        fields["reply_markup"] = json.dumps({"inline_keyboard": keyboard}, ensure_ascii=False)
    return fields


def _multipart(fields: dict[str, str], photo: bytes) -> tuple[bytes, str]:
    boundary = uuid.uuid4().hex
    chunks = []
    for name, value in fields.items():
        chunks.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n'.encode() + value.encode() + b"\r\n")
    chunks.append(f'--{boundary}\r\nContent-Disposition: form-data; name="photo"; filename="card.png"\r\nContent-Type: image/png\r\n\r\n'.encode() + photo + b"\r\n")
    chunks.append(f'--{boundary}--\r\n'.encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message", choices=["message"])
    parser.add_argument("send", choices=["send"])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--channel", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--media", required=True)
    parser.add_argument("--presentation")
    parser.add_argument("--thread-id")
    parser.add_argument("--reply-to")
    args = parser.parse_args(argv)
    try:
        if args.channel != "telegram" or args.reply_to:
            raise ValueError("Unsupported notification channel or reply primitive")
        card = json.loads(args.presentation) if args.presentation else None
        fields = photo_fields(args.target, args.message, card, args.thread_id)
        photo = Path(args.media).read_bytes()
        if not photo.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("Expected PNG card")
        token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
        if not token:
            raise ValueError("Telegram credential unavailable")
        body, content_type = _multipart(fields, photo)
        request = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendPhoto", data=body,
            headers={"Content-Type": content_type}, method="POST",
        )
        with urllib.request.urlopen(request, timeout=18) as response:
            result = json.load(response)
        if result.get("ok") is not True or not result.get("result", {}).get("message_id"):
            raise RuntimeError("Telegram delivery not confirmed")
        print(json.dumps({"ok": True, "message_id": result["result"]["message_id"]}))
        return 0
    except (ValueError, OSError, RuntimeError, json.JSONDecodeError, KeyError, TypeError):
        # Never echo the token, message, destination, or URL in errors.
        print("Telegram delivery not confirmed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
