# T3 isolated-renderer recheck — partial evidence

- captured_at: `2026-09-04T07:46:13Z`
- renderer: fresh isolated Snap Chromium profile, ANGLE SwiftShader software WebGL, CDP port `19304`
- source: live `https://safety-map.aws.shdkej.com/`

## Observed interaction state

`observations.json` records, for desktop 1440px and mobile 390px:

- one Mapbox canvas with WebGL context;
- labelled search and layer controls;
- no horizontal overflow at both viewports;
- search output transition;
- pan/zoom event path retaining a canvas;
- layer control transition from `aria-pressed=false` / “야간 지도 보기” to `aria-pressed=true` / “주간 지도 보기”, with the corresponding no-data-safe status message.

## Capture integrity limitation

All four screenshots for a given viewport have the same SHA-256 despite the DOM-observed state transitions. The current CDP screenshot path therefore does not independently demonstrate a visible search/pan/style delta. This artifact is **partial T3 evidence**, not T3 completion or Red-pass evidence.

The raw PNGs, `observations.json`, and `sha256.json` remain immutable under this directory for a follow-up renderer/capture method. No Mapbox token value was read, retained, or logged.
