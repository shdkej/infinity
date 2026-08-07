# build-17 Planner

- 목표: Instagram Maker의 CSS 적용 상태와 모바일 preview 가로 overflow를 원인부터 확인하고, 두 배포 경로의 렌더 증거를 남긴다.
- 범위: `sites/instagram-maker/dist/`와 `sites/infinity/dist/instagram-maker/`의 정적 HTML/CSS/JS 및 로컬 브라우저 검증. 공개 URL·registry·인프라 변경은 범위 밖이다.
- Knowledge Lab 근거: `agent-wiki/README.md`의 변경 가능성과 운영 관측 원칙, `content/docs/mapped/Meta/Troubleshooting.mdx`의 재현→원인 분리→검증 원칙을 적용했다.
- 완료 기준: CSS/폰트 HTTP 200, 390px에서 `scrollWidth <= innerWidth`, preview 및 입력 surface 가시성, 1440px 회귀, 역할 기록·Red pass·HTML report.
- 우려: 기존 작업트리의 변경을 덮지 않고 두 정적 복사본을 동일하게 유지해야 한다.
- 인계: Developer가 실제 CSS와 브라우저 렌더를 고정하고, Operator가 git 원격 반영 게이트를 확인한다.
