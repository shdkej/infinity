#!/usr/bin/env python3
"""Build a readable Infinity morning recap for Telegram."""

from __future__ import annotations

import datetime as dt
import os
import re
import sqlite3
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTENTS = ROOT / "INTENTS.md"
GATES = ROOT / "GATES.md"
OPENCLAW_DB = Path("/home/ubuntu/.openclaw/state/openclaw.sqlite")
KST = dt.timezone(dt.timedelta(hours=9), name="KST")
CLOSED_STATES = {"completed", "resolved", "done", "archived", "closed", "canceled", "cancelled", "rejected", "approved", "failed"}
EVALUATOR_JOBS = {
    "f1027114-6430-433a-b4cb-6aa0dfc53157": "OpenClaw 평가",
    "986c49b2-c615-4134-b95a-2cf74217c5b7": "kl 평가",
}
ROUTER_JOB_ID = "7502ef19-45c7-45f9-aa0e-b05c40ba670e"


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


def parse_entries(body: str, state: str) -> list[dict[str, str]]:
    """Waiting/Active/Inbox의 실제 `### [id] 제목` 엔트리를 파싱한다.

    2026-07-15 이전 리캡은 HTML 주석만 읽어서, 사용자 행동을 기다리는
    Waiting 엔트리(ops-12·13)가 '대기 없음'으로 발송되는 누락이 있었다.
    """
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in body.splitlines():
        head = re.match(r"^### \[([^\]]+)\]\s*(.*)", line)
        if head:
            current = {
                "id": head.group(1),
                "state": state,
                "title": head.group(2).strip(),
                "display": head.group(2).strip() or head.group(1),
                "status": state,
                "summary": "",
                "fields": {},
                "progress_dates": [],
            }
            items.append(current)
            continue
        if current is None:
            continue
        field = re.match(r"^- ([a-zA-Z_][a-zA-Z0-9_]*):\s*(.+)", line)
        if field:
            key, value = field.group(1), field.group(2).strip()
            if key.startswith("progress_"):
                ts = re.search(r"(\d{8})", key)
                if ts:
                    current["progress_dates"].append(ts.group(1))
            else:
                current["fields"][key] = value
            if key == "status":
                current["status"] = value
    return items


def parse_iso_date(text: str) -> dt.date | None:
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text or "")
    if not match:
        return None
    try:
        return dt.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return None


def is_user_turn(entry: dict) -> bool:
    """waiting_on: user가 정본. 필드 없는 과거 엔트리는 waiting_reason 휴리스틱으로 보완."""
    waiting_on = entry["fields"].get("waiting_on", "").lower()
    if waiting_on:
        return waiting_on == "user"
    reason = entry["fields"].get("waiting_reason", "")
    return bool(re.search(r"로컬 Claude|사용자", reason))


def waited_days(entry: dict, today: dt.date) -> int | None:
    for key in ("approval", "requested", "waiting_reason"):
        d = parse_iso_date(entry["fields"].get(key, ""))
        if d:
            return (today - d).days
    return None


def your_turn_lines(waiting_entries: list[dict], today: dt.date) -> list[str]:
    lines = []
    for entry in waiting_entries:
        if not is_user_turn(entry):
            continue
        days = waited_days(entry, today)
        prefix = f"[{days}일째] " if days and days >= 2 else ""
        action = clean_summary(entry["fields"].get("next_action", ""), 90)
        line = f"{prefix}{entry['id']} {entry['display']}"
        if action:
            line += f" — 첫 액션: {action}"
        lines.append(line)
    return lines


def pipeline_line(entry: dict, today: dt.date) -> str:
    stages = []
    approval_date = parse_iso_date(entry["fields"].get("approval", ""))
    if approval_date:
        stages.append(f"L2 승인 {approval_date:%m-%d}")
    if entry["progress_dates"]:
        latest = max(entry["progress_dates"])
        stages.append(f"L3 진행 {latest[4:6]}-{latest[6:8]}")
    if entry["state"] == "waiting":
        stages.append("내 공(내 손 대기)" if is_user_turn(entry) else "대기(외부/에이전트)")
    else:
        stages.append("실행중")
    flow = " → ".join(stages) if stages else entry["status"]
    return f"{entry['id']} {entry['display']} — {flow}"


