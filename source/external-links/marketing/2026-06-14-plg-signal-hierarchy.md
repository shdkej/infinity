# PLG Signal Hierarchy for Prelaunch Products

Source: PLG signal hierarchy notes (2026-06-14)
Referenced by: marketing-59

## Core Principle

PLG signals have a natural hierarchy. The error in measurement-first thinking is trying to read all signals at once before you have enough users or behavior data to make them meaningful. For prelaunch products with under 10 users, most monetization and growth signals produce noise, not insight.

## Signal Hierarchy (Tier 1-4)

### Tier 1 — First Win Signals (Count Now)
These signals are reliable even with 5–10 users. They show whether the product delivered the promised output for the user's job.

- First successful output reached (for Virtue: `deed_saved` for J1/J2/J4; `deed_judged` for J3)
- Output acceptance: did the user keep or act on the output?
- Time to first output: qualitative observation only (not a stopwatch)
- Retry or rejudge reason: why the user rerolled, rewrote, or paused (if applicable)
- Reproducibility: can the user say when they would use this again?

### Tier 2 — Activation Signals (Observe, Do Not Judge Yet)
These signals need 10–20 sessions minimum to be directional. They show whether users "got it" well enough to return.

- Voluntary return without prompting
- Repeat use within 7 days
- Second deed or continuation behavior
- "I would use this again" language signal

### Tier 3 — PQL Signals (Hold Until Launch)
These signals require a larger population (50–100) and a stable feature surface and pricing context.

- Power user behavior (multi-feature use)
- Sharing or referral language
- Explicit value articulation unprompted
- Willingness-to-pay signals

### Tier 4 — Monetization Signals (Launch-After Gate)
- Upgrade intent
- Paid conversion
- Expansion (team/family/org)
- Viral coefficient

## Prelaunch Reading Rule

Prelaunch = Tier 1 only. Read Tier 1 carefully with manual observation notes. Acknowledge Tier 2 observations qualitatively. Lock Tier 3 and Tier 4 behind explicit launch gates.

**The failure mode:** reading Tier 3/4 signals from 3–5 users and drawing growth conclusions.

## Three Confusion Patterns to Prevent

### 1. Acquisition vs. Activation
- Mistake: user arrived but didn't save → "acquisition problem"
- Correct: check the job first. J3 (deed_judged) no-save can be normal completion.

### 2. Activation vs. Retention
- Mistake: one `deed_saved` → "activated user" → optimize for retention
- Correct: one save is first value. Observe repeat without interpreting it yet.

### 3. Activation vs. PQL
- Mistake: 3 enthusiastic early users → "strong PQL signal"
- Correct: PQL needs 50+ users and a stable feature surface. Too early.

## Application to Virtue

Virtue's current first-value mapping (`deed_saved` for J1/J2/J4; `deed_judged` for J3) correctly represents Tier 1. The risk is conflating:
- "no save" with "activation failure" (may be J3 normal completion)
- "first save" with "habit" or "retention" (one save is not habit)
- "one interested user" with "PQL" (far too early)

The signal gate (marketing-59) should make explicit: what to count now (Tier 1), what to observe qualitatively without judging (Tier 2), and what to defer entirely (Tier 3+).
