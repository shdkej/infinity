---
id: marketing-61
status: archived
archived_at: 2026-06-15T10:07Z
display: Virtue Launch-After Activation Cohort Boundary
projects:
  - virtue
type: strategy
topics:
  - plg
  - activation
  - pql
  - measurement
  - prelaunch
permission: L1-docs-only
---

# marketing-61 - Virtue Launch-After Activation Cohort Boundary

## result_summary

Mixpanel 2026 PLG activation/PQL lens was translated into a Virtue docs-only launch-after measurement boundary. The artifact separates first-10 manual observation from later cohort/PQL judgment across J1-J4, keeps activation candidates distinct from 7-day repeat-value candidates, and fixes PQL as a future frequency + breadth + depth threshold rather than a prelaunch label.

## artifacts

- path: artifacts/marketing-61/virtue-launch-after-activation-cohort-boundary.md
  role: Artifact

## reports

- path: reports/marketing-61/2026-06-15T1007Z-local.html
  role: Report

## commits

- none: docs-only local artifact/update in Infinity working tree; no push performed by this bounded router pass.

## urls

- none

## next_actions

- Use this boundary when reading Virtue first-10 interviews and launch-after cohorts so `first value`, `activation`, `7-day repeat value`, and `PQL` are not collapsed into one metric.
