# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

<!-- research-15 inbox 2026-06-18T06:20Z → intents/inbox/research-15.md [display: 3D Interactive Character Background Feasibility; projects: personal-ops,infinity,design-system; type: research; topics: 3d-background,interactive-character,threejs,design-system,skill] (YouTube reference `https://www.youtube.com/watch?v=dROkEnvxch4`를 보고, Sam Samuel 웹의 핵심 공간 문법인 interactive 3D character background + floating HUD/buttons를 구현하는 방법과 더 단순한 대안을 비교한다. 산출물은 구현 옵션 3단계, 기술 스택/성능/모바일 배치, Status 적용안, DESIGN.md/DESIGN_SYSTEM.md 반영 위치, 향후 reusable skill 초안.) -->


## Active
<!-- naver-shopping-01 active 2026-06-17T1200Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: prepare-complete-session-waiting; approval: sample-order-gated] (cloud prepare 완료: 1688 현장 확인 체크리스트(Huanhuan/Zhanhong/Kemeng 색상·MOQ·리뷰·최근거래·커넥터·패치) + 네이버 스마트스토어 손목 스트랩 등록 초안(상품명 후보·키워드·가격 KRW 1800-2500·설명·이미지가이드·콘텐츠앵글) 작성. 공급사 shortlist(Huanhuan/Zhanhong/Kemeng) 유지. 사용자 브라우저 세션 1회로 체크리스트 실행 → 공급사 확정 → 샘플 주문 승인 요청 가능. 추가 cloud prepare 불필요. 샘플 주문·라이브 등록·가격·배송·재고·광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-18T04:00Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; decision: 사용자 브라우저 세션 열어서 1688 체크리스트 실행 → 공급사(Huanhuan/Zhanhong) 확정 → 샘플 주문 승인 요청; options: 지금 브라우저 열어서 체크리스트 실행 | 나래 대기 유지 | 보류; reason: 1688 verified session 필요(unusual-traffic slider), SmartStore Commerce ID login wall; next: 사용자 브라우저 세션이 열리면 체크리스트 1회로 공급사 확정 + 샘플 주문 승인 요청 가능. cloud prepare 완료, do_not_repeat_cloud 활성, 추가 cloud 작업 없음.] (2026-06-18 heartbeat: cloud prepare 완료 확인. 1688 현장 확인 체크리스트(artifacts/naver-shopping-01/wrist-strap-1688-verification-checklist.md) + 네이버 등록 초안(artifacts/naver-shopping-01/naver-listing-draft-wrist-strap.md) 작성 완료. 다음 유효 액션은 사용자 브라우저 세션만으로 가능. loop-guard 활성, 반복 cloud 리서치 금지. sample-order-gated 유지.) -->

## Archive
<!-- marketing-66 completed 2026-06-17T22:07Z → intents/archive/marketing-66.md [display: Virtue Agentic Context Map; projects: virtue; type: strategy; topics: agentic-plg,positioning,activation,prelaunch] (J1-J4별 user_intent, context_before_output, first_output, context_after_output, agent_misread_boundary를 정리한 내부 문맥 지도 완성. 신규 이벤트·tracking/privacy·API/MCP·public copy·deploy·external message·cost 변경 0. 기존 marketing-18/55/58/60/63/65 참조와 충돌 없이 prelaunch low-signal 금지선 유지. HTML report gate 통과.) -->
<!-- 이 섹션의 상세 이력은 2026-06-17T10:24Z Heartbeat 과정에서 INTENTS.md 갱신 중 일시 유실됨. 개별 intent 원장은 intents/archive/*.md 에 모두 보존되어 있음. -->
<!-- build-11 completed 2026-06-16T21:56Z → intents/archive/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] -->
<!-- marketing-64 completed 2026-06-17T01:18Z → intents/archive/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy] -->
<!-- marketing-65 completed 2026-06-17T10:24Z → intents/archive/marketing-65.md [display: Virtue Agent Trust Evidence Inventory; projects: virtue; type: strategy] -->
