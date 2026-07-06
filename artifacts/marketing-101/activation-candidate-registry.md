# Virtue J1-J4 activation candidate registry

- intent: marketing-101
- status: final
- scope: docs-only registry for post-launch validation candidates
- inherited 기준: MARKETING_LEARNINGS First Value Mapping, Measurement Readiness, Correlation Readiness, Session Value, Post-Response Flow
- source: `source/external-links/marketing/2026-06-01-activation-metric-bundles.md`

## Purpose

This registry does not define an activation rate. It records candidate activation bundles that can later be compared with retention once real traffic, event quality, and sample size are sufficient. In prelaunch, every bundle below is a hypothesis and observation aid.

## First value baseline

| Job | First value event | Why this remains unchanged |
|---|---|---|
| J1 daily record | `deed_saved` | The job is complete when a small daily act is stored and can return as proof. |
| J2 cumulative growth | `deed_saved` | The first save is the entry point; cumulative payoff needs later return or repeat save. |
| J3 AI curiosity | `deed_judged` | The job can complete at the result card without saving. Save is optional, not required. |
| J4 reflection archive | `deed_saved` | The job is complete when the moment is preserved for later reflection. |

## Candidate bundles

| Job | Candidate bundle | Suggested window | Readable from current events | Manual-only observation | First verification gate |
|---|---|---|---|---|---|
| J1 daily record | `/add` starts, `deed_judged`, then `deed_saved`; optionally D1 return to home proof | first session for save, D1 for return check | `deed_judged`, `deed_saved`, return session if available | whether the user says the record was easy enough to repeat | Compare first 10 users against `marketing-79`/`marketing-98`: J1 is activated only after save, even if value language appears earlier. |
| J2 cumulative growth | first `deed_saved`, then level/progress surface noticed or second save | first session plus first week | `deed_saved`, possible `level_up_viewed`/second save if available | whether the user notices score/progress as a reason to return | After at least one saved record, check whether D1/D7 return language references accumulation before treating J2 as activated. |
| J3 AI curiosity | `deed_judged`, then one of: result read, reroll, another input, or natural stop without save | same session, result-card/post-response window | `deed_judged`, `deed_rerolled`, another judged input if available | result reading, surprise, showing to someone, spoken "AI perspective" value | Preserve `marketing-98`: judged-without-saved can be value discovered + activation reached. Do not require save. |
| J4 reflection archive | `deed_saved`, then the saved item remains legible on return or user names later recall value | first session for save, D1/D7 for archive value | `deed_saved`, return session if available | whether the user says this is something they want to revisit | Use the `marketing-79` observation table: save is required, but later reflection value remains manual until repeated returns exist. |

## Interpretation bans while sample is small

- Do not convert any bundle into PMF, conversion, retention, PQL, upgrade demand, or public proof.
- Do not compare jobs by raw event count. J3 can need fewer events than J1/J2/J4.
- Do not read `deed_save_capped`, 503, latency, or failed save as value or upgrade demand.
- Do not treat `judged but not saved` as failure for J3.
- Do not treat one happy quote, one reroll, or one D1 return as a validated activation metric.
- Do not run or publish correlation claims until traffic source, mock/self-test exclusion, event quality, and retention window are ready.

## Data readiness before retention comparison

1. The job label or manual job inference is recorded separately from event counts.
2. Current events can distinguish `deed_judged`, `deed_saved`, `deed_rerolled`, return sessions, and availability/friction cases.
3. Manual notes preserve value-discovery language, next-action clarity, recommendation language, and J3 natural-stop signals.
4. Mock, synthetic, maker self-test, cap, 503, and latency sessions are excluded from activation validation and kept only as friction evidence.
5. The comparison window is selected by job: same-session for J3 first value, first-session plus D1/D7 for J1/J2/J4 follow-through.

## Relationship to prior artifacts

- `marketing-79` supplies the first 10 user observation surface and checkpoint order.
- `marketing-98` separates value discovery from activation reached, which this registry keeps.
- `marketing-99` and `marketing-100` remain onboarding/path comparison documents, not activation metric definitions.
- The external PostHog note contributes only the bundle-and-window method; its benchmarks are not copied into Virtue.
