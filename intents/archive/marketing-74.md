# marketing-74 Virtue /add 입력 전 기대 형성 비교안

- id: marketing-74
- status: archived
- completed_at: 2026-06-22T0600Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, product, onboarding]
- result_summary: /add 입력 전 기대 형성 3안(현행/sample 결과 1줄/결과+권한 경계 1줄) 비교 완료. Option B(sample 결과 1줄)가 J3 hesitation 해소 최우선 추천안. J4 경계 문구는 결과 카드 footer 배치 권고. 구현은 approval-needed.
- artifacts:
  - path: artifacts/marketing-74/virtue-add-preinput-compare.html
    role: design
    note: /add 입력 전 기대 형성 3안 비교표. J1/J3/J4 오해 위험·J3 기대 형성·J4 경계 인지·구현 난이도 정리.
- reports:
  - path: reports/marketing-74/2026-06-22T0600Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - Option B(sample 결과 1줄) 구현 — approval-needed (copy/UI 변경, 별도 intent)
  - J4 권한 경계 문구 위치 결정 (결과 카드 footer vs /add 입력 전) — approval-needed (별도 intent)
  - 내부 관찰로 J3 hesitation 신호 확인 후 3안 중 단일 선택

## Collaboration Context

- source_agent: Infinity Heartbeat
- target_agent: Marketer / Cloud docs
- request_type: docs-only strategy compare
- approval_boundary: L1 docs-only
- user_visible: false
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-21-add-preinput-proof-bridge.md

## Outcome

- `/add` 첫 표면의 J3/J4 hesitation gap을 3개 안으로 구조화하고, 각 안의 오해 위험과 구현 난이도를 비교했다.
- 추천안 B: sample 결과 1줄 — J3 기대 형성 직접 해소, J1/J2 부담 최소, 구현 최소.
- J4 권한 경계 문구는 입력 전보다 결과 카드 footer에 배치하는 것이 정보 순서상 자연스럽고 부담이 적다 (결과를 본 뒤 경계 인지).
- 세 안 모두 문구는 관점 프레임("AI가 본 오늘") 유지 전제. 구현·카피 변경은 별도 승인 필요.

## Inherited Learning

- Decision-Delegation Risk Rides The Verb (m45): 예시 문구는 관점 프레임 유지. "AI 채점" 금지.
- First-Input Defaults Steer The Job (m32): 예시가 J3를 조향하면서 J1/J4에 영향 최소화.
- Guided First-Value Is A Four-Stage Handoff (m51): 첫 입력 전 구간 handoff에서 사용자 행동권 보존.
- marketing-71 seeded proof: sample/preview 표식 원칙 계승.
- marketing-73 J3 AI bridge: ghost AI 결과 카드 방식 계승.

## New Learning (이번 작업)

- J4 경계 우려의 최적 노출 타이밍은 입력 전이 아니라 결과 카드 단계다. 정보 순서(결과 먼저, 경계 나중)가 신뢰 부담을 줄인다.
- 같은 경계 문구도 위치에 따라 J1/J2 부담이 달라진다 — 입력 전은 부담 중간, 결과 후는 부담 최소.

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
