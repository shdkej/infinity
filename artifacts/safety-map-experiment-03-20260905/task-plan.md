# Safety Map Experiment 03 — Task Plan

Hard deadline: **2026-09-06 06:00 UTC**. Leaf estimates are operational limits, not promises: exceeding `max` requires split/replan or a documented external blocker.

## T1 — Intake and planning

| Leaf | expected / max | depends | completion |
|---|---:|---|---|
| T1.1 Create Context Pack and rerun declared search | 10m / 15m | — | Pack and search evidence recorded |
| T1.2 Record new experiment-03 Intent and Slack origin | 10m / 15m | T1.1 | Immutable origin and deadline in registry |
| T1.3 Write PRD and acceptance boundaries | 20m / 30m | T1.1 | This PRD reviewed by Planner |
| T1.4 Plan new path and legacy protection | 15m / 25m | T1.2 | Exact create/never-touch paths listed |

## T2 — Independent role convergence

| Leaf | expected / max | depends | completion |
|---|---:|---|---|
| T2.1 Spawn Planner review | 10m / 15m | T1 | session id and judgment |
| T2.2 Spawn Developer review | 10m / 15m | T1 | session id and implementation handoff |
| T2.3 Spawn Marketer review | 10m / 15m | T1 | session id and copy/hierarchy judgment |
| T2.4 Spawn Operator review | 10m / 15m | T1 | session id and deploy/security judgment |
| T2.5 Synthesize conflicts into implementation contract | 15m / 25m | T2.1–T2.4 | adopted/rejected decisions documented |

## T3 — Build and local verification

| Leaf | expected / max | depends | completion |
|---|---:|---|---|
| T3.1 Create isolated experiment-03 static site path | 20m / 30m | T2.5 | no legacy file modified |
| T3.2 Build full-bleed canvas and Typography Rail | 35m / 50m | T3.1 | map is dominant scene |
| T3.3 Add search/place/road, zoom/pan and layer controls | 30m / 45m | T3.2 | real canvas interactions work |
| T3.4 Add no-data, failure, keyboard and reduced-motion states | 25m / 40m | T3.3 | boundary/accessibility tests pass |
| T3.5 Run local smoke and token/provenance checks | 20m / 30m | T3.4 | reproducible test output |

## T4 — Visual and live quality gates

| Leaf | expected / max | depends | completion |
|---|---:|---|---|
| T4.1 Capture desktop initial/search/pan/layer states | 25m / 40m | T3.5 | immutable browser evidence |
| T4.2 Capture 390px initial/search/pan/layer states | 25m / 40m | T3.5 | no overflow/collision evidence |
| T4.3 Red direct visual review and remediation | 30m / 50m | T4.1,T4.2 | Red pass report |
| T4.4 Formal deploy and live behavior retest | 25m / 40m | T4.3 | live URL/check proof |

## T5 — Remote closure

| Leaf | expected / max | depends | completion |
|---|---:|---|---|
| T5.1 Commit only explicit relevant paths and push | 15m / 25m | T4.4 | commit SHA + origin confirmation |
| T5.2 Verify remote archive/report requirements | 15m / 25m | T5.1 | remote verifier pass |
| T5.3 Send original Slack thread status/terminal receipt | 5m / 10m | T5.2 | immutable receipt |
| T5.4 Record knowledge decision and Archive only with Red pass | 15m / 25m | T5.2,T5.3 | archive metadata complete |

## Current state

**T3.2 Active (2026-09-05T10:30:02Z).** 전체 화면 canvas와 Typography Rail의 첫 렌더를 e03 경로에 구현합니다. legacy safety-map은 계속 변경 금지입니다.
