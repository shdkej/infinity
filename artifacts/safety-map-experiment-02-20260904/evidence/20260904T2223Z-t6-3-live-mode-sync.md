# T6.3 라이브 지도 UX·디자인 품질 개선 증거

- 대상: `https://safety-map.aws.shdkej.com/`
- 검증 환경: OpenClaw managed browser, desktop live page
- Space 변경: `2d67ee49f732c0d6c3079b6036e7dc8f89f0164b` (`origin/master` 일치)

## 개선

상단과 지도 툴바의 주야간 제어를 하나의 `mapStyleMode`와 `syncMapMode(mode)`로 통합했다. 페이지의 야간 표현, 두 버튼의 문구·`aria-pressed`, Mapbox `setStyle()`이 같은 상태를 사용한다. 안전 등급·사건·경로 데이터는 추가하지 않았다.

## 라이브 상호작용

1. 초기 상태에서 상단 `☾ 야간 맥락 보기`, 지도 `야간 지도 보기`가 모두 주간 state를 표시했다.
2. 상단 control을 눌렀다. 상단은 `☀ 주간 맥락 보기`와 `pressed`, 지도 control은 `주간 지도 보기`와 `pressed`로 함께 바뀌었다.
3. 지도 control을 눌러 되돌렸다. 상단 `☾ 야간 맥락 보기`, 지도 `야간 지도 보기`가 함께 복귀했다.
4. live page의 Mapbox application/Zoom controls, `안전 신호: 현재 검증된 데이터 없음`, 장소·도로 맥락 제한을 유지했다.

## 로컬 검증

- `node sites/safety-map/test-smoke.js`: PASS
- source/dist `app.js` SHA-256: `46599051c012e47fe8a877e9383b97e1f9a0a95bf1fa419b1fa2ff9db2779f9d` 일치
- smoke test는 두 control의 공통 state setter와 initial Mapbox style 동기화를 검사한다.

## 다음

T6.3은 완료. T6.4에서 390px의 두 control·focus·overflow·no-data 경계를 재점검한다. terminal Slack과 Archive는 금지 상태다.
