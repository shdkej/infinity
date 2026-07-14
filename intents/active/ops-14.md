# [ops-14] OpenClaw evaluator 읽기 예산 게이트 고정

- id: ops-14
- status: waiting
- priority: high
- permission: L2 (agent-approved 2026-07-14T00:00Z)
- goal: OpenClaw evaluator 정본 프롬프트 또는 관련 헬퍼에 읽기 예산과 조기 종료 조건을 고정해 NO_REPLY 실행 시 4.7万~6.7万 토큰 소비를 의미 있게 낮춘다
- context: system/docs/EVALUATION_NOTES.md, OpenClaw evaluator 정본 프롬프트/헬퍼
- prepare_report: reports/ops-14/20260714T0000Z-prepare.html
- local_exec: artifacts/ops-14/local-execution-prompt.md
- waiting_reason: 로컬 Claude Code 실행 대기. pt/purplemux Claude pane에서 artifacts/ops-14/local-execution-prompt.md 실행 필요.
- next_action: 로컬 Claude Code로 evaluator 읽기 예산 고정(OPERATING_LESSONS.md 관련 섹션, EVALUATION_NOTES.md tail 120줄, 최근 24시간 크론 요약만) 및 조기 종료 조건 추가 후 검증
- success_criteria: evaluator 실행 경로가 3종 읽기 예산만 허용하고 조기 종료 조건이 반영됐으며, 다음 2회 실행에서 NO_REPLY total_tokens가 이전 4.7万~6.7万 범위보다 의미 있게 낮아짐
