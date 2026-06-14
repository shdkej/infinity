# PLG Signal Hierarchy: First Win, Activation, PQL

Source type: Research synthesis  
Date: 2026-06-14  
Referenced by: marketing-59  
Topic: PLG signal priority for prelaunch measurement

## Core Insight

Product-Led Growth measurement is a priority stack. Measuring higher-order signals before establishing lower ones produces noise. The key discipline at prelaunch is to read first win and activation signals while explicitly deferring PQL, conversion, and viral metrics.

## Signal Stack

1. **Acquisition** — signup count, pageview, source attribution  
2. **First Win** — user receives one concrete, usable output in the first session  
3. **Activation** — user understands the core loop and has reason to return  
4. **Retained Value** — user returns unprompted, repeating the core loop  
5. **Product-Qualified Lead (PQL)** — user has experienced enough value to make upgrade intent plausible  
6. **Conversion** — paid plan uptake  
7. **Expansion / Viral** — multi-seat, referral, cross-feature spread

## Prelaunch Rule

With fewer than ~50 users:

- **Do count**: First win events and qualitative activation confirmations  
- **Do observe**: What users say about the value, what they do next  
- **Do not interpret**: Retention rate, cap hits as upgrade intent, PQL labels, viral coefficients, NPS  
- **Do not add**: New tracking, events, pricing, public copy, or deployment changes

## Why Signal Priority Matters

Misreading a cap hit as upgrade intent before pricing is finalized creates false PMF signals. Treating first-session rerolls as churn misclassifies a normal J3 completion. Reading return frequency with 5 users produces a statistically meaningless retention number.

The discipline is to let lower-order signals (first win, activation) stabilize before gating on higher-order signals (PQL, viral).

## Key Distinction: First Win vs Activation

| Stage | Question | Evidence type |
|-------|----------|---------------|
| First Win | Did the user get something useful from one action? | Single output or event |
| Activation | Does the user understand the value loop and have reason to return? | Behavior after first output |

## What to Watch vs What to Skip at Prelaunch

| Signal | Prelaunch stance |
|--------|------------------|
| First win event | ✅ Count now |
| Activation loop observation | ✅ Observe manually |
| Return visit | ⏸ Hold — too few data points to interpret |
| Cap or upgrade trigger | ⏸ Hold — pricing not yet finalized |
| PQL label | 🚫 Launch-after gate |
| Paid conversion | 🚫 Launch-after gate |
| Viral / referral | 🚫 Launch-after gate |
| NPS | 🚫 Launch-after gate |

## Application to Virtue

- Virtue's first win event = `deed_saved` (J1/J2/J4) or `deed_judged` (J3)  
- Activation = user can describe what they received and why it was useful  
- PQL, conversion, expansion, and viral all sit behind launch-after gates  
- First-10 observation should focus on: did the first win happen, and does the user understand what they got?
