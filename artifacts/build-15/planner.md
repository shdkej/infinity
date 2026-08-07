# build-15 Planner · Instagram Maker 정적페이지 배포

- intent: build-15
- role: Planner
- status: planned / handoff to Developer
- planned_at: 2026-08-06T21:24Z
- input: `/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-76421795-7722-4543-a709-0e52eff09de2/instagram-maker.tar---5060dc00-db57-41b1-8b94-d6c42d82db53.gz`

## 1. 목표

첨부 압축의 Instagram Maker 브라우저 도구를 정적 자산 그대로 배포해, 실제 라이브 URL에서 페이지가 로드되고 핵심 UI와 브라우저 내 미리보기·내보내기 동작이 확인되는 상태까지 닫는다.

입력 자산은 다음으로 한정한다.

- `index.html`
- `styles.css`
- `app.js`
- `fonts/NanumSquareNeo-Regular.woff2`
- `fonts/ChosunGu.woff`
- `fonts/A2Z-Black.woff2`

페이지는 사진/영상 업로드, 3개 템플릿, 자막·폰트·위치 조정, PNG/WebM 내보내기를 브라우저 안에서 처리한다. 외부 업로드나 서버 API를 추가하는 작업은 목표에 포함하지 않는다.

## 2. Knowledge Lab 근거와 적용 판단

- `/home/ubuntu/workspace/knowledge-lab/agent-wiki/README.md`: 변경 가능성, 운영 부담, 공개 인터페이스 신뢰, 관측 가능한 검증을 우선한다.
- `infinity/artifacts/build-03/control-center-dashboard-ops-cms-inventory.md`: 정적페이지의 정본·빌드·배포·검증을 분리 기록하고, 완료를 로컬 수정이 아니라 공개 URL 확인으로 본다. 새 CMS나 프로덕션 동작 변경은 별도 승인 대상이다.
- `/home/ubuntu/workspace/space/infra-aws-static-sites/README.md`: 앱 산출물은 `sites/<app>/dist/`에 두며, 신규 앱은 `sites/registry.json`과 Terraform 반영이 필요하다. 배포 후 CloudFront 캐시 무효화와 공개 URL 검증이 필요하다.
- `infinity/INTENTS.md`의 build-15: 전체 완료 기준은 네 역할 기록, Red `pass` 및 report, commit/push, 라이브 HTTP·화면 검증, Infinity report/archive이며, 정적페이지 배포는 승인되었지만 새 도메인·비용·권한·시크릿 변경은 Waiting 경계다.

## 3. 완료 기준

Planner 기준의 완료는 아래 실행 계약을 Developer/Marketer/Operator/Red에 넘길 수 있는 범위와 경계를 확정한 상태다. 전체 intent 완료는 다음 조건을 모두 만족해야 한다.

1. 네 역할의 독립 판단·우려·제안·인계 문서가 각각 남는다.
2. 입력 자산이 누락·변형 없이 정적 배포 디렉터리에 반영된다.
3. 선택된 배포 대상, 공개 URL, 빌드/배포 명령, 롤백 지점이 기록된다.
4. scoped commit/push가 끝난다. 기존 dirty 변경은 포함하거나 되돌리지 않는다.
5. 라이브 URL에서 HTTP 성공, HTML/CSS/JS/폰트 로드, 한국어 UI 렌더링, 템플릿 전환, 자막 변경, PNG 내보내기 가능 여부를 확인한다. WebM은 지원 브라우저에서 확인하고 미지원이면 사용자 안내 동작을 기록한다.
6. Red가 `red_status: pass`를 남기고 report 경로를 제공한다.
7. Infinity HTML report, intent archive 원장, 다음 첫 액션이 갱신된다.

## 4. 범위 축소

이번 작업은 “첨부된 정적페이지의 배포”로 제한한다.

- 포함: 압축 해제·무결성 확인, 정적 파일 배치, 기존 배포 파이프라인에 맞춘 scoped deploy, 라이브 HTTP·브라우저 검증, 역할별 기록.
- 제외: 기능 추가·리디자인·카피 수정, 이미지/영상 서버 업로드, 로그인·인증·권한, API/Lambda, 분석·추적 코드, 새 CMS, Terraform 구조 개선, 공용 registry 정리, 다른 앱의 dirty 변경 정리.
- 사용자 제약: 공용 코드, `sites/registry.json`, 공용 registry, 배포 설정을 Planner가 수정하지 않는다. 다른 역할 파일도 수정하지 않는다.

