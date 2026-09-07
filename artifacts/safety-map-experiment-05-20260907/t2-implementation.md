# T2 구현 — Termini 주의 영역과 근거 drawer

## 사용자 관측 변화

기존 `safety-map-experiment-03` 배포본은 이제 Roma Termini 환승 허브를 기본 화면으로 열고, 넓은 반투명 빨간 영역을 누르면 행동 문구·근거 수·날짜·범위·한계·출처 링크를 열어 보여 줍니다.

## 구현 경계

- 지도 레이어: 넓은 GeoJSON 다각형(`termini-caution`)만 사용하며 정확한 사건 위치나 핀은 만들지 않았습니다.
- drawer: ‘환승 시 소지품 주의’만 말하며, 안전/위험/발생률 판단을 명시적으로 배제합니다.
- 검색: `Termini`는 영역으로 이동하고, 다른 검색은 로마 bbox 안에서만 찾습니다.
- 클릭: 정보 레일의 빈 영역이 지도 레이어 클릭을 가리지 않도록, 검색 폼만 pointer 이벤트를 받도록 조정했습니다.

## 검증 증거

- Space source: `infra-aws-static-sites/sites/safety-map-experiment-03/dist/{index.html,app.js,styles.css}`
- JavaScript syntax: `node --check` 통과
- 배포: Space `4dca65e` + 클릭 영역 보정 `1b62d28`
- GitHub Actions: run `34129702370` 성공
- 라이브에서 영역 클릭 후 drawer와 3개 출처 링크를 확인: 2026-09-07T13:52:55Z
