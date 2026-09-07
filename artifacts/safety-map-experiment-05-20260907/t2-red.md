# T2 Red 검증 — 지도 hit-area·주장 경계

판정: **PASS** · P0 없음

- 라이브 `https://safety-map-experiment-03.aws.shdkej.com/?v=fac1050`에서 데스크톱과 정확히 390×844 모바일 모두 Mapbox canvas가 생성됐다.
- 각 화면에서 Roma Termini 지도 중심을 한 번 눌러 근거 drawer가 열리는 것을 확인했다.
- 모바일은 `innerWidth=390`, `scrollWidth=390`으로 가로 overflow가 없다.
- drawer는 행동 문구·근거 수·날짜·넓은 범위·한계·출처만 표시하며, 안전 보장·위험 점수·발생률 주장은 없다.

검증 시각: 2026-09-07T14:11:20Z
