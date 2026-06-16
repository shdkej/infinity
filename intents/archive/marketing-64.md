# marketing-64: Virtue Early Behavior Intent Sequence Columns

- id: marketing-64
- status: archived
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, behavioral-analytics, prelaunch]
- permission: L1 docs-only
- created_at: 2026-06-16T22:00Z
- completed_at: 2026-06-16T22:00Z
- owner: Infinity Heartbeat

## Goal

기존 first-10/activation 관찰 문서에 `activation event vs intent sequence` 구분과 `early_behavior_sequence` 컬럼 묶음(첫 탐색 기능, 멈춘 화면, 건너뛴 행동, 저장 후 다음 행동)을 제안한다.

## Result Summary

`activation event`(단일 first value 이벤트) vs `intent sequence`(전·후 행동 흔적) 구분을 명시적으로 도입하고, first-10 수기 관찰 테이블용 `early_behavior_sequence` 4열 묶음을 제안했다. 신규 이벤트·tracking·privacy·dashboard·public copy·deploy 0. marketing-55~63 activation 문서와 충돌 0.

## Artifacts

- `artifacts/marketing-64/virtue-early-behavior-intent-sequence-columns.md`

## Reports

- `reports/marketing-64/2026-06-16T2200Z.html`

## Next Actions

- 없음 (docs-only 완료)
- 후속 마케팅 작업에서 `early_behavior_sequence` 제안을 first-10 관찰 템플릿에 통합 여부 검토

## Verification

- [x] source note 존재 확인: Inbox 설명에 source 명시됨
- [x] conflict marker: 0
- [x] synthetic/test 및 prelaunch low-signal 금지선 유지
- [x] 신규 이벤트·tracking·privacy·dashboard·public copy·deploy: 0
- [x] marketing-55~63 충돌 없음 (MARKETING_LEARNINGS.md 기준 대조)
