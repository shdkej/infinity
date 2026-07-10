# [ops-10] Signal-to-intent Proposer Tool-Failure 수리 — 로컬 실행 프롬프트

Infinity Intent: ops-10 Signal-to-intent proposer tool-failure diagnostics repair  
Mode: execute_local  
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to a fresh bounded Claude Code call only if no usable pt pane exists.  
Workflow: For nontrivial local-code or multi-file/shared behavior, use workflow-master first. Find it under `~/.claude/skills/workflow-master/` and `~/.claude/agents/workflow-master.md`.

---

## Goal

Signal-to-intent proposer가 git status/stage/commit/push 호출 실패 시 NO_REPLY로 조용히 종료하는 대신, INTENTS.md Inbox에 **명시적 blocker 항목**을 남기도록 프롬프트 계약 또는 워크플로우를 수정한다.

## Context

- 기간: 2026-07-05~07-09 동안 proposer가 반복 tool-failure → NO_REPLY 종료
- 문제: git 도구 체인 실패가 조용히 흡수되어 실제 blocker가 숨겨짐
- 위치: openclaw workspace의 signal-to-intent proposer 워크플로우 또는 프롬프트 계약
- Prepare report: `reports/ops-10/2026-07-10T1700Z-prepare.html`

## 탐색 경로 후보

```bash
find /home/ubuntu/.openclaw -name "*proposer*" -o -name "*signal*intent*" 2>/dev/null | head -20
find /home/ubuntu/.claude -name "*proposer*" 2>/dev/null | head -10
find /home/ubuntu/.openclaw -path "*/crons/*" -name "*.md" 2>/dev/null | head -20
find /home/ubuntu/.openclaw -path "*/skills/*" -name "*.md" 2>/dev/null | head -20
```

## 수리 단계

### 1단계: git 도구 체인 현재 상태 진단

```bash
cd "$(find /home/ubuntu -name 'infinity' -type d 2>/dev/null | head -1)"
git status
git remote -v
git log --oneline -3
```

### 2단계: proposer 파일 탐색 및 내용 확인

탐색 경로 후보 중 proposer 관련 파일을 찾아 내용 확인:
- tool 호출 실패 처리 규칙이 있는지
- NO_REPLY 처리 경로가 어디인지
- git commit/push 관련 코드/프롬프트가 어디인지

### 3단계: 수리 적용 (옵션 A 우선)

찾은 파일에 다음 규칙을 추가한다:

**프롬프트 계약 추가 규칙 (한국어로 작성):**

```
## Tool 실패 처리 규칙

- git status, add, commit, push 호출이 실패하거나 오류를 반환하면 NO_REPLY로 종료하지 않는다.
- 대신 infinity/INTENTS.md Inbox에 다음 형식으로 blocker 항목을 추가한다:
  
  ### [proposer-blocker-{YYYYMMDD}] git 도구 체인 실패
  - proposed_by: signal-to-intent-proposer
  - source_signal: {실패한 명령어} 오류 메시지 요약
  - permission_level: L1
  - next_action: openclaw에서 git 인증/권한 상태 진단 필요

- cron 관련 도구 호출이 실패하면 report에 오류 메시지를 기록하고 blocker로 남긴다.
- 모든 tool 실패는 "신호 없음 (NO_REPLY)"과 명확히 구별한다.
```

### 4단계: 변경 커밋

```bash
git add -p  # 변경된 파일만 선택적으로 스테이징
git commit -m "fix(proposer): tool-failure → explicit blocker instead of NO_REPLY

ops-10: git/cron tool 호출 실패 시 INTENTS.md Inbox에 blocker 항목 생성 규칙 추가.
이전에는 실패가 NO_REPLY에 흡수되어 실제 blockers가 숨겨졌음."
git push
```

## Allowed

- L0/L1: 파일 읽기, 프롬프트 계약/스킬 파일 수정, git commit/push (openclaw workspace)
- L2 (agent-approvable): openclaw workspace 파일 변경 후 push
  - [x] ops-10 목표와 직접 연결
  - [x] 되돌림 가능 (git revert)
  - [x] 비용 없음
  - [x] 프로덕션/시크릿 미변경
  - [x] 외부 알림 없음

## Forbidden

- git push --force, 브랜치 삭제
- openclaw 외 다른 프로젝트 파일 수정
- 프로덕션 배포

## Verification

수정 후 다음을 확인:
1. `git log --oneline -3` 으로 커밋 생성 확인
2. 수정된 파일 내용 캡처 (변경 규칙 포함 여부)
3. 다음 proposer 실행에서: tool-failure diagnostics 없이 완료 또는 INTENTS.md Inbox에 blocker 항목 생성

## Report back to

`reports/ops-10/{YYYYMMDD}T{HH}00Z-local-fix.html`

(HTML 필수, 결론 2축 양식, reports/_TEMPLATE.html 기반, 감시형 muted gold 색상)
- 축1: 무엇을 점검했나 — 수정 전 상태와 문제 위치
- 축2: 이상 여부·조치 — 수정 결과와 검증 상태
