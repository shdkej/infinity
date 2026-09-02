# wiki-retrieval-test-20q-01 — Agent Wiki 20문항 회수성 검증

- status: archived
- archived_at: 2026-09-02T08:10:00Z
- execution_mode: multi_subagent_roles
- source_context_pack: `intents/context/wiki-retrieval-test-20q-01.json`
- artifact: `artifacts/wiki-retrieval-test-20q-01/retrieval-matrix.md`
- report: `reports/wiki-retrieval-test-20q-01/20260902T0810Z-final.md`
- red_status: pass
- red_report: `artifacts/wiki-retrieval-test-20q-01/red-report.md`
- role_sessions: ai=`/root/wiki_ai`; architecture=`/root/wiki_architecture`; lifestyle=`/root/wiki_lifestyle`; operator=`/root`; red=`/root/red_wiki_retrieval`

## 결론

Agent Wiki만으로 Found 6/20 (30%), Partial 6/20 (30%), Not found 8/20 (40%)였다. 8×8 분류 수보다 고유명사·수치·정형 목록 질문의 alias·FAQ·evidence locator 부족이 실제 병목이다.

## 지표·지식 판정

- metric_result: Found 6/20, Partial 6/20, Not found 8/20; 외부/raw 근거 0건.
- metric_next_decision: change — alias·FAQ·evidence locator를 Retrieval Card로 보강하는 별도 Intent를 검토한다.
- knowledge_status: used
- knowledge_decision: promote
- knowledge_targets: `agent-wiki/content/docs/log.mdx`
- knowledge_reflection: 개념 탐색은 축과 노드로 가능하지만 정확 질의의 회수성은 query surface에 좌우된다.
- knowledge_commit: agent-wiki@7e2e3d3

## 경계

Agent Wiki `content/docs/`만 근거로 사용했다. raw source·외부 웹·위키 본문 수정·공개 배포는 수행하지 않았다.
