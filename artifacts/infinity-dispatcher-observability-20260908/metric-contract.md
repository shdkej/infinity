# Dispatcher read-only metric contract

## 목적과 범위

이 계약은 Grafana가 원인을 확정하거나 자동 조치하는 도구가 아니라, **다음 점검 위치를 좁히는 read-only 관측 입력**을 정의합니다. 현재 증거는 cron이 실행된 사례에서 post-handoff terminal notifier가 새 Waiting 전이를 보지 못한 관측 결함까지만 뒷받침합니다.

exporter는 dispatcher run record, 이미 갱신된 local `origin/main` ref, 실행 checkout `HEAD`, canonical `INTENTS.md`·task plan·trace만 읽습니다. `git fetch/pull/push`, cron·dispatcher·notifier 실행, state·trace·plan 쓰기, Slack/Alertmanager 발송, Grafana/Prometheus 배포, 권한·시크릿 접근은 수행하지 않습니다.

## 지표와 판정

| 신호 | 지표·값 | source / fail-safe | 화면 분류와 다음 점검 |
| --- | --- | --- | --- |
| scrape | Prometheus 기본 `up{job="infinity-dispatcher-exporter"}` | scrape 결측·0이면 exporter 값은 unknown | **수집 실패** — `수집 실패: exporter 또는 Prometheus scrape 상태를 확인하세요.` exporter endpoint → Prometheus target/scrape 로그 |
| source validity | `infinity_dispatcher_source_ok{source="run_record\|git_ref\|ledger\|trace"}` (0/1) | 파일 누락·권한·JSON/시간 parse 오류는 0; run/revision/freshness를 0 또는 정지로 위장하지 않음 | 해당 read source를 확인하고, 다른 해석은 unknown으로 유지 |
| recent run | `infinity_dispatcher_last_run_timestamp_seconds` (무라벨 gauge) | canonical run record의 최근 시각만 epoch로 파싱; 결측은 series 없음 | `age ≤15m` 정상, `>15–20m` 점검, `>20m` **최근 dispatcher 실행 기록 없음** — `최근 dispatcher 실행 기록이 없습니다: cron·run record를 확인하세요.` cron 실행 기록 → run record |
| revision | `infinity_dispatcher_revision_mismatch` (0/1, 무라벨) | local canonical `origin/main`과 recorded execution checkout SHA의 exact 40-hex 비교; 한쪽을 읽지 못하면 unknown | `1`이면 **정본 불일치** — `정본 불일치: origin/main과 실행 checkout SHA가 다릅니다.` canonical Git ref → 실행 worktree SHA |
| active freshness | `infinity_dispatcher_active_intents`, `infinity_dispatcher_active_freshness_seconds`, `infinity_dispatcher_active_freshness_known` (모두 무라벨 gauge) | Active가 0이면 count=0, freshness=0, known=1. Active가 있으면 최신 trace/task-plan 갱신과 active leaf `max_minutes`를 읽어 age를 계산; 어느 쪽이 불명확하면 known=0 | `active>0 && known=1 && age>max_minutes`이면 **Active intent 갱신 지연** — `Active intent 갱신 지연: 최근 trace·task-plan·Waiting 전이 사유를 확인하세요.` intent trace → task plan → Waiting 전이 사유 |

## 표시와 의사결정

1. 네 상태는 병렬·독립적으로 표시합니다. revision mismatch와 Active freshness를 하나의 장애 원인으로 합치지 않습니다.
2. `up=0` 또는 필수 `source_ok=0`이면 다른 dispatcher 신호는 **unknown**으로 취급하고 수집 경로를 먼저 확인합니다.
3. run 20분 초과는 실행 기록 부재이지 dispatcher 전체 중단의 확정이 아닙니다. Active freshness 초과는 정지가 아닌 갱신 지연 위험 신호입니다.
4. metric label/value에는 intent ID·제목·Slack/thread·SHA·local path·error detail·receipt·사용자 자유 텍스트를 넣지 않습니다. 고정 `job`/`instance` 및 제한된 source enum만 허용합니다.
5. Grafana의 최소 화면은 `Dispatcher 상태` / `원인 분류` / `다음 점검 위치`로 구성합니다. “자동 복구”, “안정성 개선”, “사용자 알림 성공·유실”, “cron 장애”, “dispatcher가 멈췄다”는 표현을 사용하지 않습니다.

## 구현 입력과 보류

T2 구현은 exporter code·local fixture·`monitoring_personal/prometheus/prometheus.yml`의 명시 scrape job·Grafana dashboard JSON만 대상으로 합니다. Prometheus 기본 scrape 15초는 후속 config 검증 입력일 뿐, 이 계약은 배포·alert rule·notification 변경을 승인하지 않습니다.

## 역할 수렴과 근거

- Planner: 네 지표가 다음 운영 결정을 바꾸고, run 20분/Active leaf max 기준이 반증 가능한지 확인했습니다.
- Developer: `up`은 Prometheus 기본 지표로, 나머지는 무라벨 gauge로 제한했습니다.
- Marketer: 네 분류의 사용자-facing 카피와 과장 금지 표현을 고정했습니다.
- Operator: source-invalid는 fail-safe unknown이며, `origin/main`은 exporter가 fetch하지 않는 local canonical ref임을 고정했습니다.

근거: `root-cause.md`, `t1-red.md`, `task-plan.json`, `/home/ubuntu/workspace/monitoring_personal/docker-compose.yml`, `/home/ubuntu/workspace/monitoring_personal/prometheus/prometheus.yml`.
