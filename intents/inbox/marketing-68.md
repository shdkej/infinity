# marketing-68 — Virtue Agent-Readable Surface Audit

- title: Virtue agent-readable surface audit
- created_at: 2026-06-18T22:00:00Z
- status: inbox
- projects: [virtue]
- type: strategy
- topics: [ai-agents, agentic-web, trust, discoverability, prelaunch]
- source_note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-18-agentic-web-access-policy.md`
- permission_level: L1 docs-only
- owner_route: Infinity → Claude Code 또는 SAM 로컬 문서 작업

## Rationale

HUMAN 2026 benchmark는 agentic AI traffic이 웹을 읽는 단계를 넘어 상호작용 단계로 이동하고 있음을 보여준다. Virtue는 아직 prelaunch라 획득 채널로 해석하면 안 되지만, AI/검색/브라우저 agent가 제품을 읽을 때 `덕행 판정 대행`이나 `도덕적 자동 판단`으로 오독되지 않도록 접근 정책과 설명 경계를 내부에서 점검할 필요가 있다.

## Expected Impact

- launch 전에 agent-readable 설명의 오독 위험을 낮춘다.
- 향후 `llms.txt`, FAQ, public explainer, AI search answer check에 재사용할 기준표를 만든다.
- 기존 marketing-65 trust evidence, marketing-66 context map, marketing-67 authorization boundary를 공개 표면 준비로 연결한다.

## Scope

- 허용: live site와 repo의 public metadata/readme/docs read-only 확인, 기존 marketing artifacts 참조, L1 내부 감사표 1개 작성.
- 금지: production code 변경, deploy, public copy 반영, robots/llms 실제 배포, privacy/tracking/PostHog 설정 변경, 외부 발송, 비용 발생.

## Proposed Output

`artifacts/marketing-68/agent-readable-surface-audit.md` 또는 HTML report에 아래 축을 정리한다.

| Surface | current evidence | agent may read | agent must not infer | human handoff wording | launch-after reuse |
| --- | --- | --- | --- | --- | --- |
| Landing metadata | 확인 필요 | 제품 목적 | 도덕 판단 대행 | 사람의 선택 보존 | SEO/AI answer |
| FAQ/explainer | 확인 필요 | AI 판정 경계 | 자동 행동 지시 | 저장/공유는 사용자 결정 | public FAQ |
| llms.txt 후보 | 미배포 | 읽기용 요약 | 민감 데이터 접근 | 앱 내 사용자 동의 필요 | launch artifact |

## Success Criteria

- `Surface`, `agent may read`, `agent must not infer`, `human handoff wording`, `launch-after reuse` 축이 모두 있다.
- marketing-65/66/67의 기존 신뢰·문맥·권한 경계를 최소 1회 이상 참조한다.
- 신규 이벤트, tracking/privacy, PostHog, production code, deploy, public copy, robots/llms 실제 배포, external message, cost 변경이 0건임을 문서에 명시한다.

## First Verification Gate

1. `rg -n "agent may read|agent must not infer|human handoff wording|launch-after reuse" <output>`
2. `rg -n "marketing-65|marketing-66|marketing-67" <output>`
3. `rg -n "production code|deploy|public copy|robots|llms|tracking|privacy|PostHog|external message|cost|0건" <output>`
4. `rg '<<<<<<<|=======|>>>>>>>' <output> || true`
