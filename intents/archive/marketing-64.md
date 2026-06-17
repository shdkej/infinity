# marketing-64: Virtue Early Behavior Intent Sequence Columns

- id: marketing-64
- status: archived
- completed_at: 2026-06-17T17:00Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, behavioral-analytics, prelaunch]
- result_summary: activation event vs intent sequence 구분 + early_behavior_sequence 4컬럼(첫 탐색 기능·멈춘 화면·건너뛴 행동·저장 후 다음 행동) docs-only 제안. 기존 marketing-55~63 충돌 0. 신규 이벤트·tracking·privacy·dashboard·public copy·deploy 0.

## Goal

Mixpanel 2026 PLG 행동 기반 의도 신호 렌즈를 Virtue prelaunch first-10 관찰 문맥으로 번역. 기존 first-10/activation 관찰 문서에 `activation event vs intent sequence` 구분과 `early_behavior_sequence` 컬럼 묶음을 제안.

## Success Criteria (충족 여부)

- [x] 신규 이벤트·tracking/privacy·dashboard·public copy·deploy 없음
- [x] docs-only 산출물 1개
- [x] 기존 marketing-55~63 activation 문서와 충돌 0
- [x] source note 경로 참조 포함
- [x] conflict marker 0
- [x] synthetic/test 및 prelaunch low-signal 금지선 유지

## artifacts

- path: artifacts/marketing-64/virtue-early-behavior-intent-sequence-columns.md
  role: design
  note: early_behavior_sequence 4컬럼 정의, J1-J4별 읽기, 기존 컬럼 통합 가이드, 호환성 체크

## reports

- path: reports/marketing-64/2026-06-17T1700Z.html
  role: final

## commits

- repo: infinity
  note: 2026-06-17 Heartbeat — marketing-64 Inbox 처리, artifact + archive + report 생성, INTENTS.md 정리

## urls

## next_actions

- 다음 first-10 관찰 시 `early_behavior_sequence` 4컬럼을 기존 marketing-54~56 필드 뒤에 추가하여 사용
- 런치 후 코호트 의도 경로 대조는 marketing-37 Correlation Readiness 게이트 참조
