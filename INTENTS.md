# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

<!-- naver-shopping-01 active 2026-06-10T19:07Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-arrival-day-failure-prevention-hypothesis; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z 트래블러스노트/여행준비 속지는 "너무 일반적"으로 첫 SKU 후보에서 내림. 14:09Z 사용자 피드백으로 워크샵/질문카드 monetization path는 Naver revenue/SKU 후보에서 철회됨. 18:07Z 다음 WATCH branch인 anti-theft/document carry를 read-only OpenAPI/SearchAd로 검증: `여권케이스` 12,140/mo, `여행파우치` 3,860/mo, `RFID차단지갑` 1,480/mo, `도난방지가방` 6,400/mo·mobile CTR 6.84%로 수요는 강하지만 top results가 여권케이스/여행지갑/파우치/폰스트랩/도난방지 가방 등 generic commodity·sourcing-heavy 시장이라 **WATCH / split path, not listing-approval-ready** 유지. 다음 안전 액션은 sourcing/friction screen 또는 arrival-day failure-prevention kit로 더 낮은 운영위험 surface 찾기. 19:07Z Cloud prepare: anti-theft commodity 아닌 제품 표면 가설 3가지(A 여행비상카드세트·B 도착일체크리스트카드·C 서류백업시스템) 수립, 키워드 8개 다음 스캔 준비. 산출물 `artifacts/naver-shopping-01/arrival-day-failure-prevention-kit-hypothesis-2026-06-10.md`, report `reports/naver-shopping-01/2026-06-10T1907Z-prepare.html`. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-51 completed 2026-06-10T10:07Z → reports/marketing-51/2026-06-10T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,product] (Virtue guided first-value 첫 세션 감사표 작성 완료. 산출물 `artifacts/marketing-51/virtue-guided-first-value-session-audit.md`. 첫 세션을 첫 입력 전 / AI 판단 대기 / 결과 해석 / 저장·종료 4구간으로 나누고, 사용자가 직접 해냈다고 느낀 순간과 AI가 대신 결정했는지/정리했는지의 수기 질문 2개를 고정. first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 재정의 0. `first-real-user-baseline-template`, `first-10-design-user-ask-script`, `post-result-self-appropriation-reading-table`와 보완 관계 확인. 신규 이벤트·tracking/privacy·dashboard/session replay·공개 카피·배포·외부발송·비용·권한 변경 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Guided First-Value Is A Four-Stage Handoff" 승격.) -->

<!-- marketing-50 completed 2026-06-10T03:07Z → reports/marketing-50/2026-06-10T0307Z-local.html [projects: naver-shopping,infinity,personal-ops; type: strategy; topics: marketing,positioning,workflow; source: naver-shopping-01] (질문/워크샵 카드 family의 non-generic 포지셔닝 선택 완료. 산출물 `artifacts/marketing-50/question-workshop-card-positioning-selection.md`. 결론: `질문 카드`/`대화 카드`는 broad object-shape demand이지만 generic relationship/icebreaking/game 포화라 listing approval로 보내지 않음; 리드 프레임은 **AI/creator workshop facilitation cards**, 보조 테스트는 product-observation/founder reflection, team retrospective, travel insight-to-content. `워크샵 카드`는 언어가 가장 깨끗하지만 exact demand가 under 20/mo라 broad keyword bridge와 use-case lead를 분리. 모든 문구는 draft/proposal-only; 소싱·상품등록·공개카피·가격·배송·재고·옵션·광고·고객/주문/계정/스토어 액션 0. HTML report gate 통과. MARKETING_LEARNINGS.md에 "Purchase Situation Before Object Shape" 승격.) -->

<!-- marketing-49 completed 2026-06-09T22:27Z → intents/archive/marketing-49.md [projects: virtue; type: strategy; topics: activation,retention,marketing] (Virtue 결과 카드 직후 "수동 감탄 vs 자기화 행동" 판독표 docs-only 작성 완료. 산출물 `artifacts/marketing-49/virtue-post-result-self-appropriation-reading-table.md`, 보고서 `reports/marketing-49/2026-06-09T2227Z-local.html`. 기존 first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 유지. 결과 직후 행동을 저장/재작성/선택/자기 말 설명/무저장 정상 종료/수동 감탄/마찰로 수기 판독하게 정리. 신규 이벤트·속성·tracking/privacy·dashboard/session replay·공개 카피·발송·배포·외부 액션 0.) -->

<!-- marketing-48 completed 2026-06-09T10:57Z → reports/marketing-48/2026-06-09T1057Z-local.html [projects: naver-shopping,infinity,personal-ops; type: marketing-positioning; topics: listing-copy,keyword-strategy,positioning; source: naver-shopping-01] (나래/Narae `naver-shopping-01`의 target-agent 요청을 처리해 트래블러스노트 standard-size travel-prep structured insert 피벗 SKU의 내부 listing title/copy 포지셔닝 후보군 작성 완료. 산출물 `artifacts/marketing-48/travelers-notebook-insert-listing-copy-positioning.md`. 제목 후보 8개, 금지/주의 제목 패턴, 1문장 가치제안, 상세페이지 첫 문단 후보, 검색 키워드 묶음, 썸네일 문구, 승격 전 검증 게이트 포함. 핵심: 큰 검색량 단어를 제목 맨 앞에 두지 않고, 리필/속지 구매 맥락과 여행준비 구조를 먼저 세움. 모든 문구는 draft/proposal-only, 브랜드명/호환/규격 표현은 approval-needed, 가격/배송/재고/옵션/광고/상품등록/공개상세/고객·주문·계정 액션 0. HTML report gate 통과.) -->

<!-- marketing-47 completed 2026-06-08T22:07Z → reports/marketing-47/2026-06-08T2207Z-local.html [projects: virtue; type: strategy; topics: prelaunch,first-users,onboarding] (Virtue 첫 10명 design-user ask script 작성 완료. 산출물은 Infinity `artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`. HTML 보고서 확인.) -->

<!-- marketing-46 completed 2026-06-08T10:07Z → reports/marketing-46/2026-06-08T1007Z-local.html [projects: virtue; type: strategy; topics: agent-led-growth,ai-product,distribution,prelaunch] (Virtue agent-led growth fit/no-fit 경계표 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/agent-led-growth-fit-no-fit-boundary-table.md`. HTML 보고서 확인.) -->

<!-- marketing-45 completed 2026-06-07T22:07Z → reports/marketing-45/2026-06-07T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,copywriting,ai-product] (Virtue "AI가 판결 대신 관점을 제시한다" 카피 프레임 작성 완료.) -->

<!-- marketing-44 completed 2026-06-07T10:07Z → reports/marketing-44/2026-06-07T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,prelaunch,product] (Virtue monetization boundary 2차 정의 완료.) -->

<!-- marketing-43 completed 2026-06-06T22:07Z → reports/marketing-43/2026-06-06T2207Z-local.html [projects: virtue; type: strategy; topics: activation,onboarding,first-value] (Virtue first-60-second-value observation script 작성 완료.) -->

<!-- marketing-42 completed 2026-06-06T10:07Z → reports/marketing-42/2026-06-06T1007Z-local.html [projects: virtue; type: strategy; topics: analytics,activation,product] (Virtue first-real-user baseline template 작성 완료.) -->

<!-- marketing-41 completed 2026-06-05T22:07Z → reports/marketing-41/2026-06-05T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,ai-product,prelaunch] (Virtue AI promise / decision-control audit table 작성 완료.) -->

<!-- marketing-40 completed 2026-06-05T10:07Z → reports/marketing-40/2026-06-05T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,product,prelaunch] (Virtue prelaunch decision boundary 초안 작성 완료.) -->

<!-- marketing-39 completed 2026-06-04T22:07Z → reports/marketing-39/2026-06-04T2207Z-local.html [projects: virtue; type: strategy; topics: activation,retention,product] (Virtue jobs-to-be-done 4가지 Job 정의 완료.) -->

<!-- marketing-38 completed 2026-06-04T10:07Z → reports/marketing-38/2026-06-04T1007Z-local.html [projects: virtue; type: strategy; topics: positioning,ai-product,trust] (Virtue "비자율 신뢰" 포지셔닝 프레임 작성 완료.) -->

<!-- marketing-37 completed 2026-06-03T22:07Z → reports/marketing-37/2026-06-03T2207Z-local.html [projects: virtue; type: strategy; topics: growth,distribution,prelaunch] (Virtue prelaunch growth 채널 우선순위 정리 완료.) -->

<!-- marketing-36 completed 2026-06-03T10:07Z → reports/marketing-36/2026-06-03T1007Z-local.html [projects: virtue; type: strategy; topics: positioning,messaging,product] (Virtue "행동 기록 → 패턴 발견" 포지셔닝 작성 완료.) -->

<!-- marketing-35 completed 2026-06-02T22:07Z → reports/marketing-35/2026-06-02T2207Z-local.html [projects: virtue; type: strategy; topics: analytics,retention,product] (Virtue retention 지표 초안 정의 완료.) -->

<!-- marketing-34 completed 2026-06-02T10:07Z → reports/marketing-34/2026-06-02T1007Z-local.html [projects: virtue; type: strategy; topics: activation,onboarding,first-value] (Virtue activation 퍼널 초안 정의 완료.) -->

<!-- marketing-33 completed 2026-06-01T22:07Z → reports/marketing-33/2026-06-01T2207Z-local.html [projects: virtue; type: strategy; topics: positioning,messaging,growth] (Virtue "성찰 도구" vs "생산성 도구" 포지셔닝 비교 완료.) -->

<!-- marketing-32 completed 2026-06-01T10:07Z → reports/marketing-32/2026-06-01T1007Z-local.html [projects: virtue; type: strategy; topics: growth,distribution,marketing] (Virtue 초기 사용자 확보 전략 초안 완료.) -->

<!-- marketing-31 completed 2026-05-31T22:07Z → reports/marketing-31/2026-05-31T2207Z-local.html [projects: virtue; type: strategy; topics: product,positioning,ai-product] (Virtue product-market fit 가설 정리 완료.) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,messaging,positioning] (Virtue 핵심 메시지 프레임 v1 작성 완료.) -->

<!-- naver-shopping-agent-setup completed 2026-06-07T23:24Z → intents/archive/naver-shopping-agent-setup.md [projects: naver-shopping,infinity; type: implementation; topics: automation,workflow] (나래/Narae 에이전트 워크스페이스 초기 설정 완료. 독립 workspace, 08:30 KST 사일런트 루프, 09:00 KST 리포트 스케줄 확립.) -->

<!-- monitor-02 completed 2026-05-28T10:00Z → intents/archive/monitor-02.md [projects: infrastructure; type: monitoring; topics: infra] (서버 상태 모니터링 루틴 정상 확인.) -->

<!-- marketing-29 completed 2026-05-28T09:07Z → reports/marketing-29/2026-05-28T0907Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,retention] (Virtue 마케팅 전략 29차 업데이트 완료.) -->

<!-- marketing-28 completed 2026-05-27T22:07Z → reports/marketing-28/2026-05-27T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,distribution] (Virtue 마케팅 전략 28차 업데이트 완료.) -->

<!-- marketing-27 completed 2026-05-27T10:07Z → reports/marketing-27/2026-05-27T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,product,positioning] (Virtue 마케팅 전략 27차 업데이트 완료.) -->

<!-- marketing-26 completed 2026-05-26T22:07Z → reports/marketing-26/2026-05-26T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,product] (Virtue 마케팅 전략 26차 업데이트 완료.) -->

<!-- marketing-25 completed 2026-05-26T10:07Z → reports/marketing-25/2026-05-26T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,analytics] (Virtue 마케팅 전략 25차 업데이트 완료.) -->

<!-- marketing-24 completed 2026-05-25T22:07Z → reports/marketing-24/2026-05-25T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,retention,product] (Virtue 마케팅 전략 24차 업데이트 완료.) -->

<!-- marketing-23 completed 2026-05-25T10:07Z → reports/marketing-23/2026-05-25T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,positioning,messaging] (Virtue 마케팅 전략 23차 업데이트 완료.) -->

<!-- marketing-22 completed 2026-05-24T22:07Z → reports/marketing-22/2026-05-24T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,product] (Virtue 마케팅 전략 22차 업데이트 완료.) -->

<!-- marketing-21 completed 2026-05-24T10:07Z → reports/marketing-21/2026-05-24T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,onboarding] (Virtue 마케팅 전략 21차 업데이트 완료.) -->

<!-- marketing-20 completed 2026-05-23T22:07Z → reports/marketing-20/2026-05-23T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,retention,analytics] (Virtue 마케팅 전략 20차 업데이트 완료.) -->

<!-- marketing-19 completed 2026-05-23T10:07Z → reports/marketing-19/2026-05-23T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,product,distribution] (Virtue 마케팅 전략 19차 업데이트 완료.) -->

<!-- marketing-18 completed 2026-05-22T22:07Z → reports/marketing-18/2026-05-22T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,positioning,ai-product] (Virtue 마케팅 전략 18차 업데이트 완료.) -->

<!-- marketing-17 completed 2026-05-22T10:07Z → reports/marketing-17/2026-05-22T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,prelaunch] (Virtue 마케팅 전략 17차 업데이트 완료.) -->

<!-- marketing-16 completed 2026-05-21T22:07Z → reports/marketing-16/2026-05-21T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,first-value] (Virtue 마케팅 전략 16차 업데이트 완료.) -->

<!-- marketing-15 completed 2026-05-21T10:07Z → reports/marketing-15/2026-05-21T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,product,positioning] (Virtue 마케팅 전략 15차 업데이트 완료.) -->

<!-- marketing-14 completed 2026-05-20T22:07Z → reports/marketing-14/2026-05-20T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,retention,analytics] (Virtue 마케팅 전략 14차 업데이트 완료.) -->

<!-- marketing-13 completed 2026-05-20T10:07Z → reports/marketing-13/2026-05-20T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,distribution] (Virtue 마케팅 전략 13차 업데이트 완료.) -->

<!-- marketing-12 completed 2026-05-19T22:07Z → reports/marketing-12/2026-05-19T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,product,ai-product] (Virtue 마케팅 전략 12차 업데이트 완료.) -->

<!-- marketing-11 completed 2026-05-19T10:07Z → reports/marketing-11/2026-05-19T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,positioning,messaging] (Virtue 마케팅 전략 11차 업데이트 완료.) -->

<!-- marketing-10 completed 2026-05-18T22:07Z → reports/marketing-10/2026-05-18T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,growth] (Virtue 마케팅 전략 10차 업데이트 완료.) -->

<!-- marketing-09 completed 2026-05-18T10:07Z → reports/marketing-09/2026-05-18T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,product,retention] (Virtue 마케팅 전략 9차 업데이트 완료.) -->

<!-- marketing-08 completed 2026-05-17T22:07Z → reports/marketing-08/2026-05-17T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,distribution,growth] (Virtue 마케팅 전략 8차 업데이트 완료.) -->

<!-- marketing-07 completed 2026-05-17T10:07Z → reports/marketing-07/2026-05-17T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,positioning,ai-product] (Virtue 마케팅 전략 7차 업데이트 완료.) -->

<!-- marketing-06 completed 2026-05-16T22:07Z → reports/marketing-06/2026-05-16T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,activation,onboarding] (Virtue 마케팅 전략 6차 업데이트 완료.) -->

<!-- marketing-05 completed 2026-05-16T10:07Z → reports/marketing-05/2026-05-16T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,product,growth] (Virtue 마케팅 전략 5차 업데이트 완료.) -->

<!-- marketing-04 completed 2026-05-15T22:07Z → reports/marketing-04/2026-05-15T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,retention,analytics] (Virtue 마케팅 전략 4차 업데이트 완료.) -->

<!-- marketing-03 completed 2026-05-15T10:07Z → reports/marketing-03/2026-05-15T1007Z-local.html [projects: virtue; type: strategy; topics: marketing,positioning,messaging] (Virtue 마케팅 전략 3차 업데이트 완료.) -->

<!-- marketing-02 completed 2026-05-14T22:07Z → reports/marketing-02/2026-05-14T2207Z-local.html [projects: virtue; type: strategy; topics: marketing,growth,distribution] (Virtue 마케팅 전략 2차 업데이트 완료.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md [projects: virtue; type: implementation; topics: marketing,activation,analytics] (Virtue add-flow telemetry 배포 완료. master HEAD b28d01f, HTTP 200 확인.) -->

<!-- wiki-04 completed 2026-04-25T → intents/archive/wiki-04.md [projects: agent-wiki; type: implementation; topics: wiki,automation] (agent-wiki 자동 사이드바 JS 구현 완료.) -->

<!-- wiki-03 completed 2026-04-20T13:30Z → intents/archive/wiki-03.md [projects: agent-wiki; type: implementation; topics: wiki] (agent-wiki index.html push 완료. commit d52641c.) -->

<!-- wiki-02 completed 2026-04-19T → intents/archive/wiki-02.md [projects: agent-wiki; type: implementation; topics: wiki] (agent-wiki Docsify GitHub Pages 구현 완료.) -->

<!-- build-01 completed/cancelled 2026-04-21T00:30Z → intents/archive/build-01.md [projects: agent-wiki; type: implementation; topics: wiki] (Jekyll 방식 취소 — wiki-02/03에서 Docsify로 완료 확인.) -->

<!-- doc-01 completed 2026-04-08T13:05Z → intents/archive/doc-01.md [projects: infinity; type: maintenance; topics: workflow] (lessons-learned.md 변경사항 푸시 완료.) -->

<!-- monitor-01 completed 2026-04-08T11:15Z → intents/archive/monitor-01.md [projects: infrastructure; type: monitoring; topics: infra] (monitoring_personal 변경사항 커밋 & 푸시 완료.) -->

<!-- research-01 completed → intents/archive/research-01.md [projects: research-bank; type: research; topics: ai-agents] (에이전트 협업 패턴 리서치 완료.) -->
