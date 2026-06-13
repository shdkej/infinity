#!/usr/bin/env python3
"""Build a readable Infinity morning recap for Telegram."""

from __future__ import annotations

import datetime as dt
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTENTS = ROOT / "INTENTS.md"
GATES = ROOT / "GATES.md"
KST = dt.timezone(dt.timedelta(hours=9), name="KST")


def run_git(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except subprocess.CalledProcessError:
        return ""


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\n(?P<body>.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group("body").strip() if match else ""


def clean_summary(raw: str, limit: int = 120) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", raw)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    # Prefer the first complete thought, not the whole archive paragraph.
    first = re.split(r"(?<=[.!?。])\s+|\. |; |\) ", text, maxsplit=1)[0].strip()
    if len(first) < 18:
        first = text
    return first[: limit - 1].rstrip() + "…" if len(first) > limit else first


def parse_comments(body: str, state: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for comment in re.findall(r"<!--\s*(.*?)\s*-->", body, re.S):
        compact = re.sub(r"\s+", " ", comment).strip()
        head = re.match(r"(?P<id>[a-z]+(?:-[a-z]+)*-\d+)\s+(?P<state>\w+)\s+(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z)?", compact)
        if not head:
            continue
        display = re.search(r"\[display:\s*([^;\]]+)", compact)
        status = re.search(r"status:\s*([^;\]]+)", compact)
        summary = re.search(r"\]\s*\((.*)\)\s*$", compact)
        items.append(
            {
                "id": head.group("id"),
                "state": state,
                "ts": head.group("ts") or "",
                "display": (display.group(1).strip() if display else head.group("id")),
                "status": (status.group(1).strip() if status else state),
                "summary": clean_summary(summary.group(1)) if summary else "",
            }
        )
    return items


def recent_completed(items: list[dict[str, str]], now_utc: dt.datetime) -> list[dict[str, str]]:
    cutoff = now_utc - dt.timedelta(hours=24)
    recent: list[dict[str, str]] = []
    for item in items:
        if not item["ts"]:
            continue
        try:
            ts = dt.datetime.strptime(item["ts"], "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
        if ts >= cutoff:
            recent.append(item)
    return recent


def pending_gates(text: str) -> int:
    pending = section(text, "대기 중")
    return len(re.findall(r"^###\s+", pending, re.M))


def bullet(items: list[str], empty: str) -> str:
    if not items:
        return f"• {empty}"
    return "\n".join(f"• {item}" for item in items)


def main() -> None:
    now_utc = dt.datetime.now(dt.timezone.utc)
    now_kst = now_utc.astimezone(KST)
    since = (now_utc - dt.timedelta(hours=24)).isoformat()
    commit_count = len(
        [
            line
            for line in run_git(["log", f"--since={since}", "--format=%H", "--", "reports/", "INTENTS.md", "GATES.md"]).splitlines()
            if line.strip()
        ]
    )

    intents_text = INTENTS.read_text(encoding="utf-8")
    gates_text = GATES.read_text(encoding="utf-8") if GATES.exists() else ""

    inbox = parse_comments(section(intents_text, "Inbox"), "inbox")
    active = parse_comments(section(intents_text, "Active"), "active")
    waiting = parse_comments(section(intents_text, "Waiting"), "waiting")
    archive = parse_comments(section(intents_text, "Archive"), "completed")
    completed = recent_completed(archive, now_utc)

    completed_lines = [
        f"{item['display']} — {item['summary'] or item['id']}" for item in completed[:5]
    ]
    next_lines = [
        f"{item['display']} ({item['status']})" for item in (inbox + active)[:5]
    ]
    waiting_lines = [f"{item['display']} ({item['status']})" for item in waiting[:3]]
    gates_count = pending_gates(gates_text)
    if gates_count:
        waiting_lines.insert(0, f"승인 대기 {gates_count}건")

    open_count = len(inbox) + len(active)
    waiting_count = len(waiting) + gates_count
    if completed:
        headline = f"최근 24시간 완료 {len(completed)}건, 열린 실행 {open_count}건, 대기 {waiting_count}건입니다."
    elif inbox or active:
        headline = "새 완료는 없고, 이어갈 작업만 남아 있습니다."
    else:
        headline = "새 완료와 열린 작업이 모두 조용합니다."

    message = f"""🌅 Infinity 07:00 리캡
{now_kst:%Y-%m-%d} KST · 최근 24시간 · 관련 커밋 {commit_count}개

{headline}

━━━━━━━━━━━━━━
✅ 완료
{bullet(completed_lines, "최근 24시간 완료 Archive 없음")}

━━━━━━━━━━━━━━
➡️ 다음
{bullet(next_lines, "Inbox/Active 비어 있음")}

━━━━━━━━━━━━━━
🟡 대기
{bullet(waiting_lines, "승인/외부 조건 대기 없음")}
"""
    print(message.strip())


if __name__ == "__main__":
    main()
