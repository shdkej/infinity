# marketing-73 Virtue J3 첫 화면 AI 약속 브리지 비교안

- id: marketing-73
- status: archived
- completed_at: 2026-06-21T0700Z
- projects: [virtue]
- task_type: strategy
- topics: [marketing, activation, product]
- result_summary: J3 AI 브리지 3안(A hero 관점 문구 / B CTA 보조 힌트 / C 빈 상태 ghost AI 결과 카드) 비교 완료. Option C가 J3 기대 강화 최대·J1/J4 훼손 최소 추천안; Option B가 가장 보수적 차선. 구현은 approval-needed.
- artifacts:
  - path: artifacts/marketing-73/virtue-j3-ai-bridge-compare.html
    role: design
    note: J3 AI 브리지 배치 3안 비교표. 각 안별 J1/J4 훼손 위험·J3 기대 강화·안전성·구현 난이도 정리.
- reports:
  - path: reports/marketing-73/2026-06-21T0700Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - Option C(빈 상태 ghost AI 결과 카드) 구현 — approval-needed (code change, 별도 intent)
  - 동사 프레임 정렬 (버튼 `AI 채점` → 관점 프레임) — approval-needed (별도 intent)
  - 내부 사용자 관찰 후 3안 중 조합 또는 단일 선택

## Collaboration Context

- source_agent: Infinity Heartbeat
- target_agent: Marketer / Cloud docs
- request_type: docs-only strategy compare
- approval_boundary: L1 docs-only
- user_visible: false
- source_note: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-21-ai-curiosity-entry-gap.md

## Outcome

- 홈 `/`의 J3 AI 호기심형 진입 경로 공백을 3개 배치 옵션으로 구조화하고 각 안의 J1/J4 훼손 위험·J3 기대 강화·안전성을 비교했다.
- 추천안 C: 빈 상태 ghost AI 결과 카드 — J1/J4 훼손 최소 + J3 기대 강화 최대. marketing-70/71 seeded proof 방식 계승.
- 차선 B: CTA 보조 힌트 — footprint 최소, prelaunch 무변경 원칙에 가장 맞음.
- 세 안 모두 동사 프레임을 관점 프레임으로 유지하는 것을 전제. `AI 채점` 버튼 변경은 별도 승인 필요.

## Inherited Learning

- First Value Mapping (m06): J3 first value = deed_judged. 저장은 선택 범퍼.
- Product Body vs Bumper By Job (m31): 홈은 J3에게 범퍼/입구. 빈 상태가 AI 결과 미리보기 적합.
- Decision-Delegation Risk Rides The Verb (m45): 관점 프레임 vs 판결 프레임 분리.
- marketing-70/71: ghost/sample 표식 원칙을 J3 결과 카드로 확장.

## Safety

- production code changes: 0
- deploys: 0
- tracking/privacy changes: 0
- public copy changes: 0
- external messages: 0
- cost: 0
