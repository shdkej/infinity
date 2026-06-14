# PLG Signal Hierarchy: First Win → Activation → PQL → Conversion

> Reference note for marketing-59 (2026-06-14). Captures PLG signal prioritization principles for prelaunch product observability.

## Core PLG Signal Sequence

Modern PLG frameworks distinguish three signal layers:

### Layer 1: First Win Signals (Prelaunch-safe)
These are the earliest, most observable signals. They answer: "Did the user reach the moment of first value?"

- **First win event**: The single action that confirms the user received initial value
- **Time-to-first-win (TTV)**: How quickly the user reached first value (observe qualitatively, no benchmarks yet)
- **Post-first-win behavior**: What the user did immediately after (30-second observation frame)

### Layer 2: Activation Signals (Limited prelaunch use)
Activation signals require sufficient traffic and clean separation of human vs. synthetic sessions.

- **Activation event**: The user completing the "aha moment" bundle, not a single click
- **D1/D3 return**: Did the user come back? (observe only, no % judgment at prelaunch)
- These are observation candidates, not conclusions, at prelaunch

### Layer 3: PQL / Conversion Signals (Post-launch only)
Product-Qualified Leads are a *bundle* pattern, not triggered by single events.

- **PQL candidate**: Repeat first-win events + D7 revisit = bundle that *correlates* with conversion
- **Upgrade demand**: Never inferred from friction events (cap hits, errors)
- **Viral coefficient / expansion**: Only meaningful at sufficient scale

## Prelaunch Reading Rule

At prelaunch (first 10–50 real users):
- **Count**: existing first-win events anchored in product code (no new events)
- **Observe manually**: friction type, user language, guided break point
- **Do not judge**: PQL, paid conversion, retention %, viral coefficient, channel quality

## Conflict Check with Virtue Context

- Virtue J1/J2/J4 first win = `deed_saved` (m06, m10, m20–m29, m55)
- Virtue J3 first win = `deed_judged` (m06, m55)
- `deed_save_capped` = availability/friction, NOT upgrade demand (m21, m22, m23, m28, m29)
- `deed_judged` without save (J3) = normal exit, NOT activation failure (m30, m31)
- PQL is a bundle, not a single event (m41)
- Prelaunch small sample = directional input only, not PMF/conversion/retention proof (m08, m11, m14, m22, m55)
