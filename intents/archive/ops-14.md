# [ops-14] OpenClaw evaluator 읽기 예산 게이트 고정

- id: ops-14
- status: archived
- completed_at: 2026-07-15T15:07
- projects: [openclaw, infinity]
- task_type: monitoring
- topics: [automation, workflow, llm]
- result_summary: OpenClaw evaluator 읽기 예산 패치 후 NO_REPLY 실행 2건이 27,498 / 25,460 tokens로 내려가 기존 4.7만~6.7만 범위보다 낮음을 확인했다.
- artifacts:
  - path: artifacts/ops-14/local-execution-prompt.md
    role: implementation
    note: evaluator 읽기 예산 고정을 위한 로컬 실행 프롬프트
- reports:
  - path: reports/ops-14/20260714T0000Z-prepare.html
    role: prepare
  - path: reports/ops-14/20260715T1008Z-local-fix.html
    role: run
  - path: reports/ops-14/20260715T1507Z.html
    role: final
- commits:
  - repo: infinity
    sha: d67ee46
    note: archive/report update for ops-14 completion
- urls: []
- next_actions:
  - No continuation. 같은 신호가 재발할 때만 별도 monitoring intent로 다시 연다.

## Result

축1 = OpenClaw evaluator가 NO_REPLY 경로에서 과도한 문서/로그를 읽어 4.7만~6.7만 tokens를 쓰던 문제를 점검했다.

축2 = 읽기 예산 3종과 조기 종료 조건 반영 뒤 2026-07-15T11:07Z, 12:07Z 실행이 각각 27,498 / 25,460 tokens로 내려가 성공 기준을 충족했다.

## Evidence

- patched surface: `/home/ubuntu/.claude/skills/infinity/SKILL.md`
- observed session key: `agent:main:cron:7502ef19-45c7-45f9-aa0e-b05c40ba670e`
- observed assistant result: `NO_REPLY`
