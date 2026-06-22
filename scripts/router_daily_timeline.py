#!/usr/bin/env python3
"""Build the daily Infinity router timeline in the user's preferred format."""

from __future__ import annotations

import datetime as dt
import sqlite3
from pathlib import Path


DB = Path("/home/ubuntu/.openclaw/state/openclaw.sqlite")
ROUTER_JOB_ID = "7502ef19-45c7-45f9-aa0e-b05c40ba670e"
KST = dt.timezone(dt.timedelta(hours=9), name="KST")


def clean_summary(summary: str | None, limit: int = 90) -> str:
    if not summary:
        return ""
    text = " ".join(summary.strip().split())
    if text == "NO_REPLY":
        return ""
    return text[: limit - 1].rstrip() + "…" if len(text) > limit else text


def main() -> None:
    now_kst = dt.datetime.now(KST)
    start_kst = now_kst.replace(hour=0, minute=0, second=0, microsecond=0)
    end_kst = start_kst + dt.timedelta(days=1)
    start_ms = int(start_kst.astimezone(dt.timezone.utc).timestamp() * 1000)
    end_ms = int(end_kst.astimezone(dt.timezone.utc).timestamp() * 1000)

    with sqlite3.connect(DB) as conn:
        rows = conn.execute(
            """
            select run_at_ms, summary
            from cron_run_logs
            where job_id = ?
              and run_at_ms >= ?
              and run_at_ms < ?
            order by run_at_ms asc
            """,
            (ROUTER_JOB_ID, start_ms, end_ms),
        ).fetchall()

    lines: list[str] = []
    work_count = 0
    for run_at_ms, summary in rows:
        ts_kst = dt.datetime.fromtimestamp(run_at_ms / 1000, dt.timezone.utc).astimezone(KST)
        note = clean_summary(summary)
        if note:
            work_count += 1
            lines.append(f"🟩 {ts_kst:%H:%M} {note}")
        else:
            lines.append(f"⬜️ {ts_kst:%H:%M}")

    if not lines:
        lines.append("⬜️ 실행 기록 없음")

    total = len(rows)
    quiet_count = total - work_count
    if work_count:
        one_line = f"오늘 KST 기준 라우터 실행 {total}회 중 작업/알림 {work_count}회, 조용한 실행 {quiet_count}회였습니다."
    else:
        one_line = f"오늘 KST 기준 라우터 실행 {total}회 모두 조용한 실행이었습니다."

    message = f"""[인피니티 라우터 요약] {now_kst:%Y-%m-%d} KST

시간순
{chr(10).join(lines)}

한줄 요약: {one_line}"""
    print(message.strip())


if __name__ == "__main__":
    main()
