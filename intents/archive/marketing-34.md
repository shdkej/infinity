# marketing-34 Virtue PLG Foundation exit gate

- id: marketing-34
- status: archived
- completed_at: 2026-06-02T11:07
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement]
- result_summary: Virtue의 Foundation 종료 조건을 활성화 성패가 아니라 측정 가능 상태로 고정하고, Activation 진입 판단을 데이터 품질·synthetic 제외·가용성 차단·같은 잡 재가치로 분리했다.
- artifacts:
  - path: apps/web/docs/plg-foundation-exit-gate.md
    role: strategy
    note: Virtue PLG Foundation 단계 종료 게이트 문서
- reports:
  - path: reports/marketing-34/2026-06-02T1007Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: 2b9d07e
    note: `apps/web/docs/plg-foundation-exit-gate.md` 추가
  - repo: infinity
    sha: this archive commit
    note: HTML report, INTENTS archive entry, marketing learning 승격, archive index
- urls: []
- next_actions:
  - 출시 후 실제 사용자 10명 OR 7일 게이트에서 G6 이벤트 도착 검증과 m33 등록 ID별 도착 점검을 수행한다.

## 결과 요약

Virtue의 기존 first value/activation candidate/baseline/TTV/D7 문서를 재정의하지 않고, PLG Foundation 종료를 위한 G1~G7 readiness 게이트로 집계했다. G1~G5·G7은 선행 문서로 준비됐고, G6 이벤트 도착 검증만 출시 후 확인 대기로 남겼다.

## 검증

- HTML report gate: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함.
- 신규 이벤트·속성·카피·계측·대시보드·코드·배포·외부발송·비용·권한 변경 0.
- `MARKETING_LEARNINGS.md`에 "Measurement Readiness Is A Separate Gate" 승격.
- L2 push 판단: 직접 연결, 되돌림 가능, 비용 0, production/secrets/permissions 변경 0, 제3자 메시징 0, 검증 방법 존재.
