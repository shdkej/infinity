#!/usr/bin/env python3
"""Create deduplicated, evidence-backed role task candidates for Infinity Backlog.

The watchers are deterministic. They observe changes and write candidates; they
do not decide whether a candidate should be executed. Genie owns backlog triage.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "INTENTS.yaml"
STATE = ROOT / "data" / "role-watcher-state.json"
CANONICAL_ROOT = Path("/home/ubuntu/workspace/knowledge-lab/infinity")
PROJECTS = Path("/home/ubuntu/workspace/projects")
MARKETING_INBOX = Path("/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/agent-inbox/marketing.jsonl")
ROLE_IDS = ("planner", "developer", "marketing", "design", "operator")


def sha_bytes(parts: list[bytes]) -> str:
    digest = hashlib.sha256()
    for part in parts:
        digest.update(len(part).to_bytes(8, "big"))
        digest.update(part)
    return digest.hexdigest()[:16]


def file_snapshot(paths: list[Path]) -> tuple[str, list[str]]:
    parts: list[bytes] = []
    evidence: list[str] = []
    for path in sorted(set(paths)):
        if not path.is_file():
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        parts.extend([str(path).encode(), data])
        evidence.append(str(path))
    return sha_bytes(parts), evidence


def git_snapshot(repo: Path) -> tuple[str, list[str], bool]:
    if not (repo / ".git").exists() and not (repo / ".git").is_file():
        return "missing", [], False
    try:
        status = subprocess.check_output(["git", "-C", str(repo), "status", "--porcelain"], text=True, stderr=subprocess.DEVNULL)
        head = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable", [str(repo)], True
    return sha_bytes([str(repo).encode(), head.encode(), status.encode()]), [str(repo)], bool(status.strip())


def project_files() -> list[Path]:
    if not PROJECTS.exists():
        return []
    return [path for path in PROJECTS.glob("*/PROJECT.md")] + [path for path in PROJECTS.glob("*/TASKS.md")]


def signal_for(role: str) -> tuple[str, list[str], str, str, bool]:
    """Return (digest, evidence_paths, kind, title, concrete_signal)."""
    if role == "planner":
        # A project file existing is not work. Only task lines that indicate a
        # live decision, blocker, deadline, or next step are actionable.
        signals: list[str] = []
        evidence: list[str] = []
        markers = ("blocked", "inbox", "ready", "active", "review", "next", "deadline", "마감", "차단", "다음")
        for path in sorted(PROJECTS.glob("*/TASKS.md")):
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            matches = [line.strip() for line in lines if any(marker in line.lower() for marker in markers)]
            if matches:
                evidence.append(str(path))
                signals.append(f"{path}\n" + "\n".join(matches[-30:]))
        digest = sha_bytes(["\n\n".join(signals).encode()])
        return digest, evidence, "planning_signal", "프로젝트의 막힘·마감·다음 행동을 검증 태스크로 정리한다", bool(signals)

    if role == "developer":
        # Infinity's own INTENTS/state commits are watcher bookkeeping, not a
        # developer signal. Exclude that repo so collection cannot trigger
        # itself on every run.
        repos = [Path("/home/ubuntu/workspace/space")]
        repos.extend(path for path in PROJECTS.glob("*") if path.is_dir())
        snapshots: list[bytes] = []
        evidence: list[str] = []
        concrete = False
        for repo in repos:
            digest, paths, repo_changed = git_snapshot(repo)
            snapshots.extend([str(repo).encode(), digest.encode()])
            evidence.extend(paths)
            concrete = concrete or repo_changed
        return sha_bytes(snapshots), evidence, "repository_signal", "저장소 변경·테스트·기술 부채 신호를 개선 태스크로 정리한다", concrete

    if role == "marketing":
        if MARKETING_INBOX.is_file():
            lines = MARKETING_INBOX.read_text(encoding="utf-8", errors="replace").splitlines()[-200:]
            digest = sha_bytes(["\n".join(lines).encode()])
            evidence = [str(MARKETING_INBOX)]
            concrete = False
            for line in lines:
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if item.get("signal") not in (None, "", "no_action") and item.get("action_candidate"):
                    concrete = True
                    break
        else:
            digest, evidence = "missing", [str(MARKETING_INBOX)]
            concrete = False
        return digest, evidence, "marketing_signal", "SNS·사용자 조사·GA/PostHog 신호의 변화를 다음 실험 태스크로 정리한다", concrete

    if role == "design":
        paths = [Path("/home/ubuntu/workspace/prompt-archive/DESIGN.md"), Path("/home/ubuntu/workspace/prompt-archive/DESIGN_SYSTEM.md"), Path("/home/ubuntu/workspace/prompt-archive/BRAND.md")]
        paths += list((Path("/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/photo-insights")).glob("**/*"))
        digest, evidence = file_snapshot(paths)
        # Design references alone are a baseline, not a task. A new/changed
        # photo-insight or design input is the actionable signal.
        concrete = any("photo-insights" in path for path in evidence)
        return digest, evidence, "design_signal", "화면·이미지·타이포그래피 관찰을 시각 개선 태스크로 정리한다", concrete

    if role == "operator":
        try:
            data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
            lanes = data.get("lanes", {})
            state = {lane: [str(item.get("id")) for item in lanes.get(lane, [])] for lane in ("backlog", "inbox", "active", "waiting")}
            digest = sha_bytes([json.dumps(state, sort_keys=True).encode()])
            evidence = [str(CANONICAL_ROOT / "INTENTS.yaml")]
            concrete = bool(state.get("active") or state.get("waiting"))
        except (OSError, yaml.YAMLError):
            digest, evidence = "unavailable", [str(REGISTRY)]
            concrete = True
        return digest, evidence, "operations_signal", "실패·대기·마감·원격 상태를 운영 태스크로 정리한다", concrete

    raise ValueError(f"unknown role: {role}")


def candidate_id(role: str, digest: str) -> str:
    # One open candidate per role/purpose. The signal digest belongs in the
    # record as evidence; it must not become the task identity.
    return f"watch-{role}-current"


def dedupe_key(role: str, kind: str) -> str:
    return f"role-watcher:{role}:{kind}"


def load_state() -> dict[str, Any]:
    if not STATE.exists():
        return {"schema_version": 1, "roles": {}}
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema_version": 1, "roles": {}}


def append_candidates(roles: list[str], apply: bool) -> dict[str, Any]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    lanes = data.setdefault("lanes", {})
    backlog = lanes.setdefault("backlog", [])
    existing = {str(item.get("id")) for lane in lanes.values() if isinstance(lane, list) for item in lane if isinstance(item, dict)}
    state = load_state()
    role_state = state.setdefault("roles", {})
    candidates: list[dict[str, Any]] = []
    added: list[str] = []
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    for role in roles:
        digest, evidence, kind, title, concrete = signal_for(role)
        previous = role_state.get(role, {}).get("digest")
        changed = digest != previous
        role_state[role] = {"digest": digest, "observed_at": now, "evidence_paths": evidence}
        candidate = {"role": role, "digest": digest, "changed": changed, "concrete": concrete, "evidence_paths": evidence, "kind": kind, "title": title}
        candidates.append(candidate)
        if not apply or not changed or not concrete:
            continue
        intent_id = candidate_id(role, digest)
        key = dedupe_key(role, kind)
        open_item = next((item for lane in ("backlog", "inbox", "active", "waiting")
                          for item in lanes.get(lane, []) or []
                          if isinstance(item, dict) and (
                              item.get("dedupe_key") == key or
                              (item.get("watcher_role") == role and item.get("title") == title)
                          )), None)
        if open_item:
            # Refresh evidence on the existing task without opening a repeat.
            if apply and changed:
                open_item.update({"signal": digest, "evidence_paths": evidence, "last_observed_at": now})
            continue
        backlog.append({
            "id": intent_id,
            "dedupe_key": key,
            "title": title,
            "task_name": title,
            "status": "backlog",
            "priority": "normal",
            "task_type": "watcher_candidate",
            "target_agent": "genie",
            "watcher_role": role,
            "source": f"role-watcher:{role}",
            "signal_type": kind,
            "signal": digest,
            "evidence_paths": evidence,
            "created_at": now,
            "last_observed_at": now,
            "user_intent": f"{role} 역할의 새 운영 신호를 사람이 판단 가능한 작업 후보로 만든다.",
            "why_now": "이번 실행에서 이전 관찰과 달라진 구체 신호가 감지되었다.",
            "desired_outcome": "Genie가 근거를 확인해 중복은 묶고, 가치 있는 후보만 Inbox로 승격한다.",
            "suggested_checks": ["근거 파일·지표의 실제 변경 확인", "현재 목표·대표 지표와의 연결 확인", "이미 해결된 문제인지 확인"],
            "out_of_scope": "신호만으로 자동 구현·공개 발행·결제·권한 변경을 실행하지 않는다.",
            "success_evidence": "동일 목적 후보가 한 건으로 유지되고, triage 결과와 다음 행동이 남는다.",
            "next_action": "Genie가 근거를 검증한 뒤 유지·통합·거절·Inbox 승격 중 하나를 기록한다.",
            "notification_channel": "slack",
            "notification_target": "channel:C0BR41W31MM",
        })
        existing.add(intent_id)
        added.append(intent_id)
    if apply:
        REGISTRY.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"observed": candidates, "added": added, "apply": apply}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", action="append", choices=ROLE_IDS)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    roles = args.role or list(ROLE_IDS)
    print(json.dumps(append_candidates(roles, args.apply), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
