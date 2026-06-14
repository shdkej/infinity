# PLG Signal Hierarchy — Prelaunch Context

Reviewed: 2026-06-14
Permission: L1 docs-only (internal reference)
Intent: marketing-59

## Source

Internal synthesis from:
- Wes Bush, "Product-Led Growth: How to Build a Product That Sells Itself" (2019) — Foundation/Activation/Conversion PLG model
- OpenView 2024–2025 PLG benchmarks — activation, PQL, expansion signal ordering
- Infinity marketing learning chain: marketing-34 (Measurement Readiness), marketing-41 (PQL Is A Bundle), marketing-47 (First-User Learning Loop), marketing-55 (Activation Measurement Contract), marketing-58 (First Successful Output Contract)

## PLG Signal Order (Framework Reference)

PLG frameworks identify three ordered tiers of signal:

1. **Activation (First Win)** — user reaches the core value moment for the first time.
   - *Prelaunch relevance*: can be DEFINED now, cannot be RATED now.
2. **Product-Qualified Lead (PQL)** — user exhibits repeat-first-win + return-visit bundle.
   - *Prelaunch relevance*: requires D7+ return data; hold until post-launch.
3. **Conversion / Expansion** — upgrade intent emerging from PQL pattern.
   - *Prelaunch relevance*: requires PQL baseline; hold until post-launch.

## Prelaunch Constraint

With < 10 real users (no synthetic/mock/self-test):
- Activation CAN be defined per job (done — see marketing-55)
- Activation RATE cannot be judged — sample too small
- PQL CANNOT be formed — needs D7 revisit data
- Conversion CANNOT be extracted — no PQL baseline exists

## Virtue Job Mapping (Inherited from MARKETING_LEARNINGS.md)

| Job | First Win Event | Note |
|-----|----------------|------|
| J1  | `deed_saved`   | Save after judged |
| J2  | `deed_saved`   | Second save / level up |
| J3  | `deed_judged`  | Result card arrives; no-save is NORMAL END |
| J4  | `deed_saved`   | Save with tag |

`deed_save_capped`: Availability/friction signal — NOT PQL, NOT upgrade demand.

## Notes

No new events, tracking/privacy, dashboard, public copy, robots/sitemap, MCP/API, pricing, deploy, external message, or cost-bearing changes occurred.
