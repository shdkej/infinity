# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox



## Active

<!-- build-03 active 2026-06-12T00:03Z → intents/active/build-03.md [display: Control Center / Ops CMS; projects: infinity,personal-ops,infrastructure; type: design; topics: dashboard,workflow,automation; status: active-inventory-draft-ready] (Inbox에서 Active로 이동. L0 research: 대시보드 inventory draft 작성 완료. Travel/Status/Infinity/Card Library/wedding 5개 대시보드 파악, 실제 경로·URL은 local 확인 필요. 다음 액션: local Claude에서 실제 경로 확인 후 inventory 완성 → MVP 정보구조 확정. 구현/배포/새 write API/프로덕션 변경은 별도 승인 후. 산출물: artifacts/build-03/dashboard-inventory-draft.md.) -->

<!-- naver-shopping-01 active 2026-06-11T00:35Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-screen-in-progress; approval: no-current-user-blocker] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 00:08Z 트래블러스노트/여행준비 속지는 "너무 일반적"으로 첫 SKU 후보에서 내림. 14:09Z 사용자 피드백으로 워크샵/질문카드 monetization path는 Naver revenue/SKU 후보에서 철회됨. 20:07Z paper/card-led arrival-day failure-prevention insert keyword test 완료: `해외여행 체크리스트`는 clean-ish paper/planner shelf(OpenAPI 32,278; SearchAd 310 PC + 1,750 mobile/mo)지만 mobile CTR 0.05%로 buyer intent 약하고 generic checklist/planner commodity. `여행 준비 카드`/`여행 체크리스트 카드`는 trading cards/photo-card holders/boards/wallets/imported goods noise가 큼. emergency/safety/contact-card 언어는 story-rich but keyword-weak/non-travel/privacy-sensitive. 결론은 **HOLD / paper-card insert를 lead SKU로 만들지 않음**. 산출물 `naver-shopping-agent/arrival-day-insert-keyword-test-2026-06-10.md`, report `reports/naver-shopping-01/2026-06-10T2007Z-local.html`. 2026-06-11 사용자 선호 업데이트: 나래는 상품제작보다 소싱 중심으로 보고, 러기지택/캐리어네임택은 선호 낮은 상품이라 다음 리드에서 내림. 다음 안전 액션은 broader sourcing-first screen. 2026-06-12T00:03Z sourcing screen 완료: 케이블 오거나이저 파우치(1위), 압축/실리콘 파우치(2위), 여권케이스(3위) 후보 선정. 실제 네이버 수요 확인은 local session 필요. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->



## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-54 completed 2026-06-11T22:07Z → reports/marketing-54/2026-06-11T2207Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,prelaunch,feedback-loop] (Virtue 첫 10명 관찰/질문 스크립트 기대-획득-막힘 이유 루프 감사표 작성 완료. 산출물 `artifacts/marketing-54/virtue-first-10-expectation-outcome-blocker-loop-audit.md`. 출처노트 `source/external-links/marketing/2026-06-11-onboarding-feedback-loop.md`는 knowledge-lab 루트 기준 존재 확인. J1/J2/J4=`deed_saved`, J3=`deed_judged` first-value 매핑 유지. 정상 종료, 혼란 종료, 가치 미전달, 이미 충분해서 종료를 manual exit class로 분리. 신규 이벤트·인앱 서베이·tracking/privacy·공개 카피·배포·외부발송·비용 변경 0. conflict marker 0건. HTML report gate(`<html`/`<body`/`axis ax1`/`axis ax2`/`<details`) 통과.) -->

<!-- marketing-53 completed 2026-06-11T10:15Z → reports/marketing-53/2026-06-11T1015Z-local.html [projects: virtue; type: strategy; topics: ai-onboarding,activation,prelaunch] (Virtue 첫 입력/결과 직후 task-completion 감사표 작성 완료. 산출물 `artifacts/marketing-53/virtue-intent-to-task-completion-audit-table.md`. 출처노트 `source/external-links/marketing/2026-06-11-ai-onboarding-intent-to-task.md`(knowledge-lab 루트 기준 존재 확인 — intent에 기재된 경로는 infinity 루트가 아니라 knowledge-lab 루트 상대경로였음)의 ProductLed/Userflow AI 온보딩 렌즈를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 3칸 분해로 번역해 답변형 vs 작업완료형 온보딩을 잡별(J1~J4)로 분리. 핵심: `add_flow_started`=의도 진입/`deed_judged`=AI 작업 수행/`deed_saved`·무저장 종료·`deed_rerolled`=다음 행동. J1/J2/J4 작업완료=`deed_saved`, J3=`deed_judged` 자체(무저장 완료).) -->

<!-- marketing-52 completed 2026-06-10T23:12Z → reports/marketing-52/2026-06-10T2312Z.html [projects: virtue; type: research; topics: positioning,competitor,ai-value] (Virtue 경쟁자 AI 에이전트/툴 포지셔닝 연구 완료. 산출물 `artifacts/marketing-52/virtue-competitor-positioning-research.md`. Gumloop/Clay/Make/Notion AI/Taskade를 분석, Virtue의 차별점은 "habit-layer/micro-context capture for personal AI value proxy" — 타사는 workflow/output 중심, Virtue는 daily-habit × context 중심.) -->

<!-- naver-shopping-01 waiting-paused 2026-06-10T20:07Z — paper-card insert HOLD. 소싱 중심으로 전환, 러기지택 내림. broader sourcing screen 진행 중 -->

<!-- marketing-51 completed 2026-06-10T07:45Z → reports/marketing-51/2026-06-10T0745Z.html [projects: virtue; type: strategy; topics: activation,onboarding,jtbd] -->

<!-- marketing-50 completed 2026-06-09T22:00Z → reports/marketing-50/2026-06-09T2200Z.html [projects: virtue; type: strategy; topics: jtbd,segmentation,persona] -->

<!-- dev-01 completed 2026-06-07T12:00Z → intents/archive/dev-01.md -->

<!-- monitor-02 completed 2026-06-06T09:00Z → intents/archive/monitor-02.md -->

<!-- wiki-04 completed 2026-04-25 → intents/archive/wiki-04.md -->

<!-- build-01 completed 2026-04-21 → intents/archive/build-01.md (cancelled - already done via wiki-02/03) -->

<!-- wiki-03 completed 2026-04-20 → intents/archive/wiki-03.md -->

<!-- wiki-02 completed 2026-04-19 → intents/archive/wiki-02.md -->

<!-- doc-01 completed 2026-04-08 → intents/archive/doc-01.md -->

<!-- monitor-01 completed 2026-04-08 → intents/archive/monitor-01.md -->
