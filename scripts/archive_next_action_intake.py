#!/usr/bin/env python3
"""Promote actionable Archive Card next actions into Inbox intents."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTENTS = ROOT / "INTENTS.md"
ARCHIVE_DIR = ROOT / "intents" / "archive"
NO_ACTION_RE = re.compile(r"^(없음|완료|no continuation|none|n/a|-)$", re.I)
PUBLIC_ACTION_RE = re.compile(
    r"(게시|발행|업로드|공유|링크\s*공유|광고|댓글|DM|디엠|메일|송신|전송|계정|가입|결제|비용|권한|시크릿|credential)",
    re.I,
)


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\n(?P<body>.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group("body") if match else ""


def replace_section(text: str, name: str, body: str) -> str:
    pattern = rf"(^## {re.escape(name)}\n)(?P<body>.*?)(?=^## |\Z)"
    return re.sub(pattern, lambda m: m.group(1) + body.rstrip() + "\n\n", text, flags=re.M | re.S)


def bracket_field(text: str, label: str) -> str:
    match = re.search(
        rf"^\[{re.escape(label)}\]\s*(?P<same>[^\n]*)\n?(?P<body>.*?)(?=^\[[^\]]+\]|\Z)",
        text,
        re.M | re.S,
    )
    if not match:
        return ""
    value = (match.group("same") or match.group("body") or "").strip()
    return re.sub(r"\s+", " ", value)


def bullet_field(text: str, key: str) -> str:
    match = re.search(rf"^\s*-\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text, re.M)
    return match.group(1).strip() if match else ""


def archive_card(text: str) -> dict[str, str]:
    return {
        "project": bracket_field(text, "프로젝트") or bullet_field(text, "archive_project"),
        "state": bracket_field(text, "상태") or bullet_field(text, "archive_state"),
        "result_criteria": bracket_field(text, "결과 기준") or bullet_field(text, "result_criteria"),
        "next_action": bracket_field(text, "다음 행동") or bullet_field(text, "next_action"),
        "next_action_intent": bullet_field(text, "next_action_intent"),
    }


def existing_ids(text: str) -> set[str]:
    return set(re.findall(r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+)*-\d+)\b", text))


def next_id(prefix: str, all_text: str) -> str:
    nums = [int(n) for n in re.findall(rf"\b{re.escape(prefix)}-(\d+)\b", all_text)]
    return f"{prefix}-{max(nums, default=0) + 1:03d}"


def prefix_for(intent_id: str) -> str:
    base = intent_id.rsplit("-", 1)[0] if "-" in intent_id else "followup"
    return base if base else "followup"


def has_similar_open_intent(open_text: str, source_id: str, next_action: str) -> str:
    entries = []
    for match in re.finditer(r"^### \[([^\]]+)\].*?(?=^### \[|\Z)", open_text, re.M | re.S):
        entries.append((match.group(1), match.group(0)))
    for entry_id, block in entries:
        if re.search(rf"source_archive:\s*intents/archive/{re.escape(source_id)}\.md", block):
            return entry_id
    action_words = [w for w in re.split(r"\s+", next_action) if len(w) >= 2][:4]
    if action_words:
        for entry_id, block in entries:
            if all(w in block for w in action_words):
                return entry_id
    return ""


def append_next_action_intent(path: Path, intent_id: str) -> None:
    text = path.read_text(encoding="utf-8")
    if re.search(r"^\s*-\s*next_action_intent\s*:", text, re.M):
        text = re.sub(r"^(\s*-\s*next_action_intent\s*:\s*).*$", rf"\g<1>{intent_id}", text, flags=re.M)
    else:
        marker = re.search(r"^\s*-\s*next_action\s*:\s*.+$", text, re.M)
        if marker:
            pos = marker.end()
            text = text[:pos] + f"\n- next_action_intent: {intent_id}" + text[pos:]
        else:
            text = text.rstrip() + f"\n- next_action_intent: {intent_id}\n"
    path.write_text(text, encoding="utf-8")


def build_inbox_entry(new_id: str, source_id: str, card: dict[str, str]) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    project = card["project"] or source_id
    next_action = card["next_action"]
    boundary = (
        "공개 게시·외부 계정 작업은 사용자 승인 전까지 실행하지 않고, 게시 후보/카피/체크리스트 준비까지만 수행한다."
        if PUBLIC_ACTION_RE.search(next_action)
        else "내부 실행 가능. 외부 발송·권한·비용 변경이 필요해지면 Waiting으로 전환한다."
    )
    return f"""### [{new_id}] {project} 후속 실행
- status: inbox
- target_agent: genie
- requested: {now}
- source_archive: intents/archive/{source_id}.md
- archive_project: {project}
- archive_state: {card["state"] or "후속 실행 필요"}
- result_criteria: {card["result_criteria"] or "후속 실행 결과를 확인한다"}
- next_action: {next_action}
- permission: approval-required-before-public-action
- goal: Archive 다음 행동을 실제 실행 가능한 작업으로 준비한다.
- success_criteria: {card["result_criteria"] or next_action}
- boundary: {boundary}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write INTENTS.md and archive files")
    args = parser.parse_args()

    intents_text = INTENTS.read_text(encoding="utf-8")
    open_text = "\n".join(section(intents_text, name) for name in ("Inbox", "Active", "Waiting"))
    all_text = intents_text + "\n" + "\n".join(p.read_text(encoding="utf-8") for p in ARCHIVE_DIR.glob("*.md"))
    inbox = section(intents_text, "Inbox").strip()
    additions: list[str] = []

    for path in sorted(ARCHIVE_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        source_id = path.stem
        text = path.read_text(encoding="utf-8")
        card = archive_card(text)
        next_action = card["next_action"].strip()
        if not next_action or NO_ACTION_RE.search(next_action):
            continue
        if card["next_action_intent"]:
            continue
        existing = has_similar_open_intent(open_text, source_id, next_action)
        if existing:
            if args.apply:
                append_next_action_intent(path, existing)
            print(f"linked {source_id} -> {existing}")
            continue
        new_id = next_id(prefix_for(source_id), all_text + "\n" + "\n".join(additions))
        additions.append(build_inbox_entry(new_id, source_id, card))
        if args.apply:
            append_next_action_intent(path, new_id)
        print(f"created {new_id} from {source_id}: {next_action}")

    if args.apply and additions:
        new_inbox = (inbox + "\n\n" if inbox else "") + "\n\n".join(additions)
        INTENTS.write_text(replace_section(intents_text, "Inbox", new_inbox), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
