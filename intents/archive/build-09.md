# build-09: Control Center Authenticated Publish + Rollback

- id: build-09
- status: completed
- waiting_since: 2026-06-12T10:47
- completed_at: 2026-06-12T14:16Z
- projects: [infinity, personal-ops, infrastructure]
- task_type: implementation
- topics: [dashboard, cms, auth, publish, deploy, rollback]
- owner: SAM
- display_name: Control Center Static Publish Target Removed
- source: continuity follow-up from build-08 shadcn UI + status composition CMS
- predecessor: build-08
- artifact:
  - path: artifacts/build-09/control-center-authenticated-publish-rollback-spec.md
    role: design
    note: non-secret publish/rollback boundary and approval decision spec

## Current State

The previous safe first pass produced a non-secret publish/rollback spec, but the user then decided to remove the static Control Center page. That removes the proposed `status-control-center-feed` target and closes this waiting decision.

The active Control Center surface is now the deployed CMS at `https://cms.oracle.shdkej.com`; the old static Status subpage should no longer be treated as an implementation or publish target.

## Outcome

- Static Control Center page removed from the Status static site.
- Status index no longer links to `./control-center/index.html`.
- `build-09` moved from Waiting to Archive as superseded by the removal of the static target.

## Approval Boundary

Actual production page write/deploy, auth/permission change, source repo write, commit/push automation, deploy trigger, rollback execution, GitHub/AWS token expansion, destructive action, force-push, secret exposure, or cost-bearing resource changes still require explicit approval before any future implementation.

## Next

If Control Center publish work returns later, start from the live CMS (`https://cms.oracle.shdkej.com`) and define a new target explicitly. Do not revive `status-control-center-feed` without a new user decision.
