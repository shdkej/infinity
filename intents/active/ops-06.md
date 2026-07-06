# [ops-06] weekly_review 동일 주차 블록 교체 게이트

- id: ops-06
- status: waiting
- priority: medium
- permission: L1
- mode: execute_local
- project: openclaw
- created_at: 2026-07-06T11:07Z
- source: sam-proposer via INTENTS.md Inbox

## Goal

weekly_review 생성기가 동일 주차에 대해 실행될 때 기존 블록을 append하지 않고 교체하거나 역할 레이블로 분리하여, 주차별 canonical 블록이 항상 1개만 존재하도록 게이트를 추가한다.

## Success Criteria

- 기존 주차(예: 2026-W27)에 weekly review flow를 실행하면 해당 주차 canonical 블록이 정확히 1개
- 또는 역할 레이블(canonical vs draft/manual-note)로 명확히 구분된 블록이 2개 이하
- 동작 규칙이 생성기/워크플로우 계약에 문서화됨

## Context

- `system/docs/EVALUATION_NOTES.md` — weekly_review.md 동일 주차 중복 누적 + 최신 주차 중복 append 재현 감시 항목
- OpenClaw weekly_review 생성기 스크립트 (로컬 경로 확인 필요)
- 이전 동일 패턴: ops-05 이후에도 W27 기준으로 재현됨

## Prepare Report

- path: reports/ops-06/2026-07-06T1107Z.html
- status: 작성 완료

## Waiting Reason

로컬 Claude Code 실행 대기. 생성기 스크립트 수정 및 dry-run 검증이 로컬 환경에서 필요하다.
Cloud Heartbeat에서 prepare 단계 완료 (2026-07-06T12:XX). 로컬 pt/purplemux pane에 아래 프롬프트 전달 필요.

## Next Action (로컬 Claude Code 위임 프롬프트)

```
Infinity Intent: ops-06 weekly_review 동일 주차 블록 교체 게이트
Mode: execute_local
Goal: weekly_review 생성기가 동일 주차에 재실행될 때 기존 canonical 블록을 교체하거나
      role-split하여 주차별 canonical 블록이 정확히 1개만 남도록 게이트를 추가한다.
Context:
  - system/docs/EVALUATION_NOTES.md 의 weekly_review.md 동일 주차 중복 항목 확인
  - OpenClaw weekly_review 생성기 스크립트 위치 확인 (예: system/scripts/ 또는 skills/ 하위)
Steps:
  1. EVALUATION_NOTES.md 에서 weekly_review 중복 항목 정확히 읽기
  2. 생성기 스크립트에서 주차 키(예: W27) 존재 여부 확인 로직 찾기
  3. 없으면 추가: append 전 동일 주차 블록 유무 확인 → 있으면 replace 또는 skip+warn
  4. 또는 역할 레이블(type: canonical / type: draft) 분리 방식으로 구현
  5. 변경사항을 생성기 주석 또는 워크플로우 계약 문서에 1줄로 기록
  6. dry-run: 기존 주차로 재실행 시 canonical 블록이 1개인지 확인
Allowed: L0/L1 (파일 읽기, 코드 수정, git commit/push)
Forbidden: L2/L3 (프로덕션 변경, force-push 등)
Verification: 해당 주차 블록 카운트가 1인지 확인 (grep -c 또는 수동 확인)
Report back to: reports/ops-06/{timestamp}.html (HTML 필수, ARTIFACT_RULES.md 참조)
```
