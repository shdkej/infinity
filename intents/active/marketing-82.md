# marketing-82 — Virtue 랜딩페이지 만들기

- id: marketing-82
- status: active
- created_at: 2026-06-24T21:07Z
- projects: [virtue]
- task_type: implementation
- topics: [marketing, activation, product]
- owner_route: Infinity router -> local execution
- requested_by: SeongHo Noh
- source: Telegram direct request
- approval: user-approved
- permission_level: L1 implementation
- user_visible: true

## 요청

Virtue 랜딩페이지를 만든다.

이번 intent의 목적은 SAM이 즉시 직접 처리하는 것이 아니라, **Infinity hourly local router cron이 나중에 이 Active intent를 발견하고 로컬 실행으로 처리하는 흐름**을 확인하는 것이다.

## 범위

허용:
- Virtue 로컬 repo 읽기
- 랜딩페이지 관련 파일 탐색
- 안전한 L1 코드/문서 수정
- 로컬 typecheck/lint/build 등 읽기/검증성 명령
- 결과 HTML report 작성
- 관련 repo commit/push
- Infinity archive/report 업데이트와 parent `knowledge-lab` submodule pointer push

금지/주의:
- production deploy 직접 실행 금지
- 외부 메시지/메일/공개 게시 금지
- 비용 발생 작업 금지
- 인증/시크릿/권한 변경 금지
- tracking/privacy/event schema 변경 금지
- unrelated dirty files stage 금지

## 산출 요구

라우터가 처리할 때 아래 중 하나를 남겨야 한다.

1. 실제 구현 완료:
   - Virtue 랜딩페이지 변경
   - 검증 결과
   - `reports/marketing-82/{timestamp}.html`
   - `intents/archive/marketing-82.md`
2. 한 사이클에 구현이 너무 크면:
   - `reports/marketing-82/{timestamp}-handoff.html`
   - 정확한 대상 repo/files
   - 다음 실행 범위
   - blocker 또는 검증 gate

## 성공 기준

- 랜딩페이지가 첫 화면에서 Virtue의 가치와 다음 행동을 분명히 보여준다.
- 기존 `marketing-80`, `marketing-81`의 second-step bridge/empty-state 학습과 충돌하지 않는다.
- 새 랜딩은 사용자를 과하게 교육하지 않고, 첫 가치와 다음 행동을 바로 연결한다.
- 구현을 했다면 typecheck/lint/build 중 적용 가능한 검증 하나 이상을 수행한다.
- 완료 또는 handoff가 저녁 `Infinity router daily` 요약에서 meaningful work slot으로 보일 수 있게 기록된다.

## 참고 맥락

- `marketing-80`: 홈 요약 카드·최근 덕행·저장 후 복귀 지점 감사
- `marketing-81`: 첫 저장/첫 판단 뒤 홈 복귀 secondary onboarding 감사
- `marketing-77`: `/add` 기대 브리지와 결과 카드 footer 안내 구현

## 현재 상태

등록만 완료. SAM은 이번 턴에서 직접 구현하지 않는다. 다음 hourly Infinity router가 이 intent를 선택해 처리해야 한다.
