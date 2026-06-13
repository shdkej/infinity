# Virtue Value Unit and Limit Trust Observation Columns

Intent: marketing-57
Scope: L1 docs-only addition to the first-10 observation contract.
Source note: `source/external-links/marketing/2026-06-13-ai-pricing-trust-credits.md`
Lens: AI pricing/credit research shows that hybrid·credit·usage gates function as trust UX even before monetization.

## Guardrails

- Preserve the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Keep as manual observation layer over first 10 sessions. Not product instrumentation.
- Do not add events, properties, timers, tracking, privacy flows, dashboards, session replay, public copy, deployment, external messages, pricing, caps, billing, credits, or cost changes.
- `deed_save_capped` = availability/friction only. Never interpret as upgrade demand, monetization readiness, or value signal.
- Limit reactions are trust calibration data, not pricing intent data.

## Context: Why Value Unit and Limit Trust

AI pricing/credit research (hybrid, credit-based, usage-gate models) shows that even in free tiers, the way users experience their "value unit" (what they get per action) and "limits" (what stops or slows them) shapes trust before any billing discussion begins.

For Virtue prelaunch:
- The value unit question: does the user understand what they "received" from one deed-save or one AI judgment? If they can't name it, they can't evaluate it.
- The limit trust question: when a cap or restriction appears (deed_save_capped, AI result not shown, session ending), does the user read it as a product quality choice, a resource constraint, or arbitrary gatekeeping?

Misreading limit reactions as pricing signals is the key risk. This observation layer prevents that.

## What Changes

Add two column sets to the first-10 manual observation table, after the `Reproducibility understanding` column from `marketing-56`.

### Column Set A: Value Unit

| New manual column | Question to ask or observe | Allowed answer shape | Why it matters |
|---|---|---|---|
| Value unit named | Can the user name what they got from one complete session? | named (deed / record / AI view / reflection) / vague / cannot name / not asked, with user's words | Checks whether the user's mental model of "one value" matches the product's event anchor. |
| Value unit match | Does the user's named value unit match the actual first-value event for their job? | matches (J1/J2/J4: deed_saved; J3: deed_judged) / partial match / mismatch / unclear | Identifies mental model gaps without introducing new metrics. |

**Reading rules:**
- "Value unit named" upgrades confidence that the user can evaluate the product on repeat; it does not create a metric.
- Mismatch does not mean failure — it is a positioning signal. Do not convert to activation rate or PMF score.
- J3: a user who names the AI's output ("I got a reading of my day") is a match even if they did not save.
- J1/J2/J4: a user who says "I saved my deed" or "I recorded what I did" is a match; "I got a score" is a mismatch (judgment frame, not record frame).

### Column Set B: Limit Trust

| New manual column | Question to ask or observe | Allowed answer shape | Why it matters |
|---|---|---|---|
| Limit encountered | Did the user hit any cap, cutoff, delay, or restriction during the session? | yes (type: deed_save_capped / AI not available / session cutoff / other) / no / unclear | Isolates limit events for separate interpretation. |
| Limit read | If a limit was encountered, how did the user interpret it? | quality gate ("the product is careful") / resource cap ("it ran out") / gatekeeping ("they want me to pay") / unexpected / neutral / not asked, with user's words | Distinguishes trust-building reads from trust-eroding reads from monetization-expectation reads. |

**Reading rules:**
- `deed_save_capped` is always availability/friction. Never read as upgrade demand, pricing intent, or value signal ([[Availability And Friction Are Not Value]]).
- "Gatekeeping" reads (user thinks the cap is a paywall signal) are trust calibration data — note them, do not act on them as pricing intent without explicit approval.
- "Quality gate" reads (user thinks the cap means the product is careful or selective) are a positive trust signal worth noting for future copy consideration — proposal-only.
- Limit reactions in prelaunch are directional observations, not decision-grade signals.

## cap/copy 해석 금지선 (Interpretation Boundaries)

The following interpretations are forbidden regardless of what the data shows in first-10 observation:

| Observation | Forbidden read | Allowed read |
|---|---|---|
| User hits `deed_save_capped` | "User wants more → upgrade demand" | "User hit a limit → availability/friction signal" |
| User hits `deed_save_capped` | "User is ready to pay" | "Limit trust read needs context before any inference" |
| User asks "is there a free plan?" | "Monetization conversation is open" | "User has pricing curiosity — note language, do not escalate" |
| User reads limit as "quality gate" | "Users accept the cap = ship the paywall" | "One read = trust signal, not PMF or pricing approval" |
| User reads limit as "gatekeeping" | "Cap is hurting conversion" | "One read = note for future copy candidate (proposal-only)" |
| AI result shown once per session | "User wants multiple results → upsell" | "Session format observation — do not convert to feature demand" |
| No cap hit in session | "Product is healthy / no monetization friction" | "No limit data for this session — observation gap, not signal" |

