# marketing-84 Virtue 첫 저장 뒤 next-step bridge 감사표/제안서

- id: marketing-84
- status: active
- created_at: 2026-06-25T10:07Z
- updated_at: 2026-06-25T10:07Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, retention]
- permission_level: L1 docs-only
- owner_route: Infinity Inbox -> Claude Code
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-25-time-to-next-value-bridge.md
- report: reports/marketing-84/2026-06-25T1007Z-handoff.html

## Current State

The source note is present and already narrows the problem to post-save return flows. No prior active record or report existed for `marketing-84`, so this cycle records a bounded handoff instead of assuming implementation details.

## Next Scope

1. Inspect the Virtue surfaces named in the source note:
   - `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`
   - `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/add/page.tsx`
2. Produce a one-page audit/proposal that maps J1-J4 to:
   - what proof remains after first value
   - what the primary next action should be
   - which return surface is canonical
3. Verify the proposal against the existing gate:
   - a reviewer should be able to explain the next action within 3 seconds after reading the return flow

## Boundaries

- Docs-only. No production code changes, deploys, tracking, privacy, or external-cost actions.
- Keep the work bounded to first-save and immediate return surfaces; do not broaden into full onboarding redesign.
