# Virtue Agent-Readable Analytics Context Card

Status: internal analytics context card, docs-only.  
Date: 2026-06-16 10:25 UTC  
Source note: `../source/external-links/marketing/2026-06-16-ai-analytics-semantic-context.md`

## Purpose

This card gives SAM, Infinity, and marketing agents one shared interpretation layer for the first Virtue analytics questions after real or PostHog-accessible usage exists. It is not a dashboard spec, event request, privacy change, public copy change, or launch decision.

## Fixed Event Vocabulary

Use only the already-established Virtue event language when reading first value:

| Event | Agent-readable meaning | Do not infer |
| --- | --- | --- |
| `deed_judged` | A deed reached the AI judgment step. For J3 this can be the first successful output because curiosity about the AI judgment is the job. | Saved value, habit, retention, or user trust. |
| `deed_saved` | A deed was accepted into the user-visible record. For J1, J2, and J4 this is the first successful output candidate. | Long-term habit, PMF, willingness to pay, or quality of the reflection. |
| `level_up_viewed` | The user saw accumulated progress or a level-up moment after saved deeds. | That the level-up caused retention or that the user understood the system. |
| `deed_rerolled` | The user requested another AI framing. | Failure by itself; it may be exploration, dissatisfaction, or unclear output. |
| `deed_save_capped` | A save attempt met the current cap/limit boundary. | Pricing acceptance, monetization intent, or paywall demand. |

No new event names, properties, tracking, dashboard widgets, public claims, or production changes are introduced by this card.

## Exclusion Rules

Before analysis, filter out records that are known or likely to be synthetic:

| Exclusion | Agent rule |
| --- | --- |
| Internal test sessions | Exclude seed data, local/dev runs, QA sessions, and known team accounts. |
| Automation or replay | Exclude scripted browser checks, synthetic telemetry, and repeated verification runs. |
| Broken attribution | Mark as `insufficient_signal` when source, session, or identity is too ambiguous to support a behavioral read. |
| Tiny sample | For first-10 or prelaunch use, describe observed cases. Do not convert them into conversion-rate claims. |

When the filtered sample is too small, the correct output is `insufficient_signal`, not a confident narrative.

## J1-J4 First Value Map

| Job | First value candidate | Supporting read | Agent caution |
| --- | --- | --- | --- |
| J1 recording | `deed_saved` | The user recorded a good deed and accepted it into their log. | `deed_judged` alone is only progress toward value. |
| J2 accumulation | `deed_saved`, then later `level_up_viewed` | The user preserved a deed and may later see accumulation. | Do not treat one level-up view as proof of a loop. |
| J3 AI curiosity | `deed_judged` | The AI judgment itself can satisfy the first curiosity job. | Saving is a second signal, not required for first curiosity value. |
| J4 reflection | `deed_saved` | The user kept a reflected deed for future self-review. | Judgment without saving may be incomplete or exploratory. |

This preserves the existing predecessor mapping: J1/J2/J4 first successful output is `deed_saved`; J3 first successful output can be `deed_judged`.

## First Analysis Sequence

Agents should answer analytics questions in this order:

1. Definition check: confirm the question uses the fixed event vocabulary and the J1-J4 first value map above.
2. Data quality check: remove synthetic/test records and label ambiguous or tiny samples as `insufficient_signal`.
3. Behavior check: compare observed steps against the job-specific first value candidate before discussing activation, retention, PQL, pricing, or acquisition.
4. Boundary check: separate launch-before first-10 manual reads from launch-after cohort reads.
5. Decision check: state whether the result supports look-now learning, a watch item, or no decision.

## Launch-Before Versus Launch-After

| Stage | Allowed read | Hold line |
| --- | --- | --- |
| Launch-before / first-10 | Manual case review, source/job fit, first successful output evidence, quality notes, next action. | No conversion-rate, retention, PQL, pricing, or channel conclusion. |
| Launch-after / cohort | Filtered cohort behavior, repeat value, return windows, activation candidate strength, PQL candidates. | No conclusion if instrumentation, identity, or sample quality is weak. |

## Cap And Limit Interpretation

Treat cap/limit signals as trust and comprehension evidence first, not revenue evidence.

| Signal | Safer read | Unsafe read |
| --- | --- | --- |
| `deed_save_capped` | The user encountered a boundary that may require explanation, product adjustment, or later pricing research. | The user is ready to pay. |
| Cap mentioned in feedback | Possible confusion, frustration, or value-unit question. | Validated pricing page copy. |
| Value before cap | User saw enough value to reach a boundary. | User accepts the current limit. |

## Agent Output Template

When an agent reports on Virtue analytics, use this compact structure:

- `definition_status`: aligned / needs clarification
- `data_quality`: usable / insufficient_signal / excluded_synthetic
- `job_read`: J1 / J2 / J3 / J4 / mixed / unknown
- `first_value_evidence`: event(s) and case notes, not broad claims
- `behavior_change_read`: observed / watch / insufficient_signal
- `forbidden_inferences_avoided`: retention, PQL, pricing, acquisition, or PMF if not supported
- `next_safe_action`: one docs, review, or waiting action

## Verification Notes

- Source note exists: `../source/external-links/marketing/2026-06-16-ai-analytics-semantic-context.md`.
- Conflict markers: none in this artifact.
- Production/code/tracking/privacy/dashboard/public copy/deploy changes: none.
- Existing first-10 and launch-after mapping retained: J1/J2/J4=`deed_saved`; J3=`deed_judged`.
