# marketing-59: Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T12:00Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- result_summary: Virtue prelaunch용 PLG 신호 위계를 지금 볼 신호/보류할 신호/launch 이후 볼 신호 3열 표로 번역하고, first-10 수기 review gate 6단계를 작성했다.
- artifacts:
  - path: artifacts/marketing-59/virtue-plg-signal-gate.md
    role: strategy
    note: PLG signal gate 3열 표 + first-10 수기 review gate + 계승/학습/다음 규칙
- reports:
  - path: reports/marketing-59/2026-06-14T1200Z-local.html
    role: final
- commits:
  - repo: infinity
    branch: claude/gifted-bohr-cqq9zu
    note: marketing-59 PLG signal gate complete — Heartbeat 2026-06-14
- urls: []
- next_actions:
  - First-10 observation can use this gate directly. Any new event, dashboard, tracking/privacy, pricing, cap, or deployment remains approval-gated.

## Result

The signal gate preserves the existing first-value mapping:
- J1/J2/J4 = `deed_saved`
- J3 = `deed_judged`

Three-column reading rule:
- **지금 볼 신호**: deed_saved (J1/J2/J4), deed_judged (J3), manual job/value observation, traffic source, deed_rerolled (observation candidate)
- **보류할 신호**: deed_save_capped, signup/page view, D7 rate %, external benchmarks
- **launch 이후 볼 신호**: PQL bundle, paid conversion, expansion, viral coefficient, PostHog dashboard numbers

## Boundaries

No new events, properties, tracking/privacy changes, PostHog dashboard, public copy, production code, deployment, external message, cost, secret, or permission change occurred.  
Conflict markers: 0.  
Source note verified: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`  
Prior contract conflicts (marketing-55/56/58): none.
