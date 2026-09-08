# T2.1 read-only implementation evidence

## 변경 파일

- `monitoring_personal/dispatcher-exporter/exporter.py`: local file/Git ref만 읽는 Python `/metrics` exporter
- `monitoring_personal/dispatcher-exporter/Dockerfile`: Git ref read를 위한 `git`만 포함한 runtime
- `monitoring_personal/dispatcher-exporter/fixtures/dispatcher-runs.json`: 합성 run fixture
- `monitoring_personal/dispatcher-exporter/test_exporter.py`: temporary local Git fixture에서 metric 노출·SHA/식별자 비노출 확인
- `monitoring_personal/docker-compose.yml`: read-only `../knowledge-lab/infinity:/data/infinity:ro` mount의 exporter service (기동하지 않음)
- `monitoring_personal/prometheus/prometheus.yml`: 15초 `infinity-dispatcher-exporter` scrape job
- `monitoring_personal/grafana/provisioning/dashboards/dispatcher-status.json`: read-only 4상태 점검 dashboard

## 검증

- `python3 dispatcher-exporter/test_exporter.py`: PASS (1 test)
- `python3 -m py_compile dispatcher-exporter/exporter.py`: PASS
- `jq . grafana/provisioning/dashboards/dispatcher-status.json`: PASS
- Python YAML parse (`docker-compose.yml`, `prometheus.yml`): PASS
- `docker compose config --quiet`: **미실행** — 이 환경에 `docker` CLI가 없음. 컨테이너 기동·배포는 수행하지 않았다.

## 범위 경계

exporter는 fetch/pull/push, cron·dispatcher·notifier 호출, trace/plan 쓰기, alert/Slack 전송, Grafana/Prometheus 배포, 권한·시크릿 접근을 하지 않는다. source parse 실패는 0 또는 “정지”로 위장하지 않고 `source_ok=0` 및 dashboard unknown으로 남긴다. 사용자 행동, 알림 성공, Grafana 효과, 전체 cron 장애는 이 검증으로 주장하지 않는다.
