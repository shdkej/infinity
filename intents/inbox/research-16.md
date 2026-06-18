# research-16: Parsed 3D Character Stage Implementation Options

- id: research-16
- status: inbox
- projects: [personal-ops, infinity, design-system]
- task_type: research
- topics: [3d-background, interactive-character, spline, unicorn-studio, threejs, skill]
- owner: Infinity
- display_name: Parsed 3D Character Stage Implementation Options
- created_at: 2026-06-18T07:15Z
- source: user asked SAM to parse YouTube because Infinity could not parse it directly
- reference_url: https://www.youtube.com/watch?v=dROkEnvxch4
- prepared_input:
  - artifacts/research-16/youtube-reference-parse.md

## Why This Replaces research-15

`research-15` produced a useful implementation matrix, but it explicitly recorded that the YouTube reference could not be reliably extracted and treated the video only as a directional brief.

For this follow-up, SAM parsed the video directly with Gemini video understanding and saved the reference notes as prepared input. Infinity should use the parsed reference rather than re-attempting server-side YouTube extraction.

## Parsed Reference Summary

The video is about a repeatable "next level website" workflow. The parts relevant to Sam Samuel's 3D background interaction are:

1. Figma is used for stylescapes rather than conventional wireframes.
2. AI image generation is used to create a 3D-looking hero asset, such as a black marble statue.
3. Spline is used to bring the 3D object into an interactive web layer and make it respond to the cursor.
4. Unicorn Studio is used to add animated background texture, atmosphere, FBM-like motion, grain, and brand-color mixing.
5. The important lesson is not "copy these tools"; it is the pipeline: visual direction first, generated 3D asset second, interaction layer third, atmospheric background fourth.

## Research Questions

1. For Sam Samuel, which implementation route best matches the new `CharacterStage / FloatingHUD` design-system pattern?
2. Can the Spline + Unicorn Studio approach be used directly, or should we implement a code-owned equivalent with Three.js/R3F and CSS/canvas fallback?
3. What is the simplest production-safe version for Status first?
4. What should the future reusable skill generate: assets, code scaffold, motion rules, or verification gates?
5. How should mobile placement differ from desktop placement?

## Output Contract

Create one artifact under `artifacts/research-16/` that includes:

- video reference interpretation grounded in `youtube-reference-parse.md`
- option matrix:
  - Spline + generated 3D asset
  - Unicorn Studio / animated texture layer
  - Three.js/R3F owned implementation
  - pre-rendered image/video sequence + pointer parallax
- Status-first recommendation
- reusable skill outline:
  - inputs
  - generated files
  - required verification
  - fallback rules
- decision: direct implementation now vs simpler staged prototype

## Boundaries

- Do not try to re-parse YouTube again unless needed.
- No production implementation.
- No deploy.
- No paid signup.
- No public posting.
- No Status code changes without a separate implementation intent.
