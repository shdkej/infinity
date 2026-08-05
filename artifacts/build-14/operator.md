# build-14 Operator Notes - Daily System Metrics Visualization

작성 시각: 2026-08-05
역할: Operator
소유 범위: 데이터 갱신 경로, 배포/라이브 검증, 장애/비용/보안 경계

## 운영 목표

Daily System Metrics Visualization은 매일 "시스템이 잘 돌고 있는가"를 한눈에 확인하는 운영 페이지다. 첫 버전은 새 인프라를 늘리기보다, 이미 등록된 Infinity 정적 사이트(`infinity.aws.shdkej.com`)와 Knowledge Lab / OpenClaw 로컬 운영 데이터를 연결하는 방향이 가장 안전하다.

완료 기준은 다음 5가지다.

- 최근 N일 지표가 날짜별로 보인다.
- 최소 3개 이상 지표군이 그래프로 보인다.
- 데이터 생성/갱신 경로가 문서화되어 있다.
- 정적 사이트 배포 후 라이브 URL에서 확인된다.
- 실패했을 때 사용자에게 보여줄 상태와 복구 첫 액션이 정해져 있다.

## 매일 지표 갱신 경로 후보

### 후보 A - 정적 JSON 스냅샷 갱신

첫 버전 권장 경로다.

- 수집 스크립트가 매일 `system` / Knowledge Lab / Infinity의 운영 파일을 읽는다.
- 결과를 날짜별 JSON으로 만든다.
- Developer가 정한 정적 앱 경로 아래, 예를 들어 `infra-aws-static-sites/sites/infinity/dist/metrics.json` 또는 `daily-metrics.json`에 쓴다.
- repo push 후 GitHub Actions가 `infra-aws-static-sites/sites/infinity/dist/**` 변경을 감지해 S3 sync와 CloudFront invalidation을 수행한다.
- 페이지는 이 JSON만 읽어 그래프를 렌더한다.

장점:

- S3 + CloudFront 정적 호스팅만 사용하므로 새 런타임 비용과 장애면이 작다.
- 데이터 스키마가 고정되면 지표 추가가 쉽다.
- 라이브 페이지 장애와 수집 장애를 분리해서 볼 수 있다.

주의:

- 개인정보가 섞인 원문 로그를 JSON에 넣으면 안 된다.
- 매일 push 기반 배포가 필요하므로 git dirty 상태와 GitHub Actions 상태를 운영 체크에 포함해야 한다.

### 후보 B - Status board feed 확장

기존 `scripts/build-status-json.py`와 `sites/status/dist/status.json` 흐름을 확장하는 방식이다.

- 현재 status board는 `sites/registry.json`의 사이트 목록과 AWS/URL health check를 합쳐 `status.json`을 만든다.
- Daily Metrics는 이 흐름에서 일부 상태 지표만 가져와 사용할 수 있다.
- 단, 사용자 개인 시스템 지표까지 status board feed에 넣으면 공개 범위가 섞일 수 있으므로 첫 버전의 주 데이터 경로로는 보류한다.

적합한 데이터:

- 사이트별 URL alive/warn
- CloudFront distribution 확인 여부
- 배포 시각
- 정적 앱 registry 상태

보류할 데이터:

- 개인 회고/생활 데이터
- OpenClaw agent 내부 로그 원문
- 비용/토큰/계정 상태처럼 민감한 값

### 후보 C - 로컬 수집 + 별도 agents-live feed

status 배포 스크립트가 `agents-live.json`을 삭제하지 않도록 exclude하고 있으므로, 라이브 수집기가 S3에 별도 feed를 올리는 구조가 이미 염두에 있다.

- system-dashboard collector가 있거나 새로 만들 수 있다면 `agents-live.json`류의 별도 feed로 운영 지표를 갱신한다.
- 정적 페이지 배포 없이 데이터만 갱신할 수 있다.
- 다만 S3 쓰기 권한, collector 실행 주기, 장애 알림 계약을 확인해야 하므로 첫 버전에서는 후순위다.

## 자동 수집할 데이터

첫 버전 자동 수집은 "원문을 공개하지 않아도 되는 집계값"만 허용한다.

### Infinity 작업 지표

- Inbox / Active / Waiting / Archive lane별 intent 수
- 최근 24시간 생성 intent 수
- 최근 24시간 archive 수
- active intent 중 deadline 초과 수
- build/report/artifact 존재 여부

수집 소스 후보:

- `/home/ubuntu/workspace/knowledge-lab/infinity/INTENTS.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/intents/active/*.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/*/STATUS.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/reports/*/*.html`

공개 가능한 형태:

- 개수, 상태, 날짜, intent id
- 제목은 공개 여부가 애매하면 짧은 slug 또는 id만 사용

### OpenClaw 런타임 지표

