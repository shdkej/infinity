# T3 compositor-visible capture blocker

- intent: `safety-map-experiment-02-20260904`
- recorded_at: `2026-09-04T08:51:00Z`
- status transition: `Active → Waiting`

## Exhausted safe paths

1. Fresh isolated Chromium + software WebGL CDP capture: DOM/WebGL interaction transitions observed, but per-viewport interaction screenshots share one hash.
2. Chrome `fromSurface=false` screenshot variation: same result; no independently visible delta.
3. Direct Computer Control screenshot: unavailable because no connected computer-capable node advertises screen capture/control.
4. Local alternative browser renderer: Firefox, Playwright, and Puppeteer are unavailable.

## Approval boundary

The remaining viable path is an operator-approved Computer Control node capable of screen capture, or another approved compositor-visible renderer. This cannot be enabled by local implementation alone.

## Resume condition

Connect and approve a computer-capable node with screen capture/control, then record actual desktop and 390px visible search, pan/zoom, and layer-delta captures. T3, final Red, terminal receipt, and Archive remain blocked until then.
