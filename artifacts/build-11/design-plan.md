# build-11: Status 3D Full-Image Floating Menu — Implementation Plan

## Design Decisions

- **3D방식**: Three.js (파티클 필드 + 토러스 낫 오브젝트, 마우스 패럴랙스)
- **배경 렌더러**: `WebGLRenderer { alpha: true }` → canvas가 body 배경 위에 투명하게 fullscreen 렌더
- **Overlay**: `position: fixed; z-index: 10; pointer-events: none` → 인터랙티브 요소만 enable
- **Nav Rail**: 상단 50px, `backdrop-filter: blur(14px)`, 전역 상태 도트 + UTC 시계
- **HUD tiles**: 우측 fixed, Score/Checks/Agents 3개 tile (glassmorphism)
- **Bottom strip**: 하단 fixed, live checks를 가로 스크롤 chip으로 표시
- **status.json**: 기존 feed 구조 유지
- **Three.js**: CDN 대신 `assets/three.min.js` 로컬 복사 권장

## Implementation Steps

1. Three.js r160 최소 번들(`three.min.js`) 다운로드 → `sites/status/dist/assets/three.min.js`
2. 아래 HTML로 `sites/status/dist/index.html` 교체
3. `python3 scripts/build-status-json.py --resolve-aws --check` 실행 → `status.json` 재생성
4. Local Chromium으로 desktop + mobile 스크린샷 검증
5. Three.js canvas가 비어있지 않음을 확인 (로딩 실패 fallback 없을 경우 배경 색으로 확인)
6. `sites/travel/dist/travel-data.json` 등 unrelated dirty file 스테이징 금지
7. 커밋 → S3/CloudFront 배포 → `https://status.aws.shdkej.com` 접속 확인

## Boundaries

- No touch: `sites/travel/dist/travel-data.json`
- No Terraform/new AWS resources
- No force-push
- No secrets or credential changes

