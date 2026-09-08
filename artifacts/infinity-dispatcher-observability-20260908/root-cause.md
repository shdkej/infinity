# Dispatcher 정지·무통지 원인 증거

- canonical: `origin/main`은 local `main`보다 30 commits 앞섰다 (`local=8ab666a`, `origin/main=338c2d3` 조사 시점).
- dispatcher: cron은 10분마다 실행됐고 run record는 canonical revision을 읽었다. cron 자체가 멈춘 것은 아니다.
- 무통지: `20260908T130001Z` handoff가 Active intent를 Waiting으로 전환해 `338c2d3`을 push했지만 `post_handoff_terminal`은 0건이었다.
- 직접 원인: `scripts/run_dispatcher_cycle.sh`가 handoff 전 detached `VERIFY_ROOT`를 post-handoff notifier에도 재사용해 새 Waiting transition을 보지 못한다.
- exporter 범위: read-only dispatcher run record와 canonical Git ref에서 최근 run, outcome, revision mismatch, Active freshness/stale만 노출한다. dispatcher 결함 수정·배포·알림·권한·시크릿 변경은 제외한다.

## 역할 회수 상태

- Developer·Operator: 완료.
- Planner·Marketer: Gateway timeout. multi-role 계약상 구현 전 재시도가 필요하다.
