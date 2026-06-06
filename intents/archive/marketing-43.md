# marketing-43 Virtue 첫 주 재초대 경계표

- id: marketing-43
- status: archived
- completed_at: 2026-06-06T22:07Z
- projects: [virtue]
- task_type: strategy
- topics: [retention, reactivation, onboarding]
- result_summary: 첫 주 D1/D3/D7 미방문을 onboarding 실패가 아니라 잡별 재초대 후보(RC-WARM/RC-PRE-LOST/RC-NORMAL/RC-AVAIL/RC-EXCLUDED)로 읽고, J1~J4별 first value·놓친 second value·돌아올 이유·보내면 안 되는 조건·승인 필요선을 한 표로 고정한 docs-only 내부 경계표를 작성했다. 발송 0건.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/first-week-reactivation-boundary-table.md
    role: strategy
    note: 미방문을 잡별 재초대 후보로 분류, value recall 방향·do-not-send·approval-needed line, no-new-instrumentation.
- reports:
  - path: reports/marketing-43/2026-06-06T2207Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: 573da8a
    note: Add first-week reactivation boundary table and remove stale tool wrapper lines.
- urls: []
- next_actions:
  - 첫 10명/첫 7일 실사용 관찰 전에는 본 문서를 m14 bridge 위 재초대 분류 렌즈로만 사용한다.
  - 재초대 카피 확정·small-batch 발송은 출시 승인 뒤 J1~J4별 1문장 value recall 후보를 별도 Waiting/approval-needed로 올린다.
  - `last_value_seen`·`missed_second_value`·`reactivation_candidate_type` 수기 칸 추가 여부는 신규 tracking 없이 proposal-only로 검토.
