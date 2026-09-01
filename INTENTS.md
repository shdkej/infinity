# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

<!-- 실행 중인 Intent 없음. -->

## Waiting

### [research-32] Starter Story 솔로프리너 사례 1개 깊은 복원
- status: waiting
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- requested: 2026-08-24T18:10Z
- execution_mode: multi_subagent_roles
- projects: starter-story,solopreneur,sns-benchmark,ai-research,infinity
- task_type: evidence-based-case-reconstruction
- topics: youtube-summary,description-ingestion,sns-parsing,x-api,launch-timeline,content-analysis,skill-design
- goal: Starter Story에 소개된 솔로프리너 사례 1개의 문제 인식부터 제작·최초 공개·초기 홍보·반응·반복 개선까지를 영상·디스크립션·SNS·공식 웹 원문으로 교차검증해 깊은 실행 타임라인으로 복원한다.
- user_request: "사례 1개 깊게 복원"
- source_url: https://youtu.be/Q4k8JNYKJT0
- source_context: 사용자가 지정한 Starter Story 사례 영상. 영상 본문·디스크립션·연결된 공식/SNS 원문을 우선 근거로 사용한다.
- success_criteria: 영상 요약·디스크립션·원문 SNS 타임라인·공식 외부 근거를 수집하고, 각 단계에 원문 링크·게시일·인용·근거 강도·해석을 붙인 사례 리포트와 재사용 가능한 수집/분석 스킬 설계, 결과 업로드용 페이지 요구사항을 만든다. 확인되지 않은 시기는 추정하지 않는다. Planner PRD와 Red 검증을 포함한다.
- metric_question: 사례 1개의 최초 실행부터 최근까지를 근거 링크와 함께 재현할 수 있는가?
- metric_signal: 영상/디스크립션 확보 여부, 플랫폼별 원문 수·최초 확인일, 단계별 근거 링크와 근거 강도, 미확인 구간 수
- metric_decision_rule: 핵심 단계 4개 이상이 1차 원문으로 재현되면 continue, SNS 한 플랫폼만 가능하면 change, 핵심 원자료가 막히면 hold
- boundary: 공개 게시·외부 발송·유료 API 구매·자격증명 변경·계정 로그인은 실행하지 않는다. 접근 불가 자료는 추정하지 않고 blocker로 기록한다. 웹페이지 구현은 PRD와 데이터 계약 이후 별도 승인된 후속 범위로 둔다.
- required_sequence: grill-me 확인값 반영 → Planner PRD → Developer 수집/분석 스킬 설계 → Marketer 벤치마킹 사용성 → Operator 수집 실패·재현성 설계 → Genie synthesis → Red 검증
- next_action: Red 지적에 따라 행 단위 source locator·인용·숫자 정의 계약을 보강했다. 사용자 원자료가 제공되면 이벤트 표를 이 계약으로 보강하고 Red 재검증을 요청한다.
- artifact: artifacts/research-32/planner-prd.md; artifacts/research-32/starter-story-toneadapt-deep-reconstruction.md; artifacts/research-32/collection-analysis-contract.md
- report: reports/research-32/20260824T-research.md
- blocker: YouTube 원본 영상/자막은 yt-dlp 봇 검증에 막혔고, Kyan X 프로필은 HTML 0 lines라 게시물 원문·게시일·반응을 확인하지 못했다. 추정 없이 부분 복원만 작성.
- red_status: pending
- next_retry_condition: 사용자가 YouTube 자막/영상 export와 Kyan X 게시물 URL 또는 export를 제공하면 이벤트 타임라인을 보강하고 Red 검증을 재개한다.

### [research-36] 한국 YouTube·Instagram 여행·미니멀·기록·신혼 제목 100건 근거 수집
- status: waiting
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- requested: 2026-08-27T00:00Z
- execution_mode: multi_subagent_roles
- projects: research-bank,infinity,knowledge-lab
- task_type: research
- topics: content,analytics,marketing
- goal: 2021-08-27 이후 공개 조회/재생 수가 실제 확인되는 한국 YouTube와 Instagram Reels의 여행·미니멀·기록·신혼부부 제목 100건 이상을 행 단위 근거와 함께 수집·분류한다.
- success_criteria: 각 포함 행에 원문 제목·채널/계정·게시일·공개 조회/재생 수·확인시각·canonical 링크·주제·후킹 패턴·포함 근거가 있고, 100건 미달이면 실제 검증 수·플랫폼별 결손·막힌 이유를 기록한다.
- metric_question: 완전한 행 단위 근거가 있는 패턴 표본이 원본 제목 실험의 다음 결정을 바꾸는가?
- metric_signal: 완전 행 수, 플랫폼·후킹 패턴 분포, 필수 필드 충족률, 차단 사유.
- metric_decision_rule: 100건 이상이며 모든 필수 필드가 있으면 continue, 근거는 완전하나 플랫폼 편향/부분 표본이면 change, 공개 수치를 검증할 수 없으면 hold.
- boundary: 로그인·쿠키·유료 API·자격증명 변경·공개 게시·봇 제한 우회를 하지 않는다. 공개 재생 수가 없는 Instagram 게시물은 제외한다.
- artifact: artifacts/research-36/korean-travel-title-evidence-audit.md
- report: reports/research-36/20260827T0000Z.html
- artifact_followup: artifacts/research-36/platform-access-github-options.md
- artifact_youtube: artifacts/research-36/youtube-title-evidence-20260827.md
- data_youtube: artifacts/research-36/youtube-title-evidence-20260827.csv
- artifact_patterns: artifacts/research-36/youtube-title-patterns-20260827.md
- artifact_threads_check: artifacts/research-36/threads-query-check-20260827.md
- artifact_instagram_smoke: artifacts/research-36/instagram-mobile-canvas-smoke-20260827.md
- result: YouTube 공식 Data API `search.list -> videos.list` 기반으로 2021-08-27 이후 한국어 여행·미니멀·기록·신혼/부부 관련 제목 120행을 확보했다. 모든 행은 제목·채널·게시일·공개 조회수·확인시각·canonical URL·주제·후킹 패턴을 가진다.
- blocker: Instagram Reels는 모바일 canvas에서 공개 popular/tag page의 URL·계정·공개 수치·캡션 일부 12행이 잡혔지만, 게시일을 한 행에서 아직 확보하지 못했다. Threads는 공식 조회 경로가 있으나 현재 로컬에 Meta/Threads API 토큰이 없어 실제 API smoke test 전이다.
- next_action: YouTube 패턴 분석을 바탕으로 사용자 콘텐츠 제목 실험을 `숫자 조건 / 현실 반전 / 선택 비교 / 기록 방식` 후보군으로 만든다. Instagram은 모바일 canvas 공개 조회를 `partial smoke pass`로 두고, 릴스 permalink 개별 페이지에서 게시일 추출 가능 여부를 확인한다. Threads는 사용자 승인 후 공식 API 토큰/권한 기반 5키워드 smoke test를 별도 진행한다. Instaloader 로그인 세션·Apify/외부 API·브라우저 세션 대량 수집은 별도 승인 후 진행한다.
- red_status: youtube-pass-instagram-waiting
- red_report: artifacts/research-36/red-report.md
- role_sessions: planner=/root/planner_research36; developer=/root/developer_research36; marketer=/root/marketer_research36; operator=/root/operator_research36; red=/root/red_research36
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; concepts/metric-question-contract.mdx; concepts/evidence-bounded-content-experiment.mdx; concepts/currentness-safe-travel-context.mdx; TASTE.md; Threads.md; Content_Strategy.md; BRAND.md
- knowledge_reflection: 공개 수치가 보이는 검색 결과를 행 단위 증거로 과장하지 않고, 제목 품질은 조회 수가 아니라 구체 선택·제약·검증 가능성으로 판단한다.
- knowledge_commit: no-promotion-needed

