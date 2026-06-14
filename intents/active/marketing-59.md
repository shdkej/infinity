# marketing-59 — Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: waiting
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- permission: L1 docs-only
- created_at: 2026-06-14T10:00Z
- updated_at: 2026-06-14T10:15Z

## Purpose

최신 PLG 자료의 first win / activation / PQL 우선순위를 Virtue prelaunch 신호 위계로 번역한다.

기대효과: acquisition 문제, activation 문제, measurement-too-early 상태를 첫 10명 관찰에서 혼동하지 않게 한다.

## Success Criteria

- J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지
- `지금 볼 신호 / 보류할 신호 / launch 이후 볼 신호` 표 완성
- first-10 수기 review gate 작성
- 선행 marketing-55/56/58 충돌 없음 확인
- production code / tracking / privacy 변경 0

## First Gate (실행 전 필수 확인)

- [ ] `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` 존재 확인 — **현재 미존재 (BLOCKER)**
- [ ] marketing-55/56/58 충돌 없음 확인
- [ ] conflict marker 0 확인
- [ ] production code/tracking/privacy 변경 0 확인

## Current State

- 2026-06-14T10:15Z **Inbox → Active 전환. source note 미존재로 실행 대기.** `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`가 존재하지 않아 first_gate 실패. 파일이 추가되면 즉시 실행 가능. 실행 범위: docs-only, Infinity 캐노니컬 루트 내, virtue-rebirth-app 미변경.

## Blocker

- **source note 미존재**: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`를 사용자가 추가해야 함.
- route: user-side (사용자가 PLG 자료를 읽고 source note 파일을 생성해야 함)
- work_continues: no (source note가 실행의 핵심 입력 자료)

## Notes

- 선행 참조 artifact: marketing-55/56/58
- PostHog는 읽기 전용 미래 체크리스트로만 — 실제 access/project id 없이 metrics 생성 금지
- 실행 시 Virtue prelaunch 단계(low-signal learning mode) 적합성 유지
