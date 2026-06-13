# Virtue First Successful Output Contract

Source note: `source/external-links/marketing/2026-06-13-agentic-plg-outcome-readable.md`

## Scope

This is a prelaunch, L1 docs-only contract for reading Virtue activation as first successful output rather than UI interaction. It preserves the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.

No product code, public copy, tracking, privacy, pricing, deployment, API, robots/sitemap, external messaging, or cost-bearing change is made here.

## First Successful Output Table

| Job | First successful output event | Screen evidence | Successful output sentence | User next action | Agent-readable quality standard | First-10 manual observation columns |
| --- | --- | --- | --- | --- | --- | --- |
| J1 기록형 | `deed_saved` | Result card is accepted and saved; home/recent record can show the saved deed. | The user has a saved, usable record of a real deed they meant to keep. | Leave it as a record, revisit it, or add another deed later. | The saved item has a concrete deed, a judgment/result, and enough context for a later agent or human to understand why it counted. | output_seen, saved_without_prompting, save_reason_heard, later_reference_possible, confusion_note |
| J2 누적형 | `deed_saved` | Result card is saved and can contribute to cumulative virtue/progress surfaces. | The user has added one deed that can participate in a continuing virtue trail. | Return to the dashboard, notice accumulation, or add a second related deed. | The saved deed is not just a one-off answer; it is durable enough to support continuity, streak/progress interpretation, or future reflection. | output_seen, saved_for_continuity, progress_signal_noticed, next_deed_intent, accumulation_gap |
| J3 AI 호기심형 | `deed_judged` | AI judgment/result card appears after the user asks what the deed means. | The user received a clear AI judgment they can accept, question, reroll, or simply leave with. | Read the basis, compare with their expectation, reroll if needed, or exit without saving. | The judgment is legible as an answer: basis, final choice, and confidence/trust cues are understandable without requiring save. | output_seen, basis_understood, trust_or_doubt_phrase, reroll_or_exit_reason, save_not_required_note |
| J4 회고형 | `deed_saved` | Result card is accepted and saved as material for later reflection. | The user has saved a deed that can be used as future reflection evidence. | Keep it for later review, compare it with past deeds, or add another reflective entry. | The saved output carries enough narrative context to be useful when revisited after time has passed. | output_seen, reflection_value_heard, saved_for_later, context_sufficient, future_question |

## Reading Rule

A first successful output is counted only when the user can point to an outcome they can use next. For J1, J2, and J4, that means the output survives as `deed_saved`. For J3, the useful outcome can be the judgment itself, so `deed_judged` is sufficient and a no-save exit can be normal.

## First-10 Observation Columns

Use these as manual notes, not new analytics fields:

- `job_label`: J1/J2/J3/J4 as inferred from the session.
- `first_success_event`: `deed_saved` for J1/J2/J4, `deed_judged` for J3.
- `screen_evidence`: the exact visible surface that proved the output existed.
- `successful_output_sentence`: one plain sentence describing what the user now has.
- `user_next_action`: save, exit, reroll, revisit, add another deed, or ask for help.
- `agent_readable_quality`: whether another agent could understand the output and its basis.
- `observer_confidence`: low/medium/high qualitative confidence only.
- `do_not_count_reason`: availability block, synthetic/test traffic, unclear job, or no usable output.

## Guardrails

Do not infer paid intent, retention, PMF, or activation rate from the first 10 observations. Do not collapse J3 judged-without-saved into failure. Do not add new tracking, events, public copy, robots/sitemap, API, pricing, privacy, deployment, or cost changes from this contract.
