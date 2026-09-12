# [research-github-skills-20260912] GitHub 리서치 스킬 후보 조사

- id: research-github-skills-20260912
- status: waiting
- target_agent: genie
- execution_mode: multi_subagent_roles
- projects: [infinity, research-bank, openclaw]
- task_type: research
- topics: [ai-agents, workflow, automation]
- context_pack: intents/context/research-github-skills-20260912.json
- trace: traces/research-github-skills-20260912.json
- notification_channel: slack
- notification_target: channel:C0BR41W31MM
- notification_reply_to: 1789247197.159489
- notification_origin: channel:C0BR41W31MM;reply_to:1789247197.159489
- decision_question: GitHub 공개 스킬 가운데, 마스터님의 반복 리서치 품질을 실제로 높이고 현재 시스템과 겹치지 않는 후보는 무엇인가?
- decision_owner: Kimi
- decision_deadline: 없음
- in_scope: GitHub 공개 스킬·스킬 컬렉션의 리서치 흐름, 출처 검증, 논문/웹 조사, 결과 구조화 기능; 설치 방식·라이선스·의존성·현재 스킬과의 중복 비교
- out_of_scope: 무검증 스킬 설치, 비공개 저장소 접근, 계정 연결·유료 API 결제, 기존 Infinity 리서치 규칙의 즉시 교체
- comparison_axes: 현재 기능 중복, 근거 추적력, 한국어/사용자 맥락 적합성, 설치·운영 비용, 안전 경계, 실험 난이도
- success_evidence: 공개 README와 실제 skill 파일을 열어 확인한 후보 5개 이상, 우선순위 3개 이하, 후보별 도입/비도입 근거와 첫 적용 실험 1개
- metric_question: 추천 후보가 기존 deep-research·Infinity 계약보다 실제로 더하는 검증 가능한 기능이 있는가?
- metric_signal: 후보별 중복/보완 기능, 설치 요구사항, 첫 적용 시나리오가 final brief에 근거 링크와 함께 남는다.
- metric_decision_rule: 근거 추적 또는 결과 품질을 구체적으로 보완하고 설치 비용·안전 경계가 수용 가능할 때만 추천한다.

## Waiting

- waiting_on: agent
- retry_policy: autonomous
- blocker: 필수 `task-plan.json`·`task-plan.md`가 없어 active leaf·의존성·증거 경로를 판정할 수 없습니다.
- next_action: ARTIFACT_RULES 양식의 계획 파일을 생성한 뒤 dispatcher가 검증 가능한 leaf를 활성화합니다.
- task_plan_template: ARTIFACT_RULES.md#대형-작업-태스크-계획

## 현재 상태

GitHub 공개 리서치 스킬의 실체와 운영 적합성을 조사합니다. 설치·활성화는 이 조사에서 하지 않습니다.

## 다음 행동

공개 저장소의 `SKILL.md`/README를 직접 열어 후보를 수집하고, 현재 `deep-research` 및 Infinity 리서치 계약과 중복을 판정합니다.
