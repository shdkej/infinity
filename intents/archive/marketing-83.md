# marketing-83 — Virtue 홈 반환형 Empty-State Gating 정렬 제안서

- id: marketing-83
- status: archived
- completed_at: 2026-06-24T2300Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, onboarding, empty-state]
- permission_level: L1 docs-only
- result_summary: 홈 hero·요약 카드·최근 덕행 3표면별 J1-J4 gating 규칙과 반환형 문장 후보를 proposal-only 1장 비교 문서로 정리했다. 핵심 충돌(누적 신호 + 첫 방문 empty-state 공존)의 구조적 원인은 최근 덕행 섹션이 전체 이력 0건(신규)과 오늘 이력 0건(반환)을 구분하지 않는 것이다. J3는 deed_judged gate로, J1/J2/J4는 deed_saved gate로 별도 처리가 필요하다.
- artifacts:
  - path: artifacts/marketing-83/return-empty-state-gating-proposal.md
    role: strategy
    note: 3표면별 gating 규칙, J1-J4 반환형 문장 후보, 구현 금지 항목을 1장으로 정리.
- reports:
  - path: reports/marketing-83/20260624T2300Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - 최근 덕행 섹션 gating 로직(deed_saved ≥ 1, 전체 이력 vs 오늘 이력 구분) 구현을 approval-needed로 올린다.
  - hero 반환형 문장 후보는 proposal-only 유지. A/B 없이 production 적용 금지.
  - J3의 deed_judged gate는 J1/J2/J4의 deed_saved gate와 별도 분기로 구현한다.
