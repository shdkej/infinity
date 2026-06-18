# build-12 Status 3D Character Background Prototype

- id: build-12
- status: archived
- completed_at: 2026-06-18T11:57
- projects: [personal-ops, infinity, design-system]
- task_type: implementation
- topics: [3d-background, interactive-character, skill]
- result_summary: Option D(pre-rendered + CSS pointer parallax) 구현 완료 — z-index 0 공간 무대(aura+presence+motes 3-depth) 위에 기존 4-card 글래스 HUD를 hud-layer(z-index 10)로 띄움. 데스크탑 perspective+78vh, 모바일 30vh 중앙 고정+parallax off, reduced-motion fallback, 390px 무스크롤. 배포·라이브 검증 완료.
- artifacts:
  - path: artifacts/build-12/spatial-presence.css
    role: implementation
    note: CSS 전체 구현체(클라우드 prepare). 로컬에서 투명 stage + 3-depth + perspective로 강화 적용.
  - path: artifacts/build-12/index-html-patch.md
    role: implementation
    note: HTML 패치 가이드(stage div · hud-layer · parallax JS)
  - path: artifacts/build-12/local-execution-prompt.md
    role: implementation
    note: 로컬 실행 프롬프트
- reports:
  - path: reports/build-12/2026-06-18T1157Z.html
    role: final
- commits:
  - repo: space
    sha: 64049a5
    note: "Add SpatialPresence 3D character background layer to status dashboard (sites/status/* 4파일, travel-data.json·naver 변경 미포함)"
- urls:
  - url: https://status.aws.shdkej.com
    note: 라이브 — character-stage + spatial-presence.css 신규본 서빙(HTTP 200)
- success_criteria:
  - "[x] 배경 캐릭터/공간 레이어 표시 (Phase 1 placeholder presence)"
  - "[x] HUD 카드가 배경 위 정상 표시 (stage z-index 0 / HUD z-index 10)"
  - "[x] 마우스 이동 시 CSS parallax 작동 (rAF throttle, rotateX/Y+translate3d)"
  - "[x] prefers-reduced-motion → static fallback (inline transform 미발생 검증)"
  - "[~] LCP ≤ 3s — Phase 1은 이미지 없음(placeholder). Phase 2 poster preload로 충족 예정"
  - "[x] 390px 가로 스크롤 없음 (scrollWidth 390 = innerWidth)"
  - "[x] DESIGN.md ## Spatial Presence Layer 섹션 추가 (sites/status/DESIGN.md)"
  - "[x] DESIGN_SYSTEM.md SpatialPresence 패턴 + CSS 토큰 추가 (sites/status/DESIGN_SYSTEM.md)"
- verification:
  - Playwright headless(chromium-1208): 로컬 1440/390 + 라이브 1440 — stage·HUD z·presence·4card·390px 무스크롤·parallax·reduced-motion 통과
  - 라이브 curl: index.html(200, character-stage 포함) · assets/spatial-presence.css(200, 신규 내용)
- notes:
  - DESIGN.md/DESIGN_SYSTEM.md는 infra 레포에 기존 파일이 없어 status 사이트와 co-locate 위치(sites/status/)에 신규 생성. dist/ 배포 대상에서 분리됨.
  - status.json은 레이아웃 변경과 무관해 재생성하지 않음(오늘자 05:50 데이터 유지). build-status-json.py는 실행 시 status.json을 항상 덮어쓰므로 불필요한 churn·네트워크 의존을 피함.
- next: Phase 2(별도 intent) — AI 캐릭터 still 생성 → assets/character/poster.webp 를 .depth-mid 에 <picture>로 삽입 + LCP preload. 현 구조는 에셋 교체만으로 동작(코드 변경 0). Phase 3은 Spline/R3F(research-16 Option B/C).
