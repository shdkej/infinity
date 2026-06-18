# research-15: 3D Interactive Character Background Feasibility

- id: research-15
- status: inbox
- projects: [personal-ops, infinity, design-system]
- task_type: research
- topics: [3d-background, interactive-character, threejs, design-system, skill]
- owner: Infinity
- display_name: 3D Interactive Character Background Feasibility
- created_at: 2026-06-18T06:20Z
- source: user request in Telegram after Status four-card cockpit redesign
- reference_url: https://www.youtube.com/watch?v=dROkEnvxch4

## User Request

마스터는 Sam Samuel 웹의 핵심 코어 디자인 컨셉으로 다음을 확정했다.

- 백그라운드에 3D 인터랙티브 캐릭터가 있다.
- 버튼과 UI 요소는 그 위에 떠 있는 구성요소다.
- 모바일에서는 캐릭터를 적당히 작고 안정적으로 위치시킨다.
- 데스크탑에서는 캐릭터를 크게, 위치 제한을 덜 두고 배치할 수 있어야 한다.
- 이 캐릭터/배경 레이어를 만드는 reusable skill도 필요하다.

이번 intent는 YouTube 레퍼런스 영상을 참고해, 이를 실제 웹에서 구현할 방법과 더 단순한 대안을 비교해 제안한다.

## Research Questions

1. 레퍼런스 영상의 핵심 구현 원리는 무엇인가?
2. Sam Samuel 웹에서 같은 감각을 구현하려면 Three.js/R3F/Spline/Lottie/video/raster fallback 중 무엇이 적합한가?
3. 모바일 성능과 배터리, 첫 로딩, fallback까지 고려했을 때 현실적인 단계별 접근은 무엇인가?
4. Status 페이지에 먼저 적용한다면 어떤 화면 구조가 맞는가?
5. `DESIGN.md`, `DESIGN_SYSTEM.md`, future skill에 각각 무엇을 기록해야 하는가?

## Output Contract

Create one concise artifact under `artifacts/research-15/` with:

- reference summary: video에서 취할 핵심 장면/인터랙션 원리
- options matrix:
  - A. full interactive 3D canvas
  - B. lightweight 3D-like scene / Spline embed
  - C. pre-rendered video/image sequence + pointer parallax
- recommendation for Sam Samuel:
  - prototype path
  - production path
  - mobile fallback
  - desktop expansion rule
- Status first application plan:
  - background layer
  - floating HUD/button layer
  - detail transition behavior
- documentation plan:
  - `DESIGN.md` section proposal
  - `DESIGN_SYSTEM.md` product pattern proposal
  - reusable skill name and responsibilities

## Boundaries

- No production implementation yet.
- No deploy.
- No paid service signup.
- No public posting.
- Do not modify Status code in this intent unless a separate implementation intent is created.

## Suggested Next Step

Research the YouTube reference first. If direct transcript extraction is blocked, use browser/video observation or a concise manual reference pass, then compare implementation paths by feasibility rather than trying to perfectly clone the effect.