<!-- 사용자 결정·외부 조건 대기만 기록한다. -->

## Archive

### [research-38] Agent Wiki 목차의 에이전트 검색 효율 감사
- status: archived
- execution_mode: multi_subagent_roles
- artifact: artifacts/research-38/mandalart-core-traversal-correction.md
- report: reports/research-38/20260901T-correction-pass.html
- red_status: pass
- red_report: artifacts/research-38/red-correction-report.md
- role_sessions: planner=/root/role_research_38c_planner; developer=/root/role_research_38c_developer; marketer=/root/role_research_38c_marketer; operator=/root/role_research_38c_operator; red=/root/role_research_38c_red
- supersedes: artifacts/research-38/agent-wiki-retrieval-ia-audit.md; reports/research-38/20260901T-final-pass.html (124 MDX·상위 컬렉션 기반 결론은 8×8 판정에 사용하지 않음)
- metric_question: 대표 에이전트 질의가 목차·메타데이터·링크만으로 관련 문서까지 일관되게 도달하는가?
- metric_result: 8축 source=62·mapped=62·누락 0; index→map=1, map→축=0/8, 중앙 node traversal=0/62, 직접 route=62/62.
- metric_next_decision: change — 별도 승인 후 map에 8축/62노드 additive 링크와 fixture를 구현한다.
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; index.mdx; mapped/source-category-map.mdx; DOCUMENT_SEARCH_PIPELINE.md
- knowledge_reflection: 8×8은 64개를 가정하는 inventory가 아니라 현재 62개 원본 대응 노드의 분류 틀이다. 원본 수와 mapped 변환 누락을 분리해 판단한다.
- knowledge_commit: no-promotion-needed
- archived_at: 2026-09-01T20:00Z (correction)
- next_action: 별도 승인 Intent에서 map→8축→62노드 additive 링크와 `1/8/62` traversal fixture를 구현한다.

<!-- marketing-123 archived 2026-08-31T21:02Z by dashboard archive_request 04ce866e-dd45-4977-a840-12d8a442d565 → intents/archive/marketing-123.md; public Threads post/link share not approved or performed. -->

<!-- marketing-127 archived 2026-08-30T19:41Z by dashboard archive_request 738ad28d-e480-4b00-8e82-b6c4187e4e59 → intents/archive/marketing-127.md; public account action not approved or performed. -->

<!-- research-37 completed 2026-08-30T09:12Z → intents/archive/research-37.md; artifacts/research-37/four-channel-api-comparison.md; artifacts/research-37/channel-top-bottom-lessons-20260828.md; red_status: pass-with-user-closure. -->

<!-- marketing-129 completed 2026-08-29T01:28Z → source/infinity/archive/marketing-129.md [projects: infinity,world-travel; type: design; topics: content] (내부 검토용 1080×1350 여행 기록 첫 장 v2와 실제 렌더 Red PASS) -->

<!-- research-37 single-channel execution superseded 2026-08-28T1920Z; superseded details retained in intents/archive/research-37.md. -->

<!-- design-05 completed 2026-08-27T00:15Z → intents/archive/design-05.md; artifacts/design-05/; reports/design-05/20260827T0015Z.html; red_status: pass. -->
### [design-05] 이집트 여행 브이로그용 세로 영수증 B-roll 오버레이
- status: archived
- target_agent: genie
- execution_mode: multi_subagent_roles
- artifact: artifacts/design-05/egypt-giza-field-receipt-overlay.png; artifacts/design-05/egypt-giza-field-receipt-overlay-preview-1920x1080.png
- report: reports/design-05/20260827T0015Z.html
- red_status: pass
- red_report: artifacts/design-05/red-report.md
- role_sessions: planner=/root/planner_egypt_receipt; developer=/root/developer_egypt_receipt; marketer=/root/marketer_egypt_receipt; operator=/root/operator_egypt_receipt; red=/root/red_egypt_receipt
- knowledge_status: used; knowledge_decision: retain-as-operating-principle; knowledge_commit: no-promotion-needed
- metric_result: RGBA 720×1800, 모서리 alpha 0·중심 alpha 240, 1920×1080 좌상단 프리뷰 가독성, Red PASS
- next_action: 편집 타임라인에 x=80,y=76,w=330 내외로 삽입

<!-- research-35 completed 2026-08-26 → intents/archive/research-35.md; artifacts/research-35/; reports/research-35/20260826T-research.md; red_status: pass. -->
### [research-35] 한국 사업자의 앱·웹 디지털 결제수단 조사
- status: archived
- target_agent: genie
- execution_mode: multi_subagent_roles
- artifact: artifacts/research-35/payment-comparison.md; report: reports/research-35/20260826T-research.md
- red_status: pass; knowledge_status: promoted; knowledge_commit: knowledge-lab@309656a
- metric_question: 한국 사업자·한국 고객 중심의 앱+웹 디지털 판매에 대해 구현 가능한 결제 조합을 하나로 선택할 수 있는가?
- metric_result: iOS Apple IAP + 웹 한국 PG 또는 온보딩 승인된 Paddle MoR; Superwall은 PSP가 아니며 해외 유심은 자격을 바꾸지 않음
- next_action: 별도 승인 후 실제 공급자 온보딩·요율·세무·개인정보 계약 조건 비교


<!-- research-34 completed 2026-08-24T23:40Z → intents/archive/research-34.md -->
### [research-34] 검증된 상위 시장 카테고리와 수익화 경로 탐색
- status: archived
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- execution_mode: multi_subagent_roles
- artifact: artifacts/research-34/established-market-monetization-map.md
- report: reports/research-34/20260824T2300Z.html
- red_status: pass
- red_report: artifacts/research-34/red-report.md
- role_sessions: planner=01a035e4-f508-77f2-85c8-25dac7d415bb; developer=01a035e5-157e-7c03-bcc7-54179bf14591; marketer=01a035e5-3db3-7780-b0b5-0a04204eefc0; operator=01a035e5-65d6-7171-b21f-97f505e8c47e; red=01a035f6-52cd-7d92-b141-f85894c6b333
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; Integration/Business; Integration/Creator; bounded-experiment-loop; Idea/Travel; currentness-safe-travel-context; research-33
- knowledge_reflection: research-33의 문제 중심 결론과 분리해 established market → monetization model → niche target의 세 층으로 시장 지도를 만들고, 시장 존재와 니치 WTP를 구분했다.
- knowledge_commit: no-promotion-needed
- archived_at: 2026-08-24T23:40Z
- next_action: 유력 3개 중 하나를 선택해 별도 승인된 5명+5명 비공개 증거 감사를 연다. 공개·광고·결제·유료 데이터·개인정보 수집·코드 구현은 실행하지 않는다.

