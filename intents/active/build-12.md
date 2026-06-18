# build-12: Status 3D Character Background Prototype

- id: build-12
- status: waiting
- priority: medium
- projects: [personal-ops, infinity, design-system]
- task_type: implementation
- mode: execute_local
- topics: [3d-background, interactive-character, skill]
- created_at: 2026-06-18T07:00Z
- activated_at: 2026-06-18T08:00Z
- source: follow-up from research-15, research-16
- cloud_prepare: completed 2026-06-18T11:00Z
- do_not_repeat_cloud: true

## Goal

Status 페이지에 3D 캐릭터 배경 레이어를 적용한다.

**Scope (research-16 결정): Option D — pre-rendered + CSS pointer parallax**

- pre-rendered 캐릭터 still(poster WebP) 또는 short loop(WebM) → background canvas
- CSS 3D perspective + pointer parallax (3 depth layers, ±8° max on desktop)
- Quiet Note 팔레트 배경 + 기존 floating HUD cards 그대로 유지
- `prefers-reduced-motion: reduce` → static poster, no JS parallax
- Mobile (< 640px): poster still, parallax 최소화(±4° 이하 or none)

## Success Criteria

- [ ] Status 페이지 배경에 캐릭터 레이어 표시
- [ ] 기존 HUD 카드가 배경 위에 정상 표시 (z-index: 0 background / z-index: 10+ HUD)
- [ ] 마우스 이동 시 CSS parallax 효과 작동
- [ ] `prefers-reduced-motion` → static poster fallback
- [ ] LCP ≤ 3s (poster 이미지 선행 로드)
- [ ] 390px 뷰포트 가로 스크롤 없음
- [ ] DESIGN.md `## Spatial Presence Layer` 섹션 추가
- [ ] DESIGN_SYSTEM.md `SpatialPresence` 패턴 + CSS 토큰 추가

## Context

- 연구 기반: artifacts/research-16/3d-character-stage-options.md
- 이전 연구: artifacts/research-15/3d-character-bg-feasibility.md
- 현재 Status: build-11에서 4-card floating 레이아웃 완성
- Target repo: `/home/ubuntu/workspace/space/infra-aws-static-sites`
- Target surface: `https://status.aws.shdkej.com`
- Target files:
  - `sites/status/dist/index.html`
  - `sites/status/dist/assets/spatial-presence.css` (신규)
  - `DESIGN.md`, `DESIGN_SYSTEM.md`
- CSS 토큰 참조:
  - `--character-z: 0; --hud-z: 10; --hud-bg: rgba(244,242,234,0.75); --hud-blur: blur(8px)`
  - `--character-scale-desktop: 75vh; --character-scale-mobile: 30vh`
  - `--parallax-desktop: 8; --parallax-mobile: 4`
- character asset: Phase 1은 placeholder gradient, Phase 2는 AI 생성 still(poster WebP)

## Cloud Prepare 완료 (2026-06-18T11:00Z)

구현 파일 준비 완료 — do_not_repeat_cloud 활성:
- `artifacts/build-12/spatial-presence.css` — CSS 전체 구현체
- `artifacts/build-12/index-html-patch.md` — HTML 패치 가이드
- `artifacts/build-12/local-execution-prompt.md` — 로컬 Claude Code 실행 프롬프트

## Next Action (execute_local — 로컬 Claude Code)

`artifacts/build-12/local-execution-prompt.md`를 로컬 Claude Code에 전달하여 실행:
1. `spatial-presence.css`를 `sites/status/dist/assets/`에 복사
2. `index.html`에 CSS 링크·`.character-stage` div·parallax JS 추가
3. HUD 래퍼 z-index 확인 및 `.hud-layer` 클래스 적용
4. `DESIGN.md` + `DESIGN_SYSTEM.md` 업데이트
5. 검증 게이트 모두 통과 확인
6. HTML report 작성 + push → `reports/build-12/{timestamp}Z.html`

## Phase 2 (별도 intent, build-12 완료 후)

Spline embed prototype (Option B) — build-12 Option D 완료 후 별도 브랜치.
