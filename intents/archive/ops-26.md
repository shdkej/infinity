# [ops-26] 산출물 Intent 지표 질문 적용

- id: ops-26
- status: archived
- completed_at: 2026-08-21T20:12Z
- target_agent: genie
- execution_mode: single_genie_roles
- projects: [infinity, openclaw]
- task_type: maintenance
- topics: [workflow, analytics, automation]
- result_summary: 모든 비단순 산출물 Intent에 대표 지표 질문·신호·판정 규칙을 연결하고 대시보드 상세 표시와 전용 검사를 추가했다.
- metric_question: 지표 질문 계약이 산출물 Intent의 다음 결정에 실제로 연결되는가?
- metric_result: pass
- metric_next_decision: continue
- artifacts:
  - path: artifacts/ops-26/metric-contract.md
    role: design
    note: 지표 질문 계약과 적용 범위
- reports:
  - path: reports/ops-26/20260821T2008Z.html
    role: final
- commits:
  - repo: infinity
    sha: 0e0a59b
    note: 지표 질문 계약·검사·대시보드 반영
- urls: []
- next_actions:
  - 다음 산출물 Intent부터 metric contract 검사와 완료 report 필드를 적용한다.

## Archive Card

[프로젝트]
Infinity 산출물 Intent 지표 계약

[상태]
운영 규칙 반영 완료

[결과 기준]
모든 비단순 산출물 Intent가 지표 질문·신호·판정 규칙을 갖고 완료 시 결과·다음 결정을 남긴다.

[다음 행동]
다음 산출물 Intent부터 새 계약을 적용한다.
