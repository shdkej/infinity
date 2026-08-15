# research-27 — 디지털 여행 스크랩북 시장 조사

- id: research-27
- status: waiting
- created_at: 2026-08-15T22:17Z
- requested_by: user
- source: Telegram DM
- target_agent: genie
- priority: high
- permission: internal-research-only
- execution_mode: multi_subagent_roles_blocked
- fallback_reason: Planner/Developer/Marketer/Operator 세션 병렬 시작 호출이 장시간 반환되지 않아 session id/status를 확인하지 못함. 계약상 single_genie_roles로 downgrade하지 않음.
- next_retry_condition: 다음 유효 dispatcher 사이클에서 role subagent 생성과 session id/status 확인을 재시도하고, 네 세션 모두 확인될 때까지 조사 실행을 보류한다.
- projects: [world-travel, digital-scrapbook, personal-product, infinity]
- task_type: market-research
- topics: [travel-scrapbook, memory-keeping, ai-travel-journal, creator-tools, consumer-app, monetization]
- goal: 디지털 여행 스크랩북/여행 기억 아카이브 앱의 시장 기회와 2주 검증 가능한 첫 MVP를 판단한다.
- success_criteria: 경쟁/대안 8개 이상 비교, 결론(만들 가치 있음/보류/만들지 말 것), 2주 실험 3개와 지표, 세계여행 기반 MVP 1개, 근거 링크·조사일 기록, 역할별 session id/status와 Red 결과 기록.

## User Request

인피니티에 디지털 여행 스크랩북 시장 조사 부탁

## Goal

디지털 여행 스크랩북/여행 기억 아카이브 앱 시장을 조사하고, 사용자가 세계여행 중 직접 만들거나 검증할 만한 제품 기회인지 판단한다.

## Required Execution

Genie must run this as `multi_subagent_roles`.

- Planner: 사용자 맥락과 세계여행 프로젝트를 기준으로 핵심 사용자, 사용 시나리오, 불편, 기존 대안의 빈틈을 정리한다.
- Developer: 구현 가능성, 데이터 구조, AI/미디어 처리, 모바일/웹 MVP 범위, 외부 연동 난이도를 비교한다.
- Marketer: 경쟁 앱/서비스의 포지셔닝, 가격, 콘텐츠 각도, 수요검증 메시지를 조사한다.
- Operator: 운영 리스크, 비용, 개인정보/사진 데이터 취급, 반복 기록 루프, 검증 실험 운영 방식을 점검한다.
- Red: Archive 전 별도 검증을 수행한다.

## Scope

조사 범위:

- 디지털 여행 스크랩북, AI 여행일기, 지도 기반 여행 기록, 사진/영상 여행 아카이브, 커플/가족 여행 메모 앱
- 국내외 경쟁 서비스와 인접 대안: Instagram/Threads, Google Photos/Apple Photos, Notion/Obsidian, Polarsteps, FindPenguins, Day One, Journey, map-based journal tools, travel itinerary apps
- 수익화 가능성: 구독, 프린트/포토북, 클라우드 저장, AI 요약/영상화, 여행 크리에이터용 템플릿
- MVP 가능성: 현재 세계여행 기록을 재료로 2주 안에 검증 가능한 좁은 첫 버전

제외:

- 공개 발행, 결제, 배포, 외부 계정 권한 변경
- 사용자 사진 원본의 외부 업로드/공유가 필요한 실험
- 확인되지 않은 시장 수치의 단정

## Success Criteria

- 경쟁/대안 8개 이상을 비교하고, 각 서비스의 실제 차별점과 빈틈을 분리한다.
- "만들 가치 있음 / 보류 / 만들지 말 것" 중 하나로 결론을 낸다.
- 2주 검증 실험 3개와 관찰 지표를 제안한다.
- 사용자의 세계여행 프로젝트와 연결되는 구체적 첫 MVP를 1개로 좁힌다.
- 근거 링크, 조사일, 가격/기능 확인일을 남긴다.
- report에는 `execution_mode`, 역할별 session id/status, role output summary, Genie synthesis, Red 결과를 기록한다.

## Next Action

Genie가 Knowledge Lab의 세계여행 프로젝트 맥락을 먼저 확인한 뒤, Planner/Developer/Marketer/Operator 역할을 실제 서브에이전트로 분리해 시장 조사를 시작한다.
