# build-03: Dashboard Control Center / Ops CMS 설계 인벤토리

- intent: build-03
- status: design complete
- created_at: 2026-06-12T06:35Z
- scope: L0/L1 설계와 인벤토리
- implementation_status: not started

## 결론

Dashboard Control Center는 범용 CMS가 아니라 **운영 원장 + 수정 진입점 + 배포/검증 상태판**으로 시작하는 편이 맞다.

첫 MVP는 새 편집기를 크게 만들기보다, 흩어진 정적 페이지의 위치와 데이터 원천, 빌드/배포/검증 방법, 승인 경계를 한 화면에 모으는 내부 운영 도구여야 한다. 버튼 자동화는 `수정 -> 빌드 -> push -> 공개 URL 확인` 흐름이 반복 검증된 작업부터 붙인다.

## 현재 운영 표면

| 이름 | 공개 URL | 정본/로컬 위치 | 데이터 원천 | 빌드/생성 | 배포/검증 |
| --- | --- | --- | --- | --- | --- |
| Status | `https://status.aws.shdkej.com` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/status/dist` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/registry.json` | `python3 scripts/build-status-json.py --resolve-aws --check` | GitHub Actions 또는 `aws s3 sync sites/status/dist/ ...` + CloudFront invalidation |
| Travel Ops | `https://travel.aws.shdkej.com` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/travel` | `data/raw-events-private.json`, `data/geocode-cache.json`, `dist/travel-data.json` | `scripts/build-travel-data.py`가 원장 데이터를 `dist/travel-data.json`으로 생성 | GitHub Actions 또는 `aws s3 sync sites/travel/dist/ ...` + 공개 URL 키워드 확인 |
| Card News Library | `https://library.aws.shdkej.com` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/library/dist` | `/home/ubuntu/.openclaw/workspace/system/data/card-news-library/items.json` | 카드뉴스 라이브러리 재생성 스크립트/수동 HTML 갱신 흐름 | GitHub Actions 또는 static site deploy 후 공개 archive 확인 |
| Infinity | `https://infinity.aws.shdkej.com` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/infinity/dist` + `/home/ubuntu/workspace/knowledge-lab/infinity` | `INTENTS.md`, `intents/*`, `reports/*`, `artifacts/*` | 대시보드 HTML 생성/갱신 후 dist 반영 | Infinity repo push와 정적 페이지 반영 확인을 분리해서 봐야 함 |
| Virtue Static | `https://virtue.aws.shdkej.com` | `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/virtue/dist` | Virtue 앱 빌드 산출물 | 앱 빌드 산출물이 dist로 들어오는 구조 | 앱/프로덕션 영향이 있어 Control Center에서는 읽기 우선 |
| Family Wedding | likely `https://shdkej.github.io/family-wedding-2026-06-27/` | `/home/ubuntu/workspace/shdkej.github.io/static/family-wedding-2026-06-27` and `public/family-wedding-2026-06-27` | 정적 HTML/CSS/assets | shdkej.github.io 빌드/정적 파일 동기화 | 초대장 문구/디자인 변경은 이미 승인된 범위 고정 원칙 필요 |

## MVP 정보 구조

### 1. Registry

한 행은 하나의 운영 표면을 뜻한다.

- 표시 이름
- 공개 URL
- 로컬 정본 경로
- 관련 repo / branch
- 데이터 파일
- 빌드 명령
- 배포 방식
- 검증 URL과 검증 키워드
- 최근 커밋/배포/확인 시각
- 승인 필요 경계

### 2. Data Edit Panel

초기에는 파일을 직접 편집하지 않고, 안전한 진입점만 보여준다.

- Travel: 일정/이동/숙소/결제 상태 데이터 위치와 마지막 생성 결과
- Status: `registry.json` 항목과 현재 `status.json`
- Infinity: Inbox / Active / Waiting / Archive 개수, 최근 Archive, 밀린 push 여부
- Card Library: 최근 카드뉴스 항목, 누락된 이미지/배포 상태
- Family Wedding: 고정된 디자인 기준과 수정 가능한 문구/연락처 범위

### 3. Deploy State

Control Center의 핵심은 "수정했나"보다 "보이는 곳까지 닫혔나"다.

- local dirty 여부
- last commit hash
- origin과 ahead/behind 여부
- GitHub Actions 또는 수동 deploy 상태
- 공개 URL HTTP 상태
- 공개 페이지에서 확인할 키워드
- cache waiting 여부

### 4. Change Log

각 작업은 다음 형태로 남긴다.

- 요청
- 변경 파일
- 빌드 결과
- push 결과
- 공개 URL 검증 결과
- 남긴 범위 / 건드리지 않은 범위

## 권한과 승인 경계

### 자동/내부 처리 가능

- repo/file 위치 인벤토리
- 읽기 전용 상태 확인
- 정적 데이터 파일의 초안 작성
- 로컬 빌드
- scoped commit/push
- 공개 URL 반영 확인
- Infinity intent 상태 정리

### 승인이 필요한 일

- 새 CMS 구현/배포
- 쓰기 API, auth, permission 변경
- 프로덕션 앱 동작 변경
- 비용 발생 AWS/Terraform 변경
- 외부 메시지/공개 게시/광고/커머스 액션
- 기존 디자인 방향이 승인된 페이지의 주변 레이아웃 변경

## 첫 구현 제안

### 가치

마스터님이 "어디를 고쳐야 하지?"를 기억하지 않아도 되게 만든다. SAM은 수정 후 배포/검증까지 닫는 데 집중하고, 사용자는 결과와 다음 판단만 본다.

### 정책

처음부터 편집 가능한 CMS가 아니라 read-only 운영 대시보드로 시작한다. 쓰기 기능은 반복 작업 2-3개만 먼저 버튼화한다.

### 실행

1. `sites/registry.json`과 Infinity 원장을 읽는 내부 Control Center HTML을 만든다.
2. 각 표면별 `원장 파일`, `빌드 명령`, `배포 방식`, `검증 키워드`를 카드가 아니라 촘촘한 표로 보여준다.
3. Travel/Infinity/Status만 먼저 1차 연결한다.
4. 버튼은 처음에는 `검증 명령 표시` 수준으로 두고, 자동 실행은 별도 승인 후 붙인다.

### 순환

각 정적페이지 작업이 끝날 때 Control Center change log에 자동 기록되도록 만든다. "완료"의 기준은 로컬 수정이 아니라 공개 URL에서 확인된 상태다.

## 닫은 범위

- 현재 정적 대시보드와 페이지 운영 표면을 1차 인벤토리로 묶었다.
- Data edit / deploy action / approval boundary를 분리했다.
- 구현 전 안전한 MVP 정보 구조를 정의했다.

## 남은 범위

- 실제 Control Center 페이지 구현
- 자동 검증 스크립트 연결
- write API 또는 버튼 실행
- Terraform/CloudFront/S3 변경
- 각 페이지별 상세 수정 UI
