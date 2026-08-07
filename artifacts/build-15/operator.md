# build-15 Operator

- intent: build-15
- role: Operator
- inspected_at: 2026-08-06 UTC
- scope: AWS/GitHub/배포·로그·보안·비용·권한·원격 가시성·반복 운영 점검
- execution: 실제 배포 및 외부 변경 없음

## 독립 판단

첨부 `instagram-maker`는 `index.html`, `styles.css`, `app.js`, 로컬 폰트 3개로 구성된 약 2.79MB의 독립 정적 번들이다. `app.js` 정적 구문 검사는 통과했고, 외부 URL/API, 쿠키·스토리지, WebSocket, 서버 업로드 호출은 확인되지 않았다. 선택한 이미지·영상은 `URL.createObjectURL`로 브라우저 안에서만 처리하고 PNG/WebM을 다운로드한다.

따라서 S3 private bucket + CloudFront OAC 정적 사이트 구조에는 적합하다. 다만 현재 인프라의 `sites/registry.json`에는 `instagram-maker` 항목과 전용 호스트가 없고, 이 작업 요청은 공용 코드/registry/배포를 수정하지 말라고 명시했다. 이번 Operator 단계에서 배포 완료나 공개 URL을 주장할 수 없다.

## 근거 및 현재 상태

- Knowledge Lab 인덱스: `/home/ubuntu/workspace/knowledge-lab/agent-wiki/README.md`
- build-03 운영 인벤토리: `/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-03/control-center-dashboard-ops-cms-inventory.md`
- 인프라 기준: `/home/ubuntu/workspace/space/infra-aws-static-sites/README.md`
- 표준 배치 경로는 `infra-aws-static-sites/sites/<app>/dist/`이다.
- `sites/registry.json`이 Terraform 앱 생성과 Status 피드의 원천이다. 현재 등록 앱은 `status`, `travel`, `schengen`, `library`, `infinity`, `virtue`, `control-center-cms`, `reel-room`이며 Instagram Maker는 없다.
- 신규 호스트를 쓰려면 registry 등록 후 Terraform으로 S3/CloudFront/OAC/ACM/Route53 자원을 생성해야 한다. 이 변경은 이번 범위에서 실행하지 않았다.
- 기존 infra worktree에는 `main.tf`, travel/library 산출물 및 `sites/schengen/` 등을 포함한 dirty/untracked 변경이 있다. 보존했으며 되돌리거나 정리하지 않았다.

## 영역별 점검

### AWS / 배포

- 미실행: `terraform plan/apply`, S3 업로드, CloudFront invalidation, Route53/ACM 변경, 공개 URL HTTP 확인.
- 표준 후속 경로는 전용 앱 경로와 registry 항목을 준비한 뒤 인프라를 계획/승인하고, 변경된 앱만 GitHub Actions로 배포하거나 수동 `aws s3 sync` 후 CloudFront invalidation을 수행하는 것이다.
- 현재는 bucket/distribution/domain ID가 확정되지 않았으므로 수동 배포 명령을 실행할 대상이 없다.
- `--delete` sync는 대상 prefix와 bucket을 재확인한 뒤에만 사용해야 한다. 기존 사이트나 라이브 피드를 잘못 지우지 않도록 앱별 bucket/prefix를 고정해야 한다.
- 정적 번들에는 SPA 라우팅이 필요 없으므로 `spa_fallback`은 기본값을 따르되, 최종 registry 정책에 맞춰 명시적으로 결정한다.

### GitHub / 원격 가시성

- 이번 작업에서 commit/push 및 GitHub Actions 실행은 하지 않았다.
- 배포 전에는 앱 경로, 도메인, build directory, 배포 workflow의 변경 감지 규칙이 일치하는지 확인해야 한다. README에 workflow 자동 배포가 기술되어 있으나 현재 확인한 infra 저장소 루트에는 `.github` workflow 디렉터리가 보이지 않아, 실제 workflow 위치/원격 저장소를 별도로 확인해야 한다.
- 완료 기준은 로컬 파일 존재가 아니라 commit hash, 원격 반영, workflow 성공, CloudFront 공개 URL의 HTTP 상태와 랜딩 콘텐츠 확인까지다.
- Status registry 갱신은 새 CloudFront distribution이 생긴 뒤에만 유효하다. registry만 먼저 바꾸면 Status에 존재하지만 접근 불가능한 항목이 생길 수 있다.

### 로그 / 관측

- 번들은 서버 로그를 생성하지 않으며 모든 편집 처리가 클라이언트에서 끝난다. 운영 시 최소 관측점은 CloudFront/S3 access log 설정 여부, 4xx/5xx, 캐시 상태, 배포 workflow 로그다.
- 별도 API가 없으므로 애플리케이션 health endpoint를 추가할 필요는 없지만, 공개 URL에서 `Frame — Instagram Maker` title과 JS/CSS/font 200 응답을 확인하는 smoke check가 필요하다.
- PNG/WebM export는 브라우저 기능 의존성이 있다. Chromium 계열에서 이미지 업로드, PNG 생성, WebM 생성 여부를 수동 또는 브라우저 테스트로 기록해야 한다.

