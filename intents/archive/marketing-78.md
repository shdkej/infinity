# marketing-78 홈 `최근 덕행` 빈 상태 3요소 패킷

- id: marketing-78
- status: archived
- completed_at: 2026-06-22T1700Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, product]
- permission_level: L1 docs-only
- result_summary: 홈 `최근 덕행` empty state 3요소(다음 행동/왜 중요한가/어떤 결과가 남는가) 비교 완료. ghost sample card 1장(Option B)이 결과 예시 가시성 갭 해소 최우선 추천안. 기존 archive 충돌 0건.
- artifacts:
  - path: artifacts/marketing-78/empty-state-triad-packet.html
    role: design
    note: Appcues 2026 3요소 × 3안 비교표 및 추천안
- reports:
  - path: reports/marketing-78/2026-06-22T1700Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - ghost sample card 1장(Option B) 구현은 approval-needed 후속 intent로 분리
  - 한 줄 보조문구(Option A)는 더 보수적 첫 실험 후보로 검토 가능 (approval-needed)
  - ghost card 구현 시 기존 CTA와 협력 관계 재확인 필요 (CTA 중복 방지)

## Goal

Appcues 2026 기준 empty state 3요소(다음 행동 / 왜 중요한가 / 어떤 결과가 남는가) 관점에서 홈 `최근 덕행` 빈 상태를 분석하고, 3안(한 줄 보조문구 / ghost sample card 1장 / 둘 다) 비교 패킷을 작성한다.

## Success Criteria (충족 여부)

- [x] 3안이 3요소를 각각 얼마나 채우는지 비교표로 정리
- [x] 첫 검증 게이트: 갭이 CTA 부족이 아닌 결과 예시 가시성 부족임을 marketing-70/76 archive로 확인
- [x] 기존 archive 문서(marketing-70/71/73/76/77) 충돌 0건 확인
- [x] HTML report gate 통과

## Collaboration Context

- source_agent: Infinity router (heartbeat)
- target_agent: cloud docs
- request_type: docs-only strategy comparison
- approval_boundary: L1 docs-only
- user_visible: false
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-22-empty-state-triad-onboarding.md

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
