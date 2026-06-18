# YouTube Reference Parse: 3D Character Stage Workflow

- source: https://www.youtube.com/watch?v=dROkEnvxch4
- parsed_by: SAM
- parse_method: Gemini direct video understanding after `yt-dlp` and generic summarize extraction were blocked or unhelpful
- date: 2026-06-18

## Video Identity

Title detected by parser: `5 TOOLS YOU NEED TO BUILD NEXT LEVEL WEBSITES EVERY SINGLE TIME`

The video presents a website-building workflow around five tools:

1. Figma
2. Magnific / Freepik-style AI image generation
3. Showit
4. Spline
5. Unicorn Studio

## Relevant Workflow For Sam Samuel

The useful reference is not the no-code site builder stack itself. The useful part is the visual production chain:

1. **Stylescape first**
   - The creator uses Figma to explore mood, type, layout, imagery, and the overall visual direction before building the site.
   - This matches Sam Samuel's need to define the stage feeling before choosing Three.js, Spline, or a fallback.

2. **Generate a 3D-like hero asset**
   - The video shows AI image generation being used to create a specific 3D-looking asset, such as a black marble statue.
   - The creator iterates prompts until the object has the right detail and mood.
   - Sam Samuel equivalent: generate or model a warm, living 3D companion/character that can become the background identity.

3. **Bring the object into Spline**
   - The video uses Spline to add 3D interaction to the object.
   - The important interaction described is cursor-reactive movement, compared to eyes or object orientation following the pointer.
   - Sam Samuel equivalent: the background character subtly responds to pointer, focus, status, or page transition.

4. **Add atmospheric motion in Unicorn Studio**
   - The video uses Unicorn Studio to animate background texture, cloud/FBM-like movement, film grain, and brand-color blending.
   - This adds depth and motion behind the 3D object without making the whole site a full game-like scene.
   - Sam Samuel equivalent: warm motion/texture around the character, while foreground HUD controls stay readable.

5. **Process matters more than the individual tools**
   - The creator emphasizes that tools do not fix weak design.
   - The visual direction and process must be solid first.
   - Sam Samuel equivalent: `DESIGN.md` defines the 3D character stage; `DESIGN_SYSTEM.md` defines CharacterStage/FloatingHUD; implementation tools are chosen after that.

## What To Borrow

- A staged pipeline:
  - `stylescape -> generated/modelled character -> interaction layer -> atmospheric background -> web HUD`
- Cursor-reactive 3D object behavior
- Animated texture/background layer as a cheaper way to create life
- Iterative AI asset generation before engineering
- A fallback mindset: not every site needs full custom WebGL at first

## What Not To Borrow Directly

- Do not treat Spline/Unicorn/Showit as required dependencies.
- Do not copy the black marble statue aesthetic literally.
- Do not make the 3D layer a spectacle that hides the first action.
- Do not skip implementation ownership if this becomes a long-term Sam Samuel pattern.

## Implication For Sam Samuel

The simplest faithful version is:

1. Create a distinctive character/stage still or short loop.
2. Add light pointer parallax and idle motion.
3. Layer floating controls as HUD.
4. Use Spline or Unicorn Studio only if they speed up prototyping.
5. Move to code-owned Three.js/R3F only after the character direction is stable.

For Status first, the most realistic implementation is likely:

- pre-rendered character/scene background
- CSS/canvas pointer parallax
- small animated grain/texture layer
- floating HUD cards/buttons
- reduced-motion and still-image fallback

For a reusable skill, the durable output should be a workflow that can choose among:

- generated raster/video stage
- Spline embed prototype
- Three.js/R3F implementation
- fallback and verification gates
