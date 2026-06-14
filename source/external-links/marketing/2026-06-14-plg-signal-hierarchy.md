# PLG Signal Hierarchy — Virtue Prelaunch Reference

Captured: 2026-06-14  
Intent: marketing-59  
Scope: docs-only reference note

## PLG Signal Hierarchy (General Framework)

Product-led growth signals are ordered by when they become meaningful:

1. **Signup / Page view** — vanity metrics during prelaunch. Everyone has them. They don't distinguish acquirer quality from activation.

2. **First Win / Activation** — the moment a user reaches the core value of the product. This is the first meaningful PLG signal. For Virtue: J1/J2/J4 = `deed_saved`, J3 = `deed_judged` (per marketing-55).

3. **PQL (Product-Qualified Lead)** — a user whose behavior pattern signals upgrade readiness. Requires: repeated first-value events + D7 return + observable hand-raise. Not a single event. (per marketing-41)

4. **Paid Conversion** — user moves from free to paid tier. Requires pricing/plan decisions outside L1 scope.

5. **Expansion** — user spreads usage to team/family/workflow. Requires account/context evidence.

6. **Viral Coefficient** — net new users from existing users. Requires tracking/referral/privacy decisions.

## Virtue Prelaunch Context

Virtue is in prelaunch / low-signal learning mode (first 10 users, manual observation).

Key constraints:
- First-value mapping: J1/J2/J4 = `deed_saved`, J3 = `deed_judged` (do not change)
- External events, tracking, privacy, dashboard, public copy, deploy, external messaging: not allowed in L1
- PostHog: read-only future checklist (no project ID available yet)
- Small sample (first 10): directional observation only, not conclusive

## Signal Classification Rule

| PLG Layer | Prelaunch stance | Reason |
|---|---|---|
| Signup / Page view | HOLD — vanity metric | Can't distinguish acquisition quality from activation |
| First win (`deed_saved` / `deed_judged`) | NOW — count and observe | Core PLG signal, existing event anchor |
| Quality of first win (manual observation) | NOW — hands-on notes | Explains why the event happened |
| PQL signals | AFTER LAUNCH | Requires repeat + D7 + bundle, not single event |
| Paid conversion intent | AFTER LAUNCH | Pricing/plan decisions required |
| Expansion signals | AFTER LAUNCH | Account/context evidence required |
| Viral coefficient | AFTER LAUNCH | Tracking/referral/privacy decisions required |

## Cross-Reference

- marketing-55: Activation measurement contract (count now / observe manually / do not judge yet / launch-after)
- marketing-56: First reliable value observation columns (accepted output / useful-result time / retry-rejudge reason / reproducibility)
- marketing-58: First successful output contract (screen evidence / successful output sentence / user next action / agent-readable quality standard)
- MARKETING_LEARNINGS.md: "PQL Is A Bundle, Not A Single Event", "Measurement Readiness Is A Separate Gate", "Prelaunch Decision Boundary"
