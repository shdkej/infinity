# Virtue Prelaunch Activation Measurement Contract

Intent: marketing-55  
Scope: docs-only activation measurement contract for prelaunch Virtue.  
Source note: `source/external-links/marketing/2026-06-12-plg-activation-measurement.md` at the Knowledge Lab root.  
Lens: Mixpanel 2026 PLG measurement framing, translated into a prelaunch-safe first-value contract.

## Guardrails

- Preserve the existing first-value mapping: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Use only existing event names as interpretation anchors. Do not add events, properties, tracking, privacy flows, dashboards, public copy, deployment, external sending, or cost.
- Treat signup, pageview, total visits, and small synthetic/test traffic as context only, not as activation proof.
- Keep PQL, paid conversion, expansion, and viral coefficient behind launch-after gates.
- Read `deed_judged` vs `deed_saved` by job. A J3 no-save path can be normal completion; a J1/J2/J4 no-save path needs a manual reason before interpretation.

## Contract Table

| Job | First value | Existing event anchor | Manual observation question | Count now | Observe manually | Do not judge yet | Launch-after gate |
|---|---|---|---|---|---|---|---|
| J1 기록형 | A deed result felt worth preserving as a record. | `deed_saved` | What made this result worth keeping, or what stopped you before saving? | Count `deed_saved` as the current activation anchor for J1 sessions. | Reason for save/no-save: useful record, wrong output, too much effort, privacy concern, already enough. | Do not treat `deed_judged` alone as J1 activation. Do not turn no-save into churn without the reason. | After launch, compare first-session `deed_saved` users against 7-day return or second deed. PQL stays gated until repeat value is visible. |
| J2 누적형 | The user sees something they want to accumulate or revisit. | `deed_saved` | What would make this worth coming back to or adding to again? | Count `deed_saved` as the first accumulation proof. | Return reason, level/progress meaning, whether save created a visible next step. | Do not read one save as retention, paid intent, or habit value. | After launch, check repeat deed creation and return reason before any paid conversion or expansion read. |
| J3 AI 호기심형 | The AI judgment answered the user's curiosity. | `deed_judged` | Did the judgment answer the curiosity, surprise you, or give language you could use? | Count `deed_judged` as the J3 first-value anchor. | Whether no-save was normal completion, mistrust, confusion, or no useful output. | Do not count judged-minus-saved as failure by default. Do not force J3 into a save-led activation definition. | After launch, compare J3 judged-only completion against optional later save, reroll, or return behavior before PQL labeling. |
| J4 회고형 | The reflection felt true enough to keep or revisit. | `deed_saved` | What part of the result felt true enough to keep, or what made it complete without saving? | Count `deed_saved` as the strongest first-value anchor. | Emotional fit, self-appropriation, completion-without-save, privacy or effort blocker. | Do not interpret a one-time reflection as expansion, viral intent, or upgrade demand. | After launch, check repeat reflection or explicit sharing/referral language before any viral coefficient or expansion read. |

## Metric Boundary

| Layer | Prelaunch stance | Reason |
|---|---|---|
| Activation | Define by job now. Count only the existing first-value anchors and pair them with first-10 manual notes. | Activation is the root contract; later PLG metrics are noisy if this layer is wrong. |
| PQL | Launch-after gate. Use as a future candidate label only after repeated value or clear hand-raise behavior. | A single event, especially `deed_save_capped`, is not upgrade intent. |
| Paid conversion | Launch-after gate. Do not infer from saves, caps, or curiosity completions before pricing/plan approval. | Price, plan, and paywall decisions are outside this L1 scope. |
| Expansion | Launch-after gate. Look only after repeated use, team/family/workflow spread, or explicit multi-user need. | Expansion requires account/context evidence, not first-session behavior. |
| Viral coefficient | Launch-after gate. Treat sharing/referral as qualitative post-launch observation until explicit tracking is approved. | Viral measurement would require tracking/public-copy/privacy decisions. |

## First-10 Reading Rule

Use one row per observed person or session:

| Field | Allowed input | Interpretation rule |
|---|---|---|
| Job | J1/J2/J3/J4 or unknown | If unknown, do not force the event into a job-specific activation label. |
| Count now | Existing event anchor only: `deed_saved` or `deed_judged` according to the table. | Count as a rough prelaunch signal, not as a growth conclusion. |
| Observe manually | User words about expected value, acquired value, no-save reason, and next-step reason. | Manual notes explain why the event happened. They do not create new telemetry. |
| Do not judge yet | PQL, paid conversion, expansion, viral coefficient, channel quality, retention rate, and pricing intent. | Reopen only after launch or after an explicit approval-gated measurement plan. |

## Verification

- Source note path confirmed: `../source/external-links/marketing/2026-06-12-plg-activation-measurement.md`.
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.
- Required terms included: `count now`, `observe manually`, `do not judge yet`.
- PQL, paid conversion, expansion, and viral coefficient are separated into launch-after gates.
- New events, tracking/privacy, dashboard, public copy, deployment, external message, and cost changes: 0.
