# 3D Interactive Character Background Feasibility

> intent: research-15 | created: 2026-06-18T07:00Z | heartbeat: cloud research (L0)

## 레퍼런스 요약

YouTube 영상 `https://www.youtube.com/watch?v=dROkEnvxch4` 직접 열람은 차단됨(403). 연관 검색 결과와 맥락 기반 분석으로 재구성:

- 레퍼런스 영상은 **Spline 또는 Three.js** 기반 인터랙티브 3D 캐릭터를 개인 포트폴리오 배경으로 사용하는 튜토리얼로 추정 (연관 검색: "Making a 3D interactive character for web with Spline", "How to Create an Interactive 3D Character with Three.js | Codrops").
- 핵심 감각: 캐릭터가 마우스 커서를 따라 시선/몸을 돌리거나 클릭에 반응하고, UI 버튼/카드가 그 위에 떠 있는 레이어 구조.
- 확인된 레퍼런스: Codrops "How to Create an Interactive 3D Character with Three.js" (2019), Wawa Sensei R3F avatar animation series, Spline 3D character web embed tutorials.

**취할 핵심 장면/인터랙션 원리:**
1. 캐릭터(GLTF/GLB 또는 Spline 씬)가 배경 canvas 전체를 차지
2. 마우스 이동 → 캐릭터 머리/눈이 마우스 방향으로 rotate (IK 또는 bone 회전)
3. HUD 버튼/카드가 canvas 위에 `position: fixed / absolute`, `z-index: 10+`으로 떠 있음
4. 아이들 애니메이션: 숨쉬기, 미세 흔들림 (loop)
5. 클릭/호버 이벤트: 특정 카드 hover → 캐릭터 시선 이동 or 손들기/표정 변화

---

## 옵션 매트릭스

### Option A: Full Interactive 3D Canvas (Three.js / React Three Fiber)

| 항목 | 내용 |
|------|------|
| **기술 스택** | React Three Fiber + @react-three/drei + Three.js + GLTF 캐릭터 |
| **캐릭터 소스** | Ready Player Me (무료 아바타), Mixamo 애니메이션 리타겟, 또는 구매 에셋 |
| **인터랙티브** | 마우스 추적(IK/bone rotation), 클릭 반응, 아이들 루프, 씬 조명 완전 제어 |
| **번들 크기** | ~300-500KB min (Three.js 150KB + R3F 50KB + 캐릭터 GLB 100-300KB; Draco 압축 시 GLB 50-80% 절감) |
| **첫 로딩** | GLB lazy load + Draco 압축 필수; 느린 기기에서 LCP 영향 있음 |
| **모바일 성능** | GPU 의존성 높음, 배터리 부담 있음; LOD mesh + autorotate fallback 필수; mid-range 이상 기기에서 60fps |
| **모바일 fallback** | `prefers-reduced-motion` 또는 성능 tier 감지 후 Option C로 자동 전환 권장 |
| **제어권** | 최대 (shader, physics, bone, 커스텀 재질 전부) |
| **개발 난이도** | 높음 (3D 개념, GLTF 파이프라인, bone 애니메이션 지식 필요) |
| **디자이너 접근성** | 낮음 |

**적합한 케이스:** 장기 운영 프로덕션, 완전한 브랜드 제어, 성능 예산 관리 가능 환경

---

### Option B: Spline Embed (추천 — 최속 Prototype)

| 항목 | 내용 |
|------|------|
| **기술 스택** | @splinetool/react-spline + Spline 씬 파일 (.splinecode) |
| **캐릭터 소스** | Spline 에디터 직접 제작 또는 Spline Community 에셋 |
| **인터랙티브** | 마우스 hover/click states, 내장 physics, 이벤트-기반 애니메이션, 시선 추적 |
| **번들 크기** | runtime.js ~300KB + scene.splinecode 2-15MB (씬 복잡도에 따라 변동) |
| **첫 로딩** | 씬 파일이 크면 초기 LCP 영향; lazy 로딩 + placeholder 이미지 필수 |
| **모바일 성능** | Web: GPU 의존성 중간. iOS: Metal 렌더러(native SDK). Android: Vulkan 렌더러(native SDK). 웹 임베드는 복잡한 씬일수록 저사양 기기 부담 |
| **모바일 fallback** | 씬 로딩 실패 시 배경색 + 정적 poster 이미지 자동 fallback 설정 가능 |
| **제어권** | 중간 (Spline 런타임 종속, shader 커스텀 불가, 씬 구조 수정은 에디터에서만) |
| **개발 난이도** | 낮음 (임베드 1줄, Figma 수준 에디터) |
| **디자이너 접근성** | 높음 |
| **비용/제한** | 프리티어: Spline 서버 호스팅(씬 URL 공개). 셀프 호스팅은 Pro 플랜 필요. 2026 기준 월 $12-18 추정 |

