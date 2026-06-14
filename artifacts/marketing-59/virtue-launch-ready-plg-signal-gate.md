# Virtue Launch-Ready PLG Signal Gate

Intent: marketing-59  
Scope: L1 docs-only prelaunch signal gate  
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`  
Prior contracts: marketing-55 (activation measurement), marketing-56 (observation columns), marketing-58 (first successful output)

## Guardrails

J1/J2/J4 = `deed_saved`; J3 = `deed_judged`. No new events, tracking/privacy, dashboard, public copy, deploy, external messaging, pricing, or cost changes.

## Signal Gate Table

| Signal | Event (existing) | Job | Gate | Action |
|--------|-----------------|-----|------|--------|
| First AI judgment | `deed_judged` | J3 primary, all | ✅ 지금 | Count as first-win proxy for J3 |
| Deed saved | `deed_saved` | J1/J2/J4 primary | ✅ 지금 | Count as first-win anchor per prior contracts |
| Reroll after judgment | `deed_rerolled` | J3, J1 | ✅ 지금 (observe only) | Note reroll reason; do not interpret as churn |
| Level-up view | `level_up_viewed` | J2 | ⏸ 보류 | Progress interest signal; no pattern possible with 10 users |
| Second `add_flow_started` (same session) | `add_flow_started` count | All | ⏸ 보류 | Possible activation depth cue; hold until pattern emerges |
| Return visit / second session | manual note | All | ⏸ 보류 | Qualitatively note; do not compute retention rate |
| Cap hit | `deed_save_capped` | All | ⏸ 보류 | Pricing/plan decisions not approved; note, do not label as upgrade intent |
| Explicit upgrade ask (user verbal) | manual note only | All | ⏸ 보류 | Note verbatim; do not infer from events alone |
| Feature breadth (cross-job use) | manual note | All | ⏸ 보류 | Context signal; requires pattern across ≥5 users |
| Product-qualified lead | none yet | All | 🚫 launch 이후 | Label only after repeated value and pricing/plan approval |
| Paid conversion | none yet | All | 🚫 launch 이후 | No pricing, plan, or paywall scope in this contract |
| Expansion (multi-user) | none yet | All | 🚫 launch 이후 | Account/context evidence required |
| Viral / referral | none yet | All | 🚫 launch 이후 | Tracking/public-copy/privacy decisions required |
| NPS or satisfaction score | none yet | All | 🚫 launch 이후 | Too few data points for reliable interpretation |
| Acquisition (signup, pageview) | various | All | ℹ️ Context only | Record but do not use as activation or health signal |

## Gate Summary

| Tier | Signals | Stance |
|------|---------|--------|
| ✅ 지금 볼 신호 | `deed_saved`, `deed_judged`, `deed_rerolled` (observe) | Count and observe in first-10 |
| ⏸ 보류할 신호 | `deed_save_capped`, `level_up_viewed`, return visit, second session, cross-job, verbal upgrade ask | Record, do not interpret at <10 users |
| 🚫 launch 이후 볼 신호 | PQL, paid conversion, expansion, viral, NPS, retention rate, channel quality | Reopen only after launch or explicit approval |

## First-10 Manual Review Gate

### Review Criteria

For each of the first 10 observed users/sessions, record:

| Column | Allowed input | Rule |
|--------|--------------|------|
| Person # | 1–10 | Sequential identifier only |
| Job | J1 / J2 / J3 / J4 / unknown | If unknown, do not force into job-specific definition |
| Now signal | `deed_saved` / `deed_judged` / neither | Per job mapping above |
| Now gate passed? | yes / no / unclear | Yes only if the expected event fired |
| Hold signals seen | List (cap hit, return, level-up, etc.) | Note only; do not interpret |
| After-launch marker? | yes / no + verbatim quote if yes | Only if user explicitly mentioned upgrade, sharing, or referral |
| Activation read | activated / not activated / unclear | Decision rule below |

### Activation Decision Rule

**Activated**: Now signal fired for the user's job (`deed_saved` for J1/J2/J4; `deed_judged` for J3) AND the observer notes that the user could point to something concrete they received.

**Not activated**: No Now signal fired, OR session ended without a usable output (confusion, blank result, technical failure).

**Unclear**: Now signal fired but observer is uncertain whether the user understood what they received. Flag for second-session observation if possible.

Do not use reroll, cap hit, or return-visit alone to determine activation. These are context signals, not activation gates.

### Hold Interpretation Rule

Hold signals are recorded but not interpreted until:
- A clear pattern exists across ≥5 users, OR
- After launch, OR
- An explicit user-stated behavior (verbal upgrade ask, voluntary referral) triggers qualitative review.

Explicit pricing asks: note verbatim, do not infer plan intent from events alone.

## Integration with Prior Contracts

| Prior contract | Relationship |
|----------------|--------------|
| marketing-55 (Activation Measurement) | This gate extends the count / observe / don't-judge framework by adding an explicit "after launch" third tier |
| marketing-56 (Observation Columns) | First-10 review table columns are compatible with prior observation column definitions |
| marketing-58 (First Successful Output) | "Now" tier anchors (`deed_saved` / `deed_judged`) align with first-successful-output per job |

## Verification

- Source note confirmed: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` ✅
- J1/J2/J4 = `deed_saved`; J3 = `deed_judged`: preserved, no change ✅
- Prior marketing contracts (m55/m56/m58): no conflict, gate extends without overriding ✅
- Conflict markers: 0 ✅
- New events / tracking / privacy / dashboard / public copy / deploy / external message / cost: 0 ✅
