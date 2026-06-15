# INTENTS.md 복원 필요

- created: 2026-06-15T13:20Z
- branch: claude/gifted-bohr-ap9p7t
- issue: heartbeat push 중 INTENTS.md 가 헤더+Active 코멘트만 포함된 짧은 버전으로 교체됨 (Archive 섹션 누락)
- action: 이 브랜치를 main에 머지 전에 INTENTS.md를 main 브랜치 버전으로 복원할 것
- active_comment_update: Active 코멘트는 2026-06-15T13:02Z로 업데이트 완료 (status: active-sourcing-spec)
- safe_to_merge: intents/active/naver-shopping-01.md, reports/, artifacts/ 변경분은 안전

## 복원 명령

```bash
git checkout main -- INTENTS.md
# 그 다음 Active 코멘트 한 줄만 업데이트:
# 2026-06-15T00:14Z → 2026-06-15T13:02Z
# status: active-sourcing-first → active-sourcing-spec
# 나머지 내용은 main과 동일
```

이 파일은 복원 완료 후 삭제하세요.