**적합한 케이스:** 빠른 prototype, 비개발 배경 디자이너, 셀프 호스팅 불필요할 때

---

### Option C: Pre-rendered Video/Image Sequence + CSS Pointer Parallax (Mobile Fallback)

| 항목 | 내용 |
|------|------|
| **기술 스택** | HTML5 `<video loop muted autoplay playsinline>` + CSS 3D perspective + minimal JS (mousemove 20줄) |
| **캐릭터 소스** | Blender / Spline에서 아이들 애니메이션 렌더 후 WebM/MP4 export |
| **인터랙티브** | 마우스 이동 → CSS `transform: rotate3d` parallax (레이어별 깊이감, 최대 ±10° 느낌) |
| **번들 크기** | WebM 1-3MB (해상도·길이 조절 가능), JS 거의 없음 |
| **첫 로딩** | `preload="none"` + `poster` 이미지로 LCP 완전 보호 |
| **모바일 성능** | 최고 (no GPU computation, hardware video decoding 사용, 배터리 영향 미미) |
| **모바일 fallback** | `poster` 정지 이미지 또는 저해상도 WebP 애니메이션 (500KB 미만 목표) |
| **제어권** | 낮음 (실시간 캐릭터 반응 없음, 고정 루프만) |
| **개발 난이도** | 낮음 (3D 렌더 파이프라인 별도지만, 웹 통합 단순) |
| **디자이너 접근성** | 높음 (렌더 파이프라인만 알면 됨) |

**적합한 케이스:** 모바일 우선 사이트, 성능 예산 타이트한 환경, WebGL fallback 레이어

---

## Sam Samuel 웹 추천

### Prototype Path (최속 ~ 1-2일)
→ **Option B (Spline)**
1. Spline 에디터에서 캐릭터 씬 제작 (또는 Community 에셋 fork)
2. `@splinetool/react-spline` React 컴포넌트로 임베드 (1줄)
3. 배경 canvas: `pointer-events: none`, HUD 레이어: `z-index: 10, pointer-events: all`
4. 씬 로딩 실패 시 배경색 + poster 이미지 fallback 설정
5. 시각적 검증 후 Option A로 업그레이드 결정

### Production Path (장기 제어 우선)
→ **Option A (R3F)**
1. Ready Player Me 또는 구매 캐릭터 GLB 조달
2. Mixamo에서 idle / wave / look 애니메이션 리타겟 (무료)
3. R3F + `useFrame`으로 마우스 추적 IK 구현
4. Draco 압축 + KTX2 texture 적용 (번들 50% 절감)
5. 성능 tier 감지 후 Option C로 자동 fallback

### Mobile Fallback (항상 병행 필요)
→ **Option C (video + CSS parallax)**
- 감지 기준: `prefers-reduced-motion: reduce` OR GPU score < threshold OR viewport < 768px
- WebM loop (2-3MB) + CSS floating 아이들 keyframe + mousemove parallax (JS 20줄)
- iOS Safari: video autoplay는 `muted + playsinline` 반드시 필요

### Desktop Expansion Rule
- Desktop (≥1024px): 캐릭터 viewport 높이 70-80%, 우측 또는 중앙 자유 배치
- Tablet (768-1023px): 캐릭터 50% 높이, 중앙 고정
- Mobile (<768px): Option C fallback 또는 Spline 경량화 버전, 30% 높이 하단 고정

---

## Status 첫 적용 계획

> Status = Sam Samuel 개인 cockpit/대시보드 페이지 (build-11에서 4-card floating 레이아웃 완성)

### Background Layer (z-index: 0)
```css
/* canvas 또는 video 래퍼 */
position: fixed;
top: 0; left: 0;
width: 100vw; height: 100vh;
z-index: 0;
pointer-events: none;
```
- `<canvas>` (Spline/R3F) 또는 `<video loop muted autoplay>` (fallback)
- 캐릭터 위치: 데스크탑 우측 20-30%, 모바일 하단 중앙
- 배경색: `--bg: #f4f2ea` (Quiet Note 팔레트) 또는 다크 테마 기준