def parse_comments(body: str, state: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for comment in re.findall(r"<!--\s*(.*?)\s*-->", body, re.S):
        compact = re.sub(r"\s+", " ", comment).strip()
        head = re.match(
            r"(?P<id>[a-z]+(?:-[a-z]+)*-\d+)\s+(?P<state>\w+)(?:\s+(?P<ts>\d{4}-\d{2}-\d{2}(?:[T\s](?:\d{2}:\d{2}(?::\d{2})?|\d{4}(?:\d{2})?)Z?)?))?",
            compact,
        )
        if not head:
            continue
        comment_state = (head.group("state") or "").lower()
        if state != "completed" and comment_state in CLOSED_STATES:
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
        match = re.match(
            r"(\d{4})-(\d{2})-(\d{2})(?:[T\s](?:(\d{2}):(\d{2})(?::(\d{2}))?|(\d{2})(\d{2})(\d{2})?))?",
            item["ts"],
        )
        if not match:
            continue
        year, month, day, hour, minute, second, compact_hour, compact_minute, compact_second = match.groups()
        ts = dt.datetime(
            int(year),
            int(month),
            int(day),
            int(hour or compact_hour or 0),
            int(minute or compact_minute or 0),
            int(second or compact_second or 0),
            tzinfo=dt.timezone.utc,
        )
        if ts >= cutoff:
            enriched = dict(item)
            enriched["_ts_dt"] = ts
            recent.append(enriched)
    return sorted(recent, key=lambda x: x["_ts_dt"], reverse=True)


def pending_gates(text: str) -> int:
    pending = section(text, "대기 중")
    return len(re.findall(r"^###\s+", pending, re.M))


def bullet(items: list[str], empty: str) -> str:
    if not items:
        return f"• {empty}"
    return "\n".join(f"• {item}" for item in items)


def recent_commit_events(since: str) -> list[dict[str, str]]:
    raw = run_git(
        [
            "log",
            f"--since={since}",
            "--date=iso-strict",
            "--format=%cI%x09%s",
            "--",
            "reports/",
            "INTENTS.md",
            "GATES.md",
        ]
    )
    events: list[dict[str, str]] = []
    for line in raw.splitlines():
        if not line.strip() or "\t" not in line:
            continue
        ts_raw, subject = line.split("\t", 1)
        try:
            ts = dt.datetime.fromisoformat(ts_raw).astimezone(KST)
        except ValueError:
            continue
        events.append(
            {
                "hour": f"{ts:%H}",
                "minute": f"{ts:%M}",
                "source": "클라우드",
                "subject": clean_summary(subject, 48),
            }
        )
    return events


def router_events(start_utc: dt.datetime, end_utc: dt.datetime) -> list[dict[str, str]]:
    if not OPENCLAW_DB.exists():
        return []
    start_ms = int(start_utc.timestamp() * 1000)
    end_ms = int(end_utc.timestamp() * 1000)
    try:
        with sqlite3.connect(OPENCLAW_DB) as conn:
            rows = conn.execute(
                """
                select run_at_ms, status, coalesce(summary, ''), coalesce(error, '')
                from cron_run_logs
                where job_id = ?
                  and run_at_ms >= ?
                  and run_at_ms < ?
                order by run_at_ms asc
                """,
                (ROUTER_JOB_ID, start_ms, end_ms),
            ).fetchall()
    except sqlite3.Error:
        return []

    events: list[dict[str, str]] = []
    for run_at_ms, status, summary, error in rows:
        ts = dt.datetime.fromtimestamp(run_at_ms / 1000, dt.timezone.utc).astimezone(KST)
        text = "" if summary.strip() == "NO_REPLY" else clean_summary(error or summary, 72)
        if error or status != "ok":
            subject = text or status or "실패"
        else:
            subject = text
        events.append(
            {
                "hour": f"{ts:%H}",
                "minute": f"{ts:%M}",
                "source": "로컬",
                "subject": subject,
            }
        )
    return events


def hourly_timeline(now_kst: dt.datetime, events: list[dict[str, str]]) -> str:
    notes_by_hour: dict[str, list[dict[str, str]]] = {}
    for event in events:
        notes_by_hour.setdefault(event["hour"], []).append(event)

    start = now_kst.replace(minute=0, second=0, microsecond=0) - dt.timedelta(hours=23)
    rows: list[str] = []
    for offset in range(24):
        hour = (start + dt.timedelta(hours=offset)).strftime("%H")
        notes = notes_by_hour.get(hour, [])
        if notes:
            visible = [note for note in notes if note["subject"]]
            if visible:
                parts = [f"[{note['source']}] {note['subject']}" for note in visible[:2]]
                suffix = f" 외 {len(visible) - 2}건" if len(visible) > 2 else ""
                rows.append(f"🟩{hour} {' / '.join(parts)}{suffix}")
            else:
                rows.append(f"⬜️{hour}")
        else:
            rows.append(f"⬜️{hour}")
    return "\n".join(rows)


def evaluator_events(start_utc: dt.datetime, end_utc: dt.datetime) -> list[dict[str, str]]:
    if not OPENCLAW_DB.exists():
        return []
    start_ms = int(start_utc.timestamp() * 1000)
    end_ms = int(end_utc.timestamp() * 1000)
    placeholders = ",".join("?" for _ in EVALUATOR_JOBS)
    query = f"""
        select job_id, run_at_ms, status, coalesce(summary, ''), coalesce(error, '')
        from cron_run_logs
        where job_id in ({placeholders})
          and run_at_ms >= ?
          and run_at_ms < ?
        order by run_at_ms asc
    """
    try:
        with sqlite3.connect(OPENCLAW_DB) as conn:
            rows = conn.execute(query, [*EVALUATOR_JOBS.keys(), start_ms, end_ms]).fetchall()
    except sqlite3.Error:
        return []

    events: list[dict[str, str]] = []
    for job_id, run_at_ms, status, summary, error in rows:
        ts = dt.datetime.fromtimestamp(run_at_ms / 1000, dt.timezone.utc).astimezone(KST)
        raw = error or summary or status or ""
        text = clean_summary(raw, 82)
        quiet = status == "ok" and (not summary or summary.strip() == "NO_REPLY") and not error
        if error or status != "ok":
            marker = "🟥"
            note = text or status or "error"
        elif quiet:
            marker = "⬜️"
            note = "특이사항 없음"
        else:
            marker = "🟩"
            note = text
        events.append(
            {
                "time": f"{ts:%H:%M}",
                "marker": marker,
                "name": EVALUATOR_JOBS.get(job_id, job_id),
                "note": note,
            }
        )
    return events


def evaluator_timeline(events: list[dict[str, str]]) -> str:
    if not events:
        return "⬜️ 평가기 실행 기록 없음"
    names = list(dict.fromkeys(event["name"] for event in events))
    parts = []
    for name in names:
        name_events = [event for event in events if event["name"] == name]
        failures = sum(1 for event in name_events if event["marker"] == "🟥")
        findings = sum(1 for event in name_events if event["marker"] == "🟩")
        parts.append(f"{name} {len(name_events)}회 · 정상 {len(name_events) - failures} · 기록 {findings} · 실패 {failures}")
    summary = "요약: " + " / ".join(parts)
    visible = [event for event in events if event["marker"] != "⬜️"]
    rows = [f"{event['marker']}{event['time']} {event['name']} · {event['note']}" for event in visible[:8]]
    if len(visible) > 8:
        rows.append(f"… 외 {len(visible) - 8}건")
    if not rows:
        rows.append("⬜️ 특이사항 없음")
    return "\n".join([summary, *rows])


def main() -> None:
    now_utc = dt.datetime.now(dt.timezone.utc)
    now_kst = now_utc.astimezone(KST)
    since_dt = now_utc - dt.timedelta(hours=24)
    since = since_dt.isoformat()
    cloud_events = recent_commit_events(since)
    local_events = router_events(since_dt, now_utc)
    timeline_events = [*cloud_events, *local_events]
    eval_events = evaluator_events(since_dt, now_utc)
    commit_count = len(
        [
            line
            for line in run_git(["log", f"--since={since}", "--format=%H", "--", "reports/", "INTENTS.md", "GATES.md"]).splitlines()
            if line.strip()
        ]
    )

    intents_text = INTENTS.read_text(encoding="utf-8")
    gates_text = GATES.read_text(encoding="utf-8") if GATES.exists() else ""

    today_kst = now_kst.date()
    inbox = parse_entries(section(intents_text, "Inbox"), "inbox")
    active = parse_entries(section(intents_text, "Active"), "active")
    waiting = parse_entries(section(intents_text, "Waiting"), "waiting")
    archive = parse_comments(section(intents_text, "Archive"), "completed")
    completed = recent_completed(archive, now_utc)

    # 블록 1 — 내 공: 사용자 손을 기다리는 것만
    turn_lines = your_turn_lines(waiting, today_kst)
    gates_count = pending_gates(gates_text)
    if gates_count:
        turn_lines.insert(0, f"게이트 승인 대기 {gates_count}건 (GATES.md)")

    # 블록 2 — 시스템이 한 일 (최근 24시간)
    completed_lines = [
        f"{item['display']} — {item['summary'] or item['id']}" for item in completed[:5]
    ]
    # 완료됐지만 미통보: notified 규약(2026-07-16~) 이후 완료분만 검사
    unnotified = [
        item for item in completed
        if item["_ts_dt"].date() >= dt.date(2026, 7, 16) and "notified" not in item.get("summary", "")
    ]

    # 블록 3 — 흐르는 중: 요청별 파이프라인 위치
    flow_lines = [pipeline_line(e, today_kst) for e in (active + waiting)[:6]]
    flow_lines += [f"{e['id']} {e['display']} — 접수(Inbox)" for e in inbox[:3]]

    open_count = len(inbox) + len(active)
    if turn_lines:
        headline = f"제 쪽이 아니라 마스터님 손을 기다리는 게 {len(turn_lines)}건 있습니다."
    elif completed:
        headline = f"최근 24시간 완료 {len(completed)}건, 흐르는 중 {open_count + len(waiting)}건. 마스터님 손 대기는 없습니다."
    elif inbox or active or waiting:
        headline = "새 완료는 없고, 이어갈 작업만 남아 있습니다."
    else:
        headline = "새 완료와 열린 작업이 모두 조용합니다."

    unnotified_note = (
        f"\n⚠️ 완료됐지만 미통보 {len(unnotified)}건: " + ", ".join(i["id"] for i in unnotified)
        if unnotified else ""
    )

    message = f"""🌅 Infinity 07:00 리캡
{now_kst:%Y-%m-%d} KST · 최근 24시간 · 관련 커밋 {commit_count}개 · 로컬 라우터 {len(local_events)}회

{headline}

---
🙋 내 공 — 오늘 마스터님이 하실 것
{bullet(turn_lines, "제 쪽에서 기다리는 건 없습니다")}

---
✅ 시스템이 한 일 (24시간)
{bullet(completed_lines, "최근 24시간 완료 Archive 없음")}{unnotified_note}

---
🔄 흐르는 중 — 요청별 위치
{bullet(flow_lines, "흐르는 중인 요청 없음")}

---
로컬/클라우드 타임라인
{hourly_timeline(now_kst, timeline_events)}

---
평가기
{evaluator_timeline(eval_events)}
"""
    print(message.strip())


if __name__ == "__main__":
    main()
