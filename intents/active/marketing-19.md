# marketing-19 Virtue 신규 사용자 홈 화면 FAE 감사표

- id: marketing-19
- status: in_progress
- mode: prepare+draft (cloud 완료) → execute_local
- priority: medium
- permission: L1
- created_at: 2026-05-26T12:00Z

## 다음 액션 (Local Claude Code)

```
Infinity Intent: marketing-19 Virtue 신규 사용자 홈 화면 FAE 감사표
Mode: execute_local
Required workflow: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present. Record workflow-master absence if not found.
Goal: artifacts/marketing-19/home-fae-audit-draft.md 내용을 virtue-rebirth-app apps/web/docs/home-fae-audit.md로 생성 후 커밋·push
Context: virtue-rebirth-app master (현재 HEAD f74cf59), infinity repo artifacts/marketing-19/home-fae-audit-draft.md
Prepared findings: J1~J4 FAE 방향판 감사표·3문 기준(무엇을 먼저/왜 지금/하면 무엇이 생김)·이벤트 관찰 게이트·선행 6문서 정합 확인 완료
Allowed: L0/L1 + L2 agent-approved push (doc-only 1파일 신규)
Forbidden: 코드·카피·이벤트·대시보드 변경 / 외부 발송
Verification: git diff --stat doc-only / 충돌마커 grep 0 / HEAD==origin/master / 선행 3문서 충돌 0
Report back to: reports/marketing-19/{timestamp}.html (결론 2축 양식, ARTIFACT_RULES.md 참조)
```

## 참조

- artifact: `artifacts/marketing-19/home-fae-audit-draft.md`
- cloud report: `reports/marketing-19/2026-05-26T1200Z-cloud.html`
- source note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-home-dashboard-fae.md`