<!-- research-33 completed 2026-08-24T22:25Z → intents/archive/research-33.md -->
### [research-33] 미니멀 고객의 실행 문제 기반 시장 카테고리 재검토
- status: archived
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- execution_mode: multi_subagent_roles
- artifact: artifacts/research-33/market-category-reassessment.md
- report: reports/research-33/20260824T2200Z.html
- red_status: pass
- red_report: artifacts/research-33/red-report.md
- role_sessions: planner=01a035ae-a0a4-73f3-b012-210d03cb2d03; developer=01a035ae-c82c-7090-b8f5-c843050c2a56; marketer=01a035ae-eff7-72f2-bd5c-45c414d9f976; operator=01a035af-179e-7231-9ece-edd51704f841; red=01a035b3-9af8-71c3-ae27-c68c68de6c83
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README; bounded-experiment-loop; sufficient-boundary-for-next-action; currentness-safe-travel-context; Idea/Travel; Integration/Business; research-30·31
- knowledge_reflection: 미니멀은 고객 라벨이 아니라 반복 실행 문제를 설명하는 언어로 남겼고, 기내수하물 중심 장기여행 준비·이동 운영을 첫 검증 가설로 좁혔다. 실제 시장성·가격·지불의사는 후속 승인 전까지 미검증으로 유지한다.
- knowledge_commit: no-promotion-needed
- archived_at: 2026-08-24T22:25Z
- next_action: 별도 승인 Intent에서 7~30일 기내수하물 중심 여행자 10명 비공개 검증 권한을 확인한다. 공개·광고·결제·개인정보 수집·코드 구현은 실행하지 않는다.

<!-- research-31 completed 2026-08-23T17:30Z → artifacts/research-31/; reports/research-31/20260823T1730Z.html; red_status: pass. -->
### [research-31] 미니멀·정리·균형·순환 기반 시장 카테고리 후보 발굴
- status: archived
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- requested: 2026-08-23T17:02Z
- execution_mode: multi_subagent_roles
- artifact: artifacts/research-31/market-category-candidates.md
- report: reports/research-31/20260823T1730Z.html
- red_status: pass
- red_report: artifacts/research-31/red-report.md
- role_sessions: planner=role-research-31-planner; developer=role-research-31-developer; marketer=role-research-31-marketer; operator=role-research-31-operator; red=role-research-31-red
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki README, Integration/Business, Integration/Creator, bounded-experiment-loop, research-30 artifact/archive
- knowledge_reflection: 취향은 고객 세그먼트가 아니라 경험·언어로 사용하고, 반복 문제·지불 주체·관찰 가능한 행동을 먼저 고정한다.
- knowledge_commit: no-promotion-needed
- archived_at: 2026-08-23T17:30Z
- next_action: 별도 승인 Intent에서 상위 3개 후보의 비공개 4주 검증 설계를 비교한다. 특정 카테고리 확정·코드·공개·광고·결제·개인정보 변경은 실행하지 않았다.

<!-- design-04 completed 2026-08-23T16:05Z → artifacts/design-04/; reports/design-04/20260823T1605Z-v2.html; red_status: pass (왼쪽 선 요소 제거·차콜/흑연 톤 완화 수정본 생성 및 렌더 검증. 공개 게시·외부 발송 없음.) -->
### [research-30] 개인 맞춤 공공정보 서비스 시장·MVP·수익화 검증
- status: archived
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- execution_mode: multi_subagent_roles
- projects: personal-brand,public-information,ai-service,mvp,monetization
- artifact: artifacts/research-30/public-information-service-strategy.md
- report: reports/research-30/20260823T1415Z.html
- red_status: pass
- red_report: artifacts/research-30/red-report.md
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_targets: agent-wiki Information, Life_Tracking, observable-feedback-systems, sufficient-boundary-for-next-action, Integration/Business, Infinity research-26/research-29
- knowledge_reflection: 정보량보다 공식 근거·적용 맥락·다음 행동을 남기고, 첫 실험은 자동화보다 관측 가능성과 복구 경계를 우선한다.
- knowledge_commit: no-promotion-needed
- archived_at: 2026-08-23T14:30Z
- next_action: 별도 승인된 후속 Intent에서 10~20명 비공개 수동 실험을 검토한다. 외부 공개·결제·개인정보 변경·코드 구현은 이번 Intent에서 실행하지 않았다.

### [research-29] Infinity Archive 후속 품질 반복 개선 실험
- status: archived
- artifact: artifacts/research-29/experiment-log.md
- report: reports/research-29/20260822T1900Z.html
- red_status: pass
- archived_at: 2026-08-22T19:00Z
<!-- research-29 archived 2026-08-22T19:00Z → E1 keep, E2 blocked, E3 discard; independent Red revalidation PASS. -->
<!-- marketing-127 completed 2026-08-22T08:00Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-127.md; reports/marketing-127/20260821T0000Z.html; Red PASS [공개 게시물 3건 확인, 내부 운영안 완료, 공개 행동 없음] -->
<!-- marketing-128 completed 2026-08-21T23:32Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-128.md; reports/marketing-128/20260821T2218Z.html; latest Red role-marketing-128-red-final PASS 2026-08-21T23:47Z [internal preparation complete, Red pass; public action remains approval-gated] -->
<!-- ops-26 completed 2026-08-21T20:12Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-26.md (모든 비단순 산출물 Intent에 지표 질문 계약과 전용 검사를 적용) -->
<!-- research-28 archived 2026-08-20T22:19Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-28.md (Andrej Karpathy autoresearch를 Infinity에 접목하는 운영·실험 구조 설계) -->
### [research-28] Andrej Karpathy autoresearch를 Infinity에 접목하는 운영·실험 구조 설계
- status: archived
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- requested: 2026-08-20T20:10Z
- execution_mode: multi_subagent_roles
- projects: infinity,openclaw,ai-research
- task_type: strategy
- topics: autoresearch,karpathy,experiment-loop,agent-orchestration,measurement
- goal: Andrej Karpathy의 autoresearch 핵심 원리(자동 실험 반복, 고정 평가 지표, 변경 범위, 기록·선정 루프)를 Infinity의 Intent·Heartbeat·Genie·Red 구조에 접목해, 과설계 없이 실제로 돌릴 수 있는 최소 운영 모델을 설계한다.
- user_request: "안드레 카파시의 autoresearch를 infinity에 어떻게 접목하면 좋을까"
- success_criteria: autoresearch 원리와 Infinity 현재 구조의 대응표, 적용하지 말아야 할 범위, 최소 MVP 운영 루프, 필요한 Intent/Report/Artifact 필드, 성공·중단·롤백 기준, 1~2주 검증 실험안을 포함한 한국어 전략 리포트와 Red 검증.
- boundary: 코드·cron·권한·자격증명·외부 공개 변경은 제안만 하고 실행하지 않는다. 기존 Infinity 운영 규칙과 사용자 소유권을 우선한다.
- next_action: 지니가 Andrej Karpathy autoresearch 원문·저장소와 Infinity 정본을 함께 확인한 뒤 Planner·Developer·Marketer·Operator 관점으로 접목안을 만들고 Red가 네 문장 검증을 수행한다.
- role_sessions: planner=01a0210b-48b4-77a0-8f67-d32ed7a0cb16; developer=01a0210b-7044-7bf1-9e72-a90b6049ae32; marketer=01a0210b-9845-7181-aa49-50f05010302c; operator=01a0210b-bfd2-7e61-b4cf-32fb5cce964d; red=01a02110-df6f-7613-8432-45078ca16e69
- artifact: artifacts/research-28/autoresearch-infinity-strategy.md
- report: reports/research-28/20260820T2118Z.html
- red_status: pass
- red_report: artifacts/research-28/red-report.md
- archived_at: 2026-08-20T22:19Z
- blocker: 없음 (HTML 게이트 재검증 통과)
- next_retry_condition: 없음 — 후속 구현은 별도 승인된 Intent로 생성

