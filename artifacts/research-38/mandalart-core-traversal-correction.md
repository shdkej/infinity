# research-38 정정 — 만다라트 8축 mapped traversal 감사

## 정정 범위와 supersession

이 문서는 기존 `agent-wiki-retrieval-ia-audit.md`와 `20260901T-final-pass.html`의 **8×8 관련 결론을 대체**한다. 기존 124 MDX·상위 컬렉션 중심 감사는 Agent Wiki 전체 탐색 진단으로만 남고, 만다라트 8×8의 노드 수·커버리지·traversal 결론으로 사용하지 않는다.

포함: `Fundamental`, `Deep Knowledge` → `mapped/deep-knowledge`, `Integration`, `Communication`, `Health`, `Human`, `Idea`, `Meta`의 source `.md`와 mapped `.mdx` 전수.

제외: `blog`, `mapped/README`, Portfolio와 다른 상위 폴더·컬렉션. `index.mdx`와 `mapped/source-category-map.mdx`는 traversal 관문으로만 검사했다.

## 8×8 기대와 실제 인벤토리

| 축 | source | mapped | 직접 route | source↔mapped |
|---|---:|---:|---:|---|
| Fundamental | 8 | 8 | 8 | 일치 |
| Deep Knowledge → `deep-knowledge` | 8 | 8 | 8 | 일치 |
| Integration | 8 | 8 | 8 | 일치 |
| Communication | 8 | 8 | 8 | 일치 |
| Health | 7 | 7 | 7 | 일치 |
| Human | 8 | 8 | 8 | 일치 |
| Idea | 7 | 7 | 7 | 일치 |
| Meta | 8 | 8 | 8 | 일치 |
| **합계** | **62** | **62** | **62** | **누락 0** |

**결론:** 8×8은 분류 틀(명목 64칸)이나, 현 원본은 Health=7·Idea=7이므로 현재 inventory는 **62개**다. source와 mapped의 이름 집합은 축별로 일치한다. 따라서 빠진 2개는 mapped 변환 누락이 아니며, 원본에 선언된 64-node manifest나 이름이 없으므로 임의로 이름을 붙이지 않는다.

## 축별 노드 목록

- Fundamental (8): Architecture, Coding, Computer_Architecture, Data_Structure, Infra, Math, Network, Software
- Deep Knowledge / `deep-knowledge` (8): AI/ai, Container/container, Data/data, Devops/devops, Monitoring/monitoring, Operation/operation, Product/product, Web/web
- Integration (8): Business, Creator, Design, Economics, Exploration, Marketing, Tool, Work
- Communication (8): Blogging, Document, Feedback, Foreign_language, Logical_Thinking, Open_Source, Talk, Teamwork
- Health (7): Curiosity, Decision, Food, Investment, Music, Physical, Routine
- Human (8): Balance, Evolve, Future, Love, Principle, Readability, Reality, Standard
- Idea (7): Article, History, Information, Journal, Movie, Reading, Travel
- Meta (8): AGENTS, About_Architecture, About_Development, Collection, Developer, Fail_experience, My_space, Troubleshooting

## 실제 traversal

| 경로 | 결과 | 근거 |
|---|---|---|
| `index → source-category-map` | 통과 (1 edge) | index의 `[[mapped/source-category-map]]` 대상 파일 존재 |
| `source-category-map → 8축` | 실패 (0/8) | map은 8개 heading/설명만 있고 wikilink·Markdown 문서 링크 0개 |
| `8축 → 62개 노드` | 막힘 (0/62) | 축 hub/anchor 및 node link가 없음 |
| 각 mapped node 직접 route | 통과 (62/62) | 모든 대상 `.mdx` 파일·정적 route 존재 |

대표 재현: `index → map → Fundamental → Architecture`, `… → deep-knowledge → AI`, `… → Health → Routine`, `… → Idea → Travel`은 모두 map에서 축 링크가 없어 실패한다.

## 정정 판정과 후속 수용 기준

- `metric_result`: required 중앙 traversal에서 축 0/8, 노드 0/62 도달; source↔mapped 누락 0.
- `metric_next_decision`: `change` — 8축·62개 노드의 실제 링크를 갖춘 additive map을 별도 승인 Intent에서 구현한다.
- 최소 수용 기준: `index→map=1`, `map→axis hub/anchor=8`, `axis→declared node=62`, source=mapped=62, target route=62를 검사한다. 64를 하드코딩하지 않는다.
- 롤백: 첫 변경은 map/index/축 hub의 additive 링크만 허용하고 경로 이동은 금지한다. 문제 시 해당 추가 커밋만 revert한다.

## 역할 종합

- Planner: 62를 현 재고로 고정하고, 기존 전체-위키 진단을 8×8 판정에서 분리한다.
- Developer: source/mapped 모든 8축에서 set difference 0이며, Deep Knowledge와 `deep-knowledge`의 표기/경로 매핑을 명시한다.
- Marketer: “8×8” 단독 대신 “8개 축·현재 62개 노드”로 표시해 완성된 64개라는 오해를 막는다.
- Operator: link fixture와 manifest로 1/8/62 traversal을 재현하고 62-node bijection을 검증한다.

근거: `agent-wiki/content/docs/index.mdx`, `mapped/source-category-map.mdx`, `source/shdkej-content/{8축}`, `agent-wiki/content/docs/mapped/{8축}`, `source.config.ts`.
