# PLG Signal Hierarchy — Launch-Ready Gate Framework

Source: 2026-06 PLG activation signal hierarchy synthesis
Date: 2026-06-14
Intent: marketing-59

## Core Thesis

Not all PLG signals carry equal weight. A signal hierarchy orders them by confidence and actionability at each growth stage. Treating PQL signals as activation signals, or activation signals as first-win signals, collapses the ladder and makes prelaunch data unusable.

## Signal Ladder

1. **First Win** — User achieves the outcome they came for (qualitative, per-session)
2. **Activation Event** — User completes the core action that predicts return (behavioral anchor)
3. **Habit Formation** — User returns without prompting and completes a second first-win
4. **PQL (Product Qualified Lead)** — Behavioral pattern signals upgrade intent (rate-based)
5. **Paid Conversion** — User transitions to paid tier
6. **Expansion** — User adds seats, upgrades tier, or invites others
7. **Viral Signal** — User-driven referral or organic share

## Prelaunch Positioning

At prelaunch (< 50 real users, no statistical inference), only the first two layers are readable:

- **First Win**: observable per-session without rate or sample size
- **Activation Event**: countable against existing event anchors, no rate judgment yet

PQL, retention rate, paid conversion, expansion, and viral coefficient require:
- statistical sample (typically 100+ unique sessions per segment)
- consistent acquisition channel
- stable product definition

Measuring them before those conditions are met produces noise, not signal.

## Gate Framework (Three Buckets)

| Bucket | Question | Prelaunch action |
|---|---|---|
| 지금 볼 신호 | Does the user achieve a first win? | Count existing event anchors + qualitative note per session |
| 보류할 신호 | Is the user coming back / engaging? | Track but don't judge: no sample, no channel stability |
| Launch 이후 볼 신호 | Is the user a PQL / converting / expanding? | Gate behind launch-after condition; do not compute rates |

## First Win vs Activation Event

- **First Win**: what the user can point to at end of session ("I got X")
- **Activation Event**: what the product records as the user completing the core loop

These two can coincide but are independent. If first win ≠ activation event, the event anchor is wrong.

## Signal Reliability at Prelaunch

| Signal | Reliable at prelaunch? | Why |
|---|---|---|
| First win (qualitative) | Yes | Observable in each session; does not require rate |
| Activation event count | Yes (directional) | Can count against existing anchors; no rate judgment |
| Time to first value | Directional only | Track qualitatively; don't compute TTV rate |
| Signup rate / page views | Context only | Acquisition signal, not value signal |
| Session length / depth | Noisy context | No baseline; don't judge |
| PQL signal | No | Requires rate, repeat behavior, stable sample |
| Retention / return rate | No | Requires cohort, consistent acquisition |
| Conversion rate | No | Requires pricing, plan, paid infrastructure |
| Viral coefficient | No | Requires tracking, public copy, privacy decision |
