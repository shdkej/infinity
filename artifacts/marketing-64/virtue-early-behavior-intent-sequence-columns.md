# Virtue Early Behavior Intent Sequence Columns

Intent: marketing-64
Scope: L1 docs-only addition to the first-10 observation contract.
Source note: `source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md`
Lens: Mixpanel 2026 PLG 행동 기반 의도 신호를 Virtue prelaunch first-10 관찰 문맥으로 번역.

## Guardrails

- Preserve the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Keep this as a manual observation layer over the first 10 sessions, not product instrumentation.
- Do not add events, properties, timers, tracking, privacy flows, dashboards, session replay, public copy, deployment, external messages, pricing, or cost changes.
- Treat intent sequence as additional context for the existing first-value anchor, not a replacement.
- Synthetic/test and prelaunch low-signal data must be excluded before reading any intent sequence.

## Core Distinction: Activation Event vs Intent Sequence

### Activation Event

An activation event is a single observable moment that marks first value: `deed_saved` for J1/J2/J4, `deed_judged` for J3. This is the existing anchor from `marketing-55`.

### Intent Sequence

An intent sequence is the ordered trail of early behaviors that leads a user toward or away from the activation event. It answers:

- What job expectation brought the user to the first screen?
- Where did the user pause, explore, or change direction before reaching first value?
- What did the user skip or avoid?
- What happened after the activation event that reveals whether first value opened a path or closed one?

### Why the distinction matters

Counting only the activation event tells you *whether* a user reached first value. Reading the intent sequence tells you *why* — and which friction points or job mismatches shaped the path. For prelaunch first-10 context, this distinction creates the observation baseline that makes post-launch cohort comparisons honest. Without it, the same `deed_saved` count looks identical whether the user arrived with clear intent or stumbled through three skipped behaviors first.

## early_behavior_sequence Column Group

Add four concise manual observation columns beside the existing first-10 observation fields.

| New manual column | What to observe | Allowed answer shape | Why it matters |
|---|---|---|---|
| 첫 탐색 기능 (first_explored_feature) | What was the first feature, screen, or flow the user engaged with before any deed action? | Screen or action name + user's words about expectation, or "unknown" | Reveals which job assumption brought the user; a J3 user may enter `/add` with a specific question immediately, while a J1/J4 user may browse or orient first. |
| 멈춘 화면 (stopped_screen) | Where did the user pause, hesitate, or take noticeably longer? | Screen or state name + user's words if available, or "not observed" | Identifies friction points in the path to first value. A pause at the result card differs from a pause at the input field. |
| 건너뛴 행동 (skipped_behavior) | What action or step did the user skip, bypass, or ignore entirely? | Action or screen name + reason if given, or "not observed" | Reveals job-path mismatch or intentional shortcuts. Skipping the example prompt differs from skipping the save step. |
| 저장 후 다음 행동 (post_save_action) | What did the user do immediately after `deed_saved` (J1/J2/J4) or after the session ended (J3)? | Next action + user's words about next intent, or "session ended" / "not observed" | Shows whether first value was a destination (session closed) or a stepping stone (user continued, added another deed, revisited). |

## Job-Specific Reading

| Job | Existing first-value anchor | Intent sequence read | Early behavior signal to watch |
|---|---|---|---|
| J1 기록형 | `deed_saved` | Did the sequence move directly from input → result → save? Detours or stops before saving suggest the record-value expectation was unclear or the output needed multiple attempts. | Skipping example input → strong prior intent present. Stopping at result card → evaluating whether output is worth keeping. Post-save close → first record accepted as standalone. |
| J2 누적형 | `deed_saved` | Did the user show interest in history, past records, or progress signals before or after saving? A J2 user may pause at accumulation indicators. | First explored: history or level screen → accumulation intent visible early. Post-save continued → second deed likely. Post-save close → single record may not yet trigger accumulation motivation. |
| J3 AI 호기심형 | `deed_judged` | Did the sequence move quickly to judgment, or did the user hesitate at input? J3 intent should be legible in the first input itself. | First input written quickly with a specific question → clear curiosity intent. Multiple rewrites → intent search friction. No save, quick close after judgment → normal J3 completion. |
| J4 회고형 | `deed_saved` | Did the user appear to compose carefully before submitting, or need several attempts? Reflection jobs tend to produce longer input pauses. | Long pause at input → reflection in progress (not friction). Stopped at result card → evaluating truthfulness/fit. Post-save revisit → checking the saved reflection's language. |

