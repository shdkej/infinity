# M4 Rome recovery evidence

- **Time:** 2026-09-03T14:04:52Z
- **Live build:** Space `777a71e1e21b9ceab90f832fdde5752c0e63c0e5`
- **Renderer:** isolated Snap Chromium CDP using ANGLE/SwiftShader software WebGL.
- **Boundary:** no token, runtime-config body, or token-bearing request URL was read, emitted, or included in this evidence pack.

## Repaired P0

The prior M4 capture is retained as incident evidence: unconstrained Mapbox place search selected a same-name result outside Rome. This build constrains place lookup to the Rome bounding box (`12.25,41.75,12.75,42.10`).

The final observations prove the initial map centre `[12.49640, 41.90280]` and searched place centre `[12.48253, 41.89676]`, both in Rome. The desktop search capture visibly shows Rome labels including Pantheon, Piazza Venezia, Forum of Trajan, and Monument to Vittorio Emanuele II.

## Acceptance observations

For **desktop 1440px** and **mobile 390px**, the machine-readable observations record: one WebGL canvas, `ready: true`, labelled search and layer controls, no horizontal overflow, search at Rome coordinates, pointer pan plus wheel zoom, and a day/night style transition with flipped `aria-pressed`. The no-data message remains visible; no safety rating, route recommendation, or live incident claim is introduced.

`20260903T140452Z-sha256.json` is the SHA-256 manifest for the eight viewport/interaction PNGs and the bounded observation JSON.
