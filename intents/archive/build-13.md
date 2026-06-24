# build-13 — 아프지마 앱 병원 API 호출 흐름 검증

- id: build-13
- status: archived
- completed_at: 2026-06-24T0050Z
- projects: [afzma, infinity, app-api-verification]
- task_type: implementation-verification
- topics: [hospital-api, api-flow, app-verification, data-fetching]
- owner: Infinity
- requested_by: SeongHo Noh
- created_at: 2026-06-23T14:14Z
- permission_level: L1 local/read-only verification
- target_repo: shdkej/afzma

## 결과 요약

로컬에 `shdkej/afzma`를 체크아웃해 병원 API 호출 흐름을 read-only로 검증했다. UI → `/api/chat`/`/api/history/[id]` → controller → `MedicalService` → HIRA 공공 병원 API 호출 경로는 코드상 연결되어 있다. 다만 실제 HIRA 네트워크 호출은 `HIRA_API_KEY`와 외부 공공 API를 건드리므로 실행하지 않았다. 키가 없거나 API 오류/빈 응답이면 mock 병원 데이터로 폴백한다.

## 핵심 발견

1. 홈 입력은 위치값이 있으면 `lat/lon`을 query로 넘긴다.
2. 응답 화면 hook은 `message` query가 있으면 `POST /api/chat`, 없으면 `GET /api/history/[id]`를 호출한다.
3. 서버 service는 AI 분석 후 `getRecommendedHospitals(analysis.department, lat, lon)`를 호출한다.
4. HIRA API endpoint는 `https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList`다.
5. `HIRA_API_KEY`가 없으면 즉시 mock 병원 데이터를 반환한다.
6. HIRA 응답이 비었거나 오류가 나도 mock 병원으로 폴백한다.
7. 로컬 `claude` 바이너리는 있었지만 401 인증 오류로 실행 실패해, SAM이 동일 로컬 체크아웃에서 read-only 검증을 수행했다.

## 산출물

- reports: [reports/build-13/2026-06-24T0050Z.html]

## 다음 액션

- mock fallback 여부를 응답 메타데이터로 UI에 전달하는 개선 검토
- HIRA HTTP status/API 에러코드/XML parse 실패 분기 명시
- 위치 권한 실패 상태를 UI에 별도 안내
- Claude Code 인증 복구 후 같은 repo에서 2차 검증 가능