## Full index.html Code

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Status — Operations</title>
  <script src="assets/three.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #050a14; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", sans-serif; color: #fff; }

    /* 3D Canvas — fullscreen background */
    #scene {
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      z-index: 0;
    }

    /* Everything floats above the 3D scene */
    .hud { position: fixed; inset: 0; z-index: 10; pointer-events: none; }
    .hud * { pointer-events: auto; }

    /* Top navigation rail */
    .nav {
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 50px;
      display: flex; align-items: center;
      padding: 0 20px; gap: 16px;
      background: rgba(5,10,20,0.5);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .nav-brand { font-size: 12px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: rgba(255,255,255,0.9); }
    .nav-dot { width: 7px; height: 7px; border-radius: 50%; flex: none; }
    .nav-dot.ok { background: #4ade80; box-shadow: 0 0 8px #4ade80; }
    .nav-dot.warn { background: #facc15; box-shadow: 0 0 8px #facc15; }
    .nav-dot.err { background: #f87171; box-shadow: 0 0 8px #f87171; }
    .nav-label { font-size: 11px; color: rgba(255,255,255,0.5); letter-spacing: .04em; }
    .nav-spacer { flex: 1; }
    .nav-time { font-size: 11px; color: rgba(255,255,255,0.3); font-variant-numeric: tabular-nums; letter-spacing: .04em; }

    /* Right-side HUD tiles */
    .hud-right {
      position: absolute;
      top: 62px; right: 16px;
      display: flex; flex-direction: column; gap: 8px;
      max-width: 180px;
    }
    .tile {
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.10);
      border-radius: 10px;
      padding: 10px 14px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }
    .tile-name { font-size: 10px; text-transform: uppercase; letter-spacing: .1em; color: rgba(255,255,255,0.4); margin-bottom: 4px; }
    .tile-val { font-size: 22px; font-weight: 700; line-height: 1; }
    .tile-sub { font-size: 10px; color: rgba(255,255,255,0.35); margin-top: 3px; }

    /* Bottom strip */
    .bottom-strip {
      position: absolute;
      bottom: 0; left: 0; right: 0;
      padding: 12px 16px;
      background: rgba(5,10,20,0.6);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-top: 1px solid rgba(255,255,255,0.07);
      display: flex; gap: 10px; overflow-x: auto;
    }
    .bottom-strip::-webkit-scrollbar { display: none; }
    .check-chip {
      display: flex; align-items: center; gap: 7px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 8px;
      padding: 7px 12px;
      flex: none;
      white-space: nowrap;
    }
    .check-chip .dot { width: 6px; height: 6px; border-radius: 50%; flex: none; }
    .check-chip .dot.ok { background: #4ade80; }
    .check-chip .dot.warn { background: #facc15; }
    .check-chip .dot.err { background: #f87171; }
    .check-chip .name { font-size: 11px; color: rgba(255,255,255,0.7); }
    .check-chip .ms { font-size: 10px; color: rgba(255,255,255,0.3); }

    @media (max-width: 640px) {
      .hud-right { display: none; }
      .nav { padding: 0 14px; gap: 12px; }
    }
  </style>
</head>
<body>
  <canvas id="scene"></canvas>

  <div class="hud">
    <nav class="nav">
      <span class="nav-brand">Operations</span>
      <span class="nav-dot ok" id="global-dot"></span>
      <span class="nav-label" id="global-label">Systems OK</span>
      <span class="nav-spacer"></span>
      <span class="nav-time" id="clock"></span>
    </nav>
    <div class="hud-right" id="hud-tiles"></div>
    <div class="bottom-strip" id="check-strip"></div>
  </div>

  <script>
    // ── 3D Scene ──────────────────────────────────────────────
    const canvas = document.getElementById('scene');
    const W = () => window.innerWidth, H = () => window.innerHeight;
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.setSize(W(), H());

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(55, W()/H(), 0.1, 80);
    camera.position.set(0, 0, 4);

    // Particle field
    const N = 3000;
    const pos = new Float32Array(N * 3);
    for (let i = 0; i < N * 3; i++) pos[i] = (Math.random() - 0.5) * 18;
    const starGeo = new THREE.BufferGeometry();
    starGeo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    scene.add(new THREE.Points(starGeo,
      new THREE.PointsMaterial({ color: 0x8ab4f8, size: 0.025, transparent: true, opacity: 0.5 })));

    // Torus knot (main 3D hero)
    const torus = new THREE.Mesh(
      new THREE.TorusKnotGeometry(1.2, 0.35, 200, 32),
      new THREE.MeshPhongMaterial({ color: 0x1a3a6e, transparent: true, opacity: 0.35, shininess: 180 })
    );
    scene.add(torus);
    scene.add(new THREE.Mesh(
      new THREE.TorusKnotGeometry(1.2, 0.35, 120, 18),
      new THREE.MeshBasicMaterial({ color: 0x3a6fbe, wireframe: true, transparent: true, opacity: 0.15 })
    ));

    scene.add(new THREE.AmbientLight(0x223366, 3));
    const pt = new THREE.PointLight(0x4488ff, 4, 12);
    pt.position.set(3, 2, 3);
    scene.add(pt);

    let mx = 0, my = 0;
    document.addEventListener('mousemove', e => {
      mx = (e.clientX / W() - 0.5) * 0.8;
      my = (e.clientY / H() - 0.5) * 0.8;
    });

    function animate() {
      requestAnimationFrame(animate);
      torus.rotation.x += 0.003;
      torus.rotation.y += 0.005;
      camera.position.x += (mx - camera.position.x) * 0.04;
      camera.position.y += (-my - camera.position.y) * 0.04;
      camera.lookAt(0, 0, 0);
      renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
      camera.aspect = W() / H();
      camera.updateProjectionMatrix();
      renderer.setSize(W(), H());
    });

    // ── Clock ──────────────────────────────────────────────────
    const clockEl = document.getElementById('clock');
    const tick = () => { clockEl.textContent = new Date().toISOString().slice(11,19) + ' UTC'; };
    tick(); setInterval(tick, 1000);

    // ── Status JSON Feed ──────────────────────────────────────
    fetch('status.json')
      .then(r => r.json())
      .then(data => { renderHUD(data); renderStrip(data); })
      .catch(() => { document.getElementById('global-label').textContent = 'Status unavailable'; });

    function dot(s) { return s === 'ok' ? 'ok' : s === 'warn' ? 'warn' : 'err'; }

    function renderHUD(data) {
      const s = data.summary || {};
      document.getElementById('hud-tiles').innerHTML = [
        { name: 'Score',  val: s.score ?? '—',        sub: 'health' },
        { name: 'Checks', val: s.checks_ok ?? '—',    sub: '/ ' + (s.checks_total ?? '—') + ' OK' },
        { name: 'Agents', val: s.agents_active ?? '—', sub: 'active' },
      ].map(t => `<div class="tile"><div class="tile-name">${t.name}</div><div class="tile-val">${t.val}</div><div class="tile-sub">${t.sub}</div></div>`).join('');

      const gd = document.getElementById('global-dot');
      const st = s.status ?? 'ok';
      gd.className = 'nav-dot ' + dot(st);
      document.getElementById('global-label').textContent = st === 'ok' ? 'Systems OK' : 'Degraded';
    }

    function renderStrip(data) {
      document.getElementById('check-strip').innerHTML =
        (data.checks || []).slice(0, 24).map(c =>
          `<div class="check-chip"><span class="dot ${dot(c.status)}"></span><span class="name">${c.name}</span>${c.ms ? `<span class="ms">${c.ms}ms</span>` : ''}</div>`
        ).join('');
    }
  </script>
</body>
</html>
```

## Note: Three.js Bundle Download

로컬에서 아래 명령으로 three.min.js를 가져온다:

```bash
curl -L https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js \
  -o sites/status/dist/assets/three.min.js
```

또는 npm에서:

```bash
npm pack three@0.160.0
tar xzf three-0.160.0.tgz package/build/three.min.js
cp package/build/three.min.js sites/status/dist/assets/
```