### [marketing-126] 인스타 닫힌 루프 3장 이미지 최종 후보
- status: archived
- target_agent: SAM
- priority: high
- permission: approval-required-before-public-post
- execution_mode: direct-revision-with-rendered-visual-gate
- projects: personal-brand,instagram,infinity
- task_type: design-revision
- topics: content,marketing,personal-brand,closed-loop,visual-quality
- goal: marketing-124/125 품질 한계를 반영해 완료품질 후보까지 재작업
- success_criteria: 1080×1350 PNG/SVG 3장, true circle/equal 120° step anchors/tangent arrows/no crop/no collision, 구체적 소개글 후보, 실제 PNG 직접 검수 PASS
- archived_at: 2026-08-20T21:15Z
- artifact: artifacts/marketing-126/
- report: reports/marketing-126/20260820T2115Z.md
- red_status: pass
- red_report: artifacts/marketing-126/red-report.md
- next_action: 사용자 확인 후에만 Instagram 프로필/게시 실행 검토. 공개 게시·프로필 변경·외부 업로드는 아직 실행하지 않음.

### [marketing-125] 인스타 소개글·닫힌 루프 3장 이미지 재작업
- status: archived
- target_agent: genie
- priority: high
- permission: approval-required-before-public-post
- execution_mode: multi_subagent_roles
- projects: personal-brand,instagram,infinity
- task_type: design-revision
- topics: content,marketing,personal-brand,closed-loop,visual-quality
- goal: marketing-124 품질 실패를 반영한 3장 이미지·소개글 재작업 및 렌더 직접 검증
- success_criteria: 1080×1350 PNG/SVG 3장, true circle/equal 120°/tangent arrows/no collision, 구체적 소개글 후보, Red rendered visual review PASS
- archived_at: 2026-08-20T20:35Z
- artifact: artifacts/marketing-125/
- report: reports/marketing-125/20260820T2035Z.html
- red_status: pass
- red_report: artifacts/marketing-125/red-report.md
- next_action: 사용자 승인 시에만 Instagram 프로필/게시 실행 검토. 공개 게시·프로필 변경·외부 업로드는 아직 실행하지 않음.

<!-- marketing-126 completed 2026-08-20T21:15Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-126.md; artifact: artifacts/marketing-126/; report: reports/marketing-126/20260820T2115Z.md; Red pass: artifacts/marketing-126/red-report.md [projects: personal-brand,instagram,infinity; type: instagram-intro-image-set; topics: closed-loop-experiment,visual-quality] (marketing-125를 직접 렌더 검수한 뒤 루프가 메시지를 충분히 설명하지 못한다고 판단해 한 번 더 재작업. 3분할 닫힌 루프와 가설/실행/증거 라벨, 실제 행동 중심 카피로 개선. 공개 게시·프로필 변경·외부 업로드 없음.) -->

<!-- marketing-125 completed 2026-08-20T20:35Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-125.md; artifact: artifacts/marketing-125/; report: reports/marketing-125/20260820T2035Z.html; Red pass: artifacts/marketing-125/red-report.md [projects: personal-brand,instagram,infinity; type: instagram-intro-image-set; topics: content,marketing,closed-loop-experiment] (marketing-124 실패를 반영한 신규 파라미터 기반 SVG/PNG 3장과 소개글 후보. 실제 PNG 직접 시각 검수 통과. 공개 게시·프로필 변경·외부 업로드 없음.) -->

<!-- marketing-124 completed 2026-08-20T14:05Z; quality rejected 2026-08-20T20:07Z → artifacts/marketing-124/; quality review: artifacts/marketing-124/quality-review-20260820.md; superseded by marketing-125 [projects: personal-brand,instagram,infinity; type: instagram-intro-image-set; topics: content,marketing,closed-loop-experiment] (초기 소개글 후보와 흰 배경·검정 순환 원 3장 SVG/PNG는 보존하지만 최종 사용 금지. 원형성·3분할·화살표 접선·카피 품질 검증 실패. 공개 게시·프로필 변경·외부 업로드 없음.) -->

<!-- marketing-122 completed 2026-08-16T16:25Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-122.md; artifact: artifacts/marketing-122/sharelink-threads-guide.md; evidence: artifacts/marketing-122/evidence-20260816T1625Z.md; report: reports/marketing-122/20260816T1625Z.html; Red pass: reports/marketing-122-red-20260816-pass.md [projects: personal-brand,threads,affiliate,commerce; type: monetization-guide; topics: toss-sharelink,threads,affiliate-marketing,hot-deals,compliance]
[프로젝트] 토스 쉐어링크 Threads 테스트
[상태] 실행 준비 완료
[결과 기준] 7일간 게시물 21개 테스트
[다음 행동] 내일 첫 상품 3개 게시
(공식 Sharelink 조건과 공개 Threads 사례 6개를 보강해 내부 실행 가이드 완료. 공개 발행·로그인·가입·계정 연결·광고·DM·댓글은 실행하지 않았고, 실제 게시 전 사용자 승인과 계정 화면 self-check 필요.) -->

<!-- research-27 completed 2026-08-16T03:25Z → artifacts/research-27/digital-travel-scrapbook-market-research.md; reports/dispatcher-20260816T0325Z-research-27.md; Red pass: artifacts/research-27/red-report-rerun.md [projects: world-travel,digital-scrapbook,personal-product,infinity; type: market-research; topics: travel-scrapbook,memory-keeping,ai-travel-journal,creator-tools,consumer-app,monetization] -->

<!-- research-26 completed 2026-08-14T22:15Z → artifacts/research-26/digital-organizer-market-research.md; reports/research-26/20260814T2215Z.html; Red pass: artifacts/research-26/red-report.md [projects: digital-organizer,personal-product,infinity; type: market-research; topics: digital-organizer,productivity,personal-knowledge-management,app-aggregation,visual-organization,monetization] (디지털 오거나이저 시장성은 중간. 연동 없는 시각적 디지털 서랍 MVP로 좁혀 2주 검증을 권장.) -->

