# Dispatcher 정지·무통지 원인 증거

- canonical: `origin/main`은 local `main`보다 30 commits 앞섰다 (`local=8ab666a`, `origin/main=338c2d3` 조사 시점).
- dispatcher: cron은 10분마다 실행됐고 run record는 canonical revision을 읽었다. cron 자체가 멈춘 것은 아니다.
- 무통지: `20260908T130001Z` handoff가 Active intent를 Waiting으로 전환해 `338c2d3`을 push했지만 `post_handoff_terminal`은 0건이었다.
- 직접 원인: `scripts/run_dispatcher_cycle.sh`가 handoff 전 detached `VERIFY_ROOT`를 post-handoff notifier에도 재사용해 새 Waiting transition을 보지 못한다.
- exporter 범위: read-only dispatcher run record와 canonical Git ref에서 최근 run, outcome, revision mismatch, Active freshness/stale만 노출한다. dispatcher 결함 수정·배포·알림·권한·시크릿 변경은 제외한다.

## 역할 회수 상태

- **Planner:** cron 전체 중단이 아니라 notifier의 새 terminal state 관측 결함으로만 원인을 제한한다. canonical/local SHA·최근 run·handoff·terminal receipt를 교차 확인한 뒤, T1.2 Red와 T1.3 metric contract 전에는 구현하지 않는다.
- **Developer:** `VERIFY_ROOT` 재사용은 handoff 후 원격 정본을 다시 읽지 못하게 하므로, post-handoff terminal notifier가 새 Waiting 전이를 보지 못하는 코드 경로와 일치한다. 이 leaf는 수정이 아니라 read-only 관측 입력을 고정한다.
- **Marketer:** dashboard는 원인을 확정하거나 자동 복구를 약속하지 않는다. `scrape 실패`, `최근 실행 기록 없음`, `정본 불일치`, `Active intent 갱신 지연`을 분리해 다음 점검 위치만 제시한다.
- **Operator:** exporter는 dispatcher run record와 canonical Git ref만 read-only로 읽는다. cron·배포·권한·시크릿·자동 알림 발송은 제외한다.

## T1.1 한계와 인계

이 증거는 notifier 관찰 결함의 원인만 뒷받침한다. cron 중단, Grafana 효과, 사용자 알림 성공 또는 전체 알림 시스템 장애를 증명하지 않는다. 다음 leaf는 T1.2 Red로 원인 표현과 L0 경계를 검증하고, T1.3에서 각 지표가 바꾸는 운영 결정을 고정한다.