### 보안 / 개인정보

- 장점: 업로드 파일을 서버로 전송하지 않고 object URL을 unload 시 해제한다. 외부 의존성과 인증/비밀키가 없다.
- 주의: 파일 입력은 이미지·영상 MIME을 허용하지만 파일 크기 상한이 없다. 클라이언트 메모리·브라우저 탭 장애 가능성을 안내하거나 후속 개선에서 크기/해상도 제한을 검토한다.
- 배포 시 S3 bucket public access 차단과 CloudFront OAC를 유지하고, 업로드/API origin을 추가하지 않는다. `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy` 등 응답 헤더 정책은 현재 번들만으로는 확인할 수 없으므로 CloudFront response headers 정책에서 별도 점검한다.
- 사용자 사진이 브라우저 밖으로 나가지 않는다는 문구는 기능 구현과 일치하지만, 공개 배포 후 분석 스크립트나 폰트 CDN을 추가할 때 이 보장과 충돌하지 않는지 재검토해야 한다.

### 비용

- 정적 파일만 제공하고 서버/API가 없으므로 기본 비용은 S3 저장·요청, CloudFront 전송·요청, Route53 hosted zone 및 ACM(일반적으로 인증서 자체 비용 없음) 범위다.
- 약 2.79MB 번들 중 폰트가 약 2.77MB로 대부분을 차지한다. 트래픽이 늘면 폰트 최적화/서브셋팅이 비용과 초기 로딩 모두에 유리하다.
- 영상은 서버에 저장하지 않고 브라우저에서 생성하므로 WebM export 자체의 AWS 실행 비용은 없다. CloudFront invalidation을 매 배포마다 무조건 전체 경로로 실행하면 불필요한 비용/운영 부담이 생길 수 있어 경로와 빈도를 정책화한다.

### 권한 / 승인 경계

- 이번 역할에서 허용된 것은 읽기 점검과 기록뿐이며, AWS/GitHub/Route53/CloudFront/S3에 쓰기 권한을 사용하지 않았다.
- 실제 배포에는 최소 Terraform state 변경 권한, S3 write, CloudFront invalidation, Route53/ACM 변경, GitHub push/actions 권한이 필요하다. 권한은 신규 앱 범위로 제한하고 장기 AWS access key를 코드나 workflow에 두지 않는다.
- 공개 도메인 생성, 비용 발생 인프라 생성, registry/공용 workflow 수정은 승인 경계로 둔다. 이번 요청의 “공용 코드/registry/배포 수정 금지”와 직접 충돌하므로 실행하지 않았다.

## 운영 인계

1. Planner/Developer가 최종 앱 식별자와 공개 도메인, 배치 경로를 확정한다. 권장 형태는 `sites/instagram-maker/dist/`이며, 이 문서만으로 확정하지 않는다.
2. 승인 후 Developer/Operator가 registry 변경과 Terraform plan을 별도 diff로 검토한다. 기존 dirty 변경을 포함한 broad apply는 금지하고, plan에서 신규 S3/CloudFront/OAC/ACM/Route53 자원만 확인한다.
3. 인프라가 준비되면 앱 경로만 배포하고, CloudFront invalidation 뒤 `curl -I` 및 본문/asset smoke check를 수행한다. title, `app.js`, `styles.css`, 3개 폰트 응답과 PNG export를 확인한다.
4. workflow 성공 로그, commit hash, distribution/domain, 공개 URL 검증 시각, 캐시 무효화 결과를 build-15 change log에 남긴다.
5. 장애 시 원본 정적 파일의 직전 배포 버전을 재배포하는 롤백 절차를 준비한다. registry/infra를 되돌릴 때도 기존 사용자 dirty 변경을 포함한 전체 revert는 하지 않는다.

## 결론 / Red 인계

- `operator_status`: `waiting_for_scoped_approval_and_infrastructure`
- `deployment_status`: `not_executed_by_request`
- `remote_visibility`: `not_verified`
- `red_required`: 공개 반영 전 Red 검증 필요
- Red에 확인 요청할 항목: 요청한 첨부 번들이 누락 없이 정적 배포 단위인지, 최종 도메인/앱 식별자가 다른 surface와 충돌하지 않는지, 실제 공개 URL 검증이 완료됐는지.
- 이 역할은 위 점검 외에 공용 코드, registry, 배포, 다른 역할 산출물을 수정하지 않았다.

### 2026-08-07T06:18Z cycle recheck

- 판단: 신규 도메인·AWS 리소스·Terraform/registry·비용·권한 변경은 별도 승인 전 실행하지 않는다.
- 우려: 실행 대상이 없는 상태에서 원격 가시성이나 라이브 검증을 주장할 수 없다.
- 인계: 승인 및 scoped 인프라 준비 후 plan, deploy, cache/HTTP/screen verification을 순서대로 수행한다.
