# PLG Signal Hierarchy — Virtue Prelaunch Synthesis Note

> Source type: synthesis from Virtue's own prelaunch constraint and established PLG activation frameworks.
> References: marketing-55 (activation measurement contract), marketing-56 (first reliable value columns), marketing-57 (value unit + limit trust), marketing-58 (first successful output contract).
> Created: 2026-06-14 by Heartbeat Agent for marketing-59.

## Core PLG Signal Hierarchy Concept

PLG (Product-Led Growth) signal hierarchy organizes user behavior signals by when they become observable and actionable:

1. **Activation signals** — Did the user hit their first moment of value? Observable in session 1.
2. **Engagement signals** — Do they return and go deeper? Needs 3–7 day window.
3. **PQL signals** — Are they likely to pay? Needs weeks of usage data (20–50 users).
4. **Expansion signals** — Do they spread to others? Needs months (50+ users).

For prelaunch contexts with <10 users, only activation signals are statistically meaningful. Engagement, PQL, and expansion signals should be observed but not acted on.

## The "First Win" Problem in Prelaunch

"First win" or "first value moment" is the PLG activation event. For Virtue:
- The first win must be something the user can point to afterward.
- For J1/J2/J4: `deed_saved` is the pointing moment (a record that survives the session).
- For J3: `deed_judged` is sufficient — the AI output itself is the value, and a no-save exit can be normal.

## PQL in Prelaunch

PQL (Product Qualified Lead) signals require a usage baseline to compare against. With <10 users:
- No comparison baseline exists.
- PQL scoring is premature.
- Focus on qualitative observation, not quantitative thresholds.

## The Measurement-Too-Early Trap

At prelaunch, measuring the wrong thing produces noise that looks like signal:
- Conversion rate from <10 sessions is not a rate — it's an anecdote.
- Churn rate without a return-baseline is a category error.
- "Activation rate" from first-10 is an observer note, not a KPI.

The discipline is to name what you're observing (activation) vs. what you're deferring (engagement, PQL, expansion) — and not collapse the distinction under pressure to show metrics.

## Signal Timing Reference Table

| Signal tier | Earliest observable | Minimum useful sample | Prelaunch action |
|-------------|--------------------|-----------------------|------------------|
| Activation  | Session 1          | 1 (qualitative)       | Observe + iterate |
| Engagement  | Day 3–7            | 5–10 sessions         | Observe only     |
| PQL         | Week 2–4           | 20–50 users           | Defer entirely   |
| Expansion   | Month 1–3          | 50+ users             | Defer entirely   |

## Source Limitation Note

This note synthesizes Virtue-specific context with established PLG frameworks (activation-first, PQL timing, expansion horizon). No single external document is cited; the signal hierarchy is derived from the constraint structure of Virtue's prelaunch jobs (J1–J4) and the prior marketing contracts in this series.
