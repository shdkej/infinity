# T6.2 — 모바일 접근성 반복

- 실행: 2026-09-04T21:52Z, OpenClaw 관리형 Chromium의 실제 라이브 페이지
  `https://safety-map.aws.shdkej.com/`
- viewport: 390 x 844 CSS px
- 범위: 모바일 레이아웃, 핵심 제어의 이름/키보드 이동, 지도 및 no-data 안전 고지.

## 관찰값

| 검증 | 결과 |
| --- | --- |
| 가로 overflow | 없음 (`scrollWidth` 375 <= viewport 390) |
| 실제 지도 | Mapbox canvas 1개 |
| 핵심 제어 이름 | 검색 상자(장소 또는 도로 찾기), 찾기, 주간 지도 보기, Zoom in/out, attribution 토글이 접근성 트리에 노출 |
| 키보드 순서 | 검색 상자를 선택한 뒤 `Tab`으로 `찾기` 버튼에 포커스 이동; 캡처에 노란 focus ring 확인 |
| 안전 경계 | `현재 검증된 데이터 없음` 고지 유지 |
| 브라우저 오류 | 0개 |

## 증거

- `20260904T2152Z-t6-mobile-accessibility/mobile-find-focus.png`
  - SHA-256: `a650a2781911aa2a02899d63e64097e220001c76dbff3ec0c5ce285b3520c96d`
  - PNG 390 x 844; 검색 결과와 지도, 버튼 focus 상태를 함께 보여준다.

## 역할 판단

- Planner: 모바일 수용 기준을 overflow·핵심 flow·no-data 경계로 한정했다.
- Developer: ARIA 노출과 실제 focus 이동을 확인했다.
- Marketer: 안전 보장 대신 장소/도로 맥락 및 데이터 없음 카피가 유지됨을 확인했다.
- Operator: 라이브 HTTPS 관리형 브라우저에서 검증했고, 토큰 값을 기록하지 않았다.

T6.2는 완료한다. terminal Slack, Archive, 최종 Red는 마감 또는 명시 종료 조건 전에는 실행하지 않는다.
