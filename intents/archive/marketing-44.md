# marketing-44 Virtue 결과 카드 직후 30초 행동 감사표

- id: marketing-44
- status: archived
- completed_at: 2026-06-07T10:07
- projects: [virtue]
- task_type: strategy
- topics: [ai-product, activation, onboarding, measurement]
- result_summary: Virtue 결과 카드 직후 30초를 세션 전체와 분리된 수기 판독 단위로 고정하고, J1~J4별 활성화/정상/보류/마찰 분류와 do-not-send/do-not-change 경계를 문서화했다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/post-response-30-second-action-audit-table.md
    role: strategy
    note: 결과 카드 직후 행동 흐름 감사표. 기존 이벤트 앵커만 사용하며 신규 계측·카피·코드 변경 없음.
- reports:
  - path: reports/marketing-44/2026-06-07T1007Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: 838f8a2
    note: docs-only artifact commit
  - repo: infinity
    sha: cbcfaba
    note: report, archive, learning promotion
- urls: []
- next_actions:
  - 첫 10명 또는 첫 7일 관찰에서 비율 결론 없이 결과 직후 첫 행동이 행 단위로 분류되는지만 확인한다.

## Result

결과 카드(`deed_judged`:106) 직후 행동은 잡별로 부호가 다르다. J3는 결과 카드 자체가 first value라 저장 없이 종료해도 정상일 수 있고, J1/J2/J4는 결과 카드가 저장 전 통과점이라 `deed_saved`:183까지 이어져야 활성화로 읽는다.

문서는 `deed_saved`, `deed_rerolled`, `deed_save_capped`, 저장 없는 종료, off-instrument 행동을 activation/normal/hold/friction 네 칸으로 분류한다. `deed_save_capped`는 availability/friction으로 유지했고, synthetic/mock/self-test와 작은 표본은 decision-grade 지표로 승격하지 않았다.

## Verification

- HTML report gate: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함.
- event anchor drift: 0 (`add_flow_started`:72, `add_flow_abandoned`:78, `deed_judged`:106, `deed_judge_attempted`:135, `deed_rerolled`:149, `deed_save_capped`:167, `deed_saved`:183, `level_up_viewed`:199).
- code diff: 0 (`apps/web/src`, `apps/ios` 변경 없음).
- conflict marker: 0.
- 신규 이벤트·속성·카피·tracking/privacy·dashboard·session replay·타이머·발송·비용·권한 변경: 0.

## Learning

`MARKETING_LEARNINGS.md`에 durable learning candidate `Post-Response Flow Reveals Value, Not The Result Event`를 승격했다.
