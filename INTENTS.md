# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

<!-- build-16 completed and archived 2026-08-07T13:15Z; no executable Inbox item remains. -->

## Active

<!-- build-16 | target_agent: genie | source_agent: main | status: active | reopened_at: 2026-08-07T13:44Z | priority: high | permission: workspace-local-only | projects: infinity,static-sites | task_type: redesign-and-verification | topics: instagram-maker,layout,visual-hierarchy,responsive,red-team
재개 사유: 사용자가 build-16의 조기 완료 처리를 부정했으며, 이전 실행은 Infinity 정본과 원격 반영 게이트를 충분히 따르지 않았다.
원본: 기존 build-15 입력 /home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-76421795-7722-4543-a709-0e52eff09de2/instagram-maker.tar---5060dc00-db57-41b1-8b94-d6c42d82db53.gz.
목표: 기존 build-16 산출물을 완료 근거로 재사용하지 말고 원본과 사용자 의도를 다시 대조하여 Instagram Maker를 전면 재검토·재실행한다. Planner·Developer·Marketer·Operator·Red 전체 기록, 실제 화면 검증, HTML report, Infinity push 및 parent pointer push 확인 전에는 완료나 Archive를 선언하지 않는다.
완료 기준: 사용자가 지적한 배치 문제를 해결한 결과, 모바일·데스크톱 검증, Red red_status: pass, HTML report, Infinity remote commit/push 검증, Knowledge Lab parent pointer remote commit/push 검증(해당 시), clean worktree. 공개 배포가 원래 목표에 포함되면 build-15의 대기 원인과 공개 대상 준비를 먼저 해결하고, 준비되지 않으면 Waiting으로 남긴다.
다음 첫 액션: 지니가 Infinity 정본 문서와 기존 build-15/build-16 산출물을 다시 읽고, 이전 결과를 기준선으로만 삼아 재실행 계획과 검증 범위를 먼저 기록한다. -->
<!-- dispatcher-check 2026-08-07T13:48Z: 동일 intent build-16이 이미 status: active로 진행 중이므로 중복 실행하지 않음. next_retry_condition: 기존 build-16 실행이 완료·Waiting·실패 중 하나로 명시 전환되고, 해당 전환 및 Red/remote 검증 기록이 갱신된 다음 유효 사이클에서 재확인. -->

## Waiting

<!-- 사용자 결정·외부 조건 대기만 기록한다. 현재 build-15는 사용자가 완료 처리했으므로 Waiting에서 제거했다. -->
## Archive

<!-- build-15 archived 2026-08-07T13:44Z user-completed: 공개 배포 미실행 상태를 명시적으로 보존하고 Waiting에서 제거. 원장: intents/archive/build-15.md. -->

<!-- build-14 withdrawn 2026-08-06 [projects: personal-ops,infinity,knowledge-lab; type: implementation; topics: dashboard,metrics,visualization,workflow] (사용자 판단으로 시각화 결과물을 철회하고 공개 build-14 경로를 제거했다. 현재 라이브 경로는 Infinity Kanban fallback이며, sample metrics는 운영 화면으로 유지하지 않는다. 원장은 intents/archive/build-14.md.) -->

<!-- marketing-120 archived 2026-08-02T20:35Z → intents/archive/marketing-120.md [projects: personal-brand,content,world-travel; type: analysis; topics: marketing,content-growth,threads,review] (사용자 요청으로 Waiting 항목을 정리했다. 실제 Threads 원자료가 없어 분석 결론은 내리지 않았고 기존 preflight/report는 무효로 보존.) -->

<!-- marketing-119 completed 2026-07-27T15:23Z → intents/archive/marketing-119.md [projects: personal-brand,content,world-travel; type: strategy; topics: marketing,content-growth,threads] (프라하·빈·부다페스트 콘텐츠 타이틀을 짐/미니멀 라벨이 아니라 도시를 옮기며 달라진 여행 기준 프레임으로 좁혔다. HTML report gate passed.) -->

<!-- ops-22 completed 2026-07-23T07:40Z → intents/archive/ops-22.md [projects: openclaw,infinity; type: maintenance; topics: card-news,workflow,git] (카드뉴스 publish stage 분리 차단 옵션 `build_card_news_library.py --check-stage`와 insight-card-maker commit 전 게이트를 추가했다. 현재 Budapest split 상태가 실패로 재현됨. HTML report gate passed.) -->

