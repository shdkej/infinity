# Virtue Value Unit and Limit Trust Observation Addendum

Intent: marketing-57  
Date: 2026-06-13 10:07 UTC  
Scope: L1 docs-only. No pricing, billing, credit, cap, tracking, privacy, public copy, deploy, cost-bearing, or product-affecting change.

## Source Read

Local source note confirmed: `../source/external-links/marketing/2026-06-13-ai-pricing-trust-credits.md`.

The pricing and credit materials are used only as a cautionary lens: hybrid, credit, and usage-gate systems can create trust questions before monetization. This document does not recommend a price, a credit ledger, a billing unit, a new cap, or public limit wording.

## Preserved Activation Mapping

The existing first-value event mapping stays unchanged:

| Job | Existing first-value event | Status |
| --- | --- | --- |
| J1 기록형 | `deed_saved` | Keep |
| J2 누적형 | `deed_saved` | Keep |
| J3 AI 호기심형 | `deed_judged` | Keep |
| J4 회고형 | `deed_saved` | Keep |

This addendum adds manual observation columns for the first 10 users only. It must not create product analytics events, pricing rules, dashboard fields, account state, or automated tracking.

## First-10 Observation Columns

Add these candidate columns to the manual first-10 observation table when reviewing sessions or notes:

| Column | What to write | Allowed interpretation | Do not infer |
| --- | --- | --- | --- |
| `value_unit_heard` | The user's own phrase for what felt like the unit of value: one saved deed, one judged reflection, one streak/day, one useful insight, one review moment, or another phrase. | Helps learn whether users frame Virtue by output, time, reflection quality, continuity, or AI feedback. | Do not turn this into pricing, credits, quotas, billing copy, or a metric definition. |
| `limit_trust_signal` | Any moment where a user asks what is limited, what happens after a cap, whether work is saved, or whether AI/usage is being metered. Use direct internal notes, not public copy. | Flags trust questions that may need clearer internal support or later copy review. | Do not change caps, add tracking, expose limits, or promise availability. |
| `cap_copy_risk` | One of: `none`, `confused`, `anxious`, `gaming`, `privacy`, `unknown`, plus a short note. | Separates limit anxiety from normal curiosity. | Do not treat a single risk tag as evidence for removing, raising, lowering, or publicizing a cap. |
| `value_before_limit` | Whether the user reached the preserved first-value event before noticing or asking about a limit: `before`, `after`, `not_observed`, `unknown`. | Checks whether limit attention appears before or after first value. | Do not calculate conversion, willingness to pay, or churn risk from this column. |
| `support_phrase_needed` | Internal draft only: the smallest plain-language explanation that would have reduced confusion in that moment. | Feeds a later copy/support review after enough real examples exist. | Do not publish, A/B test, or ship this phrase from the table. |

## Reading Guardrails

1. Read `value_unit_heard` as user vocabulary, not as a business model.
2. Read `limit_trust_signal` as a trust-support clue, not as proof that current limits are wrong.
3. Keep J1/J2/J4 anchored to `deed_saved` and J3 anchored to `deed_judged` unless a separate approved analytics intent changes the contract.
4. Treat all rows from the first 10 users as qualitative evidence. No percentage threshold, PQL score, paid-conversion claim, or pricing decision is allowed here.
5. If a note would require pricing, billing, credit balance, cap mechanics, privacy/tracking, public copy, or deploy work, move that work to a separate approval-needed intent.

## Example Row Shape

| User | Job | First-value event | value_unit_heard | limit_trust_signal | cap_copy_risk | value_before_limit | support_phrase_needed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U-01 | J3 | `deed_judged` | "one useful judgment" | Asked whether re-judging consumes anything | confused | after | Internal draft only |

## Verification

- Source note existence confirmed.
- Existing J1/J2/J4 = `deed_saved` and J3 = `deed_judged` mapping preserved.
- New product analytics events: 0.
- Pricing, billing, credit, cap, public copy, privacy, deploy, cost-bearing, and product-affecting changes: 0.
