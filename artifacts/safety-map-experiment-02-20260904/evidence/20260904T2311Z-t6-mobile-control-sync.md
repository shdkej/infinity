# T6.4 · 390px 접근성·상호작용 재점검

- 시각: 2026-09-04T23:11Z
- 대상: `https://safety-map.aws.shdkej.com/`
- viewport: 390×844, managed browser

## 확인 결과

1. `documentElement.scrollWidth > innerWidth`는 `false`였다.
2. Mapbox canvas는 1개였고 브라우저 오류 수는 0이었다.
3. 검색 상자를 선택한 뒤 `Tab`을 누르면 포커스가 **찾기** 버튼으로 이동했다.
4. 상단 제어와 지도 툴바 제어는 어느 한쪽을 눌러도 함께 전환됐다.
   - 야간 전환 뒤: `☀ 주간 맥락 보기` / `주간 지도 보기`, 두 `aria-pressed=true`
   - 주간 복귀 뒤: `☾ 야간 맥락 보기` / `야간 지도 보기`, 두 `aria-pressed=false`
5. 화면에는 지도 표현 전환이 시간대별 위험·사건 데이터가 아니라는 고지가 유지됐다.

## 캡처 무결성

OpenClaw managed browser가 남긴 390px 상태 캡처는 서로 다른 SHA-256을 가졌다.

- 초기 상태: `7617532ec2be3ce277ff6e46cb96cdad0993910d847d951f61471e6a62247ad7`
- 제어 동기화 검증 뒤 상태: `6a28517da85d01495744b8e8b56b2fde8ecab19dccade2cb1b0dbbb08be7a35a`

## 판정

T6.4 완료. 실제 코드 변경은 T6.3의 두 주야간 제어 단일 상태화에 포함됐으며, 본 재점검은 그 개선이 390px 라이브 환경에서 키보드·ARIA·화면 경계와 함께 유지되는지를 독립 확인했다.
