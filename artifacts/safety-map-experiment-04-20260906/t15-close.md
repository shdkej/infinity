# C15 마감확인 — telemetry 개인정보 경계

T15.1의 문서 전용/default-off 계약과 T15.2 독립 Red PASS를 확인했다.

- telemetry 수집, SDK, 쿠키, localStorage, 저장, 네트워크·제3자 전송, 배포는 수행·허용하지 않는다.
- 식별자, 위치, 원문 검색어, 출처 원문과 상관 가능한 timestamp는 보존하지 않는다.
- telemetry는 근거 적격성, 신호 렌더, 핀, 집계, 점수, 경로, 안전·위험 주장을 만들지 않는다.
- 향후 구현은 opt-in·개인정보 검토·승인·별도 release/rollback gate를 통과할 때까지 금지한다.

따라서 C15는 30분 제한 내에 종료한다. 현 상태는 telemetry 미구현/no-tracking이며, 다음 T16은 별도 배포·rollback gate에서 판단한다.
