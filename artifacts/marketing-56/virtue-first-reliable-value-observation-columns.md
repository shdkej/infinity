# Virtue First Reliable Value Observation Columns

Intent: marketing-56
Scope: L1 docs-only addition to the first-10 observation contract.
Source note: `source/external-links/marketing/2026-06-12-ai-plg-first-reliable-value.md` at the Knowledge Lab root.
Lens: AI PLG activation should distinguish first use from first reliable value.

## Guardrails

- Preserve the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Keep this as a manual observation layer over the first 10 sessions, not product instrumentation.
- Do not add events, properties, timers, tracking, privacy flows, dashboards, session replay, public copy, deployment, external messages, pricing, caps, or cost changes.
- Treat first reliable value as a quality check on the first-value anchor, not a replacement for it.
- For J3, judged-without-save can remain normal completion. For J1/J2/J4, no-save still needs the manual reason before interpretation.

## What Changes

Add four concise manual columns beside the existing first-10 observation fields from `marketing-54` and `marketing-55`.

| New manual column | Question to ask or observe | Allowed answer shape | Why it matters |
|---|---|---|---|
| Accepted output | Did the user accept the AI result as useful enough for the session's job? | accepted / partially accepted / rejected / unclear, with the user's words | Separates "AI produced a result" from "the user trusted or used the result." |
| Useful-result time | When did the user first appear to get something useful? | before result / at result card / after saving / not reached / unknown | Keeps time-to-value qualitative without adding a timer or event. |
| Retry or rejudge reason | If the user rerolled, rewrote, paused, or left, what reason did they give or show? | curiosity / mismatch / mistrust / unclear wording / privacy / effort / normal enough | Prevents `deed_rerolled` or no-save from being read as either success or failure without context. |
| Reproducibility understanding | Could the user explain when they would use Virtue again for a similar situation? | can explain / vague / cannot explain / not asked, with exact phrasing when available | First reliable value includes whether the user understands how to reproduce the win. |

## Job-Specific Reading

| Job | Existing first-value anchor | First reliable value read | Safe first-10 prompt |
|---|---|---|---|
| J1 기록형 | `deed_saved` | Reliable value is strongest when the saved result is accepted as a record the user would want to keep. | "What made this result worth saving as a record, or what made it not worth saving?" |
| J2 누적형 | `deed_saved` | Reliable value needs both save and a reason to continue accumulating, not just one saved deed. | "What about this saved result would make you add another one later?" |
| J3 AI 호기심형 | `deed_judged` | Reliable value can end at the result card if the user accepts the judgment or language and can say why. Save is optional. | "Did this answer what you wanted to learn from the AI, and would you try it again for a similar curiosity?" |
| J4 회고형 | `deed_saved` | Reliable value is strongest when the user accepts the reflection as true enough to keep or revisit. | "What part felt true or useful enough to keep, and what would make you return to it?" |

## How To Use With Existing Notes

Use these columns after the `Expected / Acquired / Blocked / Exit class` fields from `marketing-54` and the `Count now / Observe manually / Do not judge yet` boundary from `marketing-55`.

Suggested row order:

| Existing field | Then add |
|---|---|
| Job | Keep J1/J2/J3/J4 or unknown. |
| Count now | Keep only `deed_saved` for J1/J2/J4 and `deed_judged` for J3. |
| Expected / Acquired / Blocked / Exit class | Keep as the reason loop. |
| Accepted output | Add user acceptance language. |
| Useful-result time | Add rough observed moment, not a timer. |
| Retry or rejudge reason | Add reason only when it happens. |
| Reproducibility understanding | Add whether the user can explain when they would use it again. |

## Interpretation Rules

- Accepted output upgrades confidence in the event anchor; it does not create a new metric.
- Useful-result time is a note, not a stopwatch. Do not compute time-to-value rates in prelaunch.
- Retry can mean curiosity, distrust, mismatch, or exploration. Read it only with the user's reason.
- Reproducibility understanding is a language signal: the user can say when and why to use Virtue again.
- Do not convert these four fields into tracking properties until after launch and explicit approval.

## Compatibility Check

| Prior artifact | Compatibility |
|---|---|
| `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md` | Compatible. It preserves `count now`, `observe manually`, and `do not judge yet`; this adds observation detail inside `observe manually`. |
| `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md` | Compatible. It extends Expected/Acquired/Blocked with first reliable value quality signals. |
| `artifacts/marketing-53/virtue-intent-to-task-completion-audit-table.md` | Compatible. Accepted output and reproducibility clarify whether "AI task -> next action" was reliable, not merely completed. |
| `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md` | Compatible. These are internal observation columns, not public outreach copy. |

## Verification

- Source note path confirmed: `../source/external-links/marketing/2026-06-12-ai-plg-first-reliable-value.md`.
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Required columns included: accepted output, useful-result time, retry/rejudge reason, reproducibility understanding.
- New events, properties, tracking/privacy, dashboard, public copy, deployment, external message, pricing, cap, and cost changes: 0.
- Conflict markers: 0.
