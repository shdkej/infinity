# Virtue Launch-After Activation Cohort Boundary

## Scope

This is an L1 docs-only artifact for Virtue prelaunch marketing analysis. It translates the source note `source/external-links/marketing/2026-06-15-plg-activation-pql-boundary.md` into a launch-after measurement boundary so first-10 manual observation is not confused with cohort or PQL judgment.

No product code, public copy, tracking, privacy setting, dashboard, pricing, deploy, external message, or cost-bearing action changed.

## Inherited Rules

- From marketing-55: prelaunch first value is observed manually; PQL, paid conversion, expansion, viral, and durable retention reads stay launch-after.
- From marketing-59: first successful output and activation quality are separated; acquisition/channel and PQL conclusions are held for later evidence.
- From marketing-60: outcome-readable documentation should make good result, bad result, and next action legible to a human and an agent.

## First-10 Versus Launch-After Boundary

| Layer | Use now in first-10 | Hold until launch-after cohort |
| --- | --- | --- |
| First value | Did the user reach a job-specific useful result once? | Does the same event predict return and repeated value across enough users? |
| Activation | Candidate labels only: `first_successful_output_seen`, `deed_saved`, `deed_judged`, `level_up_viewed` depending on job. | A measured activation definition chosen because it predicts 7-day return or repeat value. |
| PQL | Do not label a user as PQL from one prelaunch session. Record only qualitative readiness signals. | Frequency + breadth + depth thresholds by product/job, validated against retention or buying intent. |
| Cap/limit signal | Interpret as trust or value-boundary feedback only. | Treat as packaging/pricing signal only after repeated high-value usage and cohort context. |

## Job Boundaries

| Job | Activation candidate now | 7-day return / repeat-value candidate later | PQL boundary |
| --- | --- | --- | --- |
| J1 기록형 | `deed_saved` after a concrete deed is entered, judged, and saved. | User adds another real deed within 7 days or returns to inspect saved continuity. | Not PQL from one saved deed; require repeated real entries and evidence that saved history matters. |
| J2 누적형 | `deed_saved` plus visible expectation that saved deeds accumulate into progress. | User returns to add another deed or checks accumulated status/level progression within 7 days. | Require frequency of saving and breadth across more than one moment; one level/cap encounter is not enough. |
| J3 AI 호기심형 | `deed_judged` can be first value because the AI judgment itself is the curiosity payoff. | User asks for another judgment, rerolls, compares outcomes, or returns to test a new deed. | Require repeated judgment-seeking plus depth of interpretation; a single entertaining result is not PQL. |
| J4 회고형 | `deed_saved` when the output becomes a durable reflection artifact. | User returns to review, add context, or connect another deed to the same self-story. | Require repeat saved reflections and evidence the archive changes future action. |

## Seven-Day Candidate Reads

Use these as later cohort questions, not current conclusions:

- Did first successful output predict a return within 7 days?
- Did return mean repeated value, or only curiosity/noise?
- Which job path showed frequency without breadth, breadth without depth, or depth without frequency?
- Did the user hit a limit after receiving enough value, or before trusting the product?

## PQL Hold Line

For launch-after analysis, PQL should be defined only when three signals can be read together:

| Signal | Meaning | Virtue example |
| --- | --- | --- |
| Frequency | The user repeats the valuable action enough times to make habit or need visible. | Multiple real deed additions/judgments over a defined window. |
| Breadth | The user applies Virtue across more than one moment, context, or job need. | A user moves from one saved deed to another category, or from curiosity to reflection. |
| Depth | The user depends on the output enough that limits, continuity, or quality matter. | User cares about saved history, level progression, interpretation quality, or cap boundaries. |

Until those three are visible, use language like `PQL candidate signal` or `launch-after PQL input`, never `PQL`.

## Cap And Limit Interpretation

- First-10 cap friction is a trust/readiness clue, not a pricing conclusion.
- If a user meets a cap before seeing value, read it as value-before-limit failure.
- If a user meets a cap after repeated valuable use, save it as launch-after packaging evidence.
- Do not change pricing, limits, copy, or tracking from this artifact.

## Verification

- Source note exists at knowledge-lab root: `source/external-links/marketing/2026-06-15-plg-activation-pql-boundary.md`.
- Predecessor alignment checked against marketing-55, marketing-59, and marketing-60 archive summaries.
- New event definitions: 0.
- Tracking/privacy/dashboard/public copy/pricing/deploy/external messaging/cost changes: 0.
