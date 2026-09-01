# research-38 — Agent Wiki 목차의 에이전트 검색 효율 감사

- status: archived
- archived_at: 2026-09-01T19:00Z
- execution_mode: multi_subagent_roles
- source_context_pack: `intents/context/research-38.json`
- artifact: `artifacts/research-38/agent-wiki-retrieval-ia-audit.md`
- report: `reports/research-38/20260901T-final-pass.html`
- red_status: pass
- red_report: `artifacts/research-38/red-report.md`
- role_sessions: planner=`/root/role_research_38_planner`; developer=`/root/role_research_38_developer`; marketer=`/root/role_research_38_marketer`; operator=`/root/role_research_38_operator`; red=`/root/role_research_38_red`

## 결론

8×8 원본 지도는 유지한다. 에이전트 검색에는 목적형 진입층, 실제 링크를 갖는 원본 지도, 메타데이터·link lint·retrieval fixture의 회귀 게이트를 별도 승인 후 additive로 추가한다.

## 지표·지식 판정

- metric_result: 4개 대표 경로 중 1개만 명확히 2단계 이내; 다음 결정은 `change`.
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; index.mdx; mapped/source-category-map.mdx; DOCUMENT_SEARCH_PIPELINE.md
- knowledge_reflection: 원본 분류와 사용자/에이전트의 과업 언어를 한 층에 섞지 않는다.
- knowledge_commit: no-promotion-needed

## 경계

Agent Wiki, 사이드바, 배포, 공개 변경은 수행하지 않았다. 구현은 별도 승인 Intent가 필요하다.
