# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox



## Active

<!-- naver-shopping-01 active 2026-06-16T14:30Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (2026-06-16 1688 손목 스트랩 공개 소싱 사전 조회 완료: `手机防丢绳 / 手腕绳 / 手机挂绳`, 폴리에스터 CNY 0.10~1.50, 나일론+조절 클립 CNY 0.68~3.80, 목표 단가 CNY ≤3/MOQ ≤50 충족 가능. 이 cloud/public prepare 단계는 반복 금지. 다음 유효 액션은 로컬 브라우저/사용자 세션으로 1688 공급사 2~3개 실제 비교 및 샘플 주문 후보 선정. 1688/브라우저 세션이 없으면 새 리서치 반복 대신 Waiting 유지. 라이브 상품등록·가격·배송·재고·광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

## Archive
<!-- marketing-64 completed 2026-06-17T0200Z → intents/archive/marketing-64.md [display: Virtue Early Behavior Intent Sequence Columns; projects: virtue; type: strategy; topics: plg,activation,behavioral-analytics,prelaunch] (Mixpanel 2026 PLG 행동 기반 의도 신호 렌즈를 Virtue prelaunch first-10 수기 관찰 문맥으로 번역. activation event(계측 고정: J1/J2/J4=deed_saved, J3=deed_judged) vs intent sequence(수기 관찰 4컬럼: first_explored_feature·stopped_at_screen·skipped_actions·post_save_next_action) 이층 분리 제안. 신규 이벤트·tracking/privacy·dashboard·public copy·deploy 0. 기존 marketing-55~63 충돌 0. 산출물 artifacts/marketing-64/early-behavior-intent-sequence-columns.md, source note source/external-links/marketing/2026-06-16-plg-behavioral-intent-signals.md, report reports/marketing-64/2026-06-17T0200Z-cloud.html. HTML report gate passed.) -->
<!-- build-11 completed 2026-06-16T21:56Z → intents/archive/build-11.md [display: Status 3D Full-Image Floating Menu Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,3d-background,floating-menu; completion: user-confirmed] (마스터가 "아니야 끝났어"라고 완료 판정해 Active에서 Archive로 전환. 이후 마스터가 "다음 버전인데 백그라운드 이미지 있는거"라고 정정해 Status 대시보드는 배경 이미지가 있는 `a415066` 상태로 다시 복원/배포. Space commit `565cb67`; unrelated dirty file은 제외.) -->
<!-- build-10 completed 2026-06-16T11:00Z → intents/archive/build-10.md [display: Status Hers-Inspired Operations Glass Redesign; projects: infinity,personal-ops,infrastructure; type: implementation; topics: status,dashboard,ui,glassmorphism,deploy] (Behance Hers Healthcare App & Branding 레퍼런스를 밝은 wellness glass Status 페이지로 번역. 신규 배경 이미지 `sites/status/dist/assets/status-wellness-glass-bg.png`, Status index glass hero/card/panel redesign, 모바일 headline/score summary overflow 보정, `status.json` 재생성. 검증: local Chromium desktop/mobile screenshots, `python3 scripts/build-status-json.py --resolve-aws --check` PASS. Travel dirty change는 건드리지 않음. Terraform/AWS 신규 리소스/secret/force-push/external message 0.) -->
<!-- marketing-63 completed 2026-06-16T10:25Z → intents/archive/marketing-63.md [display: Virtue Agent-Readable Analytics Context Card; projects: virtue; type: strategy; topics: ai-agents,analytics,activation,measurement,prelaunch] (Amplitude AI analytics semantic-layer 사례를 Virtue prelaunch 측정 문맥으로 번역한 docs-only agent-readable context card 작성. 산출물 `artifacts/marketing-63/virtue-agent-readable-analytics-context-card.md`, report `reports/marketing-63/2026-06-16T1025Z-local.html`. 기존 이벤트 `deed_judged`/`deed_saved`/`level_up_viewed`와 J1-J4 first value mapping 유지, synthetic/test 제외 및 `insufficient_signal` 문구 포함, cap/limit 오독 방지와 launch-before/launch-after 판단선 포함. 신규 이벤트/tracking/privacy/dashboard/public copy/deploy/external message/cost 변경 0. HTML report gate passed.) -->
<!-- research-14 completed 2026-06-16T00:02Z → intents/archive/research-14.md [display: 모놀리스 아키텍처 보완 맥락 조사; projects: infinity,research-bank; type: research; topics: software-architecture,history,systems-design] (모놀리스는 특정 새 발명품이라기보다 분산 실행·분산 데이터·독립 배포가 만들 복잡도를 피하는 응집형 기본값이었고, 이후 규모가 커지며 그 응집이 병목으로 바뀌었다. 산출물 `artifacts/research-14/monolith-architecture-context.md`, report `reports/research-14/2026-06-16T0002Z-local.html`. 공개 발송·코드·배포·외부 액션 0. HTML report gate passed.) -->
<!-- research-13 completed 2026-06-15T23:47Z → intents/archive/research-13.md [display: 콘텐츠 제작 최소 설정 체크리스트; projects: infinity,research-bank,personal-ops; type: research; topics: content,workflow] (콘텐츠 제작 전 최소 설정을 `target_reader`, `reader_state`, `reader_problem`, `content_goal`, `core_message`, `angle`, `tone_voice`, `format_channel` 8개 필수값과 evidence/CTA/boundary/success 보조값으로 정리. 산출물 `artifacts/research-13/content-minimum-settings-checklist.md`, report `reports/research-13/2026-06-15T2347Z-local.html`. 공개 발송·콘텐츠 게시·코드·배포·외부 계정 액션 0.) -->
<!-- marketing-62 completed 2026-06-15T22:07Z → intents/archive/marketing-62.md [display: Virtue Agent-Delegated First Task Trust Gate; projects: virtue; type: strategy; topics: ai-agents,activation,marketing] -->
<!-- research-12 completed 2026-06-15T10:00Z → intents/archive/research-12.md -->
<!-- research-11 completed 2026-06-14T23:00Z → intents/archive/research-11.md -->
<!-- marketing-61 completed 2026-06-14T22:00Z → intents/archive/marketing-61.md -->
<!-- marketing-60 completed 2026-06-14T10:00Z → intents/archive/marketing-60.md -->
<!-- marketing-59 completed 2026-06-13T22:00Z → intents/archive/marketing-59.md -->
<!-- marketing-58 completed 2026-06-13T10:00Z → intents/archive/marketing-58.md -->
<!-- marketing-57 completed 2026-06-12T22:00Z → intents/archive/marketing-57.md -->
<!-- marketing-56 completed 2026-06-12T10:00Z → intents/archive/marketing-56.md -->
<!-- marketing-55 completed 2026-06-11T22:00Z → intents/archive/marketing-55.md -->
<!-- marketing-54 completed 2026-06-10T22:00Z → intents/archive/marketing-54.md -->
<!-- marketing-53 completed 2026-06-09T22:00Z → intents/archive/marketing-53.md -->
<!-- marketing-52 completed 2026-06-08T22:00Z → intents/archive/marketing-52.md -->
<!-- marketing-51 completed 2026-06-07T22:00Z → intents/archive/marketing-51.md -->
<!-- marketing-50 completed 2026-06-06T22:00Z → intents/archive/marketing-50.md -->
<!-- marketing-49 completed 2026-06-05T22:00Z → intents/archive/marketing-49.md -->
<!-- marketing-48 completed 2026-06-04T22:00Z → intents/archive/marketing-48.md -->
<!-- marketing-47 completed 2026-06-03T22:00Z → intents/archive/marketing-47.md -->
<!-- marketing-46 completed 2026-06-02T22:00Z → intents/archive/marketing-46.md -->
<!-- marketing-45 completed 2026-06-01T22:00Z → intents/archive/marketing-45.md -->
<!-- marketing-44 completed 2026-05-31T22:00Z → intents/archive/marketing-44.md -->
<!-- marketing-43 completed 2026-05-30T22:00Z → intents/archive/marketing-43.md -->
<!-- marketing-42 completed 2026-05-29T22:00Z → intents/archive/marketing-42.md -->
<!-- marketing-41 completed 2026-05-28T22:00Z → intents/archive/marketing-41.md -->
<!-- marketing-40 completed 2026-05-27T22:00Z → intents/archive/marketing-40.md -->
<!-- marketing-39 completed 2026-05-26T22:00Z → intents/archive/marketing-39.md -->
<!-- marketing-38 completed 2026-05-25T22:00Z → intents/archive/marketing-38.md -->
<!-- marketing-37 completed 2026-05-24T22:00Z → intents/archive/marketing-37.md -->
<!-- build-09 completed 2026-05-23T12:00Z → intents/archive/build-09.md -->
<!-- marketing-36 completed 2026-05-23T22:00Z → intents/archive/marketing-36.md -->
<!-- marketing-35 completed 2026-05-22T22:00Z → intents/archive/marketing-35.md -->
<!-- marketing-34 completed 2026-05-21T22:00Z → intents/archive/marketing-34.md -->
<!-- marketing-33 completed 2026-05-20T22:00Z → intents/archive/marketing-33.md -->
<!-- marketing-32 completed 2026-05-19T22:00Z → intents/archive/marketing-32.md -->
<!-- marketing-31 completed 2026-05-18T22:00Z → intents/archive/marketing-31.md -->
<!-- marketing-30 completed 2026-05-17T22:00Z → intents/archive/marketing-30.md -->
<!-- marketing-29 completed 2026-05-16T22:00Z → intents/archive/marketing-29.md -->
<!-- marketing-28 completed 2026-05-15T22:00Z → intents/archive/marketing-28.md -->
<!-- marketing-27 completed 2026-05-14T22:00Z → intents/archive/marketing-27.md -->
<!-- marketing-26 completed 2026-05-13T22:00Z → intents/archive/marketing-26.md -->
<!-- marketing-25 completed 2026-05-12T22:00Z → intents/archive/marketing-25.md -->
<!-- marketing-24 completed 2026-05-11T22:00Z → intents/archive/marketing-24.md -->
<!-- marketing-23 completed 2026-05-10T22:00Z → intents/archive/marketing-23.md -->
<!-- marketing-22 completed 2026-05-09T22:00Z → intents/archive/marketing-22.md -->
<!-- marketing-21 completed 2026-05-08T22:00Z → intents/archive/marketing-21.md -->
<!-- marketing-20 completed 2026-05-07T22:00Z → intents/archive/marketing-20.md -->
<!-- marketing-19 completed 2026-05-06T22:00Z → intents/archive/marketing-19.md -->
<!-- marketing-18 completed 2026-05-05T22:00Z → intents/archive/marketing-18.md -->
<!-- marketing-17 completed 2026-05-04T22:00Z → intents/archive/marketing-17.md -->
<!-- marketing-16 completed 2026-05-03T22:00Z → intents/archive/marketing-16.md -->
<!-- marketing-15 completed 2026-05-02T22:00Z → intents/archive/marketing-15.md -->
<!-- marketing-14 completed 2026-05-01T22:00Z → intents/archive/marketing-14.md -->
<!-- marketing-13 completed 2026-04-30T22:00Z → intents/archive/marketing-13.md -->
<!-- marketing-12 completed 2026-04-29T22:00Z → intents/archive/marketing-12.md -->
<!-- marketing-11 completed 2026-04-28T22:00Z → intents/archive/marketing-11.md -->
<!-- marketing-10 completed 2026-04-27T22:00Z → intents/archive/marketing-10.md -->
<!-- marketing-09 completed 2026-04-26T22:00Z → intents/archive/marketing-09.md -->
<!-- marketing-08 completed 2026-04-25T22:00Z → intents/archive/marketing-08.md -->
<!-- marketing-07 completed 2026-04-24T22:00Z → intents/archive/marketing-07.md -->
<!-- marketing-06 completed 2026-04-23T22:00Z → intents/archive/marketing-06.md -->
<!-- marketing-05 completed 2026-04-22T22:00Z → intents/archive/marketing-05.md -->
<!-- marketing-04 completed 2026-04-21T22:00Z → intents/archive/marketing-04.md -->
<!-- marketing-03 completed 2026-04-20T22:00Z → intents/archive/marketing-03.md -->
<!-- marketing-02 completed 2026-04-19T22:00Z → intents/archive/marketing-02.md -->
<!-- marketing-01 completed 2026-05-21T09:50Z → intents/archive/marketing-01.md -->
<!-- wiki-05 completed 2026-04-25T00:00 → intents/archive/wiki-05.md -->
<!-- wiki-04 completed 2026-04-25T00:00 → intents/archive/wiki-04.md -->
<!-- wiki-02 completed 2026-04-19T02:45 → intents/archive/wiki-02.md -->
<!-- wiki-03 completed 2026-04-20T13:30 → intents/archive/wiki-03.md -->
<!-- research-05 completed 2026-04-21T00:00 → intents/archive/research-05.md -->
<!-- wiki-01 completed 2026-04-21T00:00 → intents/archive/wiki-01.md -->
<!-- build-01 completed 2026-04-21T00:30 → intents/archive/build-01.md -->
<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->
# 2026-06-10T23:30Z - naver-shopping-01 source update

- `naver-shopping-01`: Added a docs-only sourcing-friction gate for the question/workshop-card family after applying the `marketing-50` rule, "purchase situation before object shape." The candidate remains DRAFT / copy-led; next useful check is small-batch production, MOQ, unit cost, category/product-info friction, and margin floor before any listing approval. No new target-agent request opened and no live commerce/account/public action occurred.