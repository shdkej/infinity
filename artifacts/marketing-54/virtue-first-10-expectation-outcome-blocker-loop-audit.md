# Virtue First-10 Expectation Outcome Blocker Loop Audit

Intent: marketing-54  
Scope: docs-only audit table for first 10 design-user observation and follow-up questions.  
Source note: `source/external-links/marketing/2026-06-11-onboarding-feedback-loop.md` exists at the Knowledge Lab root.

## Guardrails

- Keep the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Do not add events, properties, in-app surveys, tracking, privacy flows, public copy, deployment, external sending, or cost.
- Treat the expectation-outcome-blocker loop as a manual interpretation layer over the first-10 notes, not as product instrumentation.
- Separate normal completion, confused exit, no-value exit, and already-sufficient exit before reading small-number event counts.

## Audit Table

| Job | Current first-value mapping | Expectation question before/at first use | Acquired/outcome question after result | Blocker/exit question | Interpretation protected | Current document fit | Change needed |
|---|---|---|---|---|---|---|---|
| J1 기록형 | `deed_saved` | What did you hope Virtue would help you preserve or make easier to remember from this deed? | After the result, what felt worth keeping enough to save? | If you stopped before saving, was the result wrong, too much work, too private, or already enough as a one-time reflection? | Avoid treating `deed_judged` alone as activation for a record-seeking user. | Fits the first-real-user baseline and the first-10 audience brief; adds the missing reason loop after the save decision. | Add this as a manual note column beside the existing first/second value fields. |
| J2 누적형 | `deed_saved` | What did you expect to accumulate, track, or come back to later? | What did the saved deed make more visible about your progress or pattern? | If you did not save, was the blocker weak accumulation value, unclear level/progress meaning, friction, or already enough without a record? | Avoid over-reading a one-time save as habit value unless the user names a reason to return. | Consistent with baseline repeat-value fields and milestone ladder language. | Keep event mapping unchanged; add return-reason wording to the observation script. |
| J3 AI 호기심형 | `deed_judged` | What were you curious to learn from the AI judgment or wording? | Did the judgment answer the curiosity, surprise you, or give language you could use? | If you left without saving, was that a normal completed curiosity loop, confusion, mistrust, or no useful output? | Prevent judged-minus-saved gap from being misread as failure when curiosity was satisfied. | Directly preserves the J3 exception used by the JTBD and task-completion audits. | Make no-save-normal an explicit manual outcome for J3. |
| J4 회고형 | `deed_saved` | What were you hoping to understand, reframe, or close emotionally? | What part of the result felt true enough to keep or revisit? | If you stopped, was it because the reflection felt complete, not personal enough, emotionally off, or too much effort to save? | Separate complete-without-next-step from no-value or confusion exits. | Extends the guided first-value and self-appropriation tables without changing their events. | Add a follow-up prompt for completion reason when there is no save. |

## First-10 Note Fields

| Field | Manual entry | Why it matters |
|---|---|---|
| Expected | User's own reason for trying Virtue in this session. | Anchors activation against the job, not against a generic event count. |
| Acquired | What the user says they actually got after the AI result. | Distinguishes answer received, task completed, record saved, and emotional closure. |
| Blocked | What stopped the next action, if anything. | Splits friction from normal completion and from already-sufficient exit. |
| Exit class | normal completion / confused exit / value not delivered / already sufficient / friction or privacy concern | Makes small first-10 observations interpretable without adding telemetry. |

## Compatibility Check

- `first-real-user-baseline-template`: compatible; this table adds reason fields to the row-level notes and does not alter first/second value definitions.
- `minimum-viable-audience-brief` and first-10 ask script language: compatible; the added questions stay manual and candidate-facing only when a human is already observing.
- `first-session-jtbd-matrix`: compatible; J1/J2/J4 stay save-led and J3 stays judgment-led.
- `virtue-post-result-self-appropriation-reading-table`: compatible; acquired/outcome wording clarifies whether a post-result behavior is self-appropriation or passive admiration.
- `virtue-guided-first-value-session-audit`: compatible; the loop maps onto first input, AI wait/result, and save/exit stages.
- `virtue-intent-to-task-completion-audit-table`: compatible; expectation/acquired/blocker is the reason layer under intent, AI task, and next action.

## Verification

- Source note path confirmed: yes, at `../source/external-links/marketing/2026-06-11-onboarding-feedback-loop.md` from the Infinity root.
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- New events or properties: 0.
- In-app survey, tracking/privacy, public copy, deployment, external sending, cost, permission changes: 0.
- Conflict markers found in generated files: 0.
