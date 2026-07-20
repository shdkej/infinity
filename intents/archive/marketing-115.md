# [marketing-115] Virtue AI 검색 인용성 감사표 작성

- id: marketing-115
- status: archived
- completed_at: 2026-07-20T10:07
- projects: [virtue, infinity]
- task_type: strategy
- topics: [marketing, ai-agents, product]
- result_summary: Virtue의 인앱 job/first value/trust boundary는 읽히지만 공개 AI 검색 인용 표면에서는 brand entity, category, claim evidence, structured discovery가 약하다고 판정하고 canonical answer block 초안을 남겼다.
- artifacts:
  - path: artifacts/marketing-115/ai-search-citation-audit.md
    role: strategy
    note: AI/agent discovery 관점의 1장 감사표와 canonical answer block 초안
- reports:
  - path: reports/marketing-115/2026-07-20T1007Z.html
    role: final
- commits:
  - repo: infinity
    sha: f527f7e
    note: archive/report/artifact 기록
- urls:
  - url: https://virtue.oracle.shdkej.com
    note: 감사 시점에 `curl -k` 기준 nginx 404 응답
- next_actions:
  - 공개 반영은 별도 승인 후 metadata 1문장, trust-boundary 1문장, robots/sitemap/llms 또는 about 표면 후보로 진행한다.
  - API/MCP/do-for-you agent surface는 현재 Virtue의 사람 경험·선택형 제품 성격과 맞지 않으므로 열지 않는다.

## Axis

- axis ax1: Virtue의 인앱 first value와 trust boundary는 보이지만, 공개 검색/agent discovery 표면에서는 브랜드명·카테고리·claim evidence가 약하다.
- axis ax2: 공개 변경 전 내부 canonical answer block을 확정했고, 다음 구현 후보는 승인 기반 public metadata/discovery 표면 보강이다.

## Completion Notes

- 성공 기준 충족: 감사표가 `있음 / 약함 / 없음 / 공개 반영 승인 필요` 축으로 brand entity, category, job, first value, trust boundary, claim evidence를 분류했다.
- 첫 검증 게이트 충족: 라이브 URL과 로컬 레포만 읽고 AI/agent가 Virtue를 설명할 때 쓸 5문장 초안을 도출했다.
- 금지선 준수: 공개 카피, 배포, production code, 계측, 외부 발송, 비용, 계정 연결을 변경하지 않았다.
