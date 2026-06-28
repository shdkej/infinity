# Virtue First Session Three-Gate Sheet

- intent: `marketing-90`
- created_at: 2026-06-28T1007Z
- scope: L1 docs-only
- source: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-28-first-session-three-gates.md`

## Summary

Virtue's first session is easier to operate when split into three gates instead of one broad onboarding problem: entry promise, input expectation, and return-state consistency. The current highest-risk break is gate 3 because the live home still shows retained proof and first-visit empty-state copy at the same time.

## Three Gates

| Gate | User question | Current surface | Break symptom | Existing evidence | Next owner route |
|---|---|---|---|---|---|
| Gate 1. Entry promise | Why should I start now? | Home first view | The page feels like a generic tracker and the first value is not legible in one screen. | `2026-06-26-onboarding-dropoff-context-vs-friction.md`, `marketing-89` | Keep as strategy/verification unless a stronger mismatch appears than gate 3. |
| Gate 2. Input expectation | What can I type and what comes back? | `/add` pre-input and immediate result transition | Users hesitate before typing because the shape of the output is unclear. | `2026-06-21-add-preinput-proof-bridge.md`, `2026-06-26-post-first-value-next-action-helper.md`, `marketing-77` | Small UI/copy implementation slices remain valid after gate 3 is stabilized. |
| Gate 3. Return-state consistency | Did what I just did actually stick? | Home after first value | Retained proof and first-visit/empty-state copy appear together, which reads as a state-contract failure rather than a wording gap. | `2026-06-27-return-state-verification-gate.md`, `marketing-89`, 2026-06-28 live home observation | Highest-priority implementation/verification route. Keep follow-up scoped to home return-state gating. |

## Priority Order

1. Gate 3 return-state consistency
2. Gate 2 input expectation
3. Gate 1 entry promise

## First Verification Gate

When the live home and the three recent notes are read side by side, the current break can be explained in three sentences:

1. The entry promise and input expectation may still be improved, but neither is the only place where a concrete contradiction is visible right now.
2. The live home shows retained proof (`612덕`) while also showing first-visit empty-state copy, so the app is simultaneously claiming history exists and does not exist.
3. That makes gate 3 the first repair target because trust breaks after value has already been produced.
