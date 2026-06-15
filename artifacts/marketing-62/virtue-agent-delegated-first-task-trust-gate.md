# Virtue Agent-Delegated First Task Trust Gate

## Scope

This is an L1 docs-only artifact for Virtue prelaunch marketing analysis. It translates the source note `source/external-links/marketing/2026-06-15-ai-native-plg-delegation.md` into a first-task trust gate so AI-native activation is not reduced to click completion.

No product code, tracking, privacy setting, dashboard, public copy, pricing, deploy, external message, or cost-bearing action changed.

## Inherited Rules

- From marketing-55: prelaunch first value is read as a first-10 manual observation, not as a launch metric or PQL conclusion.
- From marketing-58: first successful output is job-specific; J1/J2/J4 close at `deed_saved`, while J3 can close at `deed_judged`.
- From marketing-60: a good result, bad result, and next action must be legible to both the human and a later agent reader.
- From marketing-61: cohort, PQL, seven-day return, pricing, and cap conclusions stay launch-after.

## Three Gates

| Gate | Meaning | Read now? | What it prevents |
| --- | --- | --- | --- |
| Click completed | The user reached or completed a UI step such as starting `/add`, requesting a judgment, rerolling, or saving. | Yes, as low-grade interaction evidence only. | Mistaking UI learning for value. |
| Delegated task completed | Virtue produced a job-relevant AI judgment or saved artifact that answers the user's immediate job. | Yes, as first successful output evidence. | Mistaking a raw AI response for trusted activation. |
| Trusted next action | The user accepted, used, explained, saved, rerolled, or calmly ended based on the output in a job-consistent way. | Yes, manually in first-10; quantify later only after launch. | Over-reading `deed_judged` or `deed_saved` without trust context. |

## Job Matrix

| Job | Click completed | Delegated task completed | Trusted next action | First-value event boundary |
| --- | --- | --- | --- | --- |
| J1 기록형 | User starts `/add`, submits a concrete deed, and sees a judgment path. | The deed is judged in a way that can become a record. | User saves because the result is acceptable as a record, or explains why not. | `deed_saved` remains the first value; `deed_judged` alone is a passage point. |
| J2 누적형 | User adds a deed expecting progress, level, or continuity. | The judged deed can be placed into a cumulative path. | User saves while expecting the saved deed to matter later; level/cap confusion is recorded separately. | `deed_saved` remains first value, but trust depends on visible accumulation promise. |
| J3 AI 호기심형 | User requests an AI judgment mainly to see the interpretation. | The judgment itself gives a satisfying or provocative read. | User reads, reacts, rerolls, compares, shares verbally, or exits without saving because the curiosity job is complete. | `deed_judged` can be first value; saving is optional follow-up, not required activation. |
| J4 회고형 | User enters a deed with reflective context or a future-review expectation. | Virtue produces an output worth keeping as a reflection artifact. | User saves because the result can be revisited, annotated mentally, or tied to self-story. | `deed_saved` remains first value; trust is about durability, not only correctness. |

## First-10 Manual Observation Columns

Add these as manual reading columns, not as new tracking events:

| Column | What to write | Example interpretation |
| --- | --- | --- |
| `click_completed` | Which UI action the user completed. | Started `/add`, requested judgment, saved, rerolled, hit cap. |
| `delegated_task_completed` | Whether Virtue completed the job the user implicitly handed over. | "Judged the deed clearly enough", "created a saveable reflection", "only produced a generic score". |
| `trusted_next_action` | What the user did because of the result. | Saved, rerolled, explained the judgment, closed satisfied, closed confused. |
| `trust_gap` | The gap between output existence and acceptance. | "AI answered, but user did not trust it"; "J3 got value without saving"; "save happened mechanically". |
| `job_consistent_close` | Whether the session ended in a way that fits J1-J4. | J3 no-save close can be normal; J1 no-save close needs reason. |

## Misread Guards

- Do not read `add_flow_started` or button progress as activation.
- Do not read all `deed_judged` events as trusted value; only J3 may close there by job logic.
- Do not read all missing `deed_saved` as failure; J3 may end normally after judgment.
- Do not read all `deed_saved` as trust; a mechanical save, confused save, or cap-driven save needs manual context.
- Do not read `deed_save_capped`, delay, 503, or limit friction as pricing or upgrade demand.
- Do not promote first-10 observations into PQL, PMF, conversion, retention, benchmark, pricing, or public copy decisions.

## Verification

- Source note exists at knowledge-lab root: `source/external-links/marketing/2026-06-15-ai-native-plg-delegation.md`.
- Predecessor alignment checked against marketing-55, marketing-58, marketing-60, and marketing-61 archive summaries.
- Conflict markers: 0.
- New product events, tracking properties, dashboard changes, code changes, public copy, deploys, external messages, pricing changes, cost-bearing actions: 0.
