# build-15 Developer Notes — Instagram Maker 정적페이지 배포 조사

작성 시각: 2026-08-06
역할: Developer
범위: 입력 구조, 기존 배포 경로·호출처·영향·테스트·롤백 조사
실행 제한: 구현, 공용 코드/registry/배포 변경을 하지 않음

## 결론

입력물은 별도 빌드 도구나 서버 없이 바로 제공 가능한 self-contained 정적 앱이다. 기술적으로 가장 안전한 배포 후보는 기존 사이트와 분리된 새 AWS static-site 슬롯이다.

다만 현재 `infra-aws-static-sites/sites/registry.json`에는 `instagram-maker`가 없고, Instagram Maker용 도메인·S3 bucket·CloudFront distribution도 확인되지 않았다. 따라서 지금 상태로는 정적 파일만 준비해도 기존 deploy workflow가 AWS 리소스를 찾지 못해 실패한다. registry/Terraform/AWS 반영은 사용자가 금지한 공용 코드·registry·배포 변경에 해당하므로 이 Developer 단계의 명확한 blocker다.

기존 `infinity` 또는 `library` 아래 하위 경로에 넣는 우회안은 가능하지만, 기존 공개 표면의 파일과 배포/rollback 경계를 공유한다. 독립 도구인 Instagram Maker를 기존 archive/dashboard에 섞는 영향이 커서 권장하지 않는다. `reel-room`은 이름이 비슷한 후보가 아니라 Kubernetes ingress + basic auth 앱이므로 재사용 대상이 아니다.

## 입력 파일 구조

입력 압축:

`/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-76421795-7722-4543-a709-0e52eff09de2/instagram-maker.tar---5060dc00-db57-41b1-8b94-d6c42d82db53.gz`

압축 내부:

```text
index.html
styles.css
app.js
fonts/A2Z-Black.woff2
fonts/ChosunGu.woff
fonts/NanumSquareNeo-Regular.woff2
```

- `index.html`: `Frame — Instagram Maker` UI. `styles.css`와 `app.js`만 상대 경로로 참조한다.
- `styles.css`: 화면 레이아웃, 템플릿 미리보기, 로컬 폰트 `@font-face` 정의.
- `app.js`: 1080×1920 canvas(9:16) 렌더러. 샘플 canvas를 기본으로 만들고, 이미지/영상 로컬 업로드, 3개 템플릿, 문구/폰트/위치 변경, PNG/WebM 내보내기를 처리한다.
- 폰트 3종: 앱과 함께 정적 파일로 제공되며 외부 폰트 CDN 의존성이 없다.

검사 결과:

- `node --check app.js` 통과.
- HTML/JS/CSS에서 앱 자체의 API endpoint, `fetch`, WebSocket, 외부 서비스 호출은 발견되지 않았다. CSS의 URL은 동봉된 폰트 상대 경로뿐이다.
- 압축 파일은 6개 파일과 3개 폰트로 구성되며 이미지 원본을 포함하지 않는다. 기본 샘플은 브라우저 canvas에서 생성된다.

## 기존 배포 경로와 호출처

### 정본 경로

기존 AWS static-site 저장소:

`/home/ubuntu/workspace/space/infra-aws-static-sites`

정적 앱 표준 경로:

`infra-aws-static-sites/sites/<app>/dist/`

registry 정본:

`infra-aws-static-sites/sites/registry.json`

Terraform은 registry의 AWS static-site 항목을 읽어 앱별 private S3, CloudFront OAC/distribution, ACM 인증서, Route53 alias를 만든다. 현재 registry에는 Status, Travel, Schengen, Library, Infinity, Virtue가 AWS static-site로 등록되어 있고 CMS/Reel Room은 Kubernetes hosting으로 제외된다.

### 자동 호출처

`/home/ubuntu/workspace/space/.github/workflows/static-site-aws-template.yml`의 `Deploy static site to AWS` workflow가 다음 push에서 호출된다.

- 대상 branch: `main`, `master`
- 대상 path: `infra-aws-static-sites/sites/**` 또는 status build script
- `sites/<app>/dist/**` 변경을 app 이름으로 감지
- 기본 build directory: `infra-aws-static-sites/sites/<app>/dist`
- 기본 domain: `<app>.aws.shdkej.com`
- AWS OIDC role assume 후 domain alias로 CloudFront distribution 조회
- S3 `sync --delete` 및 CloudFront `/*` invalidation 실행
- top-level `.html` 파일은 `index`, `404`, `_not-found`를 제외하고 extensionless route도 업로드

