# marketing-80 First Feedback Consistency Audit

Date: 2026-06-23
Scope: Virtue first-session feedback consistency across J1-J4 surfaces
Method: Read-only comparison of existing observations and repo strings only

## Canonical Feedback Source
- J1 home summary card / recent deeds area should describe current saved-state truth, not promise future AI output.
- J2 recent deeds list should mirror whether any deed exists and, when empty, avoid implying hidden progress.
- J3 /add result should carry the forward-looking AI judgment and immediate save outcome.
- J4 post-save return should reinforce that the saved deed now appears in home/recent surfaces.

## Surface Audit

| Surface | Current cue seen in notes/code | Canonical source | Risk | Recommendation |
| --- | --- | --- | --- | --- |
| Home summary card | `612덕` shown while nearby empty-state copy says `아직 비어있어요` | Saved-state summary after at least one deed exists | Same screen can imply both "there is progress" and "nothing exists" | Gate empty-state copy on true saved-deed absence; if aggregate score is shown, nearby status text should acknowledge existing saved activity |
| `최근 덕행` empty state | Empty-state phrasing centers absence | Actual deed list contents | Can contradict summary/proof if any score/progress surface is already populated | Keep empty-state only when both deed list and score/proof surfaces are empty or clearly labeled sample |
| `/add` result | Result surface is the first strong AI feedback moment | Newly judged deed result | Safe if framed as immediate output before save/return | Preserve as primary "what just happened" source; avoid duplicating empty-state language here |
| Save and return to home | User expects saved result to affect home proof surfaces | Persisted deed and refreshed home cards | If refresh lags or copy stays empty, trust drops after first successful action | Treat post-save home as the canonical confirmation point; copy should change from anticipation to confirmation |

## J1-J4 Consistency Table

| Journey | Expected system truth | Copy rule |
| --- | --- | --- |
| J1 first home visit, no deeds | No saved deed yet | Empty-state allowed everywhere if no score/proof surface implies existing activity |
| J2 browse home proof before action | Still no saved deed | Do not mix aggregate/progress numerals with "nothing yet" text unless explicitly marked preview/sample |
| J3 see AI result in /add | One judged result exists, not necessarily saved | Use forward-looking/result copy, not home empty-state copy |
| J4 return after save | At least one saved deed exists | Home/recent surfaces should confirm presence, not absence |

## Contradiction Cases
1. Summary/progress numeral visible while adjacent home proof surface says `아직 비어있어요`.
2. Post-save return still renders the same empty-state wording as pre-save home.
3. `/add` result copy promises a saved/home effect that the return screen does not reflect.

## Safest Next Move
- Resolve home empty-state gating first because it is the only observed contradiction that can invalidate the user's first successful save.
- Keep `/add` result language as the forward-looking moment; make home/recent surfaces the persisted-truth moment.
- If sample/proof placeholders are needed, label them as preview/sample rather than mixing them with true empty-state text.