<!-- ops-24 completed 2026-08-10T15:48Z → artifacts/ops-24/ops-24-execution-20260810.md; reports/ops-24/20260810T1548Z.html [projects: knowledge-lab,openclaw,infinity; type: maintenance; topics: automation,workflow,wiki] (6개 daily-tracking pointer와 runtime canonical cron payload를 재검증하고 card-news provenance 전용 검사 명령을 추가. detached clean checkout provenance PASS, Red red_status: pass: reports/ops-24/20260810T1548Z-red.html.) -->

<!-- ops-25 completed 2026-08-10T04:53Z → artifacts/ops-25/follow-up-capture-rule.md; reports/ops-25/20260810T0449Z.html [projects: infinity,openclaw,workflow; type: operating-rule; topics: follow-up-routing,intent-capture,automation,reporting] (완료·감사 report의 실행 가능한 후속 조치를 근거·완료 기준·중복 방지·승인 경계와 함께 별도 Inbox intent로 보존하는 계약을 INFINITY_OPERATING_RULES와 heartbeat workflow에 반영. follow_up_intent_ids/report 미생성 사유와 lane 재검증을 필수화. Red red_status: pass, Red report: reports/ops-25/20260810T0453Z-red.html.) -->
<!-- ops-23 completed 2026-08-09T21:58Z → artifacts/ops-23/audit-20260809.md; reports/ops-23/20260809T2158Z.html [projects: knowledge-lab,openclaw,infinity; type: audit; topics: ingest,indexing,daily-tracking,source-migration,cron-references] (source 이동·daily-tracking 색인·runtime 경계·cron/협업 참조 감사. symlink 호환성은 유지되나 meaningful daily-tracking pointer 누락, migrated cron 22개 중 legacy path 10개, ignored asset provenance 재현성 위험과 dispatcher snapshot 관측성 공백을 후속 조치로 기록. Planner·Developer·Marketer·Operator 판단과 Red red_status: pass 포함.) -->

<!-- research-25 completed 2026-08-09T20:48Z → artifacts/research-25/quiet-minimal-brand-research.md; reports/research-25/2026-08-09T2048Z.html [projects: personal-brand,design-system,infinity; type: research; topics: brand-research,minimal,introvert,slow-living,quiet-aesthetic] (국내외 생활용품·뷰티·출판·라이프스타일 7개 사례를 공식 자료와 Knowledge Lab 기준으로 비교하고, Sam Samuel 적용 원칙 10개와 quiet-start 프로토타입 다음 액션을 정리. Planner·Developer·Marketer·Operator 독립 판단 기록, Red pass.) -->

<!-- marketing-121 completed 2026-08-09T20:28Z → artifacts/marketing-121/instagram-hooks-100.md; reports/marketing-121/2026-08-09T2028Z.html [projects: personal-brand,instagram,content,infinity; type: research; topics: instagram,hooks,korean-copy,content-growth] (한국어 훅 100개를 10개 패턴으로 정리. 공개 한국어 자료 기반 골격과 Sam 변형을 분리하고, Red second pass PASS 및 정적 검증을 반영.) -->

<!-- build-17 completed 2026-08-09T20:26Z → reports/build-17/2026-08-09T2017Z.html [projects: status,design-system,space,infinity; type: implementation; topics: spatial-type,dashboard,frontend,deploy,visual-verification] (Spatial Type 텍스트 우선 표면으로 개편. 대상 commit 41f02b1 push, GitHub Actions run 31334185017 성공, https://status.aws.shdkej.com/ HTTP 200 및 라이브 CSS/데이터 계약 확인. Red pass.) -->

<!-- build-16 completed 2026-08-07T21:34Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-16.md [projects: infinity,static-sites; type: redesign-and-verification; topics: instagram-maker,layout,responsive,red-team] (공개 대시보드 `https://shdkej.github.io/infinity/` 200 및 raw 산출물 URL 200 확인. Red pass·Infinity/parent 원격 push 근거와 함께 Waiting에서 Archive로 정리.) -->

<!-- build-15 archived 2026-08-07T13:44Z user-completed: 공개 배포 미실행 상태를 명시적으로 보존하고 Waiting에서 제거. 원장: https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-15.md. -->

<!-- build-14 withdrawn 2026-08-06 [projects: personal-ops,infinity,knowledge-lab; type: implementation; topics: dashboard,metrics,visualization,workflow] (사용자 판단으로 시각화 결과물을 철회하고 공개 build-14 경로를 제거했다. 현재 라이브 경로는 Infinity Kanban fallback이며, sample metrics는 운영 화면으로 유지하지 않는다. 원장은 https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-14.md.) -->

<!-- marketing-120 archived 2026-08-02T20:35Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-120.md [projects: personal-brand,content,world-travel; type: analysis; topics: marketing,content-growth,threads,review] (사용자 요청으로 Waiting 항목을 정리했다. 실제 Threads 원자료가 없어 분석 결론은 내리지 않았고 기존 preflight/report는 무효로 보존.) -->

<!-- marketing-119 completed 2026-07-27T15:23Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-119.md [projects: personal-brand,content,world-travel; type: strategy; topics: marketing,content-growth,threads] (프라하·빈·부다페스트 콘텐츠 타이틀을 짐/미니멀 라벨이 아니라 도시를 옮기며 달라진 여행 기준 프레임으로 좁혔다. HTML report gate passed.) -->

<!-- ops-22 completed 2026-07-23T07:40Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-22.md [projects: openclaw,infinity; type: maintenance; topics: card-news,workflow,git] (카드뉴스 publish stage 분리 차단 옵션 `build_card_news_library.py --check-stage`와 insight-card-maker commit 전 게이트를 추가했다. 현재 Budapest split 상태가 실패로 재현됨. HTML report gate passed.) -->

<!-- ops-21 completed 2026-07-23T07:40Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-21.md [projects: openclaw,infinity; type: maintenance; topics: marketing,cron,cost] (Marketing SNS review live cron에 bounded SNS seed scan 조기 종료 규칙을 추가하고 내부 inbox 문서에 무소재 no_action 조기 종료 경계를 고정했다. HTML report gate passed.) -->

<!-- ops-20 completed 2026-07-23T07:40Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-20.md [projects: openclaw,infinity; type: maintenance; topics: media,git,workflow] (`media/inbound/openclaw-staged-*`를 runtime cache로 .gitignore 처리해 새/기존 staged 수신 폴더가 git status 검토면에 누적되지 않게 했다. HTML report gate passed.) -->

<!-- ops-19 completed 2026-07-21T06:12Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-19.md [projects: openclaw,infinity; type: maintenance; topics: card-news,workflow,skill] (insight-card-maker에서 Card 1 기본 원본사진 규칙, Cards 2-5 샘 캐릭터 적용 범위, Card 1 예외 승인 기록 조건을 한 가지 해석으로 정리했다. HTML report gate passed.) -->

<!-- ops-18 completed 2026-07-21T06:12Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-18.md [projects: openclaw,infinity; type: maintenance; topics: card-news,assets,provenance] (steel background asset.json source_reference를 tracked PNG로 바꾸고 ignored run 파일은 generation_log_reference로 낮췄으며, insight-card-maker 재사용 배경 규칙에 tracked provenance 경계를 추가했다. HTML report gate passed.) -->

<!-- proposer-blocker-20260720 resolved 2026-07-21T05:36Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/proposer-blocker-20260720.md [projects: openclaw,infinity; type: maintenance; topics: automation,cron,workflow] (사용자 승인 후 `openclaw cron runs --id 1a881731-a2f7-4faa-965f-dfbba9bac0e1 --limit 5`로 실제 실행 이력 조회를 검증했고, proposer 정본 문서와 cron payload에 id 포함 호출 규칙을 반영했다. HTML report gate passed.) -->

<!-- marketing-106 completed 2026-07-17T10:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-106.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰 companion에 저장 여부･같은 job 재방문 근거･retention 예측 신호･첫 verification gate 칸과 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- marketing-105 completed 2026-07-16T22:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-105.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰 companion에 첫 주 재방문 이유･같은 job 유지･재방문 성격 칸과 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- marketing-104 completed 2026-07-16T10:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-104.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰표 companion에 첫 가치 도달 시점･결과 이해 신호･다음 행동 명료성･자연 종료 여부와 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- ops-14 completed 2026-07-15T15:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-14.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow,llm] (evaluator NO_REPLY 실행 2건이 27,498 / 25,460 tokens로 내려가 읽기 예산 게이트 성공 기준을 충족했다. HTML report gate passed.) -->