All pricing, billing, credit, cap policy, public copy, tracking, and deployment changes based on limit observations remain approval-needed.

## Job-Specific Reading

| Job | Value unit (correct match) | Limit trust reading priority |
|---|---|---|
| J1 기록형 | "기록 하나 남겼다" / deed_saved | Cap at save = record was blocked — highest friction signal for J1. |
| J2 누적형 | "쌓이는 시작점 하나" / deed_saved as accumulation start | Cap early in session may disrupt accumulation mental model — note repetition intent. |
| J3 AI 호기심형 | "AI가 읽어준 결과 한 번" / deed_judged (save optional) | Cap at AI result is highly trust-sensitive — "the AI hid the answer" read is a risk. Note framing words. |
| J4 회고형 | "돌아볼 재료 하나 남김" / deed_saved as reflection seed | Cap late in session (after reflection started) may disrupt closure — note emotional tone. |

## How To Use With Existing Notes

Add these columns after `Reproducibility understanding` from `marketing-56`.

Suggested full row order:

| Existing field | Section |
|---|---|
| Job | Keep J1/J2/J3/J4 or unknown. |
| Count now | deed_saved for J1/J2/J4; deed_judged for J3. |
| Expected / Acquired / Blocked / Exit class | marketing-54 reason loop. |
| Accepted output / Useful-result time / Retry or rejudge reason / Reproducibility understanding | marketing-56 reliable value layer. |
| Value unit named / Value unit match | marketing-57 value unit layer (new). |
| Limit encountered / Limit read | marketing-57 limit trust layer (new). |

## Compatibility Check

| Prior artifact | Compatibility |
|---|---|
| `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md` | Compatible. Value unit extends `Accepted output` with naming; limit trust is a new axis not covered by marketing-56. |
| `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md` | Compatible. Preserves count-now boundary; limit observations stay in observe-manually layer. |
| `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md` | Compatible. Extends Blocked column with limit trust type. |
| `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md` | Compatible. §C-2 friction question may surface limit reactions; this layer provides the reading frame. |

## Verification

- Source note path: `../source/external-links/marketing/2026-06-13-ai-pricing-trust-credits.md` (local workspace reference; cloud pass uses contextual knowledge from inbox description).
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Required column sets included: value unit named / value unit match / limit encountered / limit read.
- cap/copy 해석 금지선: 7 interpretation boundaries documented.
- New events, properties, tracking/privacy, dashboard, public copy, deployment, external message, pricing, billing, credit, cap policy, cost changes: 0.
- Conflict markers: 0.

## Assumed Learning Context

### 계승한 기준 (inherited)
- `deed_save_capped` = availability/friction, not value or upgrade demand ([[Availability And Friction Are Not Value]]).
- Trust calibration is by job, not global ([[Trust Calibration By Job]]).
- No autonomous action means risk is self-calibration mismatch, not behavioral harm ([[No Autonomous Action Bounds The Trust Question]]).
- First-value mapping: J1/J2/J4=`deed_saved`, J3=`deed_judged` ([[First Value Mapping]]).
- Prelaunch small samples are directional, not decision-grade ([[Prelaunch Decision Boundary]]).

### 이번에 새로 배운 것 (new this pass)
- Limit reactions in prelaunch have three distinct read types (quality gate / resource cap / gatekeeping) that should be separated before any inference — mixing them produces false monetization signals.
- "Value unit" mental model alignment is observable at the language level ("what did you get?") without any new instrumentation.
- J3 limit trust is highest-risk because "AI hid the answer" framing exists if the cap hits between judged and any follow-up curiosity.

### 다음 작업에 넘길 규칙 (rules for next marketer)
- If first-10 data shows consistent "gatekeeping" reads for limit encounters, flag as copy/trust candidate (proposal-only) — do not escalate to pricing action.
- If value unit mismatch is prevalent (e.g., users naming "score" instead of "record"), flag as positioning/copy candidate for the J1/J2/J4 onboarding frame — proposal-only.
- If J3 limit trust is negative (AI appears to hide output), flag as product-framing candidate, not a billing gate candidate.
- All follow-up actions from these observations remain proposal-only until explicit user approval.
