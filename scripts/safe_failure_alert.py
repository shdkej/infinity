#!/usr/bin/env python3
"""Render dispatcher failures as one safe Korean status message.

Diagnostics stay in the local cycle record.  This module deliberately accepts
raw input only to classify it; neither its JSON result nor its outbox contains
that input, shell commands, exit codes, or stack traces.
"""
from __future__ import annotations
import argparse, hashlib, json, os
from pathlib import Path

MESSAGES = {
    "canonical_fetch_failed": "Infinity 점검을 시작하지 못했습니다. 원격 상태를 다시 확인한 뒤 재개하겠습니다.",
    "terminal": "상태 보고를 마치지 못했습니다. 내부 점검 후 안전하게 다시 확인하겠습니다.",
    "dashboard": "요청 처리를 마치지 못했습니다. 작업 상태를 보류하고 다시 확인하겠습니다.",
    "handoff": "실행 확인이 지연되고 있습니다. 작업을 중복 실행하지 않고 원인을 점검하겠습니다.",
    "verification": "원격 검증을 완료하지 못했습니다. 결과를 확정하지 않고 다시 확인하겠습니다.",
}

def render(stage: str, detail: str) -> dict[str, str]:
    code = stage if stage in MESSAGES else "verification"
    return {"reason_code": code, "user_message": MESSAGES[code], "diagnostic_hash": hashlib.sha256(detail.encode()).hexdigest()[:16]}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True); parser.add_argument("--detail-file", type=Path, required=True)
    parser.add_argument("--mock-outbox", type=Path); parser.add_argument("--channel"); parser.add_argument("--target"); parser.add_argument("--reply-to")
    args = parser.parse_args()
    result = render(args.stage, args.detail_file.read_text(encoding="utf-8", errors="replace"))
    if args.mock_outbox:
        args.mock_outbox.parent.mkdir(parents=True, exist_ok=True)
        destination = {"channel": args.channel or "slack", "target": args.target or "unspecified"}
        if args.reply_to: destination["reply_to"] = args.reply_to
        with args.mock_outbox.open("a", encoding="utf-8") as handle: handle.write(json.dumps({"destination": destination, "message": result["user_message"], "reason_code": result["reason_code"]}, ensure_ascii=False) + "\n")
    print(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__": raise SystemExit(main())
