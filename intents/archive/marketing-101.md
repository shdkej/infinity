# marketing-101 Virtue 잡별 activation 후보 묶음 레지스트리

- id: marketing-101
- status: archived
- completed_at: 2026-07-06T10:28
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, analytics]
- permission_level: L1 docs-only
- result_summary: Virtue J1-J4별 activation 후보 묶음, window, 현재 이벤트로 판독 가능한 항목, 수기 관찰 항목, 표본 부족 시 금지 해석을 registry로 고정했다. 기존 first value 기준 J1/J2/J4=`deed_saved`, J3=`deed_judged`와 충돌 없음.
- artifacts:
  - path: artifacts/marketing-101/activation-candidate-registry.md
    role: strategy
    note: J1-J4 activation 후보 묶음과 window, readable/manual 항목, 금지 해석 registry
  - path: artifacts/marketing-101/job-activation-bundle-registry.md
    role: prior-design
    note: 원격 동시 작업에서 생성된 같은 intent의 선행 레지스트리. 최종 정본은 activation-candidate-registry.md.
- reports:
  - path: reports/marketing-101/2026-07-06T1028Z.html
    role: final
  - path: reports/marketing-101/2026-07-06T0000Z.html
    role: prior-run
- commits: []
- urls: []
- next_actions:
  - 첫 10명 관찰표(`artifacts/marketing-79/week-one-activation-observation-table.html`)에 이 registry를 해석 기준으로 붙여 쓴다.
  - 출시 후 event quality, traffic source 분리, 표본이 갖춰지면 후보 묶음과 D1/D7 return 대조 intent를 별도로 연다.
  - 구현, 배포, 신규 tracking, dashboard, 공개 카피 변경은 이번 범위에서 제외한다.

## Success Criteria

- [x] J1-J4별 activation 후보 묶음과 window를 정리했다.
- [x] 현재 이벤트로 판독 가능한 항목과 수기 관찰 항목을 분리했다.
- [x] 표본 부족 시 금지 해석을 명시했다.
- [x] `source/external-links/marketing/2026-06-01-activation-metric-bundles.md` 후속 실험 후보 1번과 연결했다.
- [x] `marketing-79`~`marketing-100` 중 first value/관찰표 계열과 충돌하지 않음을 확인했다.
- [x] HTML report gate 통과.

## Inherited Learning

- First Value Mapping: J1/J2/J4는 `deed_saved`, J3는 `deed_judged`.
- Measurement Readiness: 측정 가능성과 측정값 성패를 분리한다.
- Correlation Readiness: retention 대조는 사전 등록된 묶음·window·제외 조건이 있어야 한다.
- Session Value: 이벤트 수가 아니라 잡별 first value와 종료 성격으로 읽는다.
- Post-Response Flow: `deed_judged` 직후 행동은 J3와 J1/J2/J4에서 다르게 해석한다.

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
