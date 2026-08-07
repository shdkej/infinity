# build-17 Red 검증

- red_status: pass
- 검증 대상: `sites/instagram-maker/dist/`와 `sites/infinity/dist/instagram-maker/`의 index/styles/app 및 390px·1440px 렌더.
- 통과 근거:
  - CSS stylesheet가 `http://127.0.0.1:8765/styles.css`로 로드되고 CSS rule 83개가 적용됨.
  - 모바일 CDP 결과: `innerWidth=390`, `scrollWidth=375`, canvas x=35.4/right=339.6. 페이지 가로 overflow가 없다.
  - 데스크톱 CDP 결과: `innerWidth=1440`, `scrollWidth=1425`, canvas x=688.1/right=1126.9. 2열 레이아웃이 유지된다.
  - `/`, `/styles.css`, `/app.js`, `A2Z-Black.woff2` HTTP 200; 두 app.js `node --check` 통과.
  - 모바일·데스크톱 캡처: `artifacts/build-17/mobile.png`, `artifacts/build-17/desktop.png`.
- 잔여 권고: canvas 텍스트 안전 폭은 별도 UX intent로 다룬다. 이번 요청의 페이지 overflow 완료 판단에는 영향이 없다.
- report: `reports/build-17/2026-08-07T1417Z.html`
