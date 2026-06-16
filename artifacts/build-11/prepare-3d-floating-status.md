# build-11: Status 3D Full-Image Floating Menu — 구현 초안

> **Mode**: prepare  
> **Target**: `sites/status/dist/index.html` + `sites/status/dist/assets/`  
> **Repo**: `/home/ubuntu/workspace/space/infra-aws-static-sites`  
> **Prepared by**: Heartbeat Agent 2026-06-16T12:00Z

---

## 설계 방향

| 항목 | build-10 (폐기) | build-11 (목표) |
|------|----------------|----------------|
| 배경 | 작은 wellness 이미지, 장식 역할 | **3D full-bleed** — 화면 전체를 채움 |
| 메뉴 | 독립 섹션/카드 그리드가 전면 | **Fixed overlay** — 위에 살짝 떠 있음 |
| 텍스트 | 큰 serif headline + health card | 최소 텍스트, 스캔 가능한 compact HUD |
| 레이아웃 | hero → panel grid → footer | top nav rail + bottom HUD cluster |

---

## 구현 옵션

### Option A: 정적 3D 래스터 이미지 (권장 — 단순·빠름)

- `sites/status/dist/assets/` 에 3D-feel 이미지 저장
- 이미지 생성 방법 (로컬에서 하나 선택):
  ```bash
  # 방법 A-1: ImageMagick 딥 퍼플 그라디언트
  magick convert -size 1920x1080 \
    -define gradient:angle=140 \
    gradient:"#050510-#1a0535" \
    -blur 0x6 \
    sites/status/dist/assets/status-3d-bg.jpg

  # 방법 A-2: 기존 이미지 어두운 처리
  magick convert sites/status/dist/assets/status-wellness-glass-bg.png \
    -colorize 50,30,70 -modulate 55,60,100 \
    sites/status/dist/assets/status-3d-bg.jpg

  # 방법 A-3: 인터넷에서 고품질 3D/우주/기하학 이미지 다운로드
  # Unsplash 검색어: dark 3d abstract geometric space purple
  ```

### Option B: Three.js 캔버스 배경 (인터랙티브, 추가 JS 필요)

- CDN: `https://cdn.jsdelivr.net/npm/three@0.162.0/build/three.min.js`
- 모바일/데스크톱 canvas nonblank 검증 필수
- 아래 HTML의 Three.js 코드 섹션(주석) 활성화

---

## HTML 전체 구현

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Status — shdkej.com</title>
<style>
/* ── Reset ──────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { height: 100%; }
body {
  width: 100%; height: 100vh;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: #fff;
}

/* ── 3D Full-bleed Background ───────────── */
.bg-layer {
  position: fixed;
  inset: 0;
  z-index: 0;
}
.bg-layer img,
.bg-layer canvas {
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
}
.bg-layer::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center,
    rgba(0,0,0,0.15) 0%,
    rgba(0,0,0,0.55) 100%);
  pointer-events: none;
}

/* ── Floating top nav rail ──────────────── */
.nav-rail {
  position: fixed;
  top: 18px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 200;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 20px 7px 14px;
  background: rgba(255,255,255,0.07);
  backdrop-filter: blur(14px) saturate(1.5);
  -webkit-backdrop-filter: blur(14px) saturate(1.5);
  border: 1px solid rgba(255,255,255,0.11);
  border-radius: 40px;
  font-size: 12.5px;
  font-weight: 500;
  letter-spacing: 0.01em;
  white-space: nowrap;
  color: rgba(255,255,255,0.88);
  user-select: none;
}
.status-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #22d17b;
  box-shadow: 0 0 0 2px rgba(34,209,123,0.25), 0 0 8px rgba(34,209,123,0.5);
  flex-shrink: 0;
  animation: pulse 2.5s ease infinite;
}
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 2px rgba(34,209,123,0.25), 0 0 8px rgba(34,209,123,0.4); }
  50%       { box-shadow: 0 0 0 4px rgba(34,209,123,0.1), 0 0 14px rgba(34,209,123,0.6); }
}
.nav-separator { color: rgba(255,255,255,0.28); }
#overall-label { color: rgba(255,255,255,0.58); font-size: 11.5px; }

/* ── Bottom HUD cluster ─────────────────── */
.hud-cluster {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 200;
  width: min(96vw, 720px);
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 8px;
}

