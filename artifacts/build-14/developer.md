# build-14 Developer Notes

작성 시각: 2026-08-05
역할: Developer
소유 범위: 기술 구현 경로, 기존 코드 위치, 데이터 계약, 8시간 MVP 작업 순서

## 결론

첫 버전은 기존 `Infinity` 정적 사이트 아래에 독립 페이지로 둔다.

- 대상 페이지: `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/index.html`
- 데이터 파일: `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/data/system-metrics.json`
- 공개 예상 URL: `https://infinity.aws.shdkej.com/build-14/index.html`
- 구현 방식: self-contained static HTML/CSS/JS + public-safe JSON aggregate

이 경로가 가장 단순하다. 새 도메인, 새 Terraform, 새 서버, Grafana 공개 설정, CMS 쓰기 권한이 필요 없다. 기존 `sites/registry.json`에 이미 `infinity.aws.shdkej.com`이 등록되어 있으므로 정적 배포 레인을 그대로 쓴다.

## 기존 관련 코드 위치

### 1. Infinity static site - 이번 MVP의 권장 수정 지점

- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/index.html`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/index.html`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/data/system-metrics.json`

현재 build-14 로컬 페이지와 샘플 JSON이 이미 존재한다. 다음 구현자는 이 두 파일을 이어서 고치면 된다.

### 2. Static site registry / Status feed

- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/registry.json`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/scripts/build-status-json.py`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/status/dist/status.json`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/status/dist/index.html`

`registry.json`은 Status, Travel, Schengen, Library, Infinity, Virtue, CMS, Reel Room의 공개 URL과 배포 종류를 가진다. `build-status-json.py`는 이 registry를 읽어 `status.json`을 만든다. 이 흐름은 사이트 alive/deploy health에는 좋지만, 개인 운영 지표를 직접 넣으면 공개 범위가 섞이므로 build-14의 주 데이터 원천으로 쓰지 않는다. 필요한 경우 `status.json`에서 Infinity URL 상태만 보조 지표로 가져온다.

### 3. 이전 Control Center / Status 작업

- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-03/control-center-dashboard-ops-cms-inventory.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-04/control-center-mvp-deployment.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-09/control-center-authenticated-publish-rollback-spec.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/reports/build-11/2026-06-16T1430Z-prepare.html`
- `/home/ubuntu/workspace/space/apps/control-center-cms/app/page.jsx`
- `/home/ubuntu/workspace/space/apps/control-center-cms/lib/status-meta.js`

주의: build-04 문서에는 `sites/status/dist/control-center/index.html` 배포 기록이 있지만, 현재 파일 트리에는 해당 정적 파일이 보이지 않는다. 따라서 이번 MVP에서 Control Center를 되살리거나 CMS를 확장하지 않는다.

### 4. 기존 Grafana/Prometheus monitoring

- `/home/ubuntu/workspace/monitoring_personal/docker-compose.yml`
- `/home/ubuntu/workspace/monitoring_personal/prometheus/prometheus.yml`
- `/home/ubuntu/workspace/monitoring_personal/grafana/provisioning/dashboards/main.json`
- `/home/ubuntu/workspace/monitoring_personal/grafana/provisioning/dashboards/layer-system.json`
- `/home/ubuntu/workspace/monitoring_personal/grafana/provisioning/dashboards/layer-business.json`
- `/home/ubuntu/workspace/monitoring_personal/grafana/provisioning/dashboards/layer-product.json`
- `/home/ubuntu/workspace/monitoring_personal/posthog-exporter/index.js`

이미 Prometheus, Grafana, Node Exporter, Loki, YACE, PostHog exporter 구성이 있다. 하지만 이건 운영 모니터링 stack이고, 이번 요청의 "매일 보는 개인 시스템 지표 페이지"와 공개/권한/데이터 계약이 다르다. MVP에서는 직접 Grafana를 공개하지 않고, 필요하면 나중에 일일 aggregate exporter만 붙인다.

## 권장 구현 경로

### 데이터 수집 원천

첫 8시간 MVP는 원문 로그 대신 public-safe aggregate만 쓴다.

- Infinity: `/home/ubuntu/workspace/knowledge-lab/infinity/INTENTS.md`, `intents/active/*.md`, `artifacts/*/STATUS.md`, `reports/*`
- OpenClaw 운영: `/home/ubuntu/.openclaw/workspace/memory/YYYY-MM-DD.md`, `system/docs/OPERATING_LESSONS.md`, `system/data/daily-tracking/`, `system/data/daily-reviews/`
- Static site health: `sites/status/dist/status.json`에서 URL alive, latency, generatedAt만 선택적으로 사용
- Monitoring stack: 첫 버전에서는 직접 연결하지 않음. Prometheus/Grafana는 후속 지표 원천 후보

`openclaw cron list --json`, `openclaw memory status --index --agent main` 같은 CLI는 timeout과 fallback 없이 페이지 생성 경로에 넣지 않는다. 멈추면 매일 갱신 전체가 막힌다.

