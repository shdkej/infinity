#!/usr/bin/env python3
"""Read-only PostHog/Grafana watcher that appends deduplicated candidates to Backlog."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import statistics
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "INTENTS.yaml"
DEFAULT_POSTHOG_HOST = "https://us.i.posthog.com"
DEFAULT_GRAFANA_URL = "https://grafana.oracle.shdkej.com"


def load_env(path: Path = Path("/home/ubuntu/.env")) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def http_json(url: str, headers: dict[str, str] | None = None) -> Any:
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8"))


def classify_series(values: list[float]) -> list[dict[str, str]]:
    """Return actionable anomaly classes without emitting duplicate variants."""
    if len(values) < 3:
        return []
    latest = values[-1]
    baseline = values[-8:-1] or values[:-1]
    median = statistics.median(baseline) if baseline else 0
    recent = values[-5:]
    recent_median = statistics.median(recent)
    # A flat series is suspicious even when it is flat at zero.  The watcher
    # runs hourly, while a PostHog insight may be hourly or daily, so use a
    # minimum observation count instead of assuming a specific interval.
    flat_tolerance = max(abs(recent_median) * 0.01, 0.000001)
    stagnant = len(recent) >= 5 and max(recent) - min(recent) <= flat_tolerance
    zero_drop = latest == 0 and max(baseline, default=0) > 0
    spike = latest >= max(10, median * 3) and latest > median + 5
    low = median > 0 and latest < median * 0.5 and (median - latest) >= 1
    findings: list[dict[str, str]] = []
    if stagnant:
        level = "0" if latest == 0 else "거의 동일"
        findings.append({"kind": "metric_stagnation", "direction": f"최근 {len(recent)}회 {level}로 정체"})
    elif zero_drop or low:
        direction = "0으로 떨어짐" if zero_drop else "평소보다 저조"
        findings.append({"kind": "metric_low", "direction": direction})
    if spike:
        findings.append({"kind": "metric_spike", "direction": "평소보다 급증"})
    return findings


def posthog_candidates() -> list[dict[str, Any]]:
    token = os.environ.get("POSTHOG_ACCESS_TOKEN", "").strip()
    if not token:
        return [{"source": "posthog", "kind": "configuration", "title": "PostHog 접근 토큰이 없어 지표 감시 설정을 확인한다", "signal": "missing_access_token"}]
    host = os.environ.get("POSTHOG_HOST", DEFAULT_POSTHOG_HOST).rstrip("/")
    headers = {"Authorization": f"Bearer {token}"}
    project = os.environ.get("POSTHOG_PROJECT_ID", "").strip()
    if not project:
        current = http_json(f"{host}/api/projects/@current", headers)
        project = str(current.get("id") or "")
    if not project:
        return [{"source": "posthog", "kind": "configuration", "title": "PostHog 프로젝트 식별자를 확인한다", "signal": "missing_project_id"}]
    listing = http_json(f"{host}/api/projects/{project}/insights/?limit=30", headers)
    candidates: list[dict[str, Any]] = []
    for insight in listing.get("results", []) if isinstance(listing, dict) else []:
        insight_id = insight.get("id")
        if not insight_id:
            continue
        detail = http_json(f"{host}/api/projects/{project}/insights/{insight_id}/?refresh=true", headers)
        results = detail.get("results") if isinstance(detail, dict) else None
        if not results or not isinstance(results[0], dict):
            continue
        values = results[0].get("data") or []
        numeric = []
        for value in values:
            try:
                if isinstance(value, bool):
                    continue
                numeric.append(float(value))
            except (TypeError, ValueError):
                continue
        metric_name = str(detail.get("name") or insight.get("name") or insight_id)
        for finding in classify_series(numeric):
            kind = finding["kind"]
            direction = finding["direction"]
            problem_key = f"posthog:{insight_id}:{kind}"
            title = f"PostHog 지표 '{metric_name}' {direction} 원인을 확인한다"
            candidates.append({
                "source": "posthog",
                "kind": kind,
                "problem_key": problem_key,
                "title": title,
                "signal": f"{insight_id}:{numeric[-1] if numeric else ''}:{direction}",
                "source_ref": str(insight_id),
            })
    return candidates


def grafana_candidates() -> list[dict[str, Any]]:
    base = os.environ.get("GRAFANA_URL", DEFAULT_GRAFANA_URL).rstrip("/")
    headers: dict[str, str] = {}
    token = os.environ.get("GRAFANA_API_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        health = http_json(f"{base}/api/health", headers)
    except Exception as exc:
        return [{"source": "grafana", "kind": "availability", "title": "Grafana 연결 상태와 운영 대시보드를 확인한다", "signal": f"unreachable:{type(exc).__name__}"}]
    if str(health.get("database") or "").lower() != "ok":
        return [{"source": "grafana", "kind": "availability", "title": "Grafana 데이터베이스 상태 이상을 확인한다", "signal": f"database:{health.get('database')}"}]
    # Dashboard search is optional because this installation may require auth.
    if not token:
        return []
    try:
        dashboards = http_json(f"{base}/api/search?type=dash-db", headers)
    except Exception:
        return [{"source": "grafana", "kind": "authorization", "title": "Grafana API 토큰 권한을 확인한다", "signal": "dashboard_search_failed"}]
    if not dashboards:
        return [{"source": "grafana", "kind": "configuration", "title": "Grafana 모니터링 대시보드가 비어 있는지 확인한다", "signal": "no_dashboards"}]
    return []


def candidate_id(candidate: dict[str, Any]) -> str:
    identity = candidate.get("problem_key") or f"{candidate['source']}|{candidate['kind']}|{candidate.get('source_ref', '')}"
    digest = hashlib.sha256(str(identity).encode()).hexdigest()[:12]
    return f"watch-{candidate['source']}-{digest}"


def append_candidates(candidates: list[dict[str, Any]], apply: bool) -> list[str]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    lanes = data.setdefault("lanes", {})
    backlog = lanes.setdefault("backlog", [])
    existing_ids = {str(item.get("id")) for lane in lanes.values() if isinstance(lane, list) for item in lane}
    existing_keys = {
        str(item.get("problem_key") or f"{item.get('source', '')}|{item.get('signal_type', '')}|{item.get('source_ref', '')}")
        for lane in lanes.values() if isinstance(lane, list) for item in lane
        if item.get("source") and item.get("signal_type")
    }
    added: list[str] = []
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for candidate in candidates:
        intent_id = candidate_id(candidate)
        problem_key = str(candidate.get("problem_key") or f"{candidate['source']}|{candidate['kind']}|{candidate.get('source_ref', '')}")
        if intent_id in existing_ids or problem_key in existing_keys:
            continue
        item = {
            "id": intent_id,
            "title": candidate["title"],
            "task_name": candidate["title"],
            "status": "backlog",
            "priority": "normal",
            "task_type": "maintenance",
            "target_agent": "genie",
            "source": candidate["source"],
            "signal_type": candidate["kind"],
            "problem_key": problem_key,
            "signal": candidate["signal"],
            "source_ref": candidate.get("source_ref", ""),
            "created_at": now,
            "user_intent": "모니터링 신호를 사람이 확인 가능한 작업 후보로 만든다.",
            "desired_outcome": "사용자가 범위를 선택해 Inbox로 옮기거나 거절할 수 있는 후보를 만든다.",
            "out_of_scope": "자동 실행, 외부 발송, 결제, 권한 변경",
            "success_evidence": "중복 없이 Backlog에 기록되고 대시보드에서 승격·거절할 수 있다.",
            "next_action": "사용자가 작업범위를 선택해 Inbox 승격 여부를 결정한다.",
            "notification_channel": "slack",
            "notification_target": "channel:C0BR41W31MM",
        }
        backlog.append(item)
        existing_ids.add(intent_id)
        existing_keys.add(problem_key)
        added.append(intent_id)
    if apply and added:
        REGISTRY.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return added


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    load_env()
    candidates: list[dict[str, Any]] = []
    for reader in (posthog_candidates, grafana_candidates):
        try:
            candidates.extend(reader())
        except Exception as exc:
            candidates.append({"source": reader.__name__.replace("_candidates", ""), "kind": "watcher_error", "title": "모니터링 와처 오류를 확인한다", "signal": type(exc).__name__})
    added = append_candidates(candidates, args.apply)
    print(json.dumps({"candidates": len(candidates), "added": added, "apply": args.apply}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
