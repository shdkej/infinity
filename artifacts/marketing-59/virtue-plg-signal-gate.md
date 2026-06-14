# Virtue Launch-Ready PLG Signal Gate

Intent: marketing-59
Scope: L1 docs-only PLG signal gate for Virtue prelaunch.
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
Prior contracts: marketing-55 (activation measurement), marketing-56 (reliable value columns), marketing-58 (first successful output contract)

## Purpose

Translate the PLG signal hierarchy into a Virtue-specific gate that prevents acquisition confusion, activation confusion, and measurement-too-early errors during the first-10-user observation window.

## Scope Guard

No new events, tracking, privacy flows, dashboards, public copy, deployment, external messages, pricing, caps, or cost changes. First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`.

## PLG Signal Gate Table

| Signal | Tier | 지금 볼 신호 | 보류할 신호 | Launch 이후 볼 신호 | Note |
|--------|------|------------|-----------|------------------|------|
| First successful output: `deed_saved` (J1/J2/J4) | Tier 1 | Count | | | Core activation anchor |
| First successful output: `deed_judged` (J3) | Tier 1 | Count | | | No-save can be normal |
| Output acceptance (kept/used it?) | Tier 1 | Observe | | | Manual note only |
| Time to first output (qualitative) | Tier 1 | Observe | | | Not a stopwatch |
| Retry or rejudge reason | Tier 1 | Observe | | | Context required |
| Reproducibility understanding | Tier 1 | Observe | | | "Would use again" language |
| Voluntary return without prompting | Tier 2 | | Note (no judgment) | | Directional only with 10+ |
| Repeat use within 7 days | Tier 2 | | Note (no judgment) | | Not yet retention |
| Second deed / continuation | Tier 2 | | Note (no judgment) | | Directional only |
| Power user feature breadth | Tier 3 | | | After launch | Stable surface needed |
| Sharing / referral language | Tier 3 | | | After launch | Qualitative only |
| Explicit value articulation | Tier 3 | | | After launch | 50+ users minimum |
| Upgrade intent | Tier 4 | | | After pricing approval | Lock gate |
| Paid conversion | Tier 4 | | | After pricing approval | Lock gate |
| Expansion (team/family) | Tier 4 | | | After account evidence | Lock gate |
| Viral coefficient | Tier 4 | | | After referral tracking approval | Lock gate |

## Confusion Prevention Map

| Error type | Confused signals | Correct reading |
|-----------|-----------------|----------------|
| Acquisition vs. Activation | No save -> "acquisition failed" | Check job type first. J3 no-save can be normal completion. |
| Activation vs. Retention | One `deed_saved` -> "activated user" -> optimize retention | One save = first value only. Observe repeat without judging. |
| Activation vs. PQL | 3 enthusiastic users -> "strong PQL signal" | Too early. PQL needs 50+ users and stable feature surface. |
| Measurement too early | Viral/expansion/paid at prelaunch | Lock Tier 3-4 gates until launch and explicit approval. |

## First-10 Review Gate

Use for each of the first 10 observed users or sessions.

### Pre-Observation Check
- [ ] Which job does this session represent? (J1 / J2 / J3 / J4 / unknown)
- [ ] What is the expected first successful output for this job?

### During Observation
- [ ] Did the user reach first successful output? (`deed_saved` or `deed_judged`)
- [ ] If no save: what is the reason? (J3 normal completion / blocked / confusion / privacy / effort / left early / unknown)
- [ ] Accepted output: accepted / partially accepted / rejected / unclear + user's words
- [ ] Useful-result time: before result / at result card / after saving / not reached / unknown
- [ ] Retry or rejudge: (if occurred) curiosity / mismatch / mistrust / unclear / normal exploration
- [ ] Reproducibility: can explain / vague / cannot explain / not asked + exact phrasing if available

### Post-Observation (Do Not Skip)
- [ ] Signal tier reached: Tier 1 only / Tier 1+2 note / partial Tier 1 / did not reach Tier 1
- [ ] Do NOT read as: retention / PQL / paid intent / expansion / viral
- [ ] One-sentence plain observation: what happened?

### Review Gate Decision
- If Tier 1 reached: record as first successful output observation. No further label.
- If Tier 1 not reached: record reason. Do not label as "failed activation" until reason is understood.
- If Tier 2 observation noted: note qualitatively. Do not compute rate.
- If Tier 3-4 language heard: note as qualitative context only. Do not count.

## Compatibility with Prior Contracts

| Prior contract | Compatibility |
|---------------|---------------|
| marketing-55: Activation measurement contract | Compatible. `count now` / `observe manually` / `do not judge yet` structure preserved. |
| marketing-56: First reliable value observation columns | Compatible. `accepted output` / `useful-result time` / `retry-rejudge reason` / `reproducibility` columns preserved. |
| marketing-58: First successful output contract | Compatible. J1/J2/J4=`deed_saved`, J3=`deed_judged` mapping preserved. |

## Verification

- Source note confirmed: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md`
- Prior contracts not contradicted: marketing-55, marketing-56, marketing-58
- Conflict markers: 0
- New events / tracking / privacy / dashboard / public copy / deploy / external message / cost changes: 0
- First-value mapping preserved: J1/J2/J4 = `deed_saved`; J3 = `deed_judged`
