#!/usr/bin/env python3
"""Consume queued Infinity dashboard action requests from S3."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any

import boto3


ROOT = Path(__file__).resolve().parents[1]
INTENTS = ROOT / "INTENTS.md"
ACTION_LOG_DIR = ROOT / "artifacts" / "dashboard-actions"
DEFAULT_BUCKET = os.environ.get("INFINITY_ACTION_QUEUE_BUCKET", "infinity-action-queue-917213086376-ap-northeast-2")
INBOX_PREFIX = "action_requests/inbox/"
PROCESSED_PREFIX = "action_requests/processed/"
REJECTED_PREFIX = "action_requests/rejected/"
ALLOWED_ACTIONS = {"resolve_waiting", "archive_request", "refresh_dashboard", "knowledge_research"}
INTENT_ID_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*-\d+$")
KNOWLEDGE_LOOP_ID_RE = re.compile(r"^kl-loop-[a-z0-9]+(?:-[a-z0-9]+)+$")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\n(?P<body>.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group("body") if match else ""


def has_open_intent(intent_id: str, text: str) -> bool:
    for lane in ("Inbox", "Active", "Waiting"):
        if re.search(rf"^### \[{re.escape(intent_id)}\]", section(text, lane), re.M):
            return True
    return False


def linked_loop_intent(loop_id: str, text: str) -> str:
    match = re.search(rf"^### \[([^\]]+)\][\s\S]*?^\s*- origin_loop_id: {re.escape(loop_id)}\s*$", text, re.M)
    return match.group(1) if match else ""


def next_research_id(text: str) -> str:
    ids = [int(value) for value in re.findall(r"^### \[research-(\d+)\]", text, re.M)]
    return f"research-{max(ids, default=0) + 1}"


def create_knowledge_research_intent(record: dict[str, str], text: str) -> tuple[str, str]:
    existing = linked_loop_intent(record["intent_id"], text)
    if existing:
        return existing, text
    intent_id = next_research_id(text)
    title = record["title"] or "Agent Wiki 재검색"
    block = (
        f"### [{intent_id}] {title}\n"
        "- status: inbox\n- target_agent: genie\n- priority: normal\n"
        "- permission: L0-research-and-strategy\n- execution_mode: multi_subagent_roles\n"
        "- projects: agent-wiki,infinity,knowledge-lab\n- task_type: research\n"
        f"- origin_loop_id: {record['intent_id']}\n"
        f"- source_url: {record['page']}\n"
        f"- goal: {record['note'] or title}\n"
        "- next_action: 구조화된 loop event에 결과 페이지·결정·commit을 연결해 루프를 닫는다.\n\n"
    )
    marker = "## Inbox\n"
    if marker not in text:
        raise ValueError("missing_inbox_section")
    return intent_id, text.replace(marker, marker + "\n" + block, 1)


def clean_record(raw: dict[str, Any]) -> dict[str, str]:
    return {
        "request_id": str(raw.get("request_id") or "").strip(),
        "created_at": str(raw.get("created_at") or "").strip(),
        "intent_id": str(raw.get("intent_id") or "").strip(),
        "action": str(raw.get("action") or "").strip(),
        "source": str(raw.get("source") or "").strip(),
        "title": str(raw.get("title") or "").strip(),
        "page": str(raw.get("page") or "").strip(),
        "note": str(raw.get("note") or "").strip(),
    }


def validate_record(record: dict[str, str], intents_text: str) -> str:
    if not record["request_id"]:
        return "missing_request_id"
    is_knowledge_loop = record["action"] == "knowledge_research"
    if not (KNOWLEDGE_LOOP_ID_RE.match(record["intent_id"]) if is_knowledge_loop else INTENT_ID_RE.match(record["intent_id"])):
        return "invalid_intent_id"
    if record["action"] not in ALLOWED_ACTIONS:
        return "unsupported_action"
    if record["action"] != "refresh_dashboard" and not is_knowledge_loop and not has_open_intent(record["intent_id"], intents_text):
        return "intent_not_open"
    return ""


def append_action_log(record: dict[str, str], object_key: str) -> None:
    ACTION_LOG_DIR.mkdir(parents=True, exist_ok=True)
    date = utc_now()[:10]
    path = ACTION_LOG_DIR / f"{date}.md"
    line = (
        f"- {utc_now()} `{record['action']}` requested for `{record['intent_id']}` "
        f"from `{record['source'] or 'dashboard'}`; request `{record['request_id']}`; "
        f"s3 `{object_key}`"
    )
    if record["note"]:
        line += f"; note: {record['note']}"
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def write_local_request(record: dict[str, str]) -> Path:
    target_dir = ACTION_LOG_DIR / "requests"
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f"{record['request_id']}.json"
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def move_s3_object(s3, bucket: str, key: str, target_prefix: str, reason: str = "") -> str:
    target = target_prefix + key.removeprefix(INBOX_PREFIX)
    s3.copy_object(
        Bucket=bucket,
        CopySource={"Bucket": bucket, "Key": key},
        Key=target,
        MetadataDirective="REPLACE",
        Metadata={"processed_at": utc_now(), **({"reason": reason[:200]} if reason else {})},
        ServerSideEncryption="AES256",
    )
    s3.delete_object(Bucket=bucket, Key=key)
    return target


def delete_dedupe_marker(s3, bucket: str, record: dict[str, str]) -> None:
    key = f"action_requests/dedupe/{record['intent_id']}/{record['action']}.json"
    s3.delete_object(Bucket=bucket, Key=key)


def list_request_keys(s3, bucket: str, limit: int) -> list[str]:
    paginator = s3.get_paginator("list_objects_v2")
    keys: list[str] = []
    for page in paginator.paginate(Bucket=bucket, Prefix=INBOX_PREFIX):
        for obj in page.get("Contents", []):
            key = obj.get("Key", "")
            if key.endswith(".json"):
                keys.append(key)
                if len(keys) >= limit:
                    return sorted(keys)
    return sorted(keys)


def process(bucket: str, apply: bool, limit: int) -> list[dict[str, str]]:
    s3 = boto3.client("s3")
    intents_text = INTENTS.read_text(encoding="utf-8")
    results: list[dict[str, str]] = []
    for key in list_request_keys(s3, bucket, limit):
        raw = json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read().decode("utf-8"))
        record = clean_record(raw)
        error = validate_record(record, intents_text)
        result = {"key": key, **record, "result": "rejected" if error else "accepted", "error": error}
        results.append(result)
        if not apply:
            continue
        if error:
            move_s3_object(s3, bucket, key, REJECTED_PREFIX, error)
            delete_dedupe_marker(s3, bucket, record)
            continue
        if record["action"] == "knowledge_research":
            linked_id, updated = create_knowledge_research_intent(record, intents_text)
            if updated != intents_text:
                INTENTS.write_text(updated, encoding="utf-8")
                intents_text = updated
            result["linked_intent_id"] = linked_id
        append_action_log(record, key)
        local_path = write_local_request(record)
        move_s3_object(s3, bucket, key, PROCESSED_PREFIX)
        delete_dedupe_marker(s3, bucket, record)
        result["local_path"] = str(local_path.relative_to(ROOT))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", default=DEFAULT_BUCKET)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    results = process(args.bucket, args.apply, args.limit)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"{item['result']} {item['action']} {item['intent_id']} {item['request_id']} {item.get('error', '')}".strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
