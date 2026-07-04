# ops-02 tool-curator 규칙 분산을 canonical 블록 1곳으로 통합

- id: ops-02
- status: completed
- completed_at: 2026-07-04T1650Z
- projects: [openclaw, infinity]
- task_type: implementation
- topics: [workflow, documentation, tool-curation]
- proposed_by: sam-proposer
- source_signal: openclaw workspace system/docs/EVALUATION_NOTES.md 미해결 감시 항목 2건 — tool-curator 규칙 분산 + 링크 검증이 같은 원인(3곳 중복)을 가리킴
- result_summary: skills/tool-curator/SKILL.md를 실행 규칙 단일 정본으로 재작성(소스 플레이북·상한·안전 규칙·웹 근거 규칙·발송 경로·발송 전 단언·완료 계약·복구 모드 통합)하고, TOOL_CURATION_WORKFLOW.md는 목적+사건 이력 보관소로 축소, Daily tool curation 크론 payload는 정본을 가리키는 얇은 인보커로 교체했다. 순 176줄의 중복 규칙이 제거됐고(+128/-304), 링크 검증 단언의 canonical 위치가 SKILL.md로 확정됐다.
- artifacts:
  - path: openclaw workspace skills/tool-curator/SKILL.md
    role: implementation
    note: 실행 규칙 단일 정본
- reports:
  - path: reports/ops-02/2026-07-04T1650Z.html
    role: final
- commits: [openclaw 43c81ee]
- next_actions:
  - 다음 09:00 UTC 정기 run이 새 인보커 payload로 정상 종료(SENT/SKIPPED/NO_REPLY)하는지 확인
