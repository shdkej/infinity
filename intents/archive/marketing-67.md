# marketing-67 — Virtue AI Authorization Boundary Table

# marketing-67 · Virtue AI 권한 경계표 작성

- title: Virtue AI 권한 경계표 작성
- created_at: 2026-06-18T10:00:00Z
- status: inbox
- projects: [virtue]
- type: strategy
- topics: [ai-agents, trust, authorization, prelaunch]
- source_note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-18-agent-authorization-boundary.md`
- permission_level: L1 docs-only
- owner_route: Infinity → Claude Code 또는 SAM 로컬 문서 작업

## Rationale

WEF/Capgemini의 ACAP 관점은 AI agent 신뢰가 기능보다 "무엇을 허용할 것인가"에서 생긴다고 본다. Virtue는 아직 자동 실행 agent는 아니지만, AI 판정이 사용자의 자기해석과 저장 행동에 영향을 주므로 J1-J4별 권한 경계를 내부 문서로 고정할 필요가 있다.

## Expected Impact

- 첫 사용자가 AI 판정을 과신하거나 도덕적 단정으로 오해하는 위험을 낮춘다.
- prelaunch 첫 10명 관찰에서 "AI에게 무엇을 맡긴다고 느꼈는가"를 더 선명하게 읽는다.
- 향후 onboarding, FAQ, public explainer, llms.txt 후보로 재사용할 신뢰 경계 원본을 만든다.

## Scope

- 허용: 기존 Virtue docs와 marketing-65/66 산출물 읽기, L1 내부 문서 1개 작성, 기존 이벤트/카피/권한 경계 인용.
- 금지: production code, deploy, public copy 반영, privacy/tracking/PostHog 설정 변경, API/MCP 공개, 외부 발송, 비용 발생.

## Proposed Output

Virtue 앱 문서 또는 Infinity artifact에 J1-J4별 표를 작성한다.

| Job | user_delegates | virtue_may_do | virtue_must_not_do | human_decision_required | evidence_to_show |
| --- | --- | --- | --- | --- | --- |
| J1 | 기록의 해석 보조 | 판정/저장 보조 | 도덕적 단정 | 저장 여부 | 근거 문장 |
| J2 | 누적 성장 해석 | 누적 피드백 | 자동 행동 지시 | 계속 기록할지 | 레벨/누적 맥락 |
| J3 | AI 코멘트 확인 | 결과 카드 제공 | 저장 강요 | 저장/건너뛰기 | 판단 한계 |
| J4 | 회고 보조 | 의미 정리 | 외부 공유 | 공유/삭제/보관 | privacy boundary |

## Success Criteria

- 기존 trust evidence inventory와 agentic context map을 재정의하지 않고 계승한다.
- `user_delegates`, `virtue_may_do`, `virtue_must_not_do`, `human_decision_required`, `evidence_to_show` 5개 칼럼이 모두 있다.
- 신규 이벤트, tracking/privacy, dashboard, public copy, production code, deploy, external message, cost 변경이 0건임을 문서에 명시한다.

## First Verification Gate

1. `rg -n "user_delegates|virtue_may_do|virtue_must_not_do|human_decision_required|evidence_to_show" <output>`
2. `rg -n "신규 이벤트|tracking|privacy|public copy|deploy|external|cost|0건" <output>`
3. `rg '<<<<<<<|=======|>>>>>>>' <output> || true`


## Completion

- Completed: 2026-06-18T12:07Z cron cycle.
- Artifact: `artifacts/marketing-67/authorization-boundary-table.html`
- Gate: report contains required html/body/axis/details markers and J1-J4 authorization table.
- Scope: L1 docs-only; no production code, deploy, tracking/privacy, PostHog, public copy, external message, or cost change.
