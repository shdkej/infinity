# marketing-77 Virtue 승인된 마케팅 UI/카피 구현 패킷

- id: marketing-77
- status: active
- created_at: 2026-06-22T11:25Z
- projects: [virtue]
- task_type: implementation
- topics: [marketing, activation, product, ui-copy]
- trigger: user said `마케팅 작업 승인`
- approval: user-approved
- approval_scope:
  - product UI/copy implementation for recent Virtue marketing recommendations
  - scoped local code/copy changes
  - normal non-force commit/push after verification if safe
- excluded_from_approval:
  - external announcements or messages
  - paid actions or new costs
  - new tracking/privacy instrumentation or analytics events
  - credential, permission, or secret changes
  - force push or irreversible production operations

## Source Recommendations

- `marketing-70`: home empty-state proof gap and implementation ordering. J3 is better served by `/add` result preview than home proof alone.
- `marketing-71`: seeded proof should use explicit sample/preview labeling.
- `marketing-73`: recommended J3 bridge is Option C, a home empty-state ghost AI result card; Option B is the conservative CTA hint.
- `marketing-74`: `/add` first surface should bridge result expectation and permission safety; recommended wording direction is 권한 안심형.
- `marketing-75`: `/add` first surface and result card are Tier 3; home empty state is Tier 2.
- `marketing-76`: `/add` and result card guidance are Yes; home empty state guidance is No, so home work should stay proof-preview rather than explanation-heavy.

## Implementation Order

1. Inspect the Virtue app surfaces for `/`, `/add`, and result card components.
2. Pick the smallest coherent packet from:
   - `/add` expectation/permission bridge
   - result-card contextual guidance
   - home empty-state ghost/sample proof preview
3. Implement only the chosen packet.
4. Verify no new tracking/privacy/external/cost/credential changes.
5. Run the relevant local checks.
6. Create an HTML report that records changed surfaces, approval source, safety boundaries, and verification result.

## Success Criteria

- Diff is limited to Virtue product UI/copy and supporting docs/report.
- Copy does not imply automatic public posting, moral judgment automation, or hidden AI authority.
- Preview/sample UI is visibly marked as non-real data if used.
- No tracking/privacy/public announcement/cost/credential changes.
- Build/test/lint or equivalent local check passes, or any blocker is recorded before implementation is considered complete.

## Completion Notes

- Do not archive until implementation and verification are actually complete.
- If the app worktree has unrelated dirty changes or deployment ambiguity, record Waiting rather than overwriting.
