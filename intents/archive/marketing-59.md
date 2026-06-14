# marketing-59 — Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T10:00Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- result_summary: Virtue prelaunch PLG 신호를 지금 볼/보류/launch 이후 3열 표와 first-10 수기 review gate로 번역. J1/J2/J4=deed_saved, J3=deed_judged 유지.
- artifacts:
  - path: artifacts/marketing-59/virtue-prelaunch-plg-signal-gate.md
    role: strategy
    note: PLG 3열 신호 위계 표 + first-10 수기 review gate
- reports:
  - path: reports/marketing-59/2026-06-14T1000Z.html
    role: final
- commits:
  - repo: infinity
    sha: (see push)
    note: marketing-59 source note, artifact, archive, report; INTENTS.md inbox→archive
- urls: []
- next_actions:
  - Launch 이후 신호 게이트(Activation rate, D7 재방문, PQL 묶음)는 20+ 실사용자 + D7 경과 후 별도 intent로 개시.
  - first-10 review gate 표는 손기록 보조 용도. 계측 이벤트/PostHog 속성 추진 금지.
  - 신규 이벤트/tracking/privacy/dashboard/public copy/deploy/cost: approval-needed.

## Result

marketing-55가 activation measurement contract를 확정했고, marketing-58이 잡별 first successful output contract를 완성했다. marketing-59는 그 위에 PLG 신호 순서(Foundation→Activation→Conversion)를 Virtue prelaunch 신호 위계로 번역했다.

세 개의 신호 열:
- **지금 볼 신호**: `deed_judged`/`deed_saved` 발화, B-분류, 결과 후 30초 행동, 사용자 자기 말, TTV 느낌 (모두 손기록)
- **보류할 신호**: activation rate, D7 재방문율, PQL 묶음, PMF survey %, deed_save_capped 빈도 등
- **Launch 이후 볼 신호**: 20+ 실사용자 + D7 경과 후 게이트가 열리는 항목들

First-10 수기 review gate 표는 J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑을 잡별 First Win 도달 Y/N으로 관찰하게 설계됐다.

## Verification

- Source note created: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` ✓
- marketing-55 conflict: 0 (activation measurement contract 보존)
- marketing-56 conflict: 0 (first reliable value columns 보존)
- marketing-58 conflict: 0 (first successful output contract 보존)
- Conflict markers: 0
- New events/tracking/privacy/dashboard/public copy/robots/sitemap/MCP/API/pricing/deploy/external message/cost: 0
- HTML report gate strings verified: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함

## Continuation

No new continuation intent needed at this time. Launch-after gates (Activation rate, D7 revisit, PQL bundle) should become a new intent once real users arrive and D7 data is available.