- 로그 보존 스크립트 최근 실행 여부
- SQLite maintenance dry-run/backup 실행 여부
- memorySearch provider/index 상태
- gateway 재시작 감지 횟수
- 주요 cron/agent 상태: ok/warn/fail 집계

수집 소스 후보:

- `/home/ubuntu/.openclaw/workspace/system/docs/OPENCLAW_RUNTIME_MAINTENANCE.md`
- `/home/ubuntu/.openclaw/workspace/memory/YYYY-MM-DD.md`
- `~/.openclaw/logs/log-retention.log`
- `openclaw memory status --index --agent main`
- `openclaw cron list --json`

주의:

- `openclaw cron list --json`은 2026-08-05 작성 시점 확인에서 응답이 멈춰 수동 중단했다. 자동 수집에 넣기 전 timeout과 fallback이 필요하다.
- memory/search 계열 확인은 SQLite lock 경고를 피하기 위해 에이전트별 순차 실행으로 제한한다.

### 리뷰/생활 운영 루프 지표

- 일일 리뷰 파일 존재 여부
- 주간/월간 리뷰 원장 갱신 여부
- 오늘 헤드라인/내일 의도 캘린더 반영 여부
- spaced repetition 항목 추가 수
- daily tracking 입력 존재 여부

수집 소스 후보:

- `/home/ubuntu/.openclaw/workspace/system/data/daily-reviews/`
- `/home/ubuntu/.openclaw/workspace/system/data/weekly_review.md`
- `/home/ubuntu/.openclaw/workspace/system/data/monthly_review.md`
- `/home/ubuntu/.openclaw/workspace/system/data/daily-tracking/`
- `/home/ubuntu/.openclaw/workspace/system/data/spaced_repetition_items.json`

공개 가능한 형태:

- 완료/미완료, 개수, 날짜
- 회고 본문, 캘린더 이벤트 내용, 생활 세부 수치는 공개 JSON에서 제외

## 수동 또는 보류할 데이터

### 수동 확인으로 둘 데이터

- 비용 추정: AWS CloudFront/S3 비용, OpenAI embedding 비용, 기타 API 사용량은 첫 버전에서 숫자 자동 공개하지 않는다. 운영자가 월 1회 콘솔/청구서로 확인해 상태만 적는다.
- 외부 계정 quota: OpenAI, Google, AWS credentials 상태는 `ok/warn`으로만 남기고 키/프로젝트/청구 상세는 노출하지 않는다.
- calendar write 성공 여부: Google Calendar는 개인 생활 정보가 섞이므로 공개 지표에는 "반영됨/보류/실패" 정도만 쓴다.

### 보류할 데이터

- Telegram/대화 원문
- 사용자 위치, 일정, 감정, 건강, 소비 상세
- API key, token, account id, billing id
- OpenClaw raw logs와 stack trace 전문
- agent별 사적 memory 내용
- 외부 서비스의 비공개 dashboard 스크린샷 또는 상세 수치

## 배포 체크리스트

### 배포 전

- `git status --short`로 target repo dirty 상태를 확인한다.
- 이번 변경이 `infra-aws-static-sites/sites/infinity/dist/**`에 들어갔는지 확인한다.
- 데이터 JSON에 민감정보가 없는지 `rg`로 토큰/키/이메일/원문 로그 패턴을 확인한다.
- JSON이 valid인지 확인한다.
- 로컬에서 페이지가 JSON을 읽고 빈 그래프 없이 렌더되는지 확인한다.
- 모바일/데스크톱 화면에서 텍스트 겹침과 그래프 빈 상태를 확인한다.

### 배포

- `infra-aws-static-sites/sites/infinity/dist/**` 변경을 `space` repo에 commit/push한다.
- GitHub Actions `Deploy static site to AWS`가 push path를 감지해야 한다.
- workflow는 기본으로 다음을 수행한다.
  - app 변경 감지
  - AWS OIDC role assume
  - bucket: `static-infinity-aws-shdkej-com`
  - CloudFront distribution alias: `infinity.aws.shdkej.com`
  - S3 sync `--delete`
  - HTML extensionless route upload
  - CloudFront invalidation `/*`

### 라이브 검증

- `https://infinity.aws.shdkej.com/build-14/index.html` HTTP 200 확인
- metric JSON HTTP 200 확인
- 페이지의 `generatedAt` 또는 최신 날짜가 오늘(KST 기준)인지 확인
- 그래프 3개 이상이 실제 데이터로 렌더되는지 확인
- 새 데이터가 CloudFront cache 뒤에서 보이는지 확인
- status board를 쓰는 경우 `https://status.aws.shdkej.com`에서 Infinity check가 warn으로 떨어지지 않았는지 확인

## 보안 / 개인정보 / 비용 리스크

### 보안

