# marketing-102 Virtue D7 재가치 관찰 게이트 정렬

- id: marketing-102
- status: archived
- completed_at: 2026-07-10T10:07
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation, retention]
- permission_level: L1 internal-doc only
- result_summary: 기존 첫 10명 관찰표와 activation 후보 등록부를 대조해 J1/J2/J4=`deed_saved`, J3=`deed_judged` 기준을 유지한 D7 재가치 손기록 게이트를 정리했다. `add_flow_started`는 activation 성공으로 보지 않는 금지선을 명시했다.
- artifacts:
  - path: artifacts/marketing-102/d7-revalue-observation-gate.md
    role: strategy
    note: 잡별 D7 재가치 질문, same-job 유지 여부, second value evidence, no-read 칸 제안
- reports:
  - path: reports/marketing-102/2026-07-10T1007Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - 첫 10-20명 관찰표를 실제로 쓸 때 D7 return reason, same job, second value evidence, no-read 칸을 손기록으로 붙여 쓴다.
  - 실제 D7 기록 후 칸이 중복되거나 비어 있으면 `marketing-79` artifact 개정 intent를 별도로 연다.
  - 신규 tracking, dashboard, PostHog 쿼리, 공개 카피, 외부 발송, 배포는 이번 범위 밖이다.

## Success Criteria

- [x] J1/J2/J4=`deed_saved`, J3=`deed_judged` 기준과 D7 관찰 질문을 함께 정리했다.
- [x] same-job 유지 여부와 second value evidence 칸을 명시했다.
- [x] `add_flow_started`를 activation 성공으로 보지 않는 금지선을 명시했다.
- [x] `marketing-101` A1-A4 후보와 충돌하거나 중복 확장하지 않음을 확인했다.
- [x] HTML report gate 통과.

## Inherited Learning

- First Value Mapping: J1/J2/J4는 `deed_saved`, J3는 `deed_judged`.
- Prelaunch Decision Boundary: 첫 10-20명은 정성 관찰이며 retention%, PMF, conversion 결론으로 환산하지 않는다.
- Measurement Readiness: 측정 가능성과 측정값 성패를 분리한다.
- Correlation Readiness: D7 대조는 사전 등록된 묶음, window, 제외 조건이 필요하다.
- First-Week Non-Return: D1/D7 미방문은 실패가 아니라 잡별 재가치/재초대 후보 분류다.

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
