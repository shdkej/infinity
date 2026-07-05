# [ops-04] OpenClaw evaluator 경고성 탐색 템플릿 축소

- id: ops-04
- status: archived
- completed_at: 2026-07-05T03:07
- projects: [openclaw, infinity]
- task_type: implementation
- topics: [automation, workflow]
- axis1: OpenClaw evaluator가 반복 `NO_REPLY` 중 불필요한 search/path 경고를 내던 문제
- result_summary: evaluator 정본이 `git status --short`, 절대경로 읽기, no-match 정상 처리, agent-scoped 전역 search 금지 규칙을 포함함을 확인하고 intent를 닫았다.
- artifacts:
  - path: /home/ubuntu/.openclaw/workspace/system/evaluators/openclaw-evaluator.md
    role: implementation
    note: evaluator 실행 제한과 출력 원칙의 canonical 절차 파일
- reports:
  - path: reports/ops-04/2026-07-05T0307Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: recorded-in-this-archive-commit
    note: ops-04 archive/report 기록
- urls: []
- next_actions:
  - No continuation: 다음 evaluator 정기 실행 diagnostics에서 search target/path warning이 다시 뜨면 새 감시 항목으로 분리한다.

## Verification

- `/home/ubuntu/.openclaw/workspace/system/evaluators/openclaw-evaluator.md`는 `git status --short`를 기본 확인 대상으로 두고, 추가 단서가 필요할 때만 절대경로 파일 대상의 좁은 읽기/`rg`를 사용하도록 명시한다.
- 같은 정본은 `~` 축약 대신 `/home/ubuntu/.openclaw/workspace/...` 절대경로를 우선 사용하도록 명시한다.
- 같은 정본은 셸 리다이렉션 조각을 search 대상 문자열에 섞지 않고, no-match 허용은 명령 레벨에서 처리하도록 명시한다.
- scoped git status 기준 target OpenClaw evaluator/EVALUATION_NOTES 파일에는 미커밋 변경이 없었다. 이번 intent 기록만 Infinity 원장에 추가했다.
