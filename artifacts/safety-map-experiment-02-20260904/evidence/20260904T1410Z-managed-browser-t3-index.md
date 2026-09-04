# T3 managed-browser visible-state evidence

- Captured: 2026-09-04T14:04Z–14:16Z
- Renderer: OpenClaw managed Chromium (`openclaw` profile), Snap Chromium with SwiftShader.
- Recovery: the managed profile's data directory was relocated under `~/snap/chromium/common/` and the original OpenClaw path now resolves to it through a symbolic link. This fixes Snap confinement's `SingletonLock` write denial without changing application or token configuration.
- Target: `https://safety-map.aws.shdkej.com/`
- Secret handling: no token values are included in this index, capture metadata, commits, or logs.

## Acceptance observations

| Viewport | Visible states captured | Accessible state observed |
| --- | --- | --- |
| 1440 × 900 | initial, Trevi Fountain search result, zoom, night-style | one canvas; search value/result `Trevi Fountain`; night control changed to `주간 지도 보기`; `scrollWidth` 1425 ≤ `innerWidth` 1440 |
| 390 × 844 | initial, Trevi Fountain search result, keyboard pan-right, night-style | one canvas; search value/result `Trevi Fountain`; map canvas received keyboard focus for pan; `scrollWidth` = `innerWidth` = 390; night control changed to `주간 지도 보기` |

All PNGs have distinct SHA-256 values in [`sha256.txt`](sha256.txt), which establishes a visible-state delta across each captured interaction. The browser recorded no page errors during the capture sequence.

## Files

### Required desktop viewport

- `desktop-1440-initial.png`
- `desktop-1440-search-trevi.png`
- `desktop-1440-zoom.png`
- `desktop-1440-night-style.png`

### Required mobile viewport

- `mobile-390-initial.png`
- `mobile-390-search-trevi.png`
- `mobile-390-pan-right.png`
- `mobile-390-night-style.png`

### Supplemental pre-resize capture sequence

- `desktop-initial.png`, `desktop-search-trevi.png`, `desktop-zoom.png`, `desktop-night-style.png`

These are retained as recovery diagnostics; the `desktop-1440-*` group is the T3 acceptance evidence.

## Scope boundary

The map proves place and road context only. It does **not** claim a safety score, safe route, incident feed, or time-based risk prediction.
