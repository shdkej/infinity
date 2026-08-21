# [ops-26] 산출물 Intent 지표 질문 적용

- id: ops-26
- status: active
- target_agent: genie
- priority: high
- permission: L1 내부 문서·대시보드 규칙 수정 + 정상 commit/push
- requested: 2026-08-21T20:03Z
- execution_mode: single_genie_roles
- projects: [infinity, openclaw]
- task_type: maintenance
- topics: [workflow, analytics, automation]
- goal: 모든 비단순 산출물 Intent가 다음 결정을 바꾸는 대표 지표 질문을 갖고 실행·완료 보고까지 연결되게 한다.
- success_criteria: INFINITY_OPERATING_RULES.md, heartbeat.md, dashboard 핵심 필드가 같은 metric contract를 사용하고, consistency 검증과 Red 검증을 통과하며, Infinity와 Knowledge Lab 원격에서 확인된다.
- metric_question: 지표 질문 계약이 산출물 Intent의 다음 결정에 실제로 연결되는가?
- metric_signal: 정본 문서 3곳의 동일 필드 정의, INTENTS consistency 검사, Red의 방향·다음 액션·선택·요청 적합성 판정
- metric_decision_rule: 세 문서와 검증이 일치하면 continue, 불일치하면 change, 외부 원격 반영이 막히면 hold
- next_action: 문서 수정 후 consistency/중복 문구/원격 가시성을 검증하고 Red 검토를 남긴다.
