# ops-11 품질 게이트 effectiveness 원장 경계 확정

- id: ops-11
- status: active
- priority: medium
- permission: L1
- created_at: 2026-07-11
- projects: [openclaw, infinity]
- task_type: maintenance
- topics: [automation, quality-gates, gitignore]
- mode: prepare → execute_local
- goal: `system/data/quality-gates/effectiveness.jsonl`의 tracked/ignored 정책을 확정하고, 07:00 리캡 산출 경로와 일치시킨다
- success_criteria: 새 07:00 리캡 실행 후 `effectiveness.jsonl`이 선택된 정책에 맞게 동작하며 `git status --short`에 반복 untracked로 노출되지 않는다
- source_signal: EVALUATION_NOTES.md#품질-게이트-효과-검증-원장-untracked-최신-날짜-재현
- proposed_by: sam-proposer
- prepare_report: reports/ops-11/2026-07-11T1200Z.html
- local_prompt: artifacts/ops-11/local-execution-prompt.md

## Context

- File: `system/data/quality-gates/effectiveness.jsonl` (OpenClaw workspace)
- 2026-07-10, 2026-07-11 두 날 연속 `git status --short` untracked 노출
- Pattern precedent: ops-07 (MEMORY/DREAMS → .gitignore), ops-08 (daily-reviews/ → .gitignore)

## Next Action

로컬 Claude Code (pt/purplemux pane 우선):
`artifacts/ops-11/local-execution-prompt.md` 참조하여 실행
