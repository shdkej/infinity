# [ops-15] layer-check 당일 라인 작성 경로 분리

- id: ops-15
- status: active
- priority: high
- permission: L1
- proposed_by: sam-proposer
- created_at: 2026-07-15T09:00Z

## Goal
KST 당일 23:00 이전에 아침/오후 크론 경로가 `layer-check.jsonl`에 `date == today` 라인을 추가하지 않도록 경계 코드 또는 설정을 추가한다.

## Context
- `system/data/quality-gates/layer-check.jsonl` — 품질 게이트 일일 기록 JSONL
- OpenClaw 07:00 아침 리캡 스크립트
- 오후 크론 실행 경로
- Source signal: `system/docs/EVALUATION_NOTES.md#layer-check.jsonl-당일-보류-라인-최신-재현`

## Problem
2026-07-13 및 07-14 연속 발생: 아침/오후 경로가 `date == today` 라인을 먼저 추가해 23:00 밤 데일리 리뷰만 당일 라인을 써야 한다는 역할 분리가 깨졌다.

## Success Criteria
KST 당일 23:00 전에는 `layer-check.jsonl`에 `date == today` 라인이 추가되지 않고, 어제 백필과 밤 리뷰 append는 정상 동작한다는 dry-run 또는 다음 실행 검증 기록이 남는다.

## Mode
prepare (Cloud) → execute_local (Local Claude Code)

## Prepare Report
`reports/ops-15/20260715T0900Z-prepare.html`

## Local Execution
`artifacts/ops-15/local-execution-prompt.md`

## Next Action
로컬 Claude Code로 `artifacts/ops-15/local-execution-prompt.md` 실행. 아침/오후 경로에서 layer-check.jsonl 쓰기 게이트 추가 후 dry-run 검증.
