# 3D Interactive Character Background Feasibility

- intent: research-15
- date: 2026-06-18
- scope: Sam Samuel web / Status first application
- reference: https://www.youtube.com/watch?v=dROkEnvxch4

## Reference Handling

The YouTube reference could not be reliably extracted on the server. `yt-dlp` hit YouTube bot confirmation, and `summarize --youtube auto` returned only a generic YouTube platform summary. This artifact therefore treats the reference as a directional visual brief from the intent text: a background character/scene is the primary spatial signal, while buttons and HUD elements float above it.

The practical question is not how to clone the exact video. It is how to get the same product grammar on the web: a character-like spatial layer that feels alive, responsive to viewport/pointer, and subordinate to usable overlay controls.

## Core Scene Principle

The effect should be built as three layers:

1. `scene layer`: full-bleed character or 3D-like visual, fixed to viewport and allowed to dominate the first impression.
2. `interaction layer`: small pointer, scroll, idle, and detail-transition motion that makes the scene feel present without turning the UI into a game.
3. `HUD layer`: compact floating buttons, status rails, and drawers that stay readable and never become big cards over the character.

For Sam Samuel, the character is not decoration. It is the spatial identity of the interface. The UI should feel like it is attached to the scene, not pasted over a marketing hero.

## Options Matrix

| Option | What It Is | Strength | Risk | Best Use |
|---|---|---|---|---|
| A. Full interactive 3D canvas | Three.js or React Three Fiber scene with rigged/animated character, lights, camera, pointer parallax, and responsive camera rules | Highest ownership, real depth, reusable skill can control camera, assets, fallbacks | Highest cost, mobile GPU/battery risk, needs asset pipeline and screenshot/canvas verification | Production flagship once visual language is proven |
| B. Lightweight 3D-like scene / Spline embed | Spline-authored scene embedded as a viewer, or a simple Three.js scene with one optimized GLB and limited motion | Fast prototype, visually close to the desired grammar, lower engineering setup | Spline dependency/export constraints, less control over runtime optimization, possible loading weight | First real prototype for Status or Sam Samuel home |
| C. Pre-rendered video/image sequence + pointer parallax | Render character/scene to WebP/AVIF/video, layer CSS transform/parallax and optional sprite/sequence states | Most reliable, mobile friendly, easiest fallback, works on static pages | Less genuinely interactive, cannot inspect/rotate the character | Status first pass and low-risk production fallback |

## Recommendation

### Prototype Path

Start with C plus a very small interaction layer:

- full-bleed pre-rendered image or short loop
- CSS `object-fit: cover` / `object-position` driven by viewport class
- pointer parallax on desktop only
- reduced-motion fallback to still image
- floating HUD with fixed z-index and strict text-safe zones

This matches the already approved Status direction without forcing a full 3D asset pipeline first.

### Production Path

Move to A when the reusable skill exists and the asset is stable:

- Three.js/R3F with one optimized GLB character
- camera presets: `mobile`, `tablet`, `desktop-wide`
- capped device pixel ratio, preferably `min(devicePixelRatio, 1.5)` or lower on weak devices
- on-demand rendering for mostly static scenes
- animation mixer for idle loops, not React state loops
- screenshot and canvas-pixel verification on desktop and mobile before release

React Three Fiber is a good fit if Sam Samuel web is React-based and the scene needs component composition. Plain Three.js is better if the scene must remain framework-neutral for a reusable skill.

### Mobile Fallback

Mobile should not be a shrunken desktop scene. It should be a composed crop:

- character smaller and anchored lower/center or lower/right
- HUD gets the stable top/bottom zones
- scene motion reduced to idle loop or pointer disabled
- fall back to still image/video if WebGL init, memory, or FPS check fails

## Status First Application Plan

### Background Layer

Use a full-viewport `.scene-root` behind the app chrome:

- `position: fixed; inset: 0; z-index: 0`
- asset fills viewport with responsive object position
- overlay gradient only for readability, not as the main visual identity
- `prefers-reduced-motion` switches to still frame

### Floating HUD / Button Layer

Keep all controls in a separate `.hud-root`:

- `position: relative; z-index: 2`
- compact top status rail
- small floating menu clusters
- no large hero headline card
- no nested UI cards
- stable dimensions for buttons and tiles so live labels do not shift layout

### Detail Transition

When opening a detail:

- desktop: selected HUD item expands into a side drawer while the scene subtly shifts camera/parallax
- mobile: bottom sheet opens and the character remains visible above or behind the sheet
- reduced motion: direct opacity/position transition only

## Documentation Plan

### `DESIGN.md`

Add a section named `Spatial Character Background`:

- the character/scene is the first-viewport identity
- UI floats over it as HUD, not card-first dashboard
- mobile uses intentional crop and simplified motion
- every implementation must include still-image fallback and reduced-motion behavior

### `DESIGN_SYSTEM.md`

Add a product pattern named `Scene + HUD`:

- layer contract: `scene-root`, `scene-scrim`, `hud-root`, `hud-drawer`
- viewport presets for character scale and safe zones
- motion budget: idle, pointer, transition, fallback
- verification checklist: desktop screenshot, mobile screenshot, nonblank canvas/image, overlap check

### Future Reusable Skill

Suggested skill name: `scene-hud-background`

Responsibilities:

- choose `image/video`, `Spline`, or `Three.js/R3F` route by project constraints
- generate responsive scene layout rules
- define safe zones for HUD overlays
- enforce fallback, reduced-motion, and mobile performance gates
- provide Playwright screenshot/canvas verification steps

## Source Notes

- React Three Fiber performance docs emphasize avoiding React state in render loops and using direct mutation/`useFrame` for fast animation paths: https://r3f.docs.pmnd.rs/advanced/pitfalls
- React Three Fiber scaling docs frame WebGL as expensive on weaker devices and recommend performance-aware rendering choices: https://r3f.docs.pmnd.rs/advanced/scaling-performance
- Spline Viewer official docs describe the web component embed route for publishing Spline scenes to websites: https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer
- Three.js documentation exposes renderer pixel ratio control, which matters for mobile performance budgets: https://threejs.org/docs/pages/CanvasTarget.html
- Lottie/web-style animation remains useful for 2D/vector motion and fallbacks, but it does not provide true 3D scene control: https://github.com/airbnb/lottie-web

## Final Recommendation

Use `pre-rendered scene + pointer parallax` for the next Status iteration, then develop a `Three.js/R3F scene + HUD` reusable skill when Sam Samuel needs a living character layer across multiple surfaces. Spline is useful as a fast prototype or designer-owned intermediate, but the durable product grammar should be owned as a code-level scene system with explicit mobile and fallback rules.
