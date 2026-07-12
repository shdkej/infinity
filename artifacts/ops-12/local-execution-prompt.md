# ops-12 로컬 실행 프롬프트

Infinity Intent: ops-12 마케팅 크론 git 동기화 실패 반복 경계 고정
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input with C-c and /clear, send this bounded prompt once, then capture the result. Fall back to a fresh bounded `claude --dangerously-skip-permissions -p` only if no usable pt pane exists.
Workflow: simple-doc scale — direct execution acceptable.

Goal: Marketing-agent-growth-review 크론 프롬프트/헬퍼에 git 실패 시 explicit blocker를 생성하는 계약을 추가한다.

Context:
- 실패 패턴 1 (2026-07-10): stash→pull→push→stash 모두 실패 → NO_REPLY 종료
- 실패 패턴 2 (2026-07-11): stage→rebase 실패 → NO_REPLY 종료
- 수정 계약 전문: infinity/artifacts/ops-12/git-failure-repair-contract.md
- 선례: ops-10 commit 46c7d62 (proposer 동일 패턴 수정)

Prepared findings:
- marketing cron 프롬프트에 git failure gate가 없다
- 실패 시 INTENTS.md Inbox에 신규 ops-* blocker를 남겨야 한다 (옵션 A)
- INTENTS.md에 쓸 수 없을 경우 exit code 1로 명시적 에러 종료 (옵션 B)

Steps:
1. marketing cron 프롬프트 파일 위치 찾기:
   find ~/.openclaw ~/.claude/skills -name '*.md' 2>/dev/null | xargs grep -l 'growth.review\|marketing.*cron' | head -5
2. 해당 파일에 git failure gate 계약 추가 (repair-contract.md 참고)
3. 변경 내용 git diff로 확인
4. 변경 커밋
5. dry-run 또는 직접 실행으로 blocker 생성 검증

Allowed: L0/L1 actions only
Forbidden: L2/L3 actions without explicit approval

Verification: git 실패 시나리오에서 INTENTS.md Inbox에 blocker 항목이 생성되는지 또는 exit code 1로 종료되는지 확인

Report back to: infinity repo reports/ops-12/{YYYYMMDDTHHMMZ}-local-fix.html
