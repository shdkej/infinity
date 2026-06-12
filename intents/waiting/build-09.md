# build-09: Control Center Authenticated Publish + Rollback

- id: build-09
- status: waiting
- waiting_since: 2026-06-12T10:47
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, auth, publish, deploy, rollback]
- owner: SAM
- display_name: Control Center Authenticated Publish + Rollback
- source: continuity follow-up from build-08 shadcn UI + status composition CMS
- predecessor: build-08
- artifact:
  - path: artifacts/build-09/control-center-authenticated-publish-rollback-spec.md
    role: design
    note: non-secret publish/rollback boundary and approval decision spec

## Current State

The safe first pass is complete: a non-secret design/spec defines the publish pipeline shape, rollback handle, auth boundary, first target recommendation, and exact approval gate. No production write or deploy action was taken.

## Decision

Control Center publish pipeline을 먼저 어떤 범위로 열까요?

## Options

- default: `dry-run-only-first`
  - label: Dry-run only first
  - effect: implement snapshot + diff preview + approval screen only; no source write/deploy.
- option: `single-target-publish`
  - label: Single target publish
  - effect: after explicit approval, allow `status-control-center-feed` only to write a generated file, commit/push, deploy, verify, and record rollback handle.
- option: `wait`
  - label: Wait
  - effect: keep build-09 parked until auth/permission expectations are decided.

## Approval Boundary

Actual production page write/deploy, auth/permission change, source repo write, commit/push automation, deploy trigger, rollback execution, GitHub/AWS token expansion, destructive action, force-push, secret exposure, or cost-bearing resource changes require explicit approval before implementation.

## Next

If the default is accepted, create a follow-up implementation intent for dry-run snapshot + diff preview only. If single-target publish is approved, keep target locked to `status-control-center-feed` and require scoped-path verification before any push/deploy.
