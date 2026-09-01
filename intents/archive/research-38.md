# research-38 — Agent Wiki 목차의 에이전트 검색 효율 감사

- status: archived
- archived_at: 2026-09-01T20:00Z (correction)
- execution_mode: multi_subagent_roles
- source_context_pack: `intents/context/research-38-correction.json`
- artifact: `artifacts/research-38/mandalart-core-traversal-correction.md`
- report: `reports/research-38/20260901T-correction-pass.html`
- red_status: pass
- red_report: `artifacts/research-38/red-correction-report.md`
- role_sessions: planner=`/root/role_research_38c_planner`; developer=`/root/role_research_38c_developer`; marketer=`/root/role_research_38c_marketer`; operator=`/root/role_research_38c_operator`; red=`/root/role_research_38c_red`

## 결론

기존 124 MDX·상위 컬렉션 기반 8×8 결론은 superseded다. 8축의 현 source/mapped inventory는 62개(Health=7, Idea=7)이며 변환 누락은 0개다. `index → map`은 통과하나 map→8축 링크가 0개여서 중앙 node traversal은 0/62다. 별도 승인 후 map에 8축/62노드 additive 링크와 fixture를 추가한다.

## 지표·지식 판정

- metric_result: source=62, mapped=62, 누락=0; index→map=1, map→축=0/8, 중앙 node traversal=0/62, 직접 route=62/62; 다음 결정은 `change`.
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; index.mdx; mapped/source-category-map.mdx; DOCUMENT_SEARCH_PIPELINE.md
- knowledge_reflection: 8×8의 명목 64와 실제 62-node 원본 inventory를 구분하고, source/mapped 누락 여부는 축별 set 대조로 판단한다.
- knowledge_commit: no-promotion-needed

## 경계

Agent Wiki, 사이드바, 배포, 공개 변경은 수행하지 않았다. 구현은 별도 승인 Intent가 필요하다.
