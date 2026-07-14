# Infinity Intent: ops-14 — OpenClaw evaluator 읽기 예산 게이트 고정

## Mode
execute_local

## Invocation
pt/purplemux Claude pane 우선 사용 (`tmux -L purple`).
capture → stale 정리 (`C-c`, `/clear`) → 아래 prompt 전송 → 결과 capture.
pane이 없거나 busy/unsafe 상태이면 bounded `claude --dangerously-skip-permissions -p`로 fallback.

## Goal
OpenClaw evaluator 정본 프롬프트/헬퍼에 읽기 예산과 조기 종료 조건을 추가해
NO_REPLY 실행 시 total_tokens를 현재 4.7万~6.7万 범위에서 의미 있게 낮춘다.

## Context
- 문제: evaluator가 NO_REPLY 정상 종료 시에도 4.7万~6.7万 tokens 소비 반복
- 원인: NO_REPLY 결론 전에 EVALUATION_NOTES.md 전체, OPERATING_LESSONS.md 전체, 크론 로그 전체를 로드
- 소스 신호: `system/docs/EVALUATION_NOTES.md#OpenClaw-evaluator-NO_REPLY-실행의-고토큰-반복`
- 준비 리포트: `reports/ops-14/20260714T0000Z-prepare.html`

## Instructions

### 1. evaluator 정본 파일 탐색
```bash
# ~/.claude 하위에서 evaluator 관련 파일 탐색
ls ~/.claude/agents/ 2>/dev/null
ls ~/.claude/skills/ 2>/dev/null
# OpenClaw workspace에서도 확인
find ~/openclaw -name "*evaluat*" -o -name "*EVALUATION*" 2>/dev/null | head -20
```
- `system/docs/EVALUATION_NOTES.md` 의 문제 섹션에서 evaluator 실행 경로/파일명 확인

### 2. 읽기 예산 제한 반영 (3가지)
아래 규칙을 evaluator 정본 프롬프트/헬퍼에 추가한다:

```
# 읽기 예산 (변경 금지)
- EVALUATION_NOTES.md: tail 120줄만 읽는다 (전체 로드 금지)
- OPERATING_LESSONS.md: 관련 섹션 헤더 키워드로 필터 후 해당 섹션만 읽는다 (전체 로드 금지)
- 크론 실행 로그: 최근 24시간 요약만 허용 (전체 로그 금지)
```

### 3. 조기 종료 조건 추가
```
# 조기 종료 게이트 (변경 금지)
- 초기 스캔(위 3가지 읽기)에서 미해결 이슈 없음이 확인되면: 추가 파일 읽기 없이 즉시 NO_REPLY 반환
- 재현 가능한 이슈 1개가 확인되면: 즉시 종료 (나머지 파일 로드 불필요)
```

### 4. 변경 후 검증
```bash
# 수정된 파일에서 읽기 예산 규칙 확인
grep -n "tail" <evaluator_file>
grep -n "120" <evaluator_file>
grep -n "24" <evaluator_file>
grep -n "조기 종료\|early exit\|NO_REPLY" <evaluator_file>
```
- evaluator 1회 dry-run 또는 next cron 대기
- total_tokens가 이전 4.7万~6.7万 범위보다 낮아졌는지 확인

## Allowed
L0/L1 범위: 파일 읽기, 프롬프트/헬퍼 수정, git commit & push (이미 agent-approved L2)

## Forbidden
L3 작업 없음 (force-push, rm -rf, 프로덕션 변경 등)

## Verification Gate
- [ ] evaluator 정본 파일에서 읽기 예산 3종 규칙 확인됨
- [ ] 조기 종료 조건이 반영됨
- [ ] git commit & push 완료
- [ ] 다음 2회 실행에서 NO_REPLY total_tokens가 이전보다 의미 있게 감소

## Report Back
완료 후 infinity 레포에 기록:
- `reports/ops-14/{timestamp}-local-exec.html` (HTML 리포트, TEMPLATE 기반)
- `INTENTS.md`에서 ops-14 status를 `waiting` → `archived`로 전환
- `intents/active/ops-14.md` → `intents/archive/ops-14.md`로 이동 (canonical final index 포맷)
