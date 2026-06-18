# build-12: index.html 패치 가이드

**Target:** `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/status/dist/index.html`

---

## Step 1. `<head>` 섹션에 추가

```html
<!-- SpatialPresence: Character Background CSS -->
<link rel="stylesheet" href="assets/spatial-presence.css">

<!-- Poster 이미지 준비 후 preload 추가 (LCP 최적화) -->
<!-- <link rel="preload" as="image" href="assets/character/poster.webp" fetchpriority="high"> -->
```

---

## Step 2. `<body>` 시작 직후 (기존 콘텐츠 앞) 추가

```html
<!-- CharacterStage: z-index 0 background layer, pointer-events: none -->
<div class="character-stage" aria-hidden="true" role="presentation">
  <div class="character-layer depth-near" id="character-bg">
    <!-- Phase 1: Placeholder gradient (poster 이미지 준비 전) -->
    <div class="character-placeholder"></div>

    <!-- Phase 2: 실제 poster 이미지 (준비 후 아래 주석 해제) -->
    <!--
    <picture>
      <source type="image/webp" srcset="assets/character/poster.webp">
      <img src="assets/character/poster.png"
           alt=""
           loading="eager"
           fetchpriority="high"
           width="600" height="900">
    </picture>
    -->
  </div>
  <div class="atmosphere"></div>
</div>
```

---

## Step 3. 기존 HUD 카드 래퍼에 클래스 추가

build-11에서 완성된 floating HUD 카드가 담긴 최상위 div를 찾아 `hud-layer` 클래스를 추가한다.

```html
<!-- 기존 -->
<div class="[기존-클래스]">

<!-- 변경 후 -->
<div class="[기존-클래스] hud-layer">
```

기존 클래스에 이미 `position: relative`와 `z-index >= 10`이 설정되어 있으면 클래스 추가 없이 z-index 값만 확인해도 된다.

---

## Step 4. `</body>` 직전에 parallax JS 추가

```html
<script>
/* Pointer parallax — Option D, ~20줄, 의존성 없음 */
(function(){
  if(window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var layers = document.querySelectorAll('.character-layer');
  if(!layers.length) return;
  var root = document.documentElement;
  var isMobile = window.innerWidth < 640;
  var MAX = isMobile
    ? parseFloat(getComputedStyle(root).getPropertyValue('--parallax-mobile') || '4')
    : parseFloat(getComputedStyle(root).getPropertyValue('--parallax-desktop') || '8');
  document.addEventListener('mousemove', function(e) {
    var cx = window.innerWidth / 2, cy = window.innerHeight / 2;
    var rx = ((e.clientY - cy) / cy) * MAX;
    var ry = ((e.clientX - cx) / cx) * -MAX;
    layers.forEach(function(l) {
      var f = parseFloat(getComputedStyle(l).getPropertyValue('--depth-factor') || '1');
      l.style.transform =
        'rotate3d(1,0,0,' + (rx * f) + 'deg) ' +
        'rotate3d(0,1,0,' + (ry * f) + 'deg)';
    });
  });
})();
</script>
```

---

## Step 5. 검증 체크리스트

- [ ] 브라우저에서 Status 페이지 열기
- [ ] 배경에 placeholder gradient(또는 캐릭터 이미지)가 표시되는지 확인
- [ ] 마우스 이동 시 배경 레이어가 CSS parallax로 반응하는지 확인
- [ ] HUD 카드가 배경 위에 정상 표시 (겹침/가림 없음)
- [ ] DevTools → 390px viewport → 가로 스크롤 없음 확인
- [ ] DevTools → Elements → `.character-stage` z-index=0, HUD z-index≥10
- [ ] OS 접근성 "애니메이션 줄이기" ON → 패럴랙스 정지, placeholder만 표시
- [ ] (이미지 준비 후) LCP ≤ 3s

---

## Step 6. DESIGN.md 추가 내용

`DESIGN.md`의 적절한 위치(예: UI 레이아웃 섹션 끝)에 아래를 추가:

```markdown
## Spatial Presence Layer

Sam Samuel 웹의 핵심 공간 문법: "캐릭터가 공간의 주인이고, UI는 그 위에 떠 있다."

- `background-layer`: z-index 0, pointer-events: none, 뷰포트 전체
- `hud-layer`: z-index 10+, 투명 카드, backdrop-blur
- `character-placement`:
  - desktop: 우측 자유 배치, 뷰포트 75% 높이
  - tablet: 50vh, 우측 10%
  - mobile: 하단 중앙 고정, 30vh, parallax 없음
- `pointer-response`: 마우스 이동 → CSS rotate3d parallax (최대 ±8°)
- `fallback-chain`: video → poster still → placeholder gradient
- `prefers-reduced-motion`: JS parallax 및 video 정지, static placeholder만
```

---

## Step 7. DESIGN_SYSTEM.md 추가 내용

`DESIGN_SYSTEM.md`에 아래를 추가:

```markdown
## SpatialPresence Pattern

컴포넌트: `.character-stage` + `.character-layer` + `.atmosphere`
(CSS-only 기반, JS parallax는 옵션)

### CSS 토큰 (`:root` 선언)

- `--character-z`: `0` — 배경 레이어 z-index
- `--hud-z`: `10` — HUD 카드 z-index
- `--hud-bg`: `rgba(244,242,234,0.75)` — HUD 카드 배경
- `--hud-blur`: `blur(8px)` — HUD backdrop-filter
- `--character-scale-desktop`: `75vh` — 데스크탑 캐릭터 높이
- `--character-scale-tablet`: `50vh` — 태블릿 캐릭터 높이
- `--character-scale-mobile`: `30vh` — 모바일 캐릭터 높이
- `--parallax-desktop`: `8` — 데스크탑 최대 회전각(deg)
- `--parallax-mobile`: `4` — 모바일 최대 회전각(deg)

### 접근성

`prefers-reduced-motion: reduce` → JS parallax 자동 비활성화, video 숨김, placeholder만 표시

### 성능

`will-change: transform` on `.character-layer`  
캐릭터 이미지 준비 후 poster preload 추가 권장 (LCP 보호)
```
