# M4 renderer recovery evidence

- **Time:** 2026-09-03T13:55:02Z
- **Renderer:** existing isolated Snap Chromium CDP profile with ANGLE/SwiftShader software WebGL; the prior managed-profile timeout remains incident evidence and was not deleted or rewritten.
- **Live target:** `https://safety-map.aws.shdkej.com/`
- **Space source:** `a2136aa7bd370d447d276825b8c28dc6372f068b`
- **Safety:** this pack contains no runtime-config contents, token values, or request URLs.

Both 1440px desktop and 390px mobile show one WebGL Mapbox canvas, a place/road-context success message, labelled search and style controls, and no horizontal overflow. The captured sequence is: search for `Trevi Fountain`, pointer pan plus wheel zoom, then the real day/night style control. The style control `aria-pressed` state flips and the live status says that only map presentation changes—not safety signals.

The paired `20260903T135502Z-observations.json` and `20260903T135502Z-sha256.json` are the bounded non-secret inventory and SHA-256 manifest for the eight PNG captures.
