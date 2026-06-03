# marketing-37 Virtue activation-retention correlation readiness spec 작성

- id: marketing-37
- status: archived
- completed_at: 2026-06-03T22:07
- projects: [virtue]
- task_type: strategy
- topics: [activation, retention, analytics]
- result_summary: Virtue의 A1~A4 activation 후보를 출시 후 retention과 대조할 때 필요한 D7 우선/D30 보류 창, 제외 조건, pseudo-query shape, prelaunch 금지선을 사전 등록한 readiness spec을 작성했다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/activation-retention-correlation-readiness.md
    role: strategy
    note: A1~A4 후보 묶음, first value 매핑, activation/retention window, 제외 조건, pseudo-query shape, 금지 해석을 정리한 Virtue 내부 문서.
- reports:
  - path: reports/marketing-37/2026-06-03T2207Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: b5c0d2e
    note: docs-only activation-retention correlation readiness spec 추가.
- urls: []
- next_actions:
  - 출시 후 decision-grade 표본과 접근권한이 생기기 전까지 pseudo-query를 실행 결과나 dashboard 요구사항으로 승격하지 않는다.
  - 다음 retention/상관 작업은 `MARKETING_LEARNINGS.md`의 `Correlation Readiness Is A Separate Gate` 기준을 먼저 확인한다.

## Result

Virtue prelaunch 단계에서 activation 후보를 retention과 대조할 준비를 문서화했다. 산출물은 `apps/web/docs/activation-retention-correlation-readiness.md` 1파일이며 제품 코드, 이벤트, 속성, PostHog 설정, dashboard, tracking/privacy, 배포, 외부 발송, 비용, 권한 변경은 0건이다.

핵심 결정은 `measurement readiness`와 `correlation readiness`를 분리한 것이다. m33의 A1~A4 후보 묶음과 W-IMM/W-CONF window는 재정의하지 않고, 그 위에 D7 우선/D30 보류 retention 대조 질문, X-MOCK/X-SYNTH/X-SELF/X-CAP/X-503 제외 조건, 읽기 전용 pseudo-query shape를 사전 고정했다. J1/J2/J4 first value는 `deed_saved`, J3 first value는 `deed_judged`로 유지하며, A3의 미완료 정의는 `deed_judged` 부재로 고정했다. 따라서 J3의 judged-saved 갭은 묶음 미완료나 이탈로 환산하지 않는다.

`MARKETING_LEARNINGS.md`에는 durable learning `Correlation Readiness Is A Separate Gate`를 승격했다. 이는 m34의 `Measurement Readiness Is A Separate Gate` 다음 단계로, retention/상관/D30/monetization 대조 작업에서 쿼리 모양, 창 tier, 제외 조건을 데이터 도착 전에 등록하고 실제 실행은 decision-grade 표본과 접근권한이 있을 때로 분리하라는 규칙이다.

## Verification

- Source note `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-03-activation-retention-correlation.md` 존재 및 인용 확인.
- `activation-candidate-registry.md`의 A1~A4 후보 묶음과 W-IMM/W-CONF window를 계승.
- First value mapping conflict 0: J1/J2/J4=`deed_saved`, J3=`deed_judged`.
- Conflict marker 0, 코드 diff 0, 신규 이벤트/속성/dashboard/tracking/privacy 변경 0.
- HTML report gate 통과: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함.
