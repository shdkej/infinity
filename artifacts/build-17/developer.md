# build-17 Developer

- 원인: CSS 링크 `./styles.css`는 존재하지만 이전 규칙 `body{min-width:980px}`가 모바일 viewport를 강제로 넓히는 구조였다. 현재 두 배포 경로의 CSS에는 `body{min-width:0;overflow-x:hidden}` 및 `max-width:800px` 반응형 분기가 적용되어 있다.
- 구현 확인: 모바일에서 workspace가 단일 열로 전환되고 preview가 먼저 배치되며, `stage-wrap`이 viewport 폭을 상한으로 사용한다. Infinity fallback과 독립 `instagram-maker` dist의 CSS가 동일한 규칙을 가진다.
- 검증: `curl`로 `/`, `/styles.css`, `/app.js`, 폰트가 모두 200; 두 `app.js`에 `node --check` 통과. Chromium CDP에서 390px `innerWidth=390`, `scrollWidth=375`, canvas x=35.4, width=304.2; 1440px `scrollWidth=1425`, canvas x=688.1, width=438.9.
- 우려: canvas 내부의 큰 제목은 콘텐츠 디자인상 일부가 잘릴 수 있어 다음 별도 UX 개선 후보지만, 이번 레이아웃 overflow와는 분리했다.
- 인계: Operator가 변경 파일 범위와 commit/push를 확인한다.
