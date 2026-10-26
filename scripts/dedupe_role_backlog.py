#!/usr/bin/env python3
"""Collapse repeated role-watcher candidates into one auditable backlog item."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "INTENTS.yaml"


def key(item: dict[str, Any]) -> str | None:
    if item.get("task_type") != "watcher_candidate" or not item.get("watcher_role"):
        return None
    return str(item.get("dedupe_key") or f"role-watcher:{item['watcher_role']}:{item.get('signal_type', '')}")


def dedupe(apply: bool = False) -> dict[str, Any]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    backlog = data.setdefault("lanes", {}).setdefault("backlog", [])
    groups: dict[str, list[dict[str, Any]]] = {}
    passthrough: list[dict[str, Any]] = []
    for item in backlog:
        group = key(item) if isinstance(item, dict) else None
        if group is None:
            passthrough.append(item)
        else:
            groups.setdefault(group, []).append(item)

    kept: list[dict[str, Any]] = list(passthrough)
    merged: list[dict[str, Any]] = []
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    for group, items in groups.items():
        items.sort(key=lambda item: str(item.get("created_at", "")))
        winner = items[-1]
        removed = [str(item.get("id")) for item in items[:-1] if item.get("id")]
        winner["dedupe_key"] = group
        if removed:
            winner["merged_from"] = sorted(set((winner.get("merged_from") or []) + removed))
            winner["dedupe_reason"] = "같은 역할·목적·변경면의 반복 후보를 최신 근거 한 건으로 통합"
            winner["last_deduped_at"] = now
            merged.append({"kept": winner.get("id"), "removed": removed, "key": group})
        kept.append(winner)

    if apply and merged:
        data["lanes"]["backlog"] = kept
        REGISTRY.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return {"before": len(backlog), "after": len(kept), "merged": merged, "apply": apply}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(yaml.safe_dump(dedupe(args.apply), allow_unicode=True, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
