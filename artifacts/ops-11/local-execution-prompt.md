# Local Execution Prompt — ops-11

Infinity Intent: ops-11 품질 게이트 effectiveness 원장 경계 확정  
Mode: execute_local  
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.  
Workflow: Simple .gitignore update — direct lightweight execution acceptable (no workflow-master needed).

## Goal

`system/data/quality-gates/effectiveness.jsonl`의 tracked/ignored 정책을 확정하고,
`git status --short`에 반복 untracked로 노출되지 않도록 한다.

## Context

- Source signal: `EVALUATION_NOTES.md#품질-게이트-효과-검증-원장-untracked-최신-날짜-재현`
- File: `/home/ubuntu/.openclaw/workspace/system/data/quality-gates/effectiveness.jsonl`
- Pattern precedent: ops-07 (MEMORY/DREAMS → .gitignore), ops-08 (daily-reviews/ → .gitignore)
- Cloud prepare report: `reports/ops-11/2026-07-11T1200Z.html`

## Prepared Findings

- `effectiveness.jsonl`이 2026-07-10, 2026-07-11 두 날 연속 untracked 노출 — 정책 미정
- ops-07/08 선례 기준 자동 생성 런타임 파일 → .gitignore 추가가 표준 정책
- 파일 생성 주체 확인 후 fresh-each-run vs cumulative-log 판단 필요

## Steps

1. 파일 생성 주체 확인:
   ```bash
   grep -r "effectiveness.jsonl" /home/ubuntu/.openclaw/workspace/system/ --include="*.sh" --include="*.py" --include="*.md" --include="*.ts" -l
   ```

2. 정책 결정:
   - **매 실행마다 재생성(fresh)** → Option A: .gitignore 추가 (권장)
   - **누적 이력이 필요** → Option B: 명시적 추적 + 07:00 스크립트에 `git add + git commit` 추가

3. Option A 실행 (권장):
   ```bash
   # openclaw workspace .gitignore에 추가
   echo 'system/data/quality-gates/effectiveness.jsonl' >> /home/ubuntu/.openclaw/workspace/.gitignore
   # 또는 패턴으로 (해당 디렉토리 전체가 runtime이면):
   # echo 'system/data/quality-gates/' >> /home/ubuntu/.openclaw/workspace/.gitignore
   ```

4. 검증:
   ```bash
   git -C /home/ubuntu/.openclaw/workspace status --short | grep effectiveness
   # 결과 없으면 성공
   ```

5. 커밋 & 푸시 (openclaw workspace):
   ```bash
   git -C /home/ubuntu/.openclaw/workspace add .gitignore
   git -C /home/ubuntu/.openclaw/workspace commit -m "ops-11: effectiveness.jsonl .gitignore 추가 (런타임 캐시 정책)"
   git -C /home/ubuntu/.openclaw/workspace push
   ```

## Allowed / Forbidden

- Allowed: L0/L1 actions (file read, .gitignore modification, git commit/push to openclaw workspace)
- Forbidden: L2/L3 actions without explicit approval

## Verification Gate

`git -C /home/ubuntu/.openclaw/workspace status --short` 결과에서 `effectiveness.jsonl` 미노출 확인

## Report Back

`reports/ops-11/{local_timestamp}-local-fix.html` (HTML 형식 필수, _TEMPLATE.html 기반)
- 완료 후 ops-11 status를 `in_progress` 또는 `completed`로 업데이트