<!-- ops-21 completed 2026-07-23T07:40Z → intents/archive/ops-21.md [projects: openclaw,infinity; type: maintenance; topics: marketing,cron,cost] (Marketing SNS review live cron에 bounded SNS seed scan 조기 종료 규칙을 추가하고 내부 inbox 문서에 무소재 no_action 조기 종료 경계를 고정했다. HTML report gate passed.) -->

<!-- ops-20 completed 2026-07-23T07:40Z → intents/archive/ops-20.md [projects: openclaw,infinity; type: maintenance; topics: media,git,workflow] (`media/inbound/openclaw-staged-*`를 runtime cache로 .gitignore 처리해 새/기존 staged 수신 폴더가 git status 검토면에 누적되지 않게 했다. HTML report gate passed.) -->

<!-- ops-19 completed 2026-07-21T06:12Z → intents/archive/ops-19.md [projects: openclaw,infinity; type: maintenance; topics: card-news,workflow,skill] (insight-card-maker에서 Card 1 기본 원본사진 규칙, Cards 2-5 샘 캐릭터 적용 범위, Card 1 예외 승인 기록 조건을 한 가지 해석으로 정리했다. HTML report gate passed.) -->

<!-- ops-18 completed 2026-07-21T06:12Z → intents/archive/ops-18.md [projects: openclaw,infinity; type: maintenance; topics: card-news,assets,provenance] (steel background asset.json source_reference를 tracked PNG로 바꾸고 ignored run 파일은 generation_log_reference로 낮췄으며, insight-card-maker 재사용 배경 규칙에 tracked provenance 경계를 추가했다. HTML report gate passed.) -->

<!-- proposer-blocker-20260720 resolved 2026-07-21T05:36Z → intents/archive/proposer-blocker-20260720.md [projects: openclaw,infinity; type: maintenance; topics: automation,cron,workflow] (사용자 승인 후 `openclaw cron runs --id 1a881731-a2f7-4faa-965f-dfbba9bac0e1 --limit 5`로 실제 실행 이력 조회를 검증했고, proposer 정본 문서와 cron payload에 id 포함 호출 규칙을 반영했다. HTML report gate passed.) -->

<!-- ops-12 completed 2026-07-13T22:15Z → intents/archive/ops-12.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow] (Marketing-agent-growth-review 크론 payload에 GIT SYNC FAILURE GATE를 추가해 git 실패를 NO_REPLY로 묵살하지 않고 Infinity Inbox blocker 또는 한국어 blocker로 남기도록 반영했다. HTML report gate passed.) -->

<!-- marketing-106 completed 2026-07-17T10:07Z → intents/archive/marketing-106.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰 companion에 저장 여부･같은 job 재방문 근거･retention 예측 신호･첫 verification gate 칸과 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- marketing-105 completed 2026-07-16T22:07Z → intents/archive/marketing-105.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰 companion에 첫 주 재방문 이유･같은 job 유지･재방문 성격 칸과 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- marketing-104 completed 2026-07-16T10:07Z → intents/archive/marketing-104.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (첫 10명 관찰표 companion에 첫 가치 도달 시점･결과 이해 신호･다음 행동 명료성･자연 종료 여부와 J1-J4 예시를 추가했다. HTML report gate passed.) -->

