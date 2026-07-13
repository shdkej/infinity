# ops-13 로컬 실행 프롬프트

Infinity Intent: ops-13 마케팅 inbox 한국어 렌더 게이트 고정
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input with C-c and /clear, send this bounded prompt once, then capture the result. Fall back to a fresh bounded `claude --dangerously-skip-permissions -p` only if no usable pt pane exists.
Workflow: simple-doc scale — direct execution acceptable.

Goal: 마케팅 크론의 `system/data/agent-inbox/marketing.jsonl` 저장 직전, signal/diagnosis/action_candidate/measurement 필드에 영어 서술형 문장이 혼재하지 않도록 렌더 게이트를 정본 프롬프트나 헬퍼에 반영한다.

Context:
- 드리프트 신호 소스: `system/docs/EVALUATION_NOTES.md#마케팅-에이전트-inbox-영어-문장-드리프트-최신-재현`
- 재현 날짜: 2026-07-12, 2026-07-13 marketing inbox 항목 (signal, measurement 필드 영어 서술형)
- 관련 선례: ops-12 (git failure gate, 동일 저장 경로에 게이트 추가한 패턴)
- ops-12 로컬 실행 프롬프트: `infinity/artifacts/ops-12/local-execution-prompt.md` (참고용)

Prepared findings:
- 마케팅 크론 저장 경로에 한국어 렌더 게이트 없음
- 게이트 대상 필드: signal, diagnosis, action_candidate, measurement
- 게이트 발동 조건: 필드 값이 영문 위주 서술형 문장(첫 단어가 영어 단어이고, 문장 형태)인 경우
- 허용 예외: 코드, URL, CLI 명령, 고유 서비스명/제품명, JSON 필드명 — 이들만 포함된 값은 원문 유지
- 처리 방법: (A) 한국어 운영 문장으로 변환 후 저장, (B) 변환 어려우면 저장 보류 후 Infinity Inbox에 blocker 항목 생성

Steps:
1. 마케팅 크론 프롬프트 파일 위치 찾기:
   find ~/.openclaw ~/.claude/skills -name '*.md' 2>/dev/null | xargs grep -l 'growth.review\|marketing.*cron\|marketing.jsonl' | head -5
2. EVALUATION_NOTES.md에서 실제 영어 서술형 문장 예시 확인 (재현 입력용)
3. 해당 파일에 렌더 게이트 계약 추가:
   - signal/diagnosis/action_candidate/measurement 저장 직전 언어 검사
   - 영어 서술형 감지 → 한국어 변환 또는 저장 보류
4. 변경 내용 git diff로 확인
5. 재현 입력으로 dry-run: 2026-07-12/13 예시를 입력했을 때 게이트가 발동하는지 확인
6. 변경 커밋

Allowed: L0/L1 actions only
Forbidden: L2/L3 actions without explicit approval

Verification: 재현 입력(영어 서술형 signal/measurement)을 넣었을 때 저장이 보류되거나 한국어로 변환되는지 확인. 다음 마케팅 크론 실행 후 marketing.jsonl에 영어 서술형 문장이 혼재하지 않음 확인.

Report back to: infinity repo reports/ops-13/{YYYYMMDDTHHMMZ}-local-fix.html
