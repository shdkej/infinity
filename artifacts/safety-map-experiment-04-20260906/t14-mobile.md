# T14.1 390px·키보드 접근성 검증

- 검증 시각: 2026-09-06T18:06:00Z
- 대상: `https://safety-map-experiment-03.aws.shdkej.com/` (Space `8ecae7c`)
- viewport: 390×844
- 결과: **PASS — T14.1 범위에 한함**

## 실제 원격 렌더

- `window.innerWidth/innerHeight`와 문서·body scroll 크기가 모두 `390×844`였다. 가로·세로 overflow가 없었다.
- 로마의 `표시할 검증 근거가 없습니다`, `현재 적격 입력: 0`, `NO SCORE · NO ROUTE · NO TRACKING`가 렌더 상태에 존재했다.
- 브라우저 오류는 0건이었다.

## 키보드 흐름

- Tab 순서에서 지도 제어 뒤 `#place-search` 검색 입력과 `#search-submit` 제출 버튼에 모두 도달했다.
- 검색 입력에 `Termini`를 입력한 뒤 Enter를 눌러 지도 상태가 `GLOBAL FIELD / Termini Imerese`로 갱신됐다.
- 이 검증은 일반 장소 검색만 확인한다. 주의 신호·점수·경로·추적·개인 위치 수집은 생성하거나 표시하지 않았다.

## 다음 경계

T14.2 Red는 이 원격 viewport·포커스·no-render 증거가 접근성 또는 안전 표현 권한으로 과장되지 않았는지 독립 검증한다.
