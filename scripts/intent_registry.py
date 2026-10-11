"""Canonical YAML registry helpers for Infinity writers and checks."""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "INTENTS.yaml"
ARCHIVE_DIR = ROOT / "intents" / "archive"
TITLE_FIELD_RE = re.compile(r"^-\s*[A-Za-z_][A-Za-z0-9_-]*\s*:")


def clean_title(value: Any, intent_id: str = "") -> str:
    title = re.sub(r"\s+", " ", str(value or "")).strip()
    title = re.sub(r"^#+\s*", "", title)
    title = re.sub(r"^\[[^\]]+\]\s*", "", title)
    if not title or TITLE_FIELD_RE.match(title):
        title = re.sub(r"[-_]+", " ", str(intent_id or "")).strip().capitalize()
    return title or "제목 없는 Intent"


def load_registry(path: Path = REGISTRY) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data.setdefault("lanes", {})
    for lane in ("inbox", "active", "waiting"):
        data["lanes"].setdefault(lane, [])
    return data


def save_registry(data: dict[str, Any], path: Path = REGISTRY) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def normalize_entry(entry: dict[str, Any], status: str | None = None) -> dict[str, Any]:
    entry = dict(entry)
    entry["id"] = str(entry.get("id") or "").strip()
    entry["title"] = clean_title(entry.get("task_name") or entry.get("title"), entry["id"])
    entry["task_name"] = entry["title"]
    if status:
        entry["status"] = status
    return entry


def open_entries(data: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for lane in ("inbox", "active", "waiting"):
        entries.extend(normalize_entry(item, lane) for item in data.get("lanes", {}).get(lane, []))
    return entries


def archive_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in sorted(ARCHIVE_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        entries.extend(normalize_entry(item, "archived") for item in data.get("archive", []))
    return entries


def all_entries(data: dict[str, Any]) -> list[dict[str, Any]]:
    return open_entries(data) + archive_entries()


def find_open(data: dict[str, Any], intent_id: str) -> tuple[str, dict[str, Any]] | None:
    for lane in ("inbox", "active", "waiting"):
        for item in data.get("lanes", {}).get(lane, []):
            if str(item.get("id") or "") == intent_id:
                return lane, item
    return None


def archive_period(item: dict[str, Any]) -> str:
    for key in ("completed_at", "archived_at", "date"):
        match = re.match(r"(\d{4}-\d{2})", str(item.get(key) or ""))
        if match:
            return match.group(1)
    return "undated"


def append_archive(item: dict[str, Any]) -> Path:
    period = archive_period(item)
    path = ARCHIVE_DIR / f"{period}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {"version": 1, "period": period, "archive": []}
    data.setdefault("archive", [])
    data["archive"] = [x for x in data["archive"] if x.get("id") != item.get("id")]
    data["archive"].append(normalize_entry(item, "archived"))
    save_registry(data, path)
    return path


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
