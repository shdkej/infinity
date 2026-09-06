# T15.2 Red — telemetry privacy

**판정: PASS — 문서 전용·기본 off 경계에 한함.**

- SDK, 쿠키, localStorage, 네트워크·제3자 전송, 배포를 허용하지 않는다.
- 원본 이벤트 보존은 0이며, 향후 집계 검토도 명시적 opt-in·개인정보 검토·Red PASS·승인·별도 배포·default-off·삭제/rollback gate 이후에만 가능하다.
- IP, 계정·세션·기기 식별자, fingerprint, 검색 원문·지역명·URL query, 출처/작성자 데이터, 주소·좌표·위치·viewport 및 상관 가능한 timestamp를 금지한다.
- telemetry는 근거 적격성, 렌더·핀·집계·점수·경로, 안전·위험 주장을 만들지 않는다.

필수 수정 없음. 향후 집계 카운터는 현재 권한이 아니라 gated consideration이라는 문구를 유지한다.
