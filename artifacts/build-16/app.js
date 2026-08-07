const canvas = document.querySelector('#previewCanvas');
const ctx = canvas.getContext('2d');
const W = canvas.width;
const H = canvas.height;
const els = {
  assetInput: document.querySelector('#assetInput'), headline: document.querySelector('#headline'),
  caption: document.querySelector('#caption'), fontSelect: document.querySelector('#fontSelect'),
  positionSelect: document.querySelector('#positionSelect'), exportPng: document.querySelector('#exportPng'),
  exportVideo: document.querySelector('#exportVideo'), assetStatus: document.querySelector('#assetStatus'),
  templateLabel: document.querySelector('#templateLabel')
};
const state = { template: 'photo', source: null, objectUrl: null, animationFrame: null };
const templates = {
  photo: { label: 'Photo Hook', overlay: 'none', titleColor: '#fffdf1', titleSize: 104, stroke: 8, subtitleColor: '#fffdf1' },
  shade: { label: 'Soft Shade', overlay: 'shade', titleColor: '#fff9d8', titleSize: 100, stroke: 3, subtitleColor: '#fff9d8' },
  editorial: { label: 'Editorial', overlay: 'editorial', titleColor: '#f7f4e9', titleSize: 86, stroke: 0, subtitleColor: '#d8ff59' }
};
const fonts = {
  a2z: { family: 'A2Z', style: 'italic', weight: 900 },
  chosun: { family: 'ChosunGu', style: 'normal', weight: 400 },
  nanum: { family: 'NanumSquareNeo', style: 'normal', weight: 400 }
};
function makeSample() {
  const c = document.createElement('canvas'); c.width = W; c.height = H;
  const x = c.getContext('2d'); const g = x.createLinearGradient(0, 0, W, H);
  g.addColorStop(0, '#dcb28b'); g.addColorStop(.28, '#78665d'); g.addColorStop(.63, '#2d4648'); g.addColorStop(1, '#111816');
  x.fillStyle = g; x.fillRect(0, 0, W, H); x.fillStyle = 'rgba(255,225,163,.45)';
  x.beginPath(); x.arc(770, 460, 240, 0, Math.PI * 2); x.fill(); x.fillStyle = 'rgba(18,26,28,.9)';
  x.beginPath(); x.moveTo(0, 1120); x.lineTo(230, 820); x.lineTo(385, 1040); x.lineTo(560, 710); x.lineTo(880, 1100); x.lineTo(1080, 870); x.lineTo(1080, H); x.lineTo(0, H); x.closePath(); x.fill();
  return c;
}
function source() { return state.source || makeSample(); }
function fitCover(s) {
  const sw = s.videoWidth || s.naturalWidth || s.width; const sh = s.videoHeight || s.naturalHeight || s.height;
  const scale = Math.max(W / sw, H / sh); const dw = sw * scale; const dh = sh * scale;
  ctx.drawImage(s, (W - dw) / 2, (H - dh) / 2, dw, dh);
}
function textLines(text, size, family, weight, maxWidth, maxLines) {
  const raw = text.replace(/\r/g, '').split('\n').map(v => v.trim()).filter(Boolean);
  const result = [];
  ctx.font = `${weight || 400} ${size}px ${family}`;
  raw.forEach(line => {
    let current = '';
    [...line].forEach(char => {
      const candidate = current + char;
      if (current && ctx.measureText(candidate).width > maxWidth) { result.push(current); current = char; } else current = candidate;
    });
    if (current) result.push(current);
  });
  return result.slice(0, maxLines);
}
function drawText(text, y, options) {
  if (!text.trim()) return;
  let size = options.size; let lines;
  const maxWidth = W - 150;
  do { lines = textLines(text, size, options.family, options.weight, maxWidth, options.maxLines || 3); size -= 2; }
  while (lines.some(line => { ctx.font = `${options.style || 'normal'} ${options.weight || 400} ${size}px ${options.family}`; return ctx.measureText(line).width > maxWidth; }) && size > 46);
  ctx.save(); ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.font = `${options.style || 'normal'} ${options.weight || 400} ${size}px ${options.family}`;
  const lineHeight = size * (options.lineHeight || 1.05); const start = y - (lines.length - 1) * lineHeight / 2;
  lines.forEach((line, index) => { const ly = start + index * lineHeight;
    if (options.stroke) { ctx.lineJoin = 'round'; ctx.strokeStyle = 'rgba(0,0,0,.88)'; ctx.lineWidth = options.stroke * 2; ctx.strokeText(line, W / 2, ly); }
    ctx.fillStyle = options.color; ctx.fillText(line, W / 2, ly);
  });
  ctx.restore();
}
function overlay(t) {
  if (t.overlay === 'shade') { const g = ctx.createLinearGradient(0, H * .4, 0, H); g.addColorStop(0, 'transparent'); g.addColorStop(.55, 'rgba(0,0,0,.18)'); g.addColorStop(1, 'rgba(0,0,0,.82)'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }
  if (t.overlay === 'editorial') { ctx.fillStyle = 'rgba(7,10,9,.68)'; ctx.fillRect(58, 78, W - 116, H - 156); ctx.fillStyle = '#d6ef62'; ctx.fillRect(86, 118, 7, 120); }
}
function render() {
  const t = templates[state.template]; ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#090a09'; ctx.fillRect(0, 0, W, H); fitCover(source()); overlay(t);
  const p = els.positionSelect.value; const y = p === 'top' ? H * .21 : p === 'bottom' ? H * .73 : H * .5; const cy = p === 'top' ? H * .38 : p === 'bottom' ? H * .89 : H * .7; const f = fonts[els.fontSelect.value];
  drawText(els.headline.value, y, { ...f, size: state.template === 'editorial' ? 86 : t.titleSize, color: t.titleColor, stroke: t.stroke, maxLines: 3, lineHeight: 1.03 });
  drawText(els.caption.value, cy, { ...f, size: state.template === 'editorial' ? 30 : 32, color: t.subtitleColor, stroke: state.template === 'photo' ? 3 : 0, maxLines: 2, lineHeight: 1.35 });
  els.templateLabel.textContent = t.label;
}
function download(blob, name) { const u = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = u; a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(u), 1000); }
function exportPng() { render(); canvas.toBlob(b => download(b, 'frame-instagram.png'), 'image/png'); }
async function exportVideo() {
  if (!('MediaRecorder' in window) || !canvas.captureStream) { alert('최신 Chrome 또는 Edge에서 영상 저장을 사용할 수 있습니다.'); return; }
  els.exportVideo.disabled = true; els.exportVideo.textContent = '생성 중…'; const type = ['video/webm;codecs=vp9', 'video/webm;codecs=vp8', 'video/webm'].find(v => MediaRecorder.isTypeSupported(v));
  if (!type) { alert('이 브라우저에서 WebM을 지원하지 않습니다.'); els.exportVideo.disabled = false; els.exportVideo.textContent = '영상으로 저장 ↗'; return; }
  const rec = new MediaRecorder(canvas.captureStream(30), { mimeType: type }); const chunks = []; rec.ondataavailable = e => e.data.size && chunks.push(e.data); rec.start(); const start = performance.now();
  await new Promise(resolve => { const tick = now => { render(); now - start < 5000 ? requestAnimationFrame(tick) : resolve(); }; requestAnimationFrame(tick); });
  const stopped = new Promise(resolve => rec.addEventListener('stop', resolve, { once: true })); rec.stop(); await stopped; download(new Blob(chunks, { type: 'video/webm' }), 'frame-instagram.webm'); els.exportVideo.disabled = false; els.exportVideo.textContent = '영상으로 저장 ↗';
}
function loadAsset(file) {
  if (!file) return; if (state.objectUrl) URL.revokeObjectURL(state.objectUrl); state.objectUrl = URL.createObjectURL(file);
  if (file.type.startsWith('video/')) { const v = document.createElement('video'); v.src = state.objectUrl; v.muted = true; v.loop = true; v.playsInline = true; v.addEventListener('loadeddata', () => { state.source = v; v.play(); const loop = () => { render(); state.animationFrame = requestAnimationFrame(loop); }; cancelAnimationFrame(state.animationFrame); loop(); }); }
  else { const im = new Image(); im.onload = () => { state.source = im; cancelAnimationFrame(state.animationFrame); render(); }; im.src = state.objectUrl; }
  els.assetStatus.textContent = `${file.name} · 로컬 소스`;
}
document.querySelectorAll('.template-card').forEach(b => b.addEventListener('click', () => { state.template = b.dataset.template; document.querySelectorAll('.template-card').forEach(x => { const active = x === b; x.classList.toggle('is-selected', active); x.setAttribute('aria-checked', String(active)); }); render(); }));
els.assetInput.addEventListener('change', e => loadAsset(e.target.files[0])); [els.headline, els.caption, els.fontSelect, els.positionSelect].forEach(e => e.addEventListener('input', render)); els.exportPng.addEventListener('click', exportPng); els.exportVideo.addEventListener('click', exportVideo);
document.addEventListener('keydown', e => { if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return; if (['1', '2', '3'].includes(e.key)) document.querySelector(`[data-template="${['photo', 'shade', 'editorial'][Number(e.key) - 1]}"]`)?.click(); if (e.key.toLowerCase() === 'r') { els.positionSelect.value = 'center'; render(); } });
window.addEventListener('beforeunload', () => state.objectUrl && URL.revokeObjectURL(state.objectUrl)); render();