## How to Use with Existing Columns

Use these four columns after the existing first-10 observation fields from `marketing-54`, `marketing-55`, and `marketing-56`.

Suggested row order for first-10 observation notes:

| Existing field | Then add |
|---|---|
| Job (J1/J2/J3/J4 or unknown) | Keep. |
| Count now (`deed_saved` or `deed_judged`) | Keep as the activation event anchor. |
| Expected / Acquired / Blocked / Exit class (marketing-54) | Keep as the value reason loop. |
| Count now / Observe manually / Do not judge yet (marketing-55) | Keep as the first-value boundary. |
| Accepted output / Useful-result time / Retry-rejudge reason / Reproducibility understanding (marketing-56) | Keep as the first reliable value quality check. |
| **첫 탐색 기능** | Add: what did the user explore first? |
| **멈춘 화면** | Add: where did they pause? |
| **건너뛴 행동** | Add: what did they skip? |
| **저장 후 다음 행동** | Add: what happened immediately after first value? |

## Interpretation Rules

- These four columns provide the *path* context around the activation event. They do not create new metrics.
- A long intent sequence (many steps before activation) is not inherently negative — it may reflect careful J4 reflection or J2 accumulation intent exploration.
- A short sequence with no save is J3 normal completion. Do not read it as friction or drop-off.
- `post_save_action: session ended` is normal for J1/J4 first sessions. It is not churn.
- `post_save_action: continued` does not confirm retention — it is a prelaunch observation note only.
- Do not convert these columns into rates, percentages, or behavioral metrics before launch.
- Do not infer upgrade intent, PQL, or monetization demand from any combination of these columns.
- Synthetic/test/self-test sessions must be excluded before reading intent sequence patterns.

## Compatibility Check

| Prior artifact | Compatibility |
|---|---|
| `artifacts/marketing-55/virtue-prelaunch-activation-measurement-contract.md` | Compatible. Activation event anchor (deed_saved/deed_judged by job) is preserved; intent sequence adds path context without replacing the anchor. Conflict markers: 0. |
| `artifacts/marketing-56/virtue-first-reliable-value-observation-columns.md` | Compatible. First reliable value columns focus on the activation moment quality; intent sequence adds the pre- and post-activation path. Conflict markers: 0. |
| `artifacts/marketing-63/virtue-agent-readable-analytics-context-card.md` | Compatible. Agent-readable card fixes event vocabulary; intent sequence columns are manual pre-analysis observation notes that align with its data-quality check step. Conflict markers: 0. |
| `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md` | Compatible. Expected/Acquired/Blocked/Exit class captures outcome reasons; intent sequence adds temporal path context (when and where, not just what). Conflict markers: 0. |
| `MARKETING_LEARNINGS.md` — Session Value Is Read By Job, Not Event Count | Compatible. Intent sequence supports job-by-job session reading without converting event counts to value claims. |
| `MARKETING_LEARNINGS.md` — Measurement Readiness Is A Separate Gate | Compatible. Intent sequence is a prelaunch observation baseline, not a measurement claim. |

Conflict markers across all listed artifacts: 0.

## Verification

- Source note path referenced: `source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md`.
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Required column group included: 첫 탐색 기능, 멈춘 화면, 건너뛴 행동, 저장 후 다음 행동.
- Conflict markers with marketing-55~63: 0.
- Synthetic/test and prelaunch low-signal prohibition maintained.
- New events, properties, tracking/privacy, dashboard, public copy, deployment, external message, cost changes: 0.
