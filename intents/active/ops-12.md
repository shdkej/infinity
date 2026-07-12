# [ops-12] 마케팅 크론 git 동기화 실패 반복 경계 고정

- id: ops-12
- status: in_progress
- priority: high
- approval: agent-approved L2 (2026-07-12T10:07Z)
- started_at: 2026-07-12T10:07Z
- goal: 마케팅 크론의 git sync/rebase/push 실패를 NO_REPLY가 아니라 명시적 blocker로 처리하는 계약을 실행 경로에 반영
- context: OpenClaw Marketing-agent-growth-review 크론 프롬프트/헬퍼
- artifacts:
  - artifacts/ops-12/git-failure-repair-contract.md (repair contract)
  - artifacts/ops-12/local-execution-prompt.md (local execution prompt)
- reports:
  - reports/ops-12/20260712T1007Z-prepare.html (cloud prepare report)
- next_action: pt/purplemux Claude Code tmux pane에 artifacts/ops-12/local-execution-prompt.md 내용을 전달해 marketing cron 프롬프트에 git failure gate 추가 후 검증
