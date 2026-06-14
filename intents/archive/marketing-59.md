# marketing-59 — Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T12:07Z
- projects: [virtue]
- task_type: strategy
- topics: [activation, measurement, prelaunch]
- result_summary: PLG first-win/activation/PQL 신호를 Virtue prelaunch 3열 위계표(지금 볼/보류/launch 이후)와 first-10 수기 review gate(Pre·Session·Post·Self-description 4구간)로 번역했다. J1/J2/J4=deed_saved, J3=deed_judged 유지. 신규 이벤트·tracking·public copy·deploy 0.
- artifacts:
  - path: artifacts/marketing-59/virtue-plg-signal-gate.md
    role: strategy
    note: PLG 신호 3열 위계표 + first-10 수기 review gate
- reports:
  - path: reports/marketing-59/2026-06-14T1207Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: TBD
    note: Heartbeat 2026-06-14 실행
- urls: []
- next_actions:
  - First-10 관찰 시작 시 artifact의 review gate 체크리스트를 손기록으로 사용한다.
  - 신규 이벤트·PostHog dashboard·공개 카피·배포는 여전히 approval-needed.
  - Launch 이후 신호 열기 전에 Measurement Readiness gate를 재확인한다.

## Verification

- source_note_exists: true (`source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`)
- prior_conflict_markers: 0
- marketing-55 conflict: none (activation measurement contract preserved)
- marketing-56 conflict: none (first reliable value columns preserved)
- marketing-58 conflict: none (first successful output contract preserved)
- production_code_changes: 0
- tracking_privacy_changes: 0
- new_events: 0
- public_copy_changes: 0
- deployment: 0

## Result Summary

**축1 (무엇이 문제)**: Virtue prelaunch에서 acquisition·activation·measurement-too-early 세 가지 상태를 첫 10명 관찰에서 혼동할 위험이 있었다.

**축2 (어떻게 해결)**: PLG 신호를 지금 볼(8개)/보류(8개)/launch 이후(6개) 3열로 분류하고, First-10 수기 review gate를 Pre·Session·Post·Self-description 4구간으로 정리했다.