<!-- ops-14 completed 2026-07-15T15:07Z → intents/archive/ops-14.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow,llm] (evaluator NO_REPLY 실행 2건이 27,498 / 25,460 tokens로 내려가 읽기 예산 게이트 성공 기준을 충족했다. HTML report gate passed.) -->
<!-- design-03 completed 2026-07-12T08:35Z → intents/archive/design-03.md [projects: personal-ops,content,design-system; type: research; topics: instagram,card-news,templates] (Instagram 카드뉴스용 힙하고 키치한 템플릿 10종을 리서치 중심으로 정리하고 한 장짜리 JPG 보드로 업로드했다. HTML report gate passed.) -->
<!-- ops-10 completed 2026-07-11T12:07Z → intents/archive/ops-10.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow] (로컬 수정 후 다음 감시 사이클에서 Inbox blocker가 비어 있음을 확인해 proposer tool-failure diagnostics repair를 완료 처리했다. HTML report gate passed.) -->
<!-- ops-11 completed 2026-07-11T23:07Z → intents/archive/ops-11.md [projects: openclaw,infinity; type: monitoring; topics: automation,workflow,dashboard] (quality-gates effectiveness.jsonl을 07:00 리캡/대시보드 append-only tracked 정본으로 확정하고 untracked 반복 노출 경계를 제거했다. HTML report gate passed.) -->
<!-- marketing-103 completed 2026-07-11T11:00Z → intents/archive/marketing-103.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,observation] (새 companion 문서에 early_behavior_sequence 칸 묶음과 J1-J4별 의도형/막힌형/자연종료 분류 기준 추가. 첫 10명 세션을 이벤트 완료 여부 넘어 행동 순서로 기록 가능. HTML report gate passed.) -->
<!-- ops-09 completed 2026-07-10T16:07 → intents/archive/ops-09.md [projects: openclaw,personal-ops; type: verification; topics: automation,calendar,review] (최신 데일리 리뷰 저장본에서 Calendar Result/raw placeholder 미검출) -->
<!-- marketing-102 completed 2026-07-10T08:00Z → intents/archive/marketing-102.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (기존 관찰표와 marketing-101 후보를 대조해 J1-J4별 D7 재가치 질문, same-job 유지 기준, add_flow_started 금지선을 1장으로 고정했다. HTML report gate passed.) -->
<!-- ops-08 completed 2026-07-09T03:58Z → intents/archive/ops-08.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow,review] (OpenClaw workspace의 daily-reviews/ 및 monthly-review-sources/를 runtime review 산출물로 .gitignore에 명시해 정본 변경 검토면에서 분리했다. HTML report gate passed.) -->
<!-- ops-07 completed 2026-07-09T0329Z → intents/archive/ops-07.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow] (MEMORY.md/DREAMS.md 런타임 원장을 .gitignore에 명시해 dreaming/memory 중간 산출물이 정본 변경 검토면에 섯이지 않도록 했다. HTML report gate passed.) -->
<!-- ops-06 completed 2026-07-07T0007Z → intents/archive/ops-06.md [projects: openclaw,infinity; type: maintenance; topics: automation,workflow,review] (weekly_review.md 같은 주 canonical 블록을 append가 아니라 replace/dedupe하는 계약과 로컬 dry-run helper를 추가했다. 2026-W27 dry-run PASS. HTML report gate passed.) -->
<!-- ops-05 completed 2026-07-06T10:07 → intents/archive/ops-05.md [projects: openclaw,infinity,knowledge-lab; type: maintenance; topics: automation,workflow,content] (OpenClaw 카드뉴스 preview/sample/variant 및 초안 config 산출물이 새 실행 후 git status 검토면에 섯기지 않도록 .gitignore 경계를 보강했다. HTML report gate passed.) -->
<!-- marketing-101 completed 2026-07-06T10:28 → intents/archive/marketing-101.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,analytics] (J1-J4별 activation 후보 묶음, window, 현재 이벤트/수기 관찰 항목, 표본 부족 시 금지 해석을 registry로 고정했다. HTML report gate passed.) -->
<!-- ops-04 completed 2026-07-05T0307Z → intents/archive/ops-04.md [projects: openclaw,infinity; type: implementation; topics: automation,workflow] (OpenClaw evaluator 정본이 `git status --short`, 절대경로 읽기, no-match 정상 처리 규칙을 이미 포함함을 확인하고 Active intent를 완료 처리했다. HTML report gate passed.) -->
<!-- ops-03 completed 2026-07-05T02:07 → intents/archive/ops-03.md [projects: openclaw,personal-ops; type: implementation; topics: automation,review] (자동 회고 저장/발송 직전 렌더 게이트를 정본 규칙에 추가하고 OpenClaw 백업에 반영) -->
<!-- ops-01 completed 2026-07-04T1650Z → intents/archive/ops-01.md [projects: openclaw,infinity; type: implementation; topics: automation,cron,reliability] (weekly autopush git sync를 결정적 스크립트 system/scripts/weekly_workspace_sync.sh로 이관하고 크론을 command payload로 교체했다. 실측 19파일 커밋 push + 하네스 run ok 검증. self-healer 프롬프트 패치 누적 표면 제거. HTML report gate passed.) -->
<!-- ops-02 completed 2026-07-04T1650Z → intents/archive/ops-02.md [projects: openclaw,infinity; type: implementation; topics: workflow,documentation,tool-curation] (tool-curator 실행 규칙을 SKILL.md 단일 정본으로 통합하고 workflow 문서는 사건 이력으로, 크론 payload는 업은 인보커로 축소. 중복 규칙 순 176줄 제거. HTML report gate passed.) -->
<!-- marketing-100 archived 2026-07-03 → intents/archive/marketing-100.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,onboarding,home] (초안에서 첫 문장･버튼 문구･판정 질문･보류 조건･preview안 차이를 고정했고, 후속 보강에서 단일 CTA 대비 필요성 질문, pass/hold cutline, 체택 신호를 추가했다. 구현/배포/계측은 제외했다.) -->
<!-- marketing-99 completed 2026-07-03T1230Z → intents/archive/marketing-99.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,onboarding,home] (홈과 `/add` 실코드를 다시 앵커링해 단일 CTA 유지안, J1/J3 2갈래 시작선, 샘플 결과 preview 3안을 판독했고, prelaunch 다음 비교 후보로 J1/J3 2갈래 시작선을 남겼다. UI 반영/카피/배치 결정은 제외.) -->
<!-- marketing-98 completed 2026-07-02T0200Z → intents/archive/marketing-98.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,observation] (첫 10명 관찰표에 가치 발견 신호･activation 판정 독립 2칸을 추가하고 J1~J4별 예시 1세트씩 고정했다.) -->
<!-- marketing-97 completed 2026-07-02T0000Z → intents/archive/marketing-97.md [projects: virtue,infinity; type: strategy; topics: marketing,activation] (질문 A "오늘 기억하고 싶은 일이 있나요?"와 잡별 예시 후보 E1~E4를 J1~J4 기준으로 판독해, 전역 예시 즉시 반영이 이른 4가지 이유와 질문 A + E1 우선 체택 근거를 한 표로 고정했다.) -->
<!-- marketing-95 completed 2026-07-02T0340Z -> intents/archive/marketing-95.md [projects: virtue,infinity; type: verification; topics: marketing,activation,deploy,return-state] (`virtue.aws.shdkej.com` 라이브에서 검증용 deed 1개를 넣은 returning state가 `나의 덕력 614덕`, `오늘 덕 쌍기`, 최근 덕행 리스트로 정상 표시됨을 확인했다. Fresh-state `612덕` 베이스라인 이슈는 이 검증 범위 밖으로 분리했다. HTML report gate passed.) -->
<!-- design-02 completed 2026-07-01T1606Z → intents/archive/design-02.md [projects: knowledge-lab,infinity; type: design; topics: content,workflow] (최근 카드뉴스 첫 페이지 2종 비교 결과 총론형보다 대상+변화가 함께 보이는 구체 변화형 훅이 우세하다는 결론과 즉시 적용할 개선안 3개, preview 증거 2개를 남겼다.) -->
<!-- design-01 completed 2026-07-01T1606Z → intents/archive/design-01.md [projects: knowledge-lab,infinity; type: design; topics: content,workflow] (최근 카드뉴스 표지/CTA 감사로 실패 패턴 5개와 표지 제목, 사진 안전영역, body 밀도, CTA 역할 분리, 라이브러리 메타 보강을 포함한 실행 규칙 7개를 고정했다.) -->
<!-- marketing-96 completed 2026-07-01T1007Z → intents/archive/marketing-96.md [projects: virtue,infinity; type: strategy; topics: marketing,activation] (기존 `marketing-79` 관찰표에 붙여 쓰는 추천 언어 보강안을 추가해 `누구에게 나는 묵었다고 소개하겠는가`와 `지금 추천을 망설이게 하는 이유` 2필드, 기록 규칙, J3 예시 1세트를 고정했다. HTML report gate passed.) -->
<!-- naver-shopping-01 completed-first-pass 2026-07-01T0035Z → intents/archive/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing] (사용자 지시에 따라 나래 1차 작업 종료. 손목 스트랩 1순위 + 크로스바디/넥 폰 스트랩 2순위 샘플 검토 준비 상태를 보존하고, 명시적 재호출 전까지 alibaba.com 공급사 확인･샘플 주문 승인 요청･08:30/09:00 자동 루프를 중단한다.) -->
<!-- marketing-94 completed 2026-06-30T1007Z -> intents/archive/marketing-94.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product,session-replay] (`marketing-87` 4분류를 유지한 체 pass-vs-hold 비교용 보조 문서 1장을 추가해, `judged but not saved`를 자동 실패로 읽지 않고 양쪽 세션에 반복되는 마산만 다음 수정 후보로 올리는 규칙을 고정했다. HTML report gate passed.) -->
<!-- marketing-93 completed 2026-06-29T2207Z -> intents/archive/marketing-93.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,product] (현재 홈･`/add`･반환 표면 언어를 J1~J4 기준으로 판독해, 지금 가장 잘 맞는 행복한 첫 사용자는 J1 기록형 중심이고 J2 누적형이 보조라는 기준표를 고정했다. HTML report gate passed.) -->
<!-- marketing-92 completed 2026-06-29T1829Z -> intents/archive/marketing-92.md [projects: virtue,infinity; type: strategy; topics: marketing,activation,retention] (홈 최근 덕행 empty-state를 `stats.count`와 `recent.length`로 분리해 복귀 사용자의 first-visit 카피 재노출을 막고, typecheck 통과･기존 lint warning만 확인했다.) -->
<!-- 이 섹션의 상세 이력은 2026-06-17T10:24Z Heartbeat 과정에서 INTENTS.md 갱신 중 일시 유실됨. 개별 intent 원장은 intents/archive/*.md 에 모두 보존되어 있음. -->
<!-- research-24 completed 2026-06-29T0600Z → intents/archive/research-24.md (capture･claim･open_loop 3필드 경계를 "있었던 것 / 내린 것 / 모르는 것"으로 고정하고 회고･Threads･카드뉴스 산출물 연결 규칙을 1장으로 정리했다.) -->
<!-- marketing-91 completed 2026-06-28T2229Z → intents/archive/marketing-91.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 이벤트 조합과 홈 반환 사례를 `정상 진행 / 자연 종료 / 마산 / 상태 모순` 4개 상태 언어로 고정했다.) -->
<!-- marketing-90 completed 2026-06-28T1007Z → intents/archive/marketing-90.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (Virtue 첫 세션을 진입 약속, 입력 기대, 반환 일관성의 3게이트로 압쳐욕다. HTML report gate passed.) -->
<!-- marketing-89 completed 2026-06-27T2236Z → intents/archive/marketing-89.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 반환 상태에서 `stats.total`, `stats.count`, `recent.length`의 계약과 empty-state 허용/금지 조건을 1장으로 고정했다.) -->
<!-- marketing-88 completed 2026-06-27T1007Z → intents/archive/marketing-88.md [projects: virtue; type: strategy; topics: marketing,activation,product] (라이브 홈, 로컈 홈 코드, 최근 canonical 제안서를 대조해 반환 세션 state drift를 한 장으로 정리했다. HTML report gate passed.) -->
<!-- marketing-87 completed 2026-06-26T222904Z → intents/archive/marketing-87.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (기존 `/add` 이벤트와 replay 관찰 질문을 묶어 첫 10~15세션을 공통 UX 마산, J3 자연 종료, 조용한 실패, 다음 행동 불명확의 4분류로 읽는 1장 판독표 완성. HTML report gate passed.) -->
<!-- marketing-86 completed 2026-06-26T10:28Z → intents/archive/marketing-86.md [projects: virtue, infinity; type: strategy; topics: marketing, activation, product] (J1/J2/J4는 홈 최근 덕행, J3는 결과 카드를 primary surface로 삼는 next action helper proposal 완료) -->
<!-- marketing-85 completed 2026-06-25T220708Z → intents/archive/marketing-85.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch,observation] (첫 10명 활성화 1장 관찰표 `다음 행동 명료성` 질문 보강 완료. HTML report gate passed.) -->
<!-- marketing-84 completed 2026-06-25T1028Z → intents/archive/marketing-84.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 가치 다음의 next-step bridge 감사표/제안서 완료. HTML report gate passed.) -->
<!-- research-21 completed 2026-06-25T0507Z → intents/archive/research-21.md [projects: infinity,research-bank,personal-ops; type: research; topics: workflow,content] (6개 사례를 기록 방식･정리 방식･검증 방식･출판 변환 방식으로 비교해, Infinity용 일일 3줄･주간 3묶음･월간 1산출물 루프를 제안했다. HTML report gate passed.) -->
<!-- marketing-82 completed 2026-06-24T2308Z → intents/archive/marketing-82.md [projects: virtue; type: strategy; topics: marketing,activation,product] (Virtue 홈 첫 방문 zero-state를 랜딩형으로 재구성해 첫 가치와 다음 행동을 같은 화면에서 바로 읽히게 했다.) -->
<!-- marketing-83 completed 2026-06-24T2300Z → intents/archive/marketing-83.md [projects: virtue; type: strategy; topics: marketing,activation,onboarding,empty-state] (홈 반환형 empty-state gating 정렬 제안서 완료. HTML report gate passed.) -->
<!-- research-23 completed 2026-06-24T2055Z → intents/archive/research-23.md [projects: infinity,research-bank,world-models; type: research; topics: military,workflow,knowledge-management] (미군 TTP 학습 루프 심화 완료. HTML report gate passed.) -->
<!-- marketing-81 completed 2026-06-24T1007Z → intents/archive/marketing-81.md [projects: virtue; type: strategy; topics: marketing,activation,retention] (첫 저장/첫 판단 뒤 홈 복귀 secondary onboarding 감사표 완료. HTML report gate passed.) -->
<!-- research-22 completed 2026-06-24T0800Z → intents/archive/research-22.md (6단계 운영표･도구 비교･현실 루프 완료. HTML report gate passed.) -->
<!-- build-13 completed 2026-06-24T0050Z → intents/archive/build-13.md [projects: afzma,infinity,app-api-verification; type: implementation-verification; topics: hospital-api,api-flow,app-verification] (로컬 shdkej/afzma read-only 검증 완료. HTML report gate passed.) -->
<!-- marketing-80 completed 2026-06-23T2207Z → intents/archive/marketing-80.md [projects: virtue; type: strategy; topics: marketing,activation,product,feedback-consistency] (홈 요약 카드･`최근 덕행`･`/add` 결과･저장 후 복귀 지점을 J1-J4 기준으로 감사표로 정리. HTML report gate passed.) -->
<!-- marketing-79 completed 2026-06-23T1000Z → intents/archive/marketing-79.md [projects: virtue; type: strategy; topics: marketing,activation,prelaunch] (첫 10명 활성화 1장 관찰표 초안 완성. HTML report gate passed.) -->
<!-- marketing-78 completed 2026-06-22T1700Z → intents/archive/marketing-78.md [projects: virtue; type: strategy; topics: marketing,activation,product] (홈 `최근 덕행` empty state 3요소 비교 완료. HTML report gate passed.) -->
<!-- marketing-77 completed 2026-06-22T1431Z → intents/archive/marketing-77.md [projects: virtue; type: strategy; topics: marketing,activation,product,ui-copy] (`/add` 기대 브리지 1줄 + 결과 카드 footer 안내 1줄 구현 완료.) -->
<!-- marketing-76 completed 2026-06-22T1029Z → intents/archive/marketing-76.md [projects: virtue; type: strategy; topics: marketing,activation,product,in-app-guidance] (`/add`･결과 카드･홈 empty state 맥락형 안내 감사표 완료. HTML report gate passed.) -->
<!-- marketing-75 completed 2026-06-22T1029Z → intents/archive/marketing-75.md [projects: virtue; type: strategy; topics: marketing,activation,launch-communication,product] (Tier 1-4 변경 등급표와 권장 안내 표면 맵 완료. HTML report gate passed.) -->
<!-- marketing-74 completed 2026-06-22T0600Z → intents/archive/marketing-74.md [projects: virtue; type: strategy; topics: marketing,activation,product,onboarding] (/add 입력 전 기대 형성 3안 비교 완료. HTML report gate passed.) -->
<!-- research-20 completed 2026-06-21T1200Z → intents/archive/research-20.md (강의/교육 퍼널 제외 국내 1인 브랜드 10선 재조사 완료. HTML report gate passed.) -->
<!-- research-19 completed 2026-06-21T0720Z → intents/archive/research-19.md (드로우앤드류･자청 제외 국내 1인 브랜드 10선 분석 완료. HTML report gate passed.) -->
<!-- marketing-73 completed 2026-06-21T0700Z → intents/archive/marketing-73.md [projects: virtue; type: strategy; topics: marketing,activation,product] (J3 AI 브리지 3안 비교 완료. HTML report gate passed.) -->
<!-- marketing-72 completed 2026-06-20T2218Z → intents/archive/marketing-72.md [display: Virtue First-Session Intent Hint Compare; projects: virtue; type: strategy; topics: activation,marketing,product] (HTML report gate passed.) -->
<!-- research-18 completed 2026-06-20T1200Z → intents/archive/research-18.md [display: 자동화 시스템 신뢰성 강화 리서치; projects: infinity,research-bank,personal-ops; type: research; topics: automation,reliability,operations] (HTML report gate passed.) -->
<!-- marketing-71 completed 2026-06-20T1108Z → intents/archive/marketing-71.md [display: Virtue Seeded Proof Proposal Compare; projects: virtue; type: strategy; topics: activation,onboarding,proof,prelaunch] (HTML report gate passed.) -->
<!-- research-17 completed 2026-06-20T0700Z → intents/archive/research-17.md [display: 미군 연구 시스템 구조 리서치; projects: infinity,research-bank,world-models; type: research; topics: military,research-system,innovation,doctrine,training] (HTML report gate passed.) -->
<!-- marketing-70 completed 2026-06-19T22:07Z → intents/archive/marketing-70.md [display: Virtue Empty-State Proof Audit; projects: virtue; type: strategy; topics: activation,empty-state,marketing] (HTML report gate passed.) -->
<!-- marketing-69 completed 2026-06-19T10:07Z → intents/archive/marketing-69.md [display: Virtue Agent Readiness Baseline; projects: virtue; type: strategy; topics: ai-agents,agentic-web,discoverability,trust,prelaunch] (HTML report gate passed.) -->
<!-- marketing-68 completed 2026-06-19T0000Z → intents/archive/marketing-68.md [display: Virtue Agent-Readable Surface Audit; projects: virtue; type: strategy; topics: ai-agents,agentic-web,trust,discoverability,prelaunch] (HTML report gate passed.) -->
<!-- marketing-67 completed 2026-06-18T12:07Z → intents/archive/marketing-67.md [display: Virtue AI Authorization Boundary Table; projects: virtue; type: strategy; topics: ai-agents,trust,authorization,prelaunch] (HTML report gate 통과.) -->
<!-- build-12 completed 2026-06-18T11:57Z → intents/archive/build-12.md [projects: personal-ops,infinity,design-system; type: implementation; topics: 3d-background,interactive-character,skill] (Option D pre-rendered+CSS parallax 구현 완료.) -->
<!-- research-16 completed 2026-06-18T08:00Z → intents/archive/research-16.md (SAM YouTube parse 기반 CharacterStage 구현 옵션 재비교 완료.) -->
<!-- research-15 completed 2026-06-18T07:00Z → intents/archive/research-15.md [display: 3D Interactive Character Background Feasibility; projects: personal-ops,infinity,design-system; type: research; topics: 3d-background,interactive-character,threejs,design-system] -->
<!-- marketing-66 completed 2026-06-17T22:07Z → intents/archive/marketing-66.md [display: Virtue Agentic Context Map; projects: virtue; type: strategy; topics: agentic-plg,positioning,activation,prelaunch] -->
<!-- marketing-65 completed 2026-06-17T10:24Z → intents/archive/marketing-65.md [display: Virtue Agent Trust Evidence Inventory; projects: virtue; type: strategy] -->
<!-- marketing-64 completed 2026-06-17T01:18Z → intents/archive/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy] -->
<!-- build-11 completed 2026-06-16T21:56Z → intents/archive/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] -->
