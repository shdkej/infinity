# Virtue Early Behavior Intent Sequence Columns

Intent: marketing-64
Scope: docs-only column proposal for existing first-10 activation observation documents.
Source note: `../source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md` (knowledge-lab root; path recorded as stated in intent — cloud-access verification not possible for knowledge-lab repo).
Lens: Mixpanel 2026 PLG behavioral intent signal framing, translated into Virtue prelaunch first-10 observation context.

## Purpose

Single activation events (`deed_saved`, `deed_judged`) tell what happened at a point in time. They do not show why it happened or what the user intended before and after. This document proposes a docs-only column set to record early behavioral sequences alongside existing event anchors in the first-10 manual observation table.

No new events, properties, tracking, privacy flows, dashboards, public copy, deployment, external sending, or cost are introduced.

## The Distinction: Activation Event vs Intent Sequence

| Concept | Definition | Virtue anchor | Scope |
|---|---|---|---|
| Activation event | A single observable moment that signals the user reached first value. | `deed_saved` (J1/J2/J4) or `deed_judged` (J3) | Counts now as the primary metric anchor. |
| Intent sequence | The behavioral pattern before and after the activation event, revealing what the user was trying to accomplish, where they paused, what they skipped, and what they did next. | Manual observation columns (this doc). | Observes manually for prelaunch interpretation. |

The activation event stays as the primary count signal. The intent sequence is a reading aid — it explains the event, not replaces it.

## Early Behavior Sequence Column Bundle

Add the following four manual observation columns to the existing first-10 observation table. These columns apply to all jobs (J1-J4).

| Column | Label | What to record | Interpretation note |
|---|---|---|---|
| `first_explored_feature` | 첫 탐색 기능 | The first screen, action, or feature the user engaged with after entering. | Reveals starting intent. Compare across jobs: J1 users may start at input; J3 users may start at the judgment panel. |
| `stopped_screen` | 멈춘 화면 | The screen or step where the user visibly paused, hesitated, or slowed. | A pause is not failure; it may mark a decision point, confusion, or moment of reflection. Note what the user did next after the pause. |
| `skipped_behavior` | 건너뛴 행동 | Any expected or available action the user bypassed without engaging. | Skipping `deed_reroll` may indicate satisfaction or confusion; skipping the save step after judgment in J1/J2/J4 warrants a manual reason note. |
| `next_action_after_save` | 저장 후 다음 행동 | What the user did immediately after `deed_saved` (or after `deed_judged` for J3 no-save paths). | Strongest behavioral signal. Return, explore more, exit, or pause each imply different value reads. Do not assign retention or habit inference from one session. |

## Column Application by Job

| Job | First value anchor | Key intent sequence lens |
|---|---|---|
| J1 기록형 | `deed_saved` | Did the user navigate directly to input, or explore first? What stopped them before saving? What did they do after saving the deed? |
| J2 누적형 | `deed_saved` | Did the user revisit or add after saving? What did they skip — reroll, level-up, back navigation? Was the save the end or a step? |
| J3 AI 호기심형 | `deed_judged` | What did the user explore before reaching judgment? Did they pause on the judgment result? Did they skip saving — normal for J3 or a quality signal? |
| J4 회고형 | `deed_saved` | Was the entry exploratory or direct? What did the user slow at — phrasing, context, confirmation? What came immediately after saving the reflection? |

## Updated First-10 Observation Row (Proposed Columns)

Existing columns preserved; four new columns added:

| Field | Type | Note |
|---|---|---|
| Job | Existing | J1/J2/J3/J4 or unknown |
| `deed_saved` / `deed_judged` count | Existing | Primary activation anchor — count now |
| Expected vs. acquired value | Existing | From marketing-55 |
| First successful output notes | Existing | From marketing-58 |
| Exit class | Existing | From marketing-54 |
| `first_explored_feature` | **New** | 첫 탐색 기능 — entry intent signal |
| `stopped_screen` | **New** | 멈춘 화면 — friction or decision point |
| `skipped_behavior` | **New** | 건너뛴 행동 — avoidance or clarity signal |
| `next_action_after_save` | **New** | 저장 후 다음 행동 — post-value behavior |

## Constraints

- Do not interpret the sequence as conversion-rate evidence before launch.
- Do not treat `stopped_screen` as churn unless corroborated by exit class.
- Do not treat `skipped_behavior` as confusion without a manual reason note.
- `next_action_after_save` applies to J3 as `next_action_after_deed_judged` when no save occurs.
- Prelaunch only: observe manually for first-10. No dashboards, no automatic tracking.
- Synthetic/test sessions excluded from all sequence reads.

## Predecessor Consistency

| Predecessor | Maintained |
|---|---|
| marketing-55: J1/J2/J4=`deed_saved`; J3=`deed_judged` as activation anchor | ✅ Preserved. Intent sequence columns are additive, not replacement. |
| marketing-56: first reliable value columns | ✅ No conflict. Sequence columns capture before/after; reliability columns capture quality at the event. |
| marketing-57: value unit and limit trust | ✅ No conflict. Sequence columns add behavioral context to cap encounters. |
| marketing-58: first successful output contract | ✅ Preserved. Adds pre/post-event observation, not first successful output redefinition. |
| marketing-59: launch-ready PLG signal gate | ✅ Compatible. New columns extend the manual review table, not the signal gate logic. |
| marketing-60: outcome-readable docs audit | ✅ Compatible. Sequence columns add pre-event and post-event lanes alongside outcome read. |
| marketing-61: launch-after activation cohort boundary | ✅ Compatible. These columns apply only to prelaunch first-10 manual read. |
| marketing-62: agent-delegated first task trust gate | ✅ Compatible. Trust gate uses first task outcome; sequence columns add behavioral path to that read. |
| marketing-63: agent-readable analytics context card | ✅ Compatible. Context card covers event vocabulary and exclusion rules; sequence columns are a manual observation layer, not an event layer. |

## Verification

- Source note path reference: `../source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md` (knowledge-lab root; cloud-access not possible — path recorded as stated in intent).
- First-value mapping preserved: J1/J2/J4=`deed_saved`; J3=`deed_judged`.
- Conflict markers with marketing-55~63: 0.
- New events, tracking/privacy, dashboard, public copy, deployment, external message, cost changes: 0.
- Synthetic/test and prelaunch low-signal boundaries: maintained.
