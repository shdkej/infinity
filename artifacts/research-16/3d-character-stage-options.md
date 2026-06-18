# 3D Character Stage 구현 옵션 비교

> intent: research-16 | created: 2026-06-18T08:00Z | heartbeat: cloud research (L0)
> basis: SAM Gemini YouTube parse (youtube-reference-parse.md) + research-15 feasibility matrix

## YouTube 레퍼런스 해석

영상: "5 TOOLS YOU NEED TO BUILD NEXT LEVEL WEBSITES EVERY SINGLE TIME"

SAM Gemini 파싱으로 확인된 핵심 파이프라인:
1. **Figma** — 시각 방향 / stylescape 먼저
2. **AI 생성** (Magnific/Freepik) — 3D-looking hero asset 제작 (예: 검은 대리석 조각상)
3. **Spline** — web에 asset 임베드, cursor-reactive 인터랙션 (눈/몸이 포인터 따라 이동)
4. **Unicorn Studio** — animated atmospheric background (FBM motion, film grain, brand color)
5. **핵심 원칙** — 도구가 아닌 파이프라인; 시각 방향이 엔지니어링보다 먼저

Sam Samuel 번역:
- Stage: 따뜻하고 살아있는 companion/character → background identity
- Spline: 캐릭터가 포인터·포커스·Status 전환에 미묘하게 반응
- Unicorn Studio 또는 동등 솔루션: 캐릭터 주변 따뜻한 motion/texture, HUD는 가독성 유지
- 원칙: DESIGN.md가 stage 정의, DESIGN_SYSTEM.md가 CharacterStage/FloatingHUD 정의 → 도구 선택은 그 이후

## 옵션 매트릭스

### Option A: Three.js / React Three Fiber (Code-Owned)

| 항목 | 세부 |
|------|------|
| 스택 | React Three Fiber + drei + Three.js + GLTF character |
| 인터랙티브 | 마우스 IK/bone rotation, 클릭 반응, idle loop, 씬 조명 완전 제어 |
| 번들 | ~350-500KB min + GLB 50-200KB (Draco 압축 시) |
| 모바일 | GPU 의존성 높음, 최적화 필수; mid-range+ 기기 60fps |
| 제어권 | 최고 (shader, physics, bone, custom material) |
| 개발 기간 | 3-5일 |
| 비용 | 없음 (코드 소유) |
| 적합한 역할 | 장기 프로덕션 |

### Option B: Spline Embed + AI-generated Asset (YouTube Reference Path)

| 항목 | 세부 |
|------|------|
| 스택 | @splinetool/react-spline + Spline scene + AI-generated character asset |
| 인터랙티브 | Spline 내장 cursor hover/click states, eye-tracking via state machine |
| 번들 | runtime.js ~300KB + .splinecode 2-15MB |
| 모바일 | 중간; 복잡한 씬은 저사양 기기 부담 |
| 제어권 | 중간; Spline runtime 종속, shader 불가 |
| 개발 기간 | 1-2일 (prototype) |
| 비용 | 셀프 호스팅: Spline Pro ~$12-18/월 |
| 적합한 역할 | 빠른 prototype, 시각 검증 |

### Option C: Unicorn Studio Animated Layer (Background Only)

| 항목 | 세부 |
|------|------|
| 스택 | Unicorn Studio embed 또는 Canvas/WebGL |
| 역할 | atmospheric background texture, grain, FBM motion, brand color |
| 인터랙티브 | 씬 내 ambient motion (포인터 아닌 배경 흐름) |
| 번들 | embed script ~30-50KB + animation data |
| 모바일 | 중간; 애니메이션 복잡도로 제어 가능 |
| 제어권 | 중간; Unicorn Studio 종속 |
| 개발 기간 | 0.5-1일 |
| 적합한 역할 | 배경 분위기 레이어 (Option B/D와 조합) |

### Option D: Pre-rendered + CSS Pointer Parallax (Status-First / Mobile Fallback)

| 항목 | 세부 |
|------|------|
| 스택 | HTML5 video (WebM) 또는 static poster WebP + CSS 3D perspective + JS 20줄 |
| 인터랙티브 | CSS transform rotate3d parallax (레이어별 ±8-10° 깊이감) |
| 번들 | WebM 1-3MB / poster WebP 100-300KB |
| 모바일 | 최고 (hardware video decode, no GPU compute, 배터리 영향 미미) |
| 제어권 | 낮음 (실시간 반응 없음, 고정 loop) |
| 개발 기간 | 반일 (웹 통합), Blender/AI render 별도 |
| 비용 | 없음 |
| 적합한 역할 | Status 즉시 적용, mobile fallback |