신규 앱을 선택하면 workflow가 자동으로 리소스를 만들지는 않는다. 먼저 registry에 도메인을 추가하고 Terraform apply로 alias가 실제로 존재해야 한다. workflow dispatch는 custom `app`, `build_dir`, `domain_name`을 받을 수 있지만, 그 경우에도 해당 CloudFront alias가 이미 있어야 한다.

### 수동 호출처

기존 README의 수동 경로는 다음과 같다.

```text
aws s3 sync sites/<app>/dist/ s3://static-<domain-with-dots-replaced-by-dashes> --delete
aws cloudfront create-invalidation --distribution-id <id> --paths "/*"
```

이는 이미 존재하는 bucket/distribution에만 적용된다. 현재는 Instagram Maker용 리소스가 확인되지 않았으므로 실행 가능한 배포 경로가 아니다.

## 배포 후보와 선택

### 후보 A — 새 `instagram-maker` AWS static-site 슬롯 (권장, 승인/Operator 작업 필요)

예상 구조:

```text
sites/instagram-maker/dist/index.html
sites/instagram-maker/dist/styles.css
sites/instagram-maker/dist/app.js
sites/instagram-maker/dist/fonts/*.woff*
```

예상 기본 URL은 workflow 규칙상 `https://instagram-maker.aws.shdkej.com`이지만, 실제 도메인 이름은 사용자가 결정해야 한다. 이 후보는 기존 dashboard/archive와 파일·bucket·CloudFront cache를 분리하고, `app=instagram-maker`로 workflow가 자연스럽게 감지되는 장점이 있다.

필요한 선행 작업:

1. 도메인/표시 이름/공개 범위 승인.
2. `sites/registry.json` 항목 추가.
3. Terraform plan 검토 및 apply로 S3/CloudFront/ACM/Route53 생성.
4. 그 뒤에 압축 파일을 해당 `dist` 경로에 배치하고 scoped commit/push.

현재 요청의 Developer 범위에서는 위 파일·registry·AWS 상태를 변경하지 않는다.

### 후보 B — 기존 `infinity` 또는 `library` 하위 경로 (비권장 fallback)

예: `sites/infinity/dist/instagram-maker/` 또는 `sites/library/dist/instagram-maker/`.

새 AWS 리소스는 필요 없지만 기존 사이트 배포에 묶이고, 공개 URL/404/cache/rollback이 부모 앱과 공유된다. `library`는 archive 성격이고 `infinity`는 운영 dashboard 성격이므로 도구의 정보 구조와 맞지 않는다. 사용자가 이 후보를 명시적으로 선택하지 않는 한 사용하지 않는다.

## 호출·영향 분석

### 런타임 호출

- 브라우저가 정적 HTML을 로드하고 CSS/JS/폰트를 상대 경로로 요청한다.
- 업로드 파일은 `URL.createObjectURL`로 브라우저 안에서만 처리한다.
- PNG/WebM 결과는 브라우저 다운로드로 생성한다.
- 서버 API, database, auth, analytics, 외부 계정 권한, 개인정보 저장 호출은 없다.

### 배포 영향

- 새 슬롯이면 새 S3/CloudFront/Route53/ACM 리소스와 비용·권한이 추가된다.
- registry 변경은 Status board용 `status.json` 재생성/배포도 유발한다.
- push 후 workflow는 대상 bucket 전체를 `--delete` sync하고 CloudFront 전체 invalidation을 요청한다. 대상 경로를 잘못 지정하면 기존 사이트 파일 삭제 위험이 있으므로 app/build_dir/domain 3자를 배포 전에 대조해야 한다.
- 현재 infra 저장소에는 사용자의 unrelated dirty 변경(`main.tf`, 모듈, travel/library 산출물, `sites/schengen/` 등)이 존재한다. 이를 되돌리거나 섞지 말고, 이후 구현자는 변경 파일을 명시적으로 분리해야 한다.

### 제품 호환성 영향

- 기본 화면에 `body { min-width: 980px; }`가 있어 모바일 폭에서는 가로 스크롤이 예상된다. Instagram Maker가 desktop-first 도구인지 확인하기 전에는 mobile 지원을 완료 기준으로 주장하면 안 된다.
- WebM은 `MediaRecorder`와 `canvas.captureStream` 및 VP8/VP9 지원 브라우저가 필요하다. PNG는 상대적으로 넓게 지원된다.
- 업로드는 `image/*,video/*`로 허용되지만 실제 파일 크기/영상 길이 제한, 브라우저 메모리 한계, 재생 불가 포맷 오류 UI는 별도 검증이 필요하다.

## 테스트 및 검증 계획

### 이미 완료한 정적 검사

- archive 목록/파일 존재 확인.
- `node --check app.js` 통과.
- 상대 폰트 참조 및 외부 API 호출 여부 확인.

