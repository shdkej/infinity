# Control Center Authenticated Publish + Rollback Spec

Intent: build-09  
Scope: non-secret design/spec only. No production write, deploy trigger, auth/permission change, source repo write, commit/push automation, or rollback execution.  
Predecessor: build-08 shadcn UI + Status Composition CMS.

## Current State

Build-08 created the operation surface:

- Public CMS URL: `https://cms.oracle.shdkej.com`
- Data model: `control_center_nodes` tree with `surface`, `section`, `card`, `link`
- Activity log: `control_center_activity`
- UI: Status composition tree, live preview, edit drawer, surface registry, activity feed
- Boundary preserved: CMS data can be edited; production page write/publish/auth/rollback is not enabled.

The next step is not more editing UI. It is a controlled path from CMS state to public source/deploy state.

## Publish Pipeline Shape

| Stage | Purpose | Safe behavior | Approval-gated behavior |
|---|---|---|---|
| Select | Choose one publish target. | Start with one target only: `status-control-center-feed` or one explicitly named surface. | Broad multi-surface publishing. |
| Snapshot | Freeze the CMS nodes used for publish. | Read current visible nodes and serialize a deterministic snapshot. | None, unless snapshot touches private data. |
| Diff Preview | Show exact generated file diff before write. | Dry-run renderer produces proposed JSON/HTML/feed diff without touching source files. | Writing generated output to repo. |
| Approval | Confirm human intent. | UI shows target, diff summary, expected public URL, rollback handle, and "publish requires approval" state. | Enabling real publish button/auth policy. |
| Source Write | Materialize approved snapshot. | Spec only: write to a narrow generated file path, never arbitrary path. | Actual source repo write. |
| Commit/Push | Preserve source history. | Spec only: one commit with scoped paths, no force-push. | Actual commit/push automation or token use. |
| Deploy Trigger | Make public page update. | Prefer existing deploy lane and record run id. | Triggering deploy/invalidation. |
| Verify | Confirm public URL reflects expected marker. | Spec only: verification checklist. | Live public verification after deploy. |
| Audit | Record what happened. | Extend `control_center_activity` schema conceptually with publish actions. | Writing audit entries from real publish. |
| Rollback | Return to prior known-good commit/snapshot. | Spec only: rollback handle points to previous commit/snapshot and expected command. | Executing rollback, revert, redeploy, or force operations. |

## Minimal Target Recommendation

Use `status-control-center-feed` as the first target, not Family Wedding production copy.

Reason:

- The Status Control Center surface already exists and is operationally owned by the same system.
- It can publish a generated status feed or static registry artifact without changing user-facing wedding content.
- It still exercises the important pipeline pieces: snapshot, diff preview, source write, commit/push, deploy, URL verification, audit, rollback.

Family Wedding NOTICE can remain a later target after the publish mechanism proves it can write only the intended generated file.

## Data Contract

Draft publish snapshot:

```json
{
  "target": "status-control-center-feed",
  "source": "control_center_nodes",
  "snapshot_id": "timestamp-or-uuid",
  "node_count": 0,
  "visible_only": true,
  "generated_paths": [],
  "expected_public_urls": [],
  "previous_commit": "",
  "rollback_handle": "",
  "requires_approval": true
}
```

Activity actions to add later:

- `publish.previewed`
- `publish.approved`
- `publish.written`
- `publish.pushed`
- `publish.deployed`
- `publish.verified`
- `publish.rollback_planned`
- `publish.rolled_back`

For now these are names in the spec only; no table migration or app mutation happened.

## Auth And Permission Boundary

Minimum future model:

- Read/preview can stay available to the current operator surface.
- Real publish must require an explicit authenticated operator session.
- The server route that can write source files or trigger deploy must not be reachable as a casual public POST.
- Tokens must stay server-side only, ideally in Kubernetes Secret or existing deployment secret manager.
- Publish requests should fail closed if target, path, branch, or commit state is ambiguous.

Approval needed before any of the above is implemented.

## Rollback Rule

Rollback should be a first-class planned action, not an emergency shell memory.

For each publish, store:

- previous source commit
- new source commit
- target public URL
- generated paths
- verification marker
- rollback method: `revert commit + deploy lane`, not force-push

Destructive rollback, force-push, direct production overwrite, and secret changes remain out of scope without explicit approval.

## Decision Needed

Question for the user:

> Control Center publish pipeline을 먼저 어떤 범위로 열까요?

Recommended default:

1. **Dry-run only first**: implement snapshot + diff preview + approval screen, with no source write/deploy.

Other options:

2. **Single target publish**: after approval, allow `status-control-center-feed` only to write a generated file, commit/push, deploy, verify, and record rollback handle.
3. **Wait**: leave build-09 parked until auth/permission expectations are decided.

## Verification

- Read build-08 report and current CMS code only.
- Produced design/spec artifact only.
- No production page write/deploy.
- No auth/permission change.
- No source repo write in `space`.
- No commit/push automation implementation.
- No deploy trigger.
- No rollback execution.
- No secrets read or changed.