<!-- ops-12 completed 2026-07-13T22:15Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-12.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow] (Marketing-agent-growth-review 크론 payload에 GIT SYNC FAILURE GATE를 추가해 git 실패를 NO_REPLY로 묵살하지 않고 Infinity Inbox blocker 또는 한국어 blocker로 남기도록 반영했다. HTML report gate passed.) -->

<!-- design-03 completed 2026-07-12T08:35Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/design-03.md [projects: personal-ops,content,design-system; type: research; topics: instagram,card-news,templates] (Instagram 카드뉴스용 힙하고 키치한 템플릿 10종을 리서치 중심으로 정리하고 한 장짜리 JPG 보드로 업로드했다. HTML report gate passed.) -->

<!-- ops-11 completed 2026-07-11T23:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-11.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow,dashboard] (quality-gates effectiveness.jsonl을 07:00 리캡/대시보드 append-only tracked 정본으로 확정하고 untracked 반복 노출 경계를 제거했다. HTML report gate passed.) -->

<!-- ops-10 completed 2026-07-11T12:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-10.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow] (로컬 수정 후 다음 감시 사이클에서 Inbox blocker가 비어 있음을 확인해 proposer tool-failure diagnostics repair를 완료 처리했다. HTML report gate passed.) -->

<!-- marketing-103 completed 2026-07-11T11:00Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-103.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,observation] (새 companion 문서에 early_behavior_sequence 칸 묶음과 J1-J4별 의도형/막힌형/자연종료 분류 기준 추가. 첫 10명 세션을 이벤트 완료 여부 넘어 행동 순서로 기록 가능. HTML report gate passed.) -->

<!-- ops-09 completed 2026-07-10T16:07 → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-09.md [projects: openclaw,personal-ops; type: verification; topics: automation,calendar,review] (최신 데일리 리뷰 저장본에서 Calendar Result/raw placeholder 미검출) -->

<!-- marketing-102 completed 2026-07-10T08:00Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-102.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (기존 관찰표와 marketing-101 후보를 대조해 J1-J4별 D7 재가치 질문, same-job 유지 기준, add_flow_started 금지선을 1장으로 고정했다. HTML report gate passed.) -->

<!-- ops-08 completed 2026-07-09T03:58Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-08.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow,review] (OpenClaw workspace의 daily-reviews/ 및 monthly-review-sources/를 runtime review 산출물로 .gitignore에 명시해 정본 변경 검토면에서 분리했다. HTML report gate passed.) -->

<!-- ops-07 completed 2026-07-09T0329Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-07.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow] (MEMORY.md/DREAMS.md 런타임 원장을 .gitignore에 명시해 dreaming/memory 중간 산출물이 정본 변경 검토면에 섯이지 않도록 했다. HTML report gate passed.) -->

<!-- ops-06 completed 2026-07-07T0007Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-06.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow,review] (weekly_review.md 같은 주 canonical 블록을 append가 아니라 replace/dedupe하는 계약과 로컬 dry-run helper를 추가했다. 2026-W27 dry-run PASS. HTML report gate passed.) -->

<!-- marketing-101 completed 2026-07-06T10:28 → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-101.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,analytics] (J1-J4별 activation 후보 묶음, window, 현재 이벤트/수기 관찰 항목, 표본 부족 시 금지 해석을 registry로 고정했다. HTML report gate passed.) -->

<!-- ops-05 completed 2026-07-06T10:07 → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-05.md [projects: openclaw,infinity,knowledge-lab; type: maintenance; topics: automation,workflow,content] (OpenClaw 카드뉴스 preview/sample/variant 및 초안 config 산출물이 새 실행 후 git status 검토면에 섯기지 않도록 .gitignore 경계를 보강했다. HTML report gate passed.) -->

<!-- ops-04 completed 2026-07-05T0307Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-04.md [projects: openclaw,infinity; type: implementation; topics: automation,workflow] (OpenClaw evaluator 정본이 `git status --short`, 절대경로 읽기, no-match 정상 처리 규칙을 이미 포함함을 확인하고 Active intent를 완료 처리했다. HTML report gate passed.) -->

<!-- ops-03 completed 2026-07-05T02:07 → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-03.md [projects: openclaw,personal-ops; type: implementation; topics: automation,review] (자동 회고 저장/발송 직전 렌더 게이트를 정본 규칙에 추가하고 OpenClaw 백업에 반영) -->

<!-- ops-02 completed 2026-07-04T1650Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-02.md [projects: openclaw,infinity; type: implementation; topics: workflow,documentation,tool-curation] (tool-curator 실행 규칙을 SKILL.md 단일 정본으로 통합하고 workflow 문서는 사건 이력으로, 크론 payload는 업은 인보커로 축소. 중복 규칙 순 176줄 제거. HTML report gate passed.) -->

<!-- ops-01 completed 2026-07-04T1650Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/ops-01.md [projects: openclaw,infinity; type: implementation; topics: automation,cron,reliability] (weekly autopush git sync를 결정적 스크립트 system/scripts/weekly_workspace_sync.sh로 이관하고 크론을 command payload로 교체했다. 실측 19파일 커밋 push + 하네스 run ok 검증. self-healer 프롬프트 패치 누적 표면 제거. HTML report gate passed.) -->

<!-- marketing-99 completed 2026-07-03T1230Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-99.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,onboarding,home] (홈과 `/add` 실코드를 다시 앵커링해 단일 CTA 유지안, J1/J3 2갈래 시작선, 샘플 결과 preview 3안을 판독했고, prelaunch 다음 비교 후보로 J1/J3 2갈래 시작선을 남겼다. UI 반영/카피/배치 결정은 제외.) -->

