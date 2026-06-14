# Virtue Launch-Ready PLG Signal Gate

Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`

## Scope

This is a prelaunch, L1 docs-only signal hierarchy for the first 10 Virtue users.
It translates PLG activation framework priorities into Virtue-specific Now/Defer/After-launch categories,
using the J1–J4 first-successful-output contract from marketing-58.

No product code, tracking, privacy, public copy, pricing, deployment, API, external messaging, or cost-bearing change is made here.

## PLG Signal Table

| Signal | Tier | Watch | J-match | Prior source | Notes |
|--------|------|-------|---------|-------------|-------|
| `deed_saved` (first session) | Activation | **Now** | J1/J2/J4 | marketing-58 | Core first-success indicator |
| `deed_judged` (first session) | Activation | **Now** | J3 | marketing-58 | J3 value without save is valid |
| `output_seen` | Activation | **Now** | all | marketing-58 | User observed a result card |
| `saved_without_prompting` | Activation quality | **Now** | J1/J2/J4 | marketing-58 | Organic save = stronger signal |
| `basis_understood` | Activation quality | **Now** | J3 | marketing-58 | Legible judgment = successful J3 |
| `value_unit_heard` | Activation quality | **Now** | all | marketing-57 | User can name what Virtue gave them |
| `limit_trust_signal` | Observation | **Now (observe)** | J3 | marketing-57 | Note trust/doubt; don't optimize yet |
| `cap_copy_risk` | Observation | **Now (observe)** | J3 | marketing-57 | Flag if cap framing causes early dropout |
| `accepted_output` | Activation quality | **Now** | all | marketing-56 | Output was used, not discarded |
| `useful_result_time` | Session quality | **Now (observe)** | all | marketing-56 | How long to first usable result |
| `retry_rejudge_reason` | Friction signal | **Now (observe)** | J3 | marketing-56 | Why reroll? Collect verbally |
| `reproducibility_understanding` | Quality | **Now (observe)** | all | marketing-56 | Does user understand the output basis? |
| `observer_confidence` | Gate meta | **Now** | all | marketing-58 | Low/medium/high; ≥7/10 medium needed |
| `return_to_add_second_deed` | Engagement | **Defer** | J1/J2 | — | Day 3+ window needed |
| `accumulation_signal_noticed` | Engagement | **Defer** | J2 | — | Requires 3+ deed baseline |
| `progress_signal_noticed` | Engagement | **Defer** | J2 | marketing-58 | Dashboard/history confirms continuity |
| `day_2_return` | Retention | **Defer** | all | — | Premature with <10 users |
| `dashboard_or_history_visited` | Engagement | **Defer** | J2/J4 | — | Requires save baseline first |
| `reroll_rate` | Engagement | **Defer** | J3 | — | Compare only after 5+ J3 sessions |
| `return_for_reflection` | Engagement | **Defer** | J4 | — | Week+ horizon for reflection revisit |
| `PQL_score` | Conversion | **After launch** | all | marketing-55 | Needs 20–50 user baseline |
| `paid_conversion_intent` | Conversion | **After launch** | all | marketing-55 | Do not infer from first 10 |
| `viral_coefficient` | Expansion | **After launch** | all | marketing-55 | Weeks to months horizon |
| `referral_mention` | Expansion | **After launch** | all | — | Note verbally; don't measure yet |
| `expansion_goal_signal` | Expansion | **After launch** | J2 | — | Multi-person/team sharing patterns |

## Signal Priority by J-Type

### J1 (기록형 / Recording)
- **Now**: `deed_saved`, `output_seen`, `saved_without_prompting`, `value_unit_heard`, `accepted_output`, `observer_confidence`
- **Defer**: `return_to_add_second_deed`, `day_2_return`
- **After launch**: PQL, viral, referral

### J2 (누적형 / Accumulation)
- **Now**: `deed_saved`, `value_unit_heard`, `accepted_output`, `observer_confidence`
- **Defer**: `accumulation_signal_noticed`, `progress_signal_noticed`, `dashboard_or_history_visited`, `day_2_return`
- **After launch**: expansion, sharing, PQL

### J3 (AI 호기심형 / AI Curiosity)
- **Now**: `deed_judged`, `output_seen`, `basis_understood`, `value_unit_heard`, `limit_trust_signal`, `cap_copy_risk`, `retry_rejudge_reason`, `reproducibility_understanding`
- **Defer**: `reroll_rate`, save-rate for J3 sessions
- **After launch**: PQL, power-user patterns, limit-hit rate

### J4 (회고형 / Reflection)
- **Now**: `deed_saved`, `output_seen`, `accepted_output`, `value_unit_heard`, `observer_confidence`
- **Defer**: `return_for_reflection`, comparative use
- **After launch**: long-term retention, journal-like behavior

## First-10 Manual Review Gate

After each of the first 10 sessions, complete this gate check manually:

### Per-session checklist
- [ ] J-type inferred: J1 / J2 / J3 / J4
- [ ] First success signal: `deed_saved` / `deed_judged` / none
- [ ] `output_seen`: yes / no / unclear
- [ ] `observer_confidence`: low / medium / high
- [ ] `do_not_count_reason` (if applicable): availability_block / synthetic_traffic / unclear_job / no_usable_output

### Aggregate gate (at 10 users)
- [ ] `deed_saved` or `deed_judged` observed in ≥ 8/10 sessions
- [ ] `observer_confidence` ≥ medium in ≥ 7/10 sessions
- [ ] `do_not_count` cases ≤ 3/10
- [ ] `value_unit_heard` verbally in ≥ 5/10 sessions
- [ ] No single J-type dominates completely (signal variety = product breadth)

## What NOT to Measure Now

Per marketing-55 (activation measurement contract):
- PQL score — no baseline exists
- Paid conversion rate — premature
- D7 or D30 retention — no cohort yet
- Viral coefficient — no sharing surface observed
- Churn or expansion metrics — no stable usage baseline

**Do not infer activation rate from first 10.** These are observation + iteration inputs, not statistical conclusions.

## Conflict Check with Prior Contracts

| Contract | Status | Note |
|----------|--------|------|
| marketing-55 | ✅ Compatible | This gate adds signal tier timing; does not change what to count/not count |
| marketing-56 | ✅ Compatible | `accepted_output`, `useful_result_time`, `retry_rejudge`, `reproducibility` columns preserved as "Now" signals |
| marketing-57 | ✅ Compatible | `value_unit_heard` and `limit_trust_signal` placed in "Now (observe)" tier as intended |
| marketing-58 | ✅ Compatible | `deed_saved`/`deed_judged` as primary activation signals preserved; J1–J4 mapping preserved |

conflict marker: 0

## Guardrails

No new tracking events, analytics, privacy changes, public copy, API changes, pricing, deployment, external messaging, or cost-bearing changes. Signal tiers are observer labels for manual review only. Production code/tracking/privacy 변경 0.
