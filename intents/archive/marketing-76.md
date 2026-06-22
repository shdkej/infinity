# marketing-76 Virtue 핵심 화면 맥락형 안내 문구 감사

- id: marketing-76
- status: archived
- completed_at: 2026-06-22T1029Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, product, in-app-guidance]
- result_summary: `/add`, 결과 카드, 홈 empty state 3개 핵심 화면에 대해 현재 기대, 설명이 필요한 변화, 추천 안내 톤, 과설명 위험, 승인 필요 항목, gate yes/no를 표로 정리했다. `/add`와 결과 카드는 Yes, 홈 empty state는 No로 판정했다.
- artifacts:
  - path: artifacts/marketing-76/virtue-contextual-guidance-audit.html
    role: design
    note: Virtue 핵심 화면별 contextual guidance audit table
- reports:
  - path: reports/marketing-76/2026-06-22T1029Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - Yes 판정 화면(`/add`, 결과 카드)의 실제 카피/UI 변경은 approval-needed 후속 intent로 분리한다.
  - No 판정 홈 empty state는 설명 추가보다 proof preview 보강 비교안 범위에서만 검토한다.

## Collaboration Context

- source_agent: Infinity router
- target_agent: Claude Code
- request_type: docs-only messaging audit
- approval_boundary: L1 docs-only
- user_visible: false
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-22-launch-tier-contextual-announcement.md

## Outcome

- `/add`와 결과 카드는 안내 부재가 실제 다음 행동 손실로 이어질 수 있어 Yes 판정했다.
- 홈 empty state는 안내가 있으면 더 좋을 수는 있지만, 없다고 즉시 행동을 놓치는 단계는 아니라 No로 분리했다.
- 화면별 추천 톤을 안심형 기대 브리지 / 관점 제안형 / 호기심 유도형으로 나눠, 과설명 없이 first value를 돕는 문구 원칙을 고정했다.

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