<!-- marketing-100 archived 2026-07-03 → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-100.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,onboarding,home] (초안에서 첫 문장･버튼 문구･판정 질문･보류 조건･preview안 차이를 고정했고, 후속 보강에서 단일 CTA 대비 필요성 질문, pass/hold cutline, 체택 신호를 추가했다. 구현/배포/계측은 제외했다.) -->

<!-- marketing-95 completed 2026-07-02T0340Z -> https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-95.md [projects: virtue,infinity; type: verification; topics: marketing,activation,deploy,return-state] (`virtue.aws.shdkej.com` 라이브에서 검증용 deed 1개를 넣은 returning state가 `나의 덕력 614덕`, `오늘 덕 쌍기`, 최근 덕행 리스트로 정상 표시됨을 확인했다. Fresh-state `612덕` 베이스라인 이슈는 이 검증 범위 밖으로 분리했다. HTML report gate passed.) -->

<!-- marketing-98 completed 2026-07-02T0200Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-98.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,observation] (첫 10명 관찰표에 가치 발견 신호･activation 판정 독립 2칸을 추가하고 J1~J4별 예시 1세트씩 고정했다.) -->

<!-- marketing-97 completed 2026-07-02T0000Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-97.md [projects: virtue,infinity; type: strategy; topics: marketing,activation] (질문 A "오늘 기억하고 싶은 일이 있나요?"와 잡별 예시 후보 E1~E4를 J1~J4 기준으로 판독해, 전역 예시 즉시 반영이 이른 4가지 이유와 질문 A + E1 우선 체택 근거를 한 표로 고정했다.) -->

<!-- design-02 completed 2026-07-01T1606Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/design-02.md [projects: knowledge-lab,infinity; type: design; topics: content,workflow] (최근 카드뉴스 첫 페이지 2종 비교 결과 총론형보다 대상+변화가 함께 보이는 구체 변화형 훅이 우세하다는 결론과 즉시 적용할 개선안 3개, preview 증거 2개를 남겼다.) -->

<!-- design-01 completed 2026-07-01T1606Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/design-01.md [projects: knowledge-lab,infinity; type: design; topics: content,workflow] (최근 카드뉴스 표지/CTA 감사로 실패 패턴 5개와 표지 제목, 사진 안전영역, body 밀도, CTA 역할 분리, 라이브러리 메타 보강을 포함한 실행 규칙 7개를 고정했다.) -->

<!-- marketing-96 completed 2026-07-01T1007Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-96.md [projects: virtue,infinity; type: strategy; topics: marketing,activation] (기존 `marketing-79` 관찰표에 붙여 쓰는 추천 언어 보강안을 추가해 `누구에게 나는 묵었다고 소개하겠는가`와 `지금 추천을 망설이게 하는 이유` 2필드, 기록 규칙, J3 예시 1세트를 고정했다. HTML report gate passed.) -->

<!-- naver-shopping-01 completed-first-pass 2026-07-01T0035Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing] (사용자 지시에 따라 나래 1차 작업 종료. 손목 스트랩 1순위 + 크로스바디/넥 폰 스트랩 2순위 샘플 검토 준비 상태를 보존하고, 명시적 재호출 전까지 alibaba.com 공급사 확인･샘플 주문 승인 요청･08:30/09:00 자동 루프를 중단한다.) -->

<!-- marketing-94 completed 2026-06-30T1007Z -> https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-94.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product,session-replay] (`marketing-87` 4분류를 유지한 체 pass-vs-hold 비교용 보조 문서 1장을 추가해, `judged but not saved`를 자동 실패로 읽지 않고 양쪽 세션에 반복되는 마산만 다음 수정 후보로 올리는 규칙을 고정했다. HTML report gate passed.) -->

<!-- marketing-93 completed 2026-06-29T2207Z -> https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-93.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product] (현재 홈･`/add`･반환 표면 언어를 J1~J4 기준으로 판독해, 지금 가장 잘 맞는 행복한 첫 사용자는 J1 기록형 중심이고 J2 누적형이 보조라는 기준표를 고정했다. HTML report gate passed.) -->

<!-- marketing-92 completed 2026-06-29T1829Z -> https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-92.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (홈 최근 덕행 empty-state를 `stats.count`와 `recent.length`로 분리해 복귀 사용자의 first-visit 카피 재노출을 막고, typecheck 통과･기존 lint warning만 확인했다.) -->

<!-- research-24 completed 2026-06-29T0600Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-24.md (capture･claim･open_loop 3필드 경계를 "있었던 것 / 내린 것 / 모르는 것"으로 고정하고 회고･Threads･카드뉴스 산출물 연결 규칙을 1장으로 정리했다.) -->

<!-- marketing-91 completed 2026-06-28T2229Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-91.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 이벤트 조합과 홈 반환 사례를 `정상 진행 / 자연 종료 / 마산 / 상태 모순` 4개 상태 언어로 고정했다.) -->

<!-- marketing-90 completed 2026-06-28T1007Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-90.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (Virtue 첫 세션을 진입 약속, 입력 기대, 반환 일관성의 3게이트로 압쳐욕다. HTML report gate passed.) -->

<!-- marketing-89 completed 2026-06-27T2236Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-89.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 반환 상태에서 `stats.total`, `stats.count`, `recent.length`의 계약과 empty-state 허용/금지 조건을 1장으로 고정했다.) -->

<!-- marketing-88 completed 2026-06-27T1007Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-88.md [projects: virtue; type: strategy; topics: marketing,activation,product] (라이브 홈, 로컈 홈 코드, 최근 canonical 제안서를 대조해 반환 세션 state drift를 한 장으로 정리했다. HTML report gate passed.) -->

<!-- marketing-87 completed 2026-06-26T222904Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-87.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 `/add` 이벤트와 replay 관찰 질문을 묶어 첫 10~15세션을 공통 UX 마산, J3 자연 종료, 조용한 실패, 다음 행동 불명확의 4분류로 읽는 1장 판독표 완성. HTML report gate passed.) -->

<!-- marketing-86 completed 2026-06-26T10:28Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-86.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (J1/J2/J4는 홈 최근 덕행, J3는 결과 카드를 primary surface로 삼는 next action helper proposal 완료) -->

<!-- marketing-85 completed 2026-06-25T220708Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-85.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch,observation] (첫 10명 활성화 1장 관찰표 `다음 행동 명료성` 질문 보강 완료. HTML report gate passed.) -->

<!-- marketing-84 completed 2026-06-25T1028Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-84.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 가치 다음의 next-step bridge 감사표/제안서 완료. HTML report gate passed.) -->

<!-- research-21 completed 2026-06-25T0507Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-21.md [projects: infinity,research-bank,personal-ops; type: research; topics: workflow,content] (6개 사례를 기록 방식･정리 방식･검증 방식･출판 변환 방식으로 비교해, Infinity용 일일 3줄･주간 3묶음･월간 1산출물 루프를 제안했다. HTML report gate passed.) -->