### 구현 후 배포 전 필수 검사

1. 압축을 새 후보 `sites/instagram-maker/dist/`에만 풀고 `find`로 예상 파일 목록과 추가 파일을 확인한다.
2. `python3 -m http.server`로 local static server를 띄워 `/index.html` 진입을 확인한다. `file://` 직접 실행은 canvas/file input 동작을 오판할 수 있다.
3. 브라우저에서 샘플 렌더, 템플릿 1/2/3, 문구 입력, 폰트 3종, 위치 top/center/bottom, `R` reset을 확인한다.
4. 이미지 업로드 후 미리보기와 PNG 다운로드를 확인한다.
5. 지원 브라우저에서 짧은 MP4 업로드와 5초 WebM 다운로드를 확인한다. 미지원 브라우저의 안내 문구도 확인한다.
6. `rg`로 secret/API key/토큰 및 의도하지 않은 외부 URL을 검사한다.
7. push 전 `git diff --name-only`가 Instagram Maker와 명시적으로 승인된 registry/infra 파일만 포함하는지 확인한다. 기존 dirty 파일은 보존한다.

### 배포 후 필수 검사

- GitHub Actions run 성공과 대상 app=`instagram-maker`를 확인한다.
- 공개 URL HTTP 200과 `index.html`, `styles.css`, `app.js`, 폰트 요청 성공을 확인한다.
- HTML title 또는 `Frame — Instagram Maker`, `한 장을 바로` 같은 고유 marker가 공개 응답에 존재하는지 확인한다.
- 브라우저에서 cache invalidation 후 샘플 canvas와 주요 버튼이 동작하는지 재확인한다.
- registry를 변경했다면 Status board의 새 surface와 기존 surface가 함께 정상인지 확인한다.

## 롤백 계획

### 새 슬롯 배포

1. 배포 commit hash와 workflow run을 기록한다.
2. 결함이면 해당 scoped commit을 `git revert`하고 동일한 deploy lane으로 다시 배포한다. force-push는 사용하지 않는다.
3. workflow가 이전 정적 파일을 S3에 재동기화하고 CloudFront `/*` invalidation을 완료한 뒤 공개 URL을 재검증한다.
4. registry/Terraform으로 만든 리소스를 없애는 rollback은 비용·DNS·인증서·공개 URL에 영향을 주므로 Operator 승인 없이는 실행하지 않는다. 첫 배포 실패 시에도 임의로 `terraform destroy`하지 않는다.

### 기존 사이트 하위 경로 fallback

부모 사이트 전체 deploy를 되돌릴 수 있으므로, rollback 시 부모 앱의 정상 파일까지 함께 복원되지 않는지 commit diff를 먼저 확인해야 한다. 이 넓은 영향 때문에 후보 B를 피한다.

## Blocker / Developer 인계

### Blocker

- Instagram Maker의 최종 공개 도메인과 독립 슬롯 사용 여부가 정해지지 않음.
- `sites/registry.json`에 앱 항목이 없음.
- Terraform apply 전이라 해당 CloudFront alias/bucket이 없음.
- 사용자가 공용 코드/registry/배포 수정을 금지했으므로 Developer가 구현·배포를 이어갈 권한이 없음.
- 실제 브라우저/라이브 URL 검증은 아직 하지 않음.

### 다음 역할에 인계할 사항

- Planner/Operator가 후보 A와 도메인, 비용·권한·공개 승인 경계를 결정해야 한다.
- 승인되면 구현자는 압축 내용을 새 app `dist`에만 복사하고, 기존 dirty worktree와 섞이지 않게 scoped diff를 만든다.
- Operator는 registry/Terraform/AWS 리소스 생성 후에만 deploy workflow를 호출한다.
- Red는 라이브 marker, 정적 자산 200, 브라우저 내 로컬 처리, PNG/WebM, rollback handle을 확인해야 한다.

## 변경 파일과 상태

이번 역할에서 변경한 파일은 다음 하나뿐이다.

`/home/ubuntu/workspace/knowledge-lab/infinity/artifacts/build-15/developer.md`

입력 압축, infra 저장소, registry, workflow, 공용 코드, 배포 상태는 변경하지 않았다. 기존 dirty worktree 변경도 되돌리지 않았다.

### 2026-08-07T06:18Z cycle recheck

- 판단: 실행 프로세스가 없고 `instagram-maker` registry·전용 S3·CloudFront 대상도 없어 배포를 실행하지 않는다.
- 우려: 기존 앱 하위 경로 우회는 rollback/cache 경계를 공유하므로 기각한다.
- 인계: 승인된 공개 대상이 준비되면 scoped diff, 배포 commit, HTTP·자산 smoke test 순으로 재개한다.
