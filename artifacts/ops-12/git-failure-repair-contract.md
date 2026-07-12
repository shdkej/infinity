# ops-12 git 실패 처리 계약 (Repair Contract)

## 현재 상태 (broken)

Marketing-agent-growth-review 크론의 git 동기화 실패 패턴 2건:

### 2026-07-10 10:03 UTC
- 실패 연쇄: `stash git changes → pull git changes → push git changes → stash git changes`
- 처리 결과: NO_REPLY로 조용히 종료
- 문제: git 동기화 실패가 INTENTS.md Inbox/Waiting에 blocker 항목을 남기지 않음

### 2026-07-11 10:04 UTC
- 실패 연쇄: `stage git changes → rebase git branch`
- 처리 결과: NO_REPLY로 조용히 종료
- 문제: 동일 — 침묵 처리

## 요구 계약 (Desired Contract)

마케팅 크론 프롬프트/헬퍼에 아래 git 실패 게이트를 추가한다:

### Git Sync Failure Gate

**적용 대상 작업:** git stash, git pull, git push, git add/stage, git rebase, git commit 중 하나라도 실패 시

**금지 행동:** 실패를 무시하고 NO_REPLY로 종료

**필수 행동 (옵션 A — 권장):** INTENTS.md ## Inbox에 신규 ops-* 항목 추가

```
### [ops-N] 마케팅 크론 git 동기화 실패 — {YYYY-MM-DD}
- proposed_by: marketing-cron
- source_signal: Marketing-agent-growth-review git sync failure
- rationale: {실패한 git 명령어}가 {YYYY-MM-DD HH:MM UTC}에 실패했다. 마케팅 크론이 NO_REPLY로 닫히면 이 실패가 사용자-visible blocker로 남지 않는다.
- expected_artifact: 로컬 git 상태 확인 및 수동 sync 후 다음 크론 정상 실행 확인
- permission_level: L1
- success_criteria: git sync가 정상 완료되고 다음 마케팅 크론 실행에서 동일 실패가 재현되지 않는다.
```

**필수 행동 (옵션 B — 최소):** INTENTS.md에 쓸 수 없는 경우 stdout/stderr에 명시적 에러 메시지를 출력하고 exit code 1로 종료 (NO_REPLY와 구별되는 방식)

## 구현 위치

아래 파일 중 marketing cron의 git 동기화를 담당하는 정본 프롬프트 또는 헬퍼 1곳에 반영:

```bash
find ~/.openclaw -name '*.md' | xargs grep -l 'marketing.*cron\|growth.review' 2>/dev/null | head -5
ls ~/.claude/skills/ | grep -i marketing
```

## 검증 방법

수정 후:
1. dry-run으로 git stash가 실패하는 시나리오를 시뮬레이션
2. INTENTS.md Inbox에 신규 blocker 항목이 생성되는지 확인
3. NO_REPLY로 조용히 닫히지 않는지 확인

## 선례

ops-10에서 signal-to-intent proposer의 동일 패턴이 수정됐다 (commit 46c7d62). 같은 방식으로 marketing cron 경로에 적용한다.