### 배포 대상 미확정에 따른 축소/조건

현재 근거에는 Instagram Maker의 최종 공개 도메인이나 기존 registry 항목이 제시되어 있지 않다. static-sites 운영 규칙상 신규 공개 앱은 registry와 인프라 반영이 필요하지만, 사용자는 공용 코드/registry/배포를 수정하지 말라고 했다. 따라서 Developer/Operator는 먼저 기존 승인된 앱 슬롯 또는 이미 존재하는 Instagram Maker 도메인이 있는지 읽기 전용으로 확인한다. 없다면 새 도메인·registry·Terraform 변경은 이 작업의 승인 경계를 넘어가므로, 배포를 강행하지 말고 Waiting으로 인계한다.

## 5. 승인 경계

### 승인된 범위

- 사용자가 배포를 명시했으므로, 이미 존재하는 승인된 정적 사이트 대상에 파일을 반영하고 그 URL을 검증하는 행위.
- 입력 압축의 정적 자산을 그대로 복사하는 작업.
- scoped commit/push 및 기존 배포 방식에 따른 공개 반영. 단, 대상 repo·경로가 확인되고 기존 dirty 변경과 분리되는 경우에 한한다.

### 별도 승인 또는 Waiting이 필요한 범위

- 새 공개 도메인, DNS, Route53, ACM, CloudFront distribution, S3 bucket 생성.
- `sites/registry.json`, Terraform, 공용 workflow, 모듈 또는 기타 공용 코드 수정.
- 비용 발생 AWS 변경, 권한/IAM 변경, secret 추가·교체.
- 기존 앱의 레이아웃·동작 변경 또는 Instagram 계정 게시/예약/광고·외부 메시지.
- 현재 dirty worktree에 대한 reset, checkout, clean, 삭제, 대규모 정리.

## 6. 역할 인계

### Developer

읽기 전용으로 배포 대상과 도메인을 확인하고, 가능하면 격리된 경로에 압축을 배치한다. 파일 수·SHA-256·상대 경로를 대조하고, 기존 dirty 변경과 섞이지 않는 scoped diff와 롤백 경로를 제시한다. 대상이 신규 앱뿐이면 공용 registry/인프라 수정 없이 멈추고 Waiting 사유를 남긴다.

### Marketer

기존 UI의 “한 장을 게시 가능한 장면으로”라는 가치 전달과 한국어 첫인상, 정적 공개 페이지에서 노출되는 제품명/카피를 검토한다. 기능·카피 변경은 제안으로만 남기며, Instagram 계정 게시나 예약은 실행하지 않는다.

### Operator

배포 방식과 공개 URL의 소유·승인 상태, 비용·권한·시크릿 영향을 확인한다. 반영 시 HTTP 및 캐시 상태, 정적 자산 로드, 원격 가시성을 기록한다. 새 인프라가 필요하거나 대상 URL이 없으면 사용자 승인 전 Waiting으로 둔다.

### Red

입력 자산 보존, 요청 범위 일치, 공개 URL 검증, 승인 경계 준수, 기존 dirty 변경 비침범을 검증한다. 라이브 화면/HTTP 확인과 report 경로 없이 `pass`를 주지 않는다.

## 7. Planner 결론

가장 작은 안전한 다음 단계는 “기존 승인된 배포 대상/URL의 존재를 읽기 전용 확인 → 없으면 새 공개 인프라 승인 대기 → 있으면 자산만 격리 배치하고 역할별 검증 진행”이다. Planner는 이 문서 외 파일을 변경하지 않았고, 공용 코드·registry·배포도 실행하지 않았다.

### 2026-08-07T06:18Z cycle recheck

- 판단: Inbox에는 실행 가능한 미완료 intent가 없고, Active에는 동일 intent `build-15` 하나만 `waiting`으로 존재한다. 새 실행이나 중복 intent를 만들지 않는다.
- 근거: Knowledge Lab 인덱스의 관측 가능성·변경 가능성 원칙 및 기존 build-15 승인 경계를 재확인했다.
- 인계: 공개 URL 또는 신규 도메인·인프라 승인과 scoped 대상 준비가 확인될 때만 동일 intent를 재개한다.
