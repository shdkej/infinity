# build-04: Dashboard Control Center MVP 배포

- intent: build-04
- status: deployed
- created_at: 2026-06-12T06:55Z
- public_url: https://status.aws.shdkej.com/control-center/
- source_intent: build-03
- implementation_scope: read-only static MVP

## 결과

Dashboard Control Center의 첫 MVP를 기존 Status 정적 사이트 아래에 배포했다.

새 AWS 리소스나 Terraform 변경 없이 기존 `status.aws.shdkej.com` 배포 레인을 사용했다. 현재 주소는 다음과 같다.

```text
https://status.aws.shdkej.com/control-center/
```

## 구현 범위

- Status 정적 사이트에 `control-center/index.html` 추가
- 기존 Status 첫 화면에 Control Center 링크 추가
- Control Center는 `../status.json`을 읽어 배포 상태와 앱 목록을 표시
- fallback registry로 Status, Travel Ops, Card News Library, Infinity, Virtue, Family Wedding 표면 표시
- 각 표면별 URL, source data, build/generation, verification target 표시
- change log model과 approval boundary 표시

## 의도적으로 제외한 것

- 쓰기 API
- auth / permission
- 자동 배포 버튼
- Terraform / AWS 리소스 추가
- 프로덕션 앱 동작 변경
- 비용 발생 작업
- 외부 메시지 또는 공개 게시

## 검증

- 로컬 파일 존재: `sites/status/dist/control-center/index.html`
- Status entry link: `sites/status/dist/index.html`에 `./control-center/` 링크 추가
- HTML smoke check: `Dashboard Control Center`, `Surface Registry`, `Approval Boundary`, `Change Log Model` 확인
- 공개 URL 검증: `https://status.aws.shdkej.com/control-center/` HTTP 200 및 핵심 문자열 확인

## 다음 단계 후보

1. Control Center에 Infinity Inbox/Active/Waiting/Archive count를 GitHub API로 직접 붙인다.
2. Travel Dashboard 수정 항목을 read-only diff 미리보기로 연결한다.
3. 반복 작업이 2-3회 안정되면 승인형 deploy command 버튼을 별도 intent로 연다.
