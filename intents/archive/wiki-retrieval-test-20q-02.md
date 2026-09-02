# wiki-retrieval-test-20q-02 — Agent Wiki 20문항 회수성 재검증

- id: wiki-retrieval-test-20q-02
- status: archived
- execution_mode: single_genie_roles
- source_context_pack: `intents/context/wiki-retrieval-test-20q-02.json`
- artifact: `artifacts/wiki-retrieval-test-20q-02/retrieval-matrix.md`
- report: `reports/wiki-retrieval-test-20q-02/20260902T0928Z-final.html`
- red_status: pass
- red_report: `artifacts/wiki-retrieval-test-20q-02/red-report.md`
- role_sessions: internal role passes; no spawn tool exposed
- metric_result: Found 6/20, Partial 6/20, Not found 8/20; Q별 변화 0; 외부/raw 근거 0건.
- metric_next_decision: change — Retrieval Card로 고유명사·수치·정형 목록 질문의 alias/answer/locator를 보강한다.
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: 없음 (이번 변경은 새 일반 원칙이 아니라 기존 query-surface 교훈의 재확인)
- knowledge_reflection: 노드 추가와 회수성 개선은 별개다. 질의 대상의 answer/alias/locator가 없으면 새 탐색 노드가 있어도 기존 회수율은 변하지 않는다.
- knowledge_commit: no-promotion-needed