.hud-tile {
  background: rgba(8, 6, 20, 0.42);
  backdrop-filter: blur(18px) saturate(1.3);
  -webkit-backdrop-filter: blur(18px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 14px;
  padding: 13px 14px 14px;
  overflow: hidden;
}
.tile-label {
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.35);
  margin-bottom: 10px;
}
.tile-items { display: flex; flex-direction: column; gap: 5px; }
.tile-item {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: rgba(255,255,255,0.80);
  line-height: 1.3;
}
.item-dot {
  width: 5px; height: 5px;
  border-radius: 50%;
  flex-shrink: 0;
}
.item-dot.ok   { background: #22d17b; }
.item-dot.warn { background: #f59e0b; }
.item-dot.err  { background: #ef4444; }
.item-dot.unk  { background: rgba(255,255,255,0.3); }

/* ── Mobile ───────────────────────────────── */
@media (max-width: 540px) {
  .hud-cluster {
    grid-template-columns: 1fr;
    width: 92vw;
    bottom: 14px;
    max-height: 55vh;
    overflow-y: auto;
    gap: 6px;
  }
  .nav-rail { font-size: 11px; padding: 6px 14px 6px 10px; }
  .hud-tile { padding: 10px 12px 11px; }
}
</style>
</head>
<body>

<!-- 3D Background — Option A: raster image -->
<div class="bg-layer">
  <img src="assets/status-3d-bg.jpg" alt="" aria-hidden="true">
</div>

<!--
Option B: Three.js canvas — swap with the <div> above and uncomment scripts below
<div class="bg-layer">
  <canvas id="three-canvas"></canvas>
</div>
-->

<!-- Floating top nav rail -->
<nav class="nav-rail" aria-label="System Status">
  <span class="status-dot" id="status-dot" aria-hidden="true"></span>
  <span>status.aws.shdkej.com</span>
  <span class="nav-separator" aria-hidden="true">·</span>
  <span id="overall-label">확인 중…</span>
</nav>

<!-- Bottom HUD cluster -->
<div class="hud-cluster" role="region" aria-label="Operations Dashboard">
  <div class="hud-tile">
    <div class="tile-label">Live Checks</div>
    <div class="tile-items" id="live-checks">
      <div class="tile-item"><span class="item-dot unk"></span><span>로딩 중</span></div>
    </div>
  </div>
  <div class="hud-tile">
    <div class="tile-label">Surfaces</div>
    <div class="tile-items" id="surfaces">
      <div class="tile-item"><span class="item-dot unk"></span><span>로딩 중</span></div>
    </div>
  </div>
  <div class="hud-tile">
    <div class="tile-label">Agent Lane</div>
    <div class="tile-items" id="agent-lane">
      <div class="tile-item"><span class="item-dot unk"></span><span>로딩 중</span></div>
    </div>
  </div>
</div>

<!--
Option B: Three.js — uncomment if using canvas background
<script src="https://cdn.jsdelivr.net/npm/three@0.162.0/build/three.min.js"></script>
<script>
(function initThree() {
  const canvas = document.getElementById('three-canvas');
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(window.innerWidth, window.innerHeight);
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x04020e);
  const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 0, 5);
  const geo = new THREE.IcosahedronGeometry(2.0, 5);
  const mat = new THREE.MeshStandardMaterial({ color: 0x2a1060, metalness: 0.85, roughness: 0.15 });
  const sphere = new THREE.Mesh(geo, mat);
  scene.add(sphere);
  const ringGeo = new THREE.TorusGeometry(2.8, 0.06, 8, 80);
  const ringMat = new THREE.MeshStandardMaterial({ color: 0x6633cc, metalness: 0.7, roughness: 0.3 });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = Math.PI / 3;
  scene.add(ring);
  scene.add(new THREE.AmbientLight(0x110022, 3));
  const dl1 = new THREE.DirectionalLight(0x7744ff, 6); dl1.position.set(3, 4, 2); scene.add(dl1);
  const dl2 = new THREE.DirectionalLight(0xff44aa, 3); dl2.position.set(-3, -2, 1); scene.add(dl2);
  let t = 0;
  (function animate() {
    requestAnimationFrame(animate);
    t += 0.004;
    sphere.rotation.y = t * 0.6;
    sphere.rotation.x = Math.sin(t * 0.3) * 0.15;
    ring.rotation.z = t * 0.25;
    renderer.render(scene, camera);
  })();
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
})();
</script>
-->

<script>
function cls(status) {
  const s = (status || '').toLowerCase();
  if (['ok','healthy','operational','up','green'].includes(s)) return 'ok';
  if (['warn','warning','degraded','partial'].includes(s)) return 'warn';
  if (['err','error','down','critical','fail','failed'].includes(s)) return 'err';
  return 'unk';
}
function renderItems(elId, items, nameKey, statusKey) {
  const el = document.getElementById(elId);
  if (!el || !items || !items.length) return;
  el.innerHTML = items.slice(0, 6).map(item => {
    const name = item[nameKey] || item.name || '?';
    const st = cls(item[statusKey] || item.status);
    return `<div class="tile-item"><span class="item-dot ${st}" aria-hidden="true"></span><span>${name}</span></div>`;
  }).join('');
}
async function loadStatus() {
  try {
    const res = await fetch('status.json');
    if (!res.ok) throw new Error(res.status);
    const data = await res.json();
    renderItems('live-checks', data.checks || data.live_checks || [], 'name', 'status');
    renderItems('surfaces',    data.surfaces || [],                     'name', 'status');
    renderItems('agent-lane',  data.agent_lane || data.agents || [],    'name', 'status');
    const allItems = [
      ...(data.checks || data.live_checks || []),
      ...(data.surfaces || []),
      ...(data.agent_lane || data.agents || [])
    ];
    const allOk = allItems.every(i => cls(i.status) === 'ok') || allItems.length === 0;
    document.getElementById('overall-label').textContent =
      allOk ? 'All Systems Operational' : 'Degraded';
    if (!allOk) {
      const dot = document.getElementById('status-dot');
      dot.style.background = '#f59e0b';
      dot.style.boxShadow = '0 0 0 2px rgba(245,158,11,0.25), 0 0 8px rgba(245,158,11,0.5)';
    }
  } catch(e) {
    document.getElementById('overall-label').textContent = 'Status 확인 중';
    console.warn('status.json load failed:', e);
  }
}
loadStatus();
</script>
</body>
</html>
```

---

## 로컬 실행 순서

```bash
cd /home/ubuntu/workspace/space/infra-aws-static-sites

# 1. 배경 이미지 생성 (Option A)
magick convert -size 1920x1080 \
  -define gradient:angle=140 \
  gradient:"#050510-#1a0535" \
  -blur 0x6 \
  sites/status/dist/assets/status-3d-bg.jpg

# 2. index.html을 위 HTML로 전체 교체

# 3. status.json 재생성
python3 scripts/build-status-json.py --resolve-aws --check

# 4. 로컬 검증
python3 -m http.server 8123 --directory sites/status/dist

# 5. 스크린샷
chromium --headless --screenshot=/tmp/status-desktop.png \
  --window-size=1440,1100 http://localhost:8123
chromium --headless --screenshot=/tmp/status-mobile.png \
  --window-size=390,844 http://localhost:8123

# 6. 확인 후 커밋
git add sites/status/dist/index.html sites/status/dist/assets/ sites/status/dist/status.json
git commit -m "build-11: 3D full-bleed background + floating HUD status redesign"

# 7. S3 배포 + CloudFront 무효화 (기존 build-10 절차 동일)
```

---

## 검증 게이트

- [ ] 배경 이미지/canvas가 전체 viewport를 채움 (object-fit: cover)
- [ ] top nav rail이 상단 중앙에 떠 있음 (fixed, translateX(-50%))
- [ ] HUD cluster 3개 타일이 하단에 떠 있음
- [ ] Desktop (1440px): 3D 배경이 첫인상, HUD는 하단에 compact
- [ ] Mobile (390px): 1열 스택, 스크롤 없이 볼 수 있음
- [ ] status.json 데이터 로드 후 dot/label 업데이트 확인
- [ ] `python3 scripts/build-status-json.py --resolve-aws --check` PASS
- [ ] `sites/travel/dist/travel-data.json` 등 unrelated dirty files 미변경

---

## 배경 이미지 대안 (추후 고려)

- Three.js Option B 코드가 주석으로 포함됨 — 인터랙티브 효과를 원하면 canvas 방식으로 전환
- CSS-only: `background: conic-gradient(...)` + `@keyframes`로 Three.js 없이 모션 효과 가능
- Unsplash 3D abstract dark purple 이미지 사용 시 저작권 표기 필요
