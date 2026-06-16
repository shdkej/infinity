# build-11 Implementation Plan
> 로컬 Claude Code 실행용 구현 가이드. Cloud Prepare 단계 산출물.

## 목표

`sites/status/dist/index.html`을 3D full-bleed background + floating HUD overlay 구조로 전면 재작성.
build-10의 glass hero card 중심 레이아웃을 버린다.

## 금지 사항

- `sites/travel/dist/travel-data.json` 등 unrelated dirty 파일 수정 금지
- Terraform/새 AWS 리소스 추가 금지
- force-push 금지
- secrets/credentials 변경 금지

## HTML 레이아웃 구조

```html
<body>
  <!-- Layer 0: 3D Full-Bleed Background -->
  <div class="bg-layer">
    <!-- Option A: CSS gradient only (권장) -->
    <!-- Option B: <canvas id="scene"> for Three.js -->
    <!-- Option C: <img src="assets/3d-bg.jpg" style="position:fixed;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;"> -->
  </div>

  <!-- Layer 1: HUD Overlay (모든 UI는 여기에) -->
  <div class="hud-overlay">

    <!-- 상단 얇은 nav rail -->
    <nav class="top-rail">
      <span class="logo">● STATUS</span>
      <span class="score"><!-- data.overall_status --></span>
      <span class="clock"><!-- current time --></span>
    </nav>

    <!-- 우측 상단 compact HUD -->
    <aside class="status-hud">
      <div class="hud-pill healthy"><!-- healthy count --></div>
      <div class="hud-pill degraded"><!-- degraded count --></div>
      <div class="hud-pill down"><!-- down count --></div>
    </aside>

    <!-- 하단 floating tile cluster -->
    <div class="bottom-cluster">
      <!-- Live Checks tiles -->
      <!-- Surfaces tiles -->
      <!-- Agent Lane tiles -->
    </div>

  </div>
</body>
```

## CSS 핵심 규칙

```css
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; }
body { background: #050810; font-family: system-ui, sans-serif; color: #e8eaf0; }

/* Background */
.bg-layer {
  position: fixed; inset: 0; z-index: 0;
  background: linear-gradient(135deg,
    #050810 0%,
    #0a1220 25%,
    #0d1828 50%,
    #091520 75%,
    #060c18 100%);
}
/* 옵션: 추가 깊이감 */
.bg-layer::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 30% 40%, rgba(30,60,120,0.3) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 70%, rgba(10,40,80,0.2) 0%, transparent 50%);
}

/* Overlay container */
.hud-overlay {
  position: fixed; inset: 0; z-index: 10;
  pointer-events: none;
}

/* Top navigation rail */
.top-rail {
  position: absolute; top: 0; left: 0; right: 0; height: 48px;
  background: rgba(5,8,16,0.6);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  display: flex; align-items: center; padding: 0 20px; gap: 16px;
  pointer-events: auto;
}
.logo { font-family: monospace; font-size: 11px; letter-spacing: .2em; color: #4fa3d1; }
.score { margin-left: auto; font-size: 12px; color: #8fa0b0; }
.clock { font-family: monospace; font-size: 11px; color: #6a7a8a; }

/* Compact HUD pills (right side) */
.status-hud {
  position: absolute; top: 60px; right: 16px;
  display: flex; flex-direction: column; gap: 8px;
  pointer-events: auto;
}
.hud-pill {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 8px; padding: 8px 14px;
  font-size: 12px; white-space: nowrap;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}
.hud-pill.healthy { border-color: rgba(80,200,120,0.3); color: #5ec48a; }
.hud-pill.degraded { border-color: rgba(240,180,60,0.3); color: #e8b84a; }
.hud-pill.down { border-color: rgba(220,80,60,0.3); color: #dc5040; }

/* Bottom tile cluster */
.bottom-cluster {
  position: absolute; bottom: 16px; left: 16px; right: 16px;
  display: flex; gap: 10px; overflow-x: auto;
  padding-bottom: 4px;
  pointer-events: auto;
  scrollbar-width: none;
}
.bottom-cluster::-webkit-scrollbar { display: none; }

.tile {
  flex: 0 0 160px; min-height: 80px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px; padding: 12px 14px;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  font-size: 12px; color: #a0aab8;
}
.tile-label {
  font-family: monospace; font-size: 10px; letter-spacing: .1em;
  text-transform: uppercase; color: #5a6a7a; margin-bottom: 8px;
}
.tile-value { font-size: 16px; color: #c8d0dc; font-weight: 600; }

/* Mobile */
@media (max-width: 480px) {
  .status-hud { flex-direction: row; top: auto; bottom: 110px; right: 16px; left: 16px; }
  .hud-pill { flex: 1; text-align: center; }
  .bottom-cluster { bottom: 16px; }
}
```

## JavaScript — status.json 연동

```javascript
async function loadStatus() {
  try {
    const data = await fetch('status.json').then(r => r.json());

    // Top rail score
    document.querySelector('.score').textContent = data.overall_status || 'OPERATIONAL';

    // HUD pills
    const checks = data.checks || [];
    const healthy = checks.filter(c => c.status === 'ok').length;
    const degraded = checks.filter(c => c.status === 'degraded').length;
    const down = checks.filter(c => c.status === 'down').length;
    document.querySelector('.hud-pill.healthy').textContent = `✓ ${healthy} healthy`;
    document.querySelector('.hud-pill.degraded').textContent = `~ ${degraded} degraded`;
    document.querySelector('.hud-pill.down').textContent = `✗ ${down} down`;

    // Bottom cluster — one tile per check
    const cluster = document.querySelector('.bottom-cluster');
    checks.forEach(check => {
      const tile = document.createElement('div');
      tile.className = 'tile';
      tile.innerHTML = `<div class="tile-label">${check.name}</div><div class="tile-value">${check.status.toUpperCase()}</div>`;
      cluster.appendChild(tile);
    });

  } catch (e) {
    console.error('status.json load failed', e);
  }
}

// Clock
function updateClock() {
  document.querySelector('.clock').textContent = new Date().toUTCString().slice(17, 25) + ' UTC';
}
setInterval(updateClock, 1000);
updateClock();
loadStatus();
```

## 검증 게이트

1. Desktop 1440px — 배경 gradient가 viewport 100% 점유, hero card/panel 없음
2. Mobile 390px — top-rail과 bottom-cluster 겹침 없음, hud-pill 가로 배치
3. status.json 데이터 정상 렌더 (healthy/degraded/down 카운트)
4. `python3 scripts/build-status-json.py --resolve-aws --check` 패스
5. Commit & push → S3/CloudFront deploy → 원격 URL HTTP 200 확인

## 완료 후 보고

`reports/build-11/{timestamp}Z-local.html` 작성 필수 (HTML, 결론 2축).
완료되면 build-11 intent status를 `in_progress`로 유지, deploy 확인 후 archived 전환.
