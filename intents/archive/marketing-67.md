# marketing-67: Virtue AI Authorization Boundary Table

- id: marketing-67
- status: archived
- completed_at: 2026-06-18T12:00Z
- projects: [virtue]
- task_type: strategy
- topics: [ai-agents, trust, authorization, prelaunch]
- result_summary: J1-J4별 user_delegates·virtue_may_do·virtue_must_not_do·human_decision_required·evidence_to_show 5컬럼 권한 경계표 완성. WEF/Capgemini ACAP 관점을 Virtue prelaunch 신뢰 경계로 번역. 신규 이벤트·tracking/privacy·public copy·deploy·external message·cost 변경 0. 기존 marketing-38/45/65/66 충돌 0.

## Goal

WEF/Capgemini의 ACAP 관점에서 AI agent 신뢰는 기능보다 "무엇을 허용할 것인가"에서 생긴다고 본다. Virtue는 아직 자동 실행 agent는 아니지만, AI 판정이 사용자의 자기해석과 저장 행동에 영향을 주므로 J1-J4별 권한 경계를 내부 문서로 고정할 필요가 있다.

## Success Criteria (충족 여부)

- [x] 기존 trust evidence inventory(marketing-65)와 agentic context map(marketing-66)을 재정의하지 않고 계승
- [x] user_delegates, virtue_may_do, virtue_must_not_do, human_decision_required, evidence_to_show 5개 컬럼 모두 존재
- [x] 신규 이벤트·tracking/privacy·dashboard·public copy·production code·deploy·external message·cost 변경 0건
- [x] conflict markers 0
- [x] HTML report gate 통과

## artifacts

- path: artifacts/marketing-67/virtue-ai-authorization-boundary-table.md
  role: design
  note: J1-J4별 5컬럼 AI 권한 경계표, 공통 구조적 경계, 충돌 점검, Marketer 인수인계

## reports

- path: reports/marketing-67/2026-06-18T1200Z.html
  role: final

## commits

- repo: infinity
  note: 2026-06-18 Heartbeat — marketing-67 Inbox 처리, artifact + archive + report 생성, INTENTS.md 정리

## urls

## next_actions

- onboarding·FAQ·public explainer 작성 시 이 표의 virtue_must_not_do·human_decision_required를 사용자 안내 기준으로 사용 (approval-needed)
- first-10 관찰에서 "AI에게 무엇을 맡긴다고 느꼈는가" 질문 설계 시 user_delegates 컬럼 활용
- llms.txt 후보로 재사용 시 별도 L2 승인 필요
