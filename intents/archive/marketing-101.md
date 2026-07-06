# marketing-101 Virtue 잡별 Activation 후보 묶음 레지스트리

- id: marketing-101
- status: archived
- completed_at: 2026-07-06T0000Z
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, activation]
- result_summary: J1-J4별 first value 이벤트·activation 후보 묶음·관찰 window·이벤트 판독 가능 항목·수기 관찰 항목·표본 부족 시 금지 해석을 1장 레지스트리로 고정했다. marketing-79~100 archive 충돌 없음 확인. source_signal 로컬 파일의 후속 실험 후보 1번 연결만 미완.
- artifacts:
  - path: artifacts/marketing-101/job-activation-bundle-registry.md
    role: design
    note: J1-J4별 activation 후보 묶음 레지스트리 정본. 잡별 first value·묶음·window·이벤트 판독·수기 관찰·금지 해석 포함.
- reports:
  - path: reports/marketing-101/2026-07-06T0000Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - source_signal 파일(/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-01-activation-metric-bundles.md) 로컬 확인 후 J1~J4 묶음 정의와 후속 실험 후보 1번 연결 완료
  - 첫 실사용자 세션 후 레지스트리 실사용 점검 및 빠진 항목 Inbox 등록
  - 5명 이상 관찰 누적 후 Correlation Readiness gate(m37) 진입 여부 판단

## Result

- J1/J2/J4는 `deed_saved`, J3는 `deed_judged`를 first value 이벤트로 고정했다.
- 각 잡마다 이벤트 판독 가능 항목(on-instrument)과 수기 관찰 항목(off-instrument)을 분리했다.
- J3의 `deed_judged` 후 무저장 종료가 정상 종료임을 표에서 명시해 judged-saved 갭 오독을 차단했다.
- 표본 부족 시 공통 금지 해석 목록 및 잡별 금지 해석을 레지스트리에 포함했다.
- marketing-79(관찰표), marketing-98(독립 2판정), marketing-93(언어 적합성)과 충돌 없음 확인.

## Inherited Learning

- First Value Mapping (m06): J1/J2/J4=deed_saved, J3=deed_judged — 레지스트리 전 항목의 first value 기준
- Measurement Readiness Is A Separate Gate (m34): 이 레지스트리는 "측정 가능 상태" 고정이지 성패 판정이 아님
- Prelaunch Decision Boundary (m08): 첫 10명 표본은 정성 손기록 중심, 비율 금지

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