- 공개 정적 사이트에 개인 운영 원문을 올리지 않는다.
- 데이터 feed는 집계값 중심으로 유지한다.
- credential, SecretRef, env var 이름은 문서에는 허용되지만 값은 절대 포함하지 않는다.
- GitHub Actions에는 `AWS_DEPLOY_ROLE_ARN`만 secret으로 쓰고, 장기 AWS key를 repo에 두지 않는다.
- 배포 전 `rg -n "sk-|AKIA|BEGIN .*PRIVATE|api[_-]?key|token|secret"` 같은 간단한 secret scan을 수행한다.

### 개인정보

- 날짜별 생활/회고/캘린더 정보는 공개 지표로 직접 노출하지 않는다.
- 사용자 이동 도시, 일정, 소비, 건강, 수면, 감정은 "입력 있음/없음" 수준으로만 집계한다.
- intent title도 공개 가능한 것과 내부 작업명이 섞일 수 있으므로 첫 버전은 id 중심 표시가 안전하다.

### 비용

- 정적 사이트 자체 비용은 S3 storage, request, CloudFront transfer/invalidation이 중심이다. 첫 버전 트래픽에서는 작을 가능성이 높다.
- 매일 전체 CloudFront invalidation은 무료 한도 내에서는 괜찮지만, 앱 수가 늘면 비용/시간이 커질 수 있다.
- OpenAI embedding이나 외부 API를 매일 지표 수집에 직접 호출하면 quota/비용 장애가 대시보드 장애로 전염된다. 첫 버전에서는 CLI 상태 확인은 선택적으로 두고, 실패해도 이전 값 + warn으로 표시한다.
- cron이 너무 잦으면 OpenClaw/GitHub/AWS 호출 비용보다 장애 노이즈가 커진다. 일 1회 정기 갱신 + 필요 시 수동 갱신으로 시작한다.

## 실패 상태와 복구 첫 액션

### 데이터 갱신 실패

사용자 표시:

- 상태: `Data stale`
- 문구: `오늘 지표를 갱신하지 못했습니다. 마지막 정상 데이터 기준으로 표시합니다.`
- 함께 표시할 값: 마지막 성공 시각, 실패한 지표군, 복구 담당 경로

복구 첫 액션:

- 수집 스크립트를 수동 실행하고 JSON valid 여부를 확인한다.

### 일부 지표 수집 실패

사용자 표시:

- 상태: `Partial`
- 문구: `일부 지표는 확인되지 않아 어제 값 또는 보류 상태로 표시합니다.`
- 그래프: 실패 지표군만 점선/회색 처리

복구 첫 액션:

- 실패 지표군의 source file 또는 CLI timeout 로그를 확인한다.

### 배포 실패

사용자 표시:

- 상태: `Deploy failed`
- 문구: `데이터는 준비됐지만 라이브 페이지 반영이 실패했습니다. 이전 배포본을 유지합니다.`
- 함께 표시할 값: commit sha, GitHub Actions run id, 실패 step

복구 첫 액션:

- GitHub Actions의 `Resolve AWS resources`, `Sync S3`, `Invalidate CloudFront` 중 어느 step에서 실패했는지 확인한다.

### 라이브 검증 실패

사용자 표시:

- 상태: `Live warn`
- 문구: `배포는 끝났지만 라이브 확인에서 경고가 있습니다. 캐시 또는 URL health를 확인합니다.`
- 함께 표시할 값: HTTP status, latency, checkedAt

복구 첫 액션:

- `curl -I https://infinity.aws.shdkej.com`와 metric JSON URL을 확인하고, 필요하면 CloudFront invalidation 상태를 확인한다.

### 보안 게이트 실패

사용자 표시:

- 상태: `Publish blocked`
- 문구: `공개 데이터에 민감정보 가능성이 있어 배포를 보류했습니다.`
- 함께 표시할 값: 파일명과 패턴 종류만, 실제 secret 후보 값은 표시하지 않음

복구 첫 액션:

- 공개 JSON에서 원문/secret 후보를 제거하고 집계값으로 다시 생성한다.

## 운영 Blocker

- `openclaw cron list --json` 확인이 작성 시점에 응답 없이 멈췄다. cron 상태를 자동 지표로 넣으려면 timeout, cache, 실패 시 `unknown` 처리부터 필요하다.
- Developer가 최종 데이터 파일명과 schema를 확정해야 운영 수집 스크립트와 페이지 검증 체크리스트를 고정할 수 있다.
- 실제 배포 완료 여부는 `space` repo 변경 commit/push와 GitHub Actions run 확인이 필요하다. Operator 문서 작성 범위에서는 배포를 실행하지 않았다.

## 다음 첫 액션

Developer가 JSON schema와 정적 파일 위치를 확정하면, Operator는 다음 1회 갱신 runbook을 고정한다.

1. 수집 스크립트 실행
2. JSON valid / secret scan
3. 로컬 렌더 확인
4. `space` repo commit/push
5. GitHub Actions 완료 확인
6. `https://infinity.aws.shdkej.com` 라이브 확인
7. 실패 시 위 상태 문구 중 하나로 사용자에게 보고
