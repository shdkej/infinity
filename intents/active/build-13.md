# build-13 — 아프지마 앱 병원 API 호출 흐름 검증

- id: build-13
- status: active
- projects: [apujima, infinity, app-api-verification]
- task_type: implementation-verification
- topics: [hospital-api, api-flow, app-verification, data-fetching]
- owner: Infinity
- requested_by: SeongHo Noh
- created_at: 2026-06-23T14:14Z
- permission_level: L1 local/read-only verification first; escalate before external-impact changes
- trigger: "아프지마 앱 병원 API 확인해서 잘 호출하는지 흐름 확인 필요"

## 목표

`아프지마` 앱에서 병원 API가 실제 화면/서버 흐름에서 올바르게 호출되는지 확인한다.

## 첫 확인 범위

- 대상 앱/레포 위치를 식별한다.
- 병원 API 관련 endpoint, client 함수, route handler, 환경변수 이름을 찾는다.
- API 호출 경로가 화면 또는 서버 action에서 실제로 연결되어 있는지 확인한다.
- 로컬에서 가능한 경우 mock/fixture 또는 안전한 read-only 요청으로 호출 형태를 검증한다.
- 외부 병원 API가 비용, 인증, 개인정보, 운영 rate limit을 건드릴 수 있으면 실제 호출 전에 Waiting으로 전환하고 사용자 승인을 요청한다.

## 산출물 요구

- `reports/build-13/<timestamp>.html`
- 확인한 호출 흐름: UI/입력 → client/server 함수 → endpoint → 응답 처리 → 에러/빈 결과 처리
- 실제 호출 여부: 성공 / 실패 / 차단 / 미확인
- 실패 시 원인 분류: env 누락, endpoint 오류, request shape 오류, auth 오류, CORS/네트워크, 응답 파싱 오류, UI 미연결
- 다음 액션: 코드 수정 필요 여부와 수정 대상 파일

## 금지/주의

- 병원 API 키, 토큰, 개인정보, 위치정보를 노출하지 않는다.
- 운영 API에 쓰기 요청을 보내지 않는다.
- 유료/민감 외부 호출은 사용자 승인 없이 반복하지 않는다.
- 레포 위치가 불명확하면 추측으로 수정하지 말고 레포 식별 결과를 먼저 남긴다.

## 완료 기준

- 병원 API 호출 경로가 실제로 연결되어 있는지 판단한다.
- 최소 하나의 안전한 검증 결과 또는 명확한 차단 사유를 남긴다.
- HTML report gate를 통과한다.