### 저장 파일 형식

단일 JSON 파일을 사용한다.

```json
{
  "schema_version": "2026-08-05.daily-system-metrics.v1",
  "generated_at": "2026-08-05T22:38:00Z",
  "timezone": "Asia/Seoul",
  "source": {
    "mode": "sample_contract",
    "notes": "Replace with daily generated aggregates only; do not publish raw private logs."
  },
  "metrics": [
    {
      "date": "2026-08-05",
      "life": { "plan_blocks": 2, "check_done": 0, "energy": 4 },
      "infinity": { "active": 3, "archived": 0, "waiting": 1, "new_intents": 1 },
      "automation": { "cron_ok": 8, "cron_failed": 1, "no_reply": 3 },
      "knowledge": { "daily_review": 0, "wiki_updates": 1, "query_gaps": 0 }
    }
  ]
}
```

규칙:

- `metrics[]`는 KST 기준 하루 1행이다.
- 값은 숫자 집계만 둔다.
- 공개 JSON에는 메시지 원문, 프롬프트, secret, 계정 식별자, private URL, raw command output을 넣지 않는다.
- 새 지표는 기존 group 아래 numeric field로 추가한다.
- 화면은 `schema_version`이 맞지 않거나 `metrics`가 비었을 때 stale/empty 상태를 보여야 한다.

### 렌더링 / 배포 경로

1. `sites/infinity/dist/build-14/index.html`이 `./data/system-metrics.json`을 fetch한다.
2. JS가 최근 7/14/30일을 필터링하고 line chart와 최신 요약을 그린다.
3. 수집 스크립트는 나중에 `system-metrics.json`만 갱신한다.
4. `space` repo commit/push 후 기존 static site GitHub Actions가 `static-infinity-aws-shdkej-com`에 sync한다.
5. 라이브 확인은 `https://infinity.aws.shdkej.com/build-14/index.html`와 JSON URL을 둘 다 확인한다. 현재 배포 워크플로우는 최상위 HTML만 extensionless route로 복제하므로 `/build-14/`는 공식 URL로 쓰지 않는다.

### 테스트 방법

- JSON parse: `python3 -m json.tool sites/infinity/dist/build-14/data/system-metrics.json`
- secret scan: `rg -n "sk-|AKIA|BEGIN .*PRIVATE|api[_-]?key|token|secret|Authorization|Bearer" sites/infinity/dist/build-14`
- local static server: `python3 -m http.server 8000 --directory sites/infinity/dist`
- browser check: `/build-14/` desktop/mobile screenshot, chart nonblank, tabs/range control 동작, empty/stale fallback 확인
- live check after deploy: `curl -I https://infinity.aws.shdkej.com/build-14/index.html` and `curl -I https://infinity.aws.shdkej.com/build-14/data/system-metrics.json`

## 8시간 MVP 체크리스트

- [ ] 현재 dirty 상태 확인: `space/infra-aws-static-sites`와 `knowledge-lab/infinity`에서 unrelated changes 분리
- [ ] `system-metrics.json` schema를 위 계약으로 고정하고 샘플 데이터에 `source.mode = "sample_contract"` 명시
- [ ] `index.html`이 JSON fetch 실패, 빈 metrics, 오래된 `generated_at`을 깨지지 않고 표시하는지 보강
- [ ] 자동화 / 일감 흐름 / 지식 흐름 3개 이상 지표군을 line chart로 표시
- [ ] sample 데이터 배지를 화면에 명확히 표시하고 실제 지표처럼 말하지 않게 수정
- [ ] 데이터 생성 스크립트 초안 추가 여부 결정. 8시간 안에 어렵다면 JSON 계약과 수동 갱신 절차만 고정
- [ ] JSON parse와 secret scan 실행
- [ ] 로컬 static server에서 desktop/mobile screenshot 확인
- [ ] 배포 전 사용자 승인 필요 여부 확인. 공개 페이지 변경이므로 자동 공개가 부담되면 로컬 검증까지만 보고
- [ ] 승인되면 `space` repo에서 scoped commit/push 후 GitHub Actions와 라이브 URL 확인

## 변경 파일

이번 Developer 정리에서 수정한 파일:

- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-14/developer.md`

이미 존재하는 구현 후보 파일:

- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/index.html`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist/build-14/data/system-metrics.json`

## 현재 검증 상태

- `rg --files`와 `rg`로 `build-11`, `status`, `dashboard`, `personal-ops`, `metrics`, `visualization` 관련 흔적을 확인했다.
- 관련 문서와 코드 후보를 읽었다.
- 브라우저 렌더링 검증과 라이브 배포 검증은 아직 실행하지 않았다.
- 다른 에이전트 변경 가능성이 있어 이번 턴에서는 본인 소유 파일인 `developer.md`만 수정했다.
