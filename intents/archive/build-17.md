# build-17 — Instagram Maker CSS 및 모바일 Preview 레이아웃 수정

- id: build-17
- status: completed
- target_agent: genie
- priority: high
- permission: L1 (로컬 정적 파일 수정·테스트·렌더 검증; 공개 배포·인프라 변경은 승인 필요)
- goal: Instagram Maker의 CSS 로딩 원인과 모바일 preview 가로 overflow를 수정하고 데스크톱·모바일 렌더 증거를 남긴다.
- success_criteria: CSS 로드 확인, 390px viewport에서 scrollWidth <= innerWidth 및 주요 조작 영역 가시성, 데스크톱 회귀 확인, Planner·Developer·Marketer·Operator·Red 기록, HTML report와 Infinity/parent 원격 push 검증
- source_agent: main
- created_at: 2026-08-07T14:03:00Z
- projects: [infinity, static-sites, personal-ops]
- task_type: bugfix-and-verification
- topics: [instagram-maker, css, preview, responsive, mobile, red-team]

## 사용자 문제

- Instagram Maker 화면에 CSS가 적용되지 않아 레이아웃이 깨진다.
- 모바일에서 미리보기가 화면 안에 들어오지 않고 오른쪽으로 밀린다.
- 사용자는 오른쪽으로 수평 스크롤해야 미리보기를 볼 수 있는데, 모바일 UI로는 허용할 수 없다.

## 작업 범위

1. 현재 라이브/로컬 재현 화면과 소스의 CSS import, 번들, asset 경로를 대조한다.
2. CSS가 적용되지 않는 직접 원인을 고친다. 단순히 overflow를 숨겨 증상을 가리지 않는다.
3. 모바일에서는 preview가 viewport 안에 맞고 수평 스크롤이 발생하지 않도록 레이아웃을 수정한다.
4. 데스크톱 레이아웃을 망가뜨리지 않는 반응형 분기와 콘텐츠 축소/재배치 기준을 검증한다.
5. 실제 모바일·데스크톱 화면 캡처 또는 동등한 렌더 증거를 남긴다.
6. Red 검증을 통과한 뒤 실행 report를 만든다.

## 완료 기준

- CSS가 실제 화면에 로드되어 의도한 레이아웃/스타일이 보인다.
- 모바일 viewport에서 preview가 우측으로 밀리지 않고 한 화면 안에서 읽힌다.
- 모바일 가로 overflow가 없고, 주요 조작 영역이 viewport 밖으로 잘리지 않는다.
- 데스크톱 preview 및 기존 기능 회귀가 확인된다.
- Infinity 원격 `main` push와 필요한 Knowledge Lab parent pointer push를 확인한다.
- `reports/build-17/{timestamp}.html`이 존재하고 Infinity HTML Report Contract(`html`, `body`, `axis ax1`, `axis ax2`, `details`)를 통과한다.

## 완료 게이트

원격 push 확인 전에는 이 intent를 Active/Waiting에서 완료 처리하거나 Archive로 옮기지 않는다. 코드 수정만 끝난 상태는 완료가 아니다. 공개 배포 대상이 없으면 공개 배포를 완료로 가장하지 말고, 검증 가능한 로컬/원격 상태와 남은 외부 조건을 Waiting으로 기록한다.

## 다음 액션

지니가 현재 Instagram Maker 구현 위치와 CSS 로딩 경로를 먼저 앵커링하고, 원인 수정 → 모바일/데스크톱 검증 → Red → report → Infinity/parent 원격 push 순서로 실행한다.

## 완료 근거

- static-sites commit/push: `abbe3f5058fd6ba33d0d31ecc86629c1130b96af` (`origin/master` verified)
- CSS 수정: `body min-width:980px` 제거, 800px 이하 단일 열 반응형 분기, viewport-contained preview
- CSS/font HTTP 200 및 Chromium 실제 렌더: `reports/build-17/build-17-mobile.png`, `reports/build-17/build-17-desktop.png`
- Red: `artifacts/build-17/red.md`, `red_status: pass`
- report: `reports/build-17/20260807T1415Z.html`
