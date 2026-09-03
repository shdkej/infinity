# Focused Red — M4 Rome recovery

**Verdict: PASS (M4 recovery scope only)**  
**Reviewed:** 2026-09-03T14:06:00Z

## Evidence checked

1. SHA-256 manifest validates all eight `20260903T140452Z` PNG captures plus the observations JSON.
2. Desktop 1440px and mobile 390px show a live WebGL canvas, labelled search/layer controls, no horizontal overflow, search, pan/zoom, and day/night transitions.
3. The Rome P0 is repaired: source build `777a71e1e21b9ceab90f832fdde5752c0e63c0e5` constrains search to `12.25,41.75,12.75,42.10`; initial `[12.49640, 41.90280]` and searched `[12.48253, 41.89676]` centres are within Rome. The desktop capture visibly shows Rome geometry and labels.
4. Live HTTPS `/` and `/app.js` returned 200, and the live app hash matched the evidence build.
5. The UI preserves `no-data` safety language: it has no safety rating, route recommendation, or live-incident claim. Runtime config is referenced but its token material is absent from source and evidence.

## Scope boundary

This is a focused M4 quality pass—not an Archive authorization. The intent stays Active until remaining lifecycle, remote-proof, and immutable original-thread terminal delivery gates are satisfied.