## 레퍼런스 파이프라인 직접 조합

YouTube workflow를 Sam Samuel에 그대로 적용:

**Option B + C 조합**: Spline cursor-reactive character (B) + Unicorn Studio atmospheric layer (C)
- Pros: 레퍼런스와 가장 근접, 빠른 prototype
- Cons: 외부 런타임 2개 종속, 셀프 호스팅 비용, 모바일 부담 누적
- 결론: prototype 환경에서만 권장. 프로덕션은 code-owned 전환 필요

## Status-First 권장 경로

**1단계 (즉시, 반일): Option D**
- pre-rendered warm character still/loop (poster WebP → WebM on demand)
- CSS pointer parallax (3 depth layers, ±8° rotate3d)
- Quiet Note 팔레트 배경 + floating HUD cards 그대로
- `prefers-reduced-motion` → static poster, no parallax
- 결과: 시각적 presence, 즉각 배포 가능, zero WebGL risk

**2단계 (prototype, 1-2일): Option B (Spline)**
- Spline 씬에서 AI-generated 3D character 임베드
- cursor hover state machine
- fallback: Option D static
- 결과: 시각 검증, 사용자 피드백 수집

**3단계 (프로덕션 결정 후): Option A (R3F)**
- Option B 검증 후 ownership 필요 시 전환
- idle/look/wave 애니메이션 + IK
- Draco + KTX2 최적화
- 결과: 완전한 제어, 외부 종속성 없음

## Reusable Skill 개요: `add-3d-character-stage`

**입력:**
- `character_asset_path` (GLB/WebM/poster PNG, 또는 Spline URL)
- `mode` (spline | r3f | video | auto)
- `target_page` (예: status, home)
- `performance_budget` (예: lcp_ok=3s, no_gpu_fallback=true)
- `design_direction` (DESIGN.md 섹션 참조 또는 인라인)

**생성 파일:**
- `components/CharacterBackground.tsx` (또는 vanilla HTML snippet)
- `components/CharacterBackground.css` (CSS tokens, parallax rules)
- `assets/character/poster.webp`, `character-idle.webm` (pre-rendered 기준)
- `DESIGN.md` diff: `## Spatial Presence Layer` 추가
- `DESIGN_SYSTEM.md` diff: `SpatialPresence` 패턴 + 토큰 추가

**필수 검증 게이트:**
- LCP ≤ 3s (poster 이미지 선행 확인)
- `prefers-reduced-motion: reduce` → static poster, no JS parallax
- 390px viewport: no horizontal scroll
- `pointer-events: none` on background layer
- HUD z-index ≥ 10, pointer-events: all

**Fallback 체인:**
- WebGL/Spline 로드 실패 → video loop
- video autoplay 실패 → poster still
- `prefers-reduced-motion` → poster still
- viewport < 640px → poster still + reduced parallax (or none)

**모바일 배치:**
- Desktop (≥ 1024px): character 70-80vh, right or center, free
- Tablet (768-1023px): 50vh, center fixed
- Mobile (< 768px): poster still or video, 30vh, bottom center, no parallax above ±4°

## 구현 경정 요약

**직접 구현 지금? vs 단계적?**

→ **단계적**: Option D를 build-12에서 Status 즉시 적용 (반일). Option B는 별도 prototype 브랜치 (Phase 2). Option A는 Phase 2 검증 후 결정.

근거:
- Option D: 즉시 Status 배포 가능, zero risk
- Option B(Spline): 씬 파일 + AI asset 생성 + 런타임 설정 필요, 별도 일정
- Option A(R3F): Option B 시각 검증 후 결정
- build-12를 Option D로 scope → 당일 완료 가능

## CSS 토큰 레퍼런스

```css
/* SpatialPresence tokens */
--character-z: 0;
--hud-z: 10;
--hud-bg: rgba(244, 242, 234, 0.75);
--hud-blur: blur(8px);
--character-scale-desktop: 75vh;
--character-scale-tablet: 50vh;
--character-scale-mobile: 30vh;
--parallax-desktop: 8deg;
--parallax-mobile: 4deg;
```
