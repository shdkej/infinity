# marketing-68 — Virtue Agent-Readable Surface Audit

- id: marketing-68
- status: archived
- completed_at: 2026-06-19T00:00Z
- projects: [virtue]
- task_type: strategy
- topics: [ai-agents, trust, prelaunch]
- result_summary: 4개 표면(Landing metadata / README / llms.txt 후보 / In-app 카피) × 5축(current evidence / agent may read / agent must not infer / human handoff wording / launch-after reuse) 감사표 완성. 공통 경계 1세트 확립, human handoff wording 후보 4개. 신규 이벤트·production code·deploy·public copy·robots/llms·tracking/privacy·PostHog·external message·cost 변경 0건.

## Goal

HUMAN 2026 AI traffic benchmark + OpenAI agent guide 근거로, Virtue의 agent-readable 공개 표면에서 AI 판결 프레임이 에이전트에게 오독될 위험을 내부에서 점검하고 경계 기준표 작성. prelaunch low-signal 유지.

## Success Criteria (충족 여부)

- [x] Surface / agent may read / agent must not infer / human handoff wording / launch-after reuse 축이 모두 존재
- [x] marketing-65 / marketing-66 / marketing-67 최소 1회 이상 참조
- [x] 신규 이벤트·tracking/privacy·PostHog·production code·deploy·public copy·robots/llms 실제 배포·external message·cost 변경 0건
- [x] conflict markers 0
- [x] HTML report gate 통과 (html, body, axis ax1, axis ax2, details 포함 확인)

## artifacts

- path: artifacts/marketing-68/agent-readable-surface-audit.md
  role: design
  note: 4개 표면 × 5축 감사표, 공통 경계, human handoff wording 후보 4개, 구조적 제약, Marketer 인수인계

## reports

- path: reports/marketing-68/2026-06-19T0000Z.html
  role: final

## commits

- repo: infinity
  note: 2026-06-19 Heartbeat — marketing-68 Inbox 처리, artifact + archive + report 생성, INTENTS.md 정리

## urls

## next_actions

- llms.txt 초안 작성은 이 표 공통 경계 그대로 사용 가능 (작성 L1, 실제 배포 approval-needed) → Inbox 등록 후보
- In-app 카피 판결→관점 프레임 정렬 proposal (m45 계승, 공개 변경 approval-needed)
- public copy/FAQ/onboarding 작성 시 이 표의 human handoff wording 후보를 기준 초안으로 사용 (approval-needed)
