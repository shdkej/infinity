# Developer
- Infinity dispatcher는 이미 `scripts/run_dispatcher_cycle.sh`에서 detached clean worktree를 사용한다.
- 실제 최소 수정 대상은 proposer의 Knowledge Lab checkpoint write/commit 경로다.
- 구현안: `origin/main` 기반 임시 checkout, exact checkpoint paths만 `git add --`, no-op 허용, non-force push, 세 SHA 비교.
- 현재 proposer payload/job이 인증 범위에 노출되지 않아 구현·실행은 보류했다.
