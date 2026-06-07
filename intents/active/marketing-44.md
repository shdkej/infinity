# marketing-44 Virtue 결과 카드 직후 30초 행동 감사표

- id: marketing-44
- status: in_progress
- priority: medium
- permission: L1
- mode: prepare (cloud done) → execute_local
- added: 2026-06-07T10:03Z

## Goal

AI 결과 카드(`deed_judged` 발화) 직후 30초 내 행동 흐름을 잡별로 분류하는 관찰 감사표를 `apps/web/docs/post-response-flow-audit.md`에 작성한다.

## Success Criteria

- `apps/web/docs/post-response-flow-audit.md` 신규 생성 (docs-only)
- J1~J4별 결과 직후 30초 행동 분류와 do-not-send 조건 포함
- 이벤트 앵커 drift 0 (`deed_judged`:106, `deed_rerolled`:78, `deed_saved`:183, `deed_save_capped`:199)
- conflict marker 0, code diff 0
- First verification gate: 첫 10명 또는 첫 7일에 비율/retention 결론 없이 관찰표가 행 단위로 채워질 수 있는지만 확인

## 다음 액션 (Local Claude Code 위임)

Cloud prepare 완료. Local Claude Code에 위임할 프롬프트:

```
Infinity Intent: marketing-44 Virtue 결과 카드 직후 30초 행동 감사표 작성
Mode: execute_local
Invocation: Prefer pt/purplemux Claude pane via `tmux -L purple`
Goal: infinity repo의 artifacts/marketing-44/post-response-flow-audit-draft.md를 참조해
      /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/post-response-flow-audit.md를 생성한다.
Context:
  - artifacts/marketing-44/post-response-flow-audit-draft.md (cloud draft)
  - MARKETING_LEARNINGS.md (계승 기준 확인)
  - 기존 docs: apps/web/docs/first-week-reactivation-boundary-table.md (형식 참고)
Allowed: L1 docs-only. 기존 이벤트 앵커만 인용.
Forbidden: 신규 이벤트/tracking/privacy/대시보드/세션리플레이/외부발송/비용/권한 변경. code diff 0.
Verification: event anchor drift 0, conflict marker 0, code diff 0
Report: reports/marketing-44/{timestamp}.html (HTML, axis ax1/ax2 포함)
```

## Context

- 대상 repo: `/home/ubuntu/dev/virtue-rebirth-app`
- 대상 파일: `apps/web/docs/post-response-flow-audit.md`
- Cloud prepare artifact: `infinity:artifacts/marketing-44/post-response-flow-audit-draft.md`
- 참고 문서: `apps/web/docs/first-week-reactivation-boundary-table.md` (형식)
- Source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-07-ai-post-response-flow.md`
