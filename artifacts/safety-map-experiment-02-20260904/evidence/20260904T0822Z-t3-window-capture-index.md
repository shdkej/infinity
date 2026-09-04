# T3 window-surface capture retry — no visual delta

- captured_at: `2026-09-04T08:22:00Z`
- renderer: fresh isolated Snap Chromium profile, ANGLE SwiftShader software WebGL
- capture variation: Chrome DevTools `Page.captureScreenshot` with `fromSurface=false`

The same desktop and 390px DOM/WebGL interaction flow was replayed against the live app. `observations.json` records canvas/WebGL, search output, pan/zoom, and layer-control state transitions.

The four PNGs for each viewport again have identical SHA-256 hashes. The window-surface variation therefore did not recover a visible state delta, and this artifact must not be used to complete T3 or pass final Red. Raw captures and their hash manifest are retained for incident diagnosis.