<!-- marketing-82 completed 2026-06-24T2308Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-82.md [projects: virtue; type: strategy; topics: marketing,activation,product] (Virtue 홈 첫 방문 zero-state를 랜딩형으로 재구성해 첫 가치와 다음 행동을 같은 화면에서 바로 읽히게 했다.) -->

<!-- marketing-83 completed 2026-06-24T2300Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-83.md [projects: virtue; type: strategy; topics: marketing,activation,onboarding,empty-state] (홈 반환형 empty-state gating 정렬 제안서 완료. HTML report gate passed.) -->

<!-- research-23 completed 2026-06-24T2055Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-23.md [projects: infinity,research-bank,world-models; type: research; topics: military,workflow,knowledge-management] (미군 TTP 학습 루프 심화 완료. HTML report gate passed.) -->

<!-- marketing-81 completed 2026-06-24T1007Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-81.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 저장/첫 판단 뒤 홈 복귀 secondary onboarding 감사표 완료. HTML report gate passed.) -->

<!-- research-22 completed 2026-06-24T0800Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-22.md (6단계 운영표･도구 비교･현실 루프 완료. HTML report gate passed.) -->

<!-- build-13 completed 2026-06-24T0050Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-13.md [projects: afzma,infinity,app-api-verification; type: implementation-verification; topics: hospital-api,api-flow,app-verification] (로컬 shdkej/afzma read-only 검증 완료. HTML report gate passed.) -->

<!-- marketing-80 completed 2026-06-23T2207Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-80.md [projects: virtue; type: strategy; topics: marketing,activation,product,feedback-consistency] (홈 요약 카드･`최근 덕행`･`/add` 결과･저장 후 복귀 지점을 J1-J4 기준으로 감사표로 정리. HTML report gate passed.) -->

<!-- marketing-79 completed 2026-06-23T1000Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-79.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch] (첫 10명 활성화 1장 관찰표 초안 완성. HTML report gate passed.) -->

<!-- marketing-78 completed 2026-06-22T1700Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-78.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 `최근 덕행` empty state 3요소 비교 완료. HTML report gate passed.) -->

<!-- marketing-77 completed 2026-06-22T1431Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-77.md [projects: virtue; type: strategy; topics: marketing,activation,product,ui-copy] (`/add` 기대 브리지 1줄 + 결과 카드 footer 안내 1줄 구현 완료.) -->

<!-- marketing-76 completed 2026-06-22T1029Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-76.md [projects: virtue; type: strategy; topics: marketing,activation,product,in-app-guidance] (`/add`･결과 카드･홈 empty state 맥락형 안내 감사표 완료. HTML report gate passed.) -->

<!-- marketing-75 completed 2026-06-22T1029Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-75.md [projects: virtue; type: strategy; topics: marketing,activation,launch-communication,product] (Tier 1-4 변경 등급표와 권장 안내 표면 맵 완료. HTML report gate passed.) -->

<!-- marketing-74 completed 2026-06-22T0600Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-74.md [projects: virtue; type: strategy; topics: marketing,activation,product,onboarding] (/add 입력 전 기대 형성 3안 비교 완료. HTML report gate passed.) -->

<!-- research-20 completed 2026-06-21T1200Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-20.md (강의/교육 퍼널 제외 국내 1인 브랜드 10선 재조사 완료. HTML report gate passed.) -->

<!-- research-19 completed 2026-06-21T0720Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-19.md (드로우앤드류･자청 제외 국내 1인 브랜드 10선 분석 완료. HTML report gate passed.) -->

<!-- marketing-73 completed 2026-06-21T0700Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-73.md [projects: virtue; type: strategy; topics: marketing,activation,product] (J3 AI 브리지 3안 비교 완료. HTML report gate passed.) -->

<!-- marketing-72 completed 2026-06-20T2218Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-72.md [display: Virtue First-Session Intent Hint Compare; projects: virtue; type: strategy; topics: activation,marketing,product] (HTML report gate passed.) -->

<!-- research-18 completed 2026-06-20T1200Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-18.md [display: 자동화 시스템 신뢰성 강화 리서치; projects: infinity,research-bank,personal-ops; type: research; topics: automation,reliability,operations] (HTML report gate passed.) -->

<!-- marketing-71 completed 2026-06-20T1108Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-71.md [display: Virtue Seeded Proof Proposal Compare; projects: virtue; type: strategy; topics: activation,onboarding,proof,prelaunch] (HTML report gate passed.) -->

<!-- research-17 completed 2026-06-20T0700Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-17.md [display: 미군 연구 시스템 구조 리서치; projects: infinity,research-bank,world-models; type: research; topics: military,research-system,innovation,doctrine,training] (HTML report gate passed.) -->

<!-- marketing-70 completed 2026-06-19T22:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-70.md [display: Virtue Empty-State Proof Audit; projects: virtue; type: strategy; topics: activation,empty-state,marketing] (HTML report gate passed.) -->

<!-- marketing-69 completed 2026-06-19T10:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-69.md [display: Virtue Agent Readiness Baseline; projects: virtue; type: strategy; topics: ai-agents,agentic-web,discoverability,trust,prelaunch] (HTML report gate passed.) -->

<!-- marketing-68 completed 2026-06-19T0000Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-68.md [display: Virtue Agent-Readable Surface Audit; projects: virtue; type: strategy; topics: ai-agents,agentic-web,trust,discoverability,prelaunch] (HTML report gate passed.) -->

<!-- marketing-67 completed 2026-06-18T12:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-67.md [display: Virtue AI Authorization Boundary Table; projects: virtue; type: strategy; topics: ai-agents,trust,authorization,prelaunch] (HTML report gate 통과.) -->

<!-- build-12 completed 2026-06-18T11:57Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-12.md [projects: personal-ops,infinity,design-system; type: implementation; topics: 3d-background,interactive-character,skill] (Option D pre-rendered+CSS parallax 구현 완료.) -->

<!-- research-16 completed 2026-06-18T08:00Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-16.md (SAM YouTube parse 기반 CharacterStage 구현 옵션 재비교 완료.) -->

<!-- research-15 completed 2026-06-18T07:00Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/research-15.md [display: 3D Interactive Character Background Feasibility; projects: personal-ops,infinity,design-system; type: research; topics: 3d-background,interactive-character,threejs,design-system] -->

<!-- marketing-66 completed 2026-06-17T22:07Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-66.md [display: Virtue Agentic Context Map; projects: virtue; type: strategy; topics: agentic-plg,positioning,activation,prelaunch] -->

<!-- marketing-65 completed 2026-06-17T10:24Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-65.md [display: Virtue Agent Trust Evidence Inventory; projects: virtue; type: strategy] -->

<!-- 이 섹션의 상세 이력은 2026-06-17T10:24Z Heartbeat 과정에서 INTENTS.md 갱신 중 일시 유실됨. 개별 intent 원장은 intents/archive/*.md 에 모두 보존되어 있음. -->

<!-- marketing-64 completed 2026-06-17T01:18Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy] -->

<!-- build-11 completed 2026-06-16T21:56Z → https://github.com/shdkej/knowledge-lab/blob/main/archive/infinity/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] -->