### Floating HUD Layer (z-index: 10+)
```css
position: relative; /* 또는 fixed for status cards */
z-index: 10;
pointer-events: all;
/* 기존 Status floating card 유지 */
background: rgba(244, 242, 234, 0.75);
backdrop-filter: blur(8px);
```
- 기존 Status floating card들 그대로 유지
- 투명도 + backdrop-blur로 캐릭터 배경 비침

### Detail Transition Behavior
- **페이지 진입**: 캐릭터 idle 애니메이션으로 등장 (0.5s fade-in canvas)
- **card hover**: 캐릭터 시선이 해당 카드 방향으로 rotate (Spline: state 전환, R3F: bone rotation)
- **카드 클릭/확장**: 캐릭터 wave 또는 표정 변화
- **스크롤**: 캐릭터 viewport sticky 고정, 콘텐츠 이동

---

## 문서화 계획

### DESIGN.md 반영 위치

새 섹션 `## Spatial Presence Layer` 추가:

```markdown
## Spatial Presence Layer

Sam Samuel 웹의 핵심 공간 문법: "캐릭터가 공간의 주인이고, UI는 그 위에 떠 있다."

- background-layer: z-index 0, pointer-events: none, 뷰포트 전체
- hud-layer: z-index 10+, 투명 카드, backdrop-blur
- character-placement:
  - desktop: 우측 자유 배치, 뷰포트 70%+ 높이
  - mobile: 하단 중앙 고정, 30% 높이 또는 video fallback
- pointer-response: 마우스 이동 → 시선/고개 방향 추적 (최대 ±30° 회전)
- fallback-chain: WebGL(A/B) → video(C) → static-poster
```

### DESIGN_SYSTEM.md 반영 위치

새 패턴 `SpatialPresence` 추가:

```markdown
## SpatialPresence Pattern

컴포넌트: <CharacterBackground option="spline|r3f|video" fallback="video|image" />

토큰:
  --character-scale-mobile: 30vh
  --character-scale-desktop: 70vh
  --character-z-index: 0
  --hud-z-index: 10
  --hud-bg: rgba(244,242,234,0.75)
  --hud-blur: blur(8px)

접근성: prefers-reduced-motion 감지 시 정지 이미지로 자동 전환
성능 예산: 첫 3초 내 LCP 영향 없도록 lazy load + poster 이미지 선행
```

### Reusable Skill

- **이름:** `add-3d-character-background`
- **역할:**
  1. 프로젝트 맥락(성능 예산, 기술 스택, 모바일 우선도)으로 옵션(A/B/C) 선택
  2. `<CharacterBackground>` 컴포넌트 또는 vanilla canvas 설정
  3. HUD 레이어 z-index / pointer-events 분리
  4. 모바일 fallback 체인 구성 (video → static image)
  5. DESIGN.md / DESIGN_SYSTEM.md 토큰·패턴 기록
- **입력:** 캐릭터 파일 경로 or Spline URL, 옵션(A/B/C), 타겟 페이지
- **출력:** 작동하는 배경 레이어 + 문서 업데이트

---

## 구현 가능성 요약

| 기준 | Option A (R3F) | Option B (Spline) | Option C (Video) |
|------|---------------|-------------------|------------------|
| 첫 prototype 속도 | 느림 (2-5일) | 빠름 (1-2일) | 빠름 (반일) |
| 모바일 성능 | 중간 (최적화 필요) | 중간 | 최고 |
| 인터랙티브 깊이 | 최고 | 중간 | 낮음 |
| 번들 크기 | 중간 | 큼 (씬 파일) | 작음 |
| 장기 제어권 | 최고 | 낮음 (런타임 종속) | 중간 |
| 권장 역할 | 프로덕션 | Prototype | Mobile fallback |

**최종 추천 경로:**
1. **Prototype**: Option B (Spline) — 즉시 시각적 검증, 1-2일
2. **Production**: Option A (R3F) — build-11 레이아웃 위에 캐릭터 레이어 추가
3. **항상 병행**: Option C (Video fallback) — mobile / reduced-motion

> 참고: YouTube 레퍼런스 영상(dROkEnvxch4) 직접 열람 차단으로 유사 튜토리얼 맥락 기반 분석 적용. 영상이 순수 Three.js 구현이라면 Option A가 더 직접적인 레퍼런스가 됨. 영상을 직접 확인 후 옵션 선택 권장.
