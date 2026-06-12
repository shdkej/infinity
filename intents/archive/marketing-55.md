# marketing-55: Virtue Prelaunch Activation Measurement Contract

- id: marketing-55
- status: archived
- completed_at: 2026-06-12T10:12
- projects: [virtue]
- task_type: strategy
- topics: [activation, measurement, prelaunch]
- result_summary: Virtue prelaunch activation을 잡별 first value로 고정하고 PQL/paid conversion/expansion/viral coefficient를 launch-after gate로 분리했다.
- artifacts:
  - path: artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md
    role: strategy
    note: Mixpanel 2026 PLG 측정 렌즈를 Virtue first-10 관찰 계약으로 번역한 문서
- reports:
  - path: reports/marketing-55/2026-06-12T1012Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: 329858e
    note: archived activation measurement contract after local verification
- urls: []
- next_actions:
  - First-10 observation notes can reuse the table fields manually; any new event, dashboard, pricing, tracking, public copy, deployment, or external message remains approval-gated.

## Result

The contract keeps the existing first-value mapping intact:

- J1/J2/J4 = `deed_saved`
- J3 = `deed_judged`

The resulting reading rule is:

- `count now`: existing event anchors only.
- `observe manually`: expectation, acquired value, no-save reason, and next-step reason.
- `do not judge yet`: PQL, paid conversion, expansion, viral coefficient, channel quality, retention rate, and pricing intent.

## Boundaries

No new events, properties, tracking/privacy changes, PostHog dashboard, public copy, production code, deployment, external message, cost, secret, or permission change occurred. `build-08` was not modified.
