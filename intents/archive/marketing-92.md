# marketing-92 Virtue 홈 반환 상태 gating 구현/검증

- id: marketing-92
- status: archived
- completed_at: 2026-06-29T1829Z
- projects: [virtue, infinity]
- task_type: implementation
- topics: [marketing, activation, retention]
- result_summary: 홈 최근 덕행 empty-state를 `stats.count`와 `recent.length`로 분리해, 복귀 사용자가 첫 방문 카피를 다시 보지 않도록 gating 분기를 구현하고 정적 검증했다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx
    role: implementation
    note: 홈 recent empty-state 분기 구현
- reports:
  - path: reports/marketing-92/2026-06-29T1829Z.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: 5a99501
    note: 홈 return-state gating 패치
- next_actions:
  - 실제 브라우저 복귀 세션에서 localStorage 복원 타이밍까지 보고 싶으면 별도 verification intent로 분리한다.

## Result

- `apps/web/src/app/page.tsx`에 `isReturningWithoutRecent`를 추가했다.
- `stats.count === 0`인 경우에만 first-visit 설명/CTA 문맥을 유지한다.
- `stats.count > 0 && recent.length === 0`이면 최근 덕행 카드에서 retained proof surface가 비어 있는 복귀 상태로 취급해 "최근 덕행을 불러오는 중이에요." 카피를 보여준다.
- `pnpm --filter virtue-rebirth-app typecheck`는 통과했다.
- `pnpm lint`는 기존 `react-hooks/set-state-in-effect` 경고 4건만 보고했고, 이번 변경으로 새 오류는 생기지 않았다.

## Links

- source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-29-return-state-gating-over-copy.md`
- report: `reports/marketing-92/2026-06-29T1829Z.html`
- implementation file: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`
