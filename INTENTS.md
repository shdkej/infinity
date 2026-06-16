# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active


<!-- naver-shopping-01 active 2026-06-15T00:14Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,marketing; status: active-sourcing-first; approval: user-setup-waiting-visible] (사용자-facing 이름 나래/Narae 확정, 내부 id/path는 naver-shopping-agent 유지. 2026-06-15 ready-made OpenAPI/SearchAd screen 결과: 휴대폰 도난방지 스트랩/테더가 WATCH lead, 압축/패킹 파우치는 WATCH, 케이블/충전기 파우치는 HOLD as lead. 다음 안전 액션은 상품 추천/승인 요청이 아니라 phone strap/tether subtype 및 compression pouch subtype의 소싱 마찰·클레임·옵션·반품 리스크 검증. 사용자 설정이 필요한 SmartStore Commerce ID / 읽기 전용 브라우저 / 공개 Naver Shopping 검색 제한은 Waiting 카드로 별도 노출한다. 라이브 상품등록/가격·배송·재고/광고·고객·주문·계정·공개발행 0. archive 안 함(active 유지).) -->



## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

<!-- naver-shopping-01 waiting 2026-06-14T05:45Z → intents/active/naver-shopping-01.md [display: 나래/Narae; projects: naver-shopping,infinity,personal-ops; type: coordination; topics: automation,workflow,commerce; decision: 네이버 커머스 사용자 설정 3가지를 언제 열어줄지 결정; options: 지금 Commerce ID/브라우저 세션 확인 | 나래는 공개/공식 데이터만으로 계속 진행 | 보류; default: 나래는 공개/공식 데이터만으로 계속 진행; reason: SmartStore Commerce ID, read-only browser access, and public Naver Shopping search restriction are user-side/external-condition blockers; next: 마스터가 Commerce ID/브라우저 접근을 열어주면 나래가 read-only 검증을 재개] (마스터 피드백 반영: 사용자가 해야 하는 설정/승인/외부조건은 적극적으로 Waiting에 걸어 둔다. 현재 대기: SmartStore Commerce ID 전환/로그인 확인, 사용자 브라우저 프로필 기반 read-only 접근 가능 여부, 에이전트 호스트의 공개 Naver Shopping 검색 제한 해소 또는 대체 접근. SAM/나래는 그 전까지 OpenAPI/SearchAd/공식 문서/공개 웹 중심의 소싱-퍼스트 리서치를 계속한다. 라이브 상품등록·가격·배송·재고·광고·고객/주문/계정 액션 0.) -->

## Archive
<!-- research-14 completed 2026-06-16T06:00Z → intents/archive/research-14.md ("모놀리스"는 의도된 아키텍처가 아니라 분산복잡성 대비 자연발생한 단일 프로세스 구조이며, 마이크로서비스 담론이 부상하면서 소급 명명된 용어임. 보완: 분산실패·네트워크오버헤드·배포복잡도. 한계: 선택적확장불가·팀조율비용·장애확산. 산출물 artifacts/research-14/, report reports/research-14/2026-06-16T0600Z-research.html.) -->
<!-- research-13 completed 2026-06-15T23:47Z → intents/archive/research-13.md [display: 콘텐츠 제작 최소 설정 체크리스트; projects: infinity,research-bank,personal-ops; type: research; topics: content,workflow] (콘텐츠 제작 전 최소 설정을 `target_reader`, `reader_state`, `reader_problem`, `content_goal`, `core_message`, `angle`, `tone_voice`, `format_channel` 8개 필수값과 evidence/CTA/boundary/success 보조값으로 정리. 산출물 `artifacts/research-13/content-minimum-settings-checklist.md`, report `reports/research-13/2026-06-15T2347Z-local.html`. 공개 발송·콘텐츠 게시·코드·배포·외부 계정 액션 0.) -->
<!-- marketing-62 completed 2026-06-15T22:07Z → intents/archive/marketing-62.md [display: Virtue Agent-Delegated First Task Trust Gate; projects: virtue; type: strategy; topics: ai-agents,activation,marketing] (AI-native PLG delegation lens를 Virtue first-task trust gate로 번역. 산출물 `artifacts/marketing-62/virtue-agent-delegated-first-task-trust-gate.md`, report `reports/marketing-62/2026-06-15T2207Z-local.html`. click completed / delegated task completed / trusted next action을 J1-J4별로 분리해 `deed_judged`/`deed_saved` 오독을 줄임. 선행 marketing-55/58/60/61 충돌 0. 신규 이벤트·tracking/privacy·dashboard·public copy·pricing·deploy·external message·cost 변경 0. HTML report gate passed.) -->
<!-- marketing-61 completed 2026-06-15T10:07Z → intents/archive/marketing-61.md [display: Virtue Launch-After Activation Cohort Boundary; projects: virtue; type: strategy; topics: plg,activation,pql,measurement,prelaunch] (Mixpanel 2026 PLG activation/PQL 렌즈를 Virtue launch-after cohort 경계로 번역. 산출물 `artifacts/marketing-61/virtue-launch-after-activation-cohort-boundary.md`, report `reports/marketing-61/2026-06-15T1007Z-local.html`. J1-J4별 activation 후보, 7일 재방문/반복 가치 후보, PQL 보류선, cap/limit 신호 해석 경계를 first-10 수기 관찰과 launch-after 정량 cohort로 분리. 선행 marketing-55/59/60 충돌 0. 신규 이벤트·tracking/privacy·dashboard·public copy·pricing·deploy·external message·cost 변경 0. HTML report gate passed.) -->
<!-- marketing-60 completed 2026-06-14T22:07Z → intents/archive/marketing-60.md [display: Virtue Outcome-Readable Docs Audit; projects: virtue; type: strategy; topics: activation,outcome-docs,prelaunch] (Agentic PLG outcome-docs 렌즈를 Virtue first-10 결과 판독 감사표로 번역. 산출물 `artifacts/marketing-60/virtue-outcome-readable-docs-audit.md`, report `reports/marketing-60/2026-06-14T2207Z-local.html`. J1-J4별 좋은 결과/나쁜 결과/다음 행동 기준, 사람/에이전트 공통 판독 칸, first successful output 및 signal gate와의 충돌 방지 기준 포함. 신규 이벤트·tracking/privacy·public copy·deploy·external message·cost 변경 0. HTML report gate passed.) -->

<!-- marketing-59 completed 2026-06-14T10:07Z → intents/archive/marketing-59.md [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy; topics: plg,activation,measurement,prelaunch] (PLG first win/activation/PQL signal hierarchy translated into a Virtue prelaunch docs-only first-10 gate. Artifact `artifacts/marketing-59/virtue-launch-ready-plg-signal-gate.md`, report `reports/marketing-59/2026-06-14T1007Z-local.html`. Clear separation of look-now first-10 signals vs. launch-after cohort PQL. Prior marketing-55/58 conflict 0. New event/tracking/privacy/public-copy/deploy/external-message/cost change 0. HTML report gate passed.) -->
<!-- marketing-58 completed 2026-06-14T06:07Z → intents/archive/marketing-58.md [display: Virtue Jobs-to-Be-Done Map; projects: virtue; type: strategy; topics: jtbd,positioning,activation,prelaunch] (JTBD framework applied to Virtue's 3-profile target (solo creator, team lead, indie dev). Artifact `artifacts/marketing-58/virtue-jtbd-map.md`, report `reports/marketing-58/2026-06-14T0607Z-local.html`. Per-job pains, functional/emotional/social outcomes, and Virtue's position vs. direct/indirect substitutes mapped. Prior marketing-55 conflict 0. New event/tracking/public-copy/deploy/external-message/cost change 0. HTML report gate passed.) -->
<!-- marketing-57 completed 2026-06-13T22:07Z → intents/archive/marketing-57.md [display: Virtue Prelaunch Positioning Statement; projects: virtue; type: strategy; topics: positioning,messaging,prelaunch] (April Dunford positioning framework applied to Virtue. Artifact `artifacts/marketing-57/virtue-prelaunch-positioning-statement.md`, report `reports/marketing-57/2026-06-13T2207Z-local.html`. Competitive alternatives, unique attributes, value for target buyers, best-fit characteristics mapped. Positioning statement and 3-tier messaging ladder drafted. Prior marketing-55 conflict 0. No new event/tracking/public copy/deploy/external message/cost change. HTML report gate passed.) -->
<!-- marketing-56 completed 2026-06-13T10:07Z → intents/archive/marketing-56.md [display: Virtue Activation Hypothesis; projects: virtue; type: strategy; topics: activation,plg,onboarding,prelaunch] (Lenny Rachitsky PLG activation lens applied to Virtue. Artifact `artifacts/marketing-56/virtue-activation-hypothesis.md`, report `reports/marketing-56/2026-06-13T1007Z-local.html`. "Aha moment" candidate, time-to-value targets, onboarding friction map, and 3-tier activation ladder (visitor→active→habit) drafted for first 10 manual testers before launch. Prior marketing-55 conflict 0. No new event/tracking/public copy/deploy/external message/cost change. HTML report gate passed.) -->
<!-- marketing-55 completed 2026-06-12T22:07Z → intents/archive/marketing-55.md [display: Virtue Ideal Customer Profile; projects: virtue; type: strategy; topics: icp,positioning,plg,prelaunch] (Seth Godin smallest-viable-audience + April Dunford positioning lens applied to Virtue. Artifact `artifacts/marketing-55/virtue-icp-v1.md`, report `reports/marketing-55/2026-06-12T2207Z-local.html`. Profiles J1 (solo creator), J2 (team lead), J3 (indie dev), J4 (AI-forward enterprise) drafted. ICP priority order J1>J3>J2>J4 for launch. No new tracking event/public copy/deploy/external message/cost change. HTML report gate passed.) -->
<!-- marketing-54 completed 2026-06-12T10:07Z → intents/archive/marketing-54.md [display: Virtue prelaunch GTM audit; projects: virtue; type: strategy; topics: positioning,activation,marketing,prelaunch] (Seth Godin minimal-viable-market + PLG activation lens applied to Virtue prelaunch state. Key: Virtue's first 10 users define the real ICP, not the assumed one. Report `reports/marketing-54/2026-06-12T1007Z-local.html`. 4 open questions surfaced for next Heartbeat. No external message/tracking/public copy/deploy change. HTML report gate passed.) -->
<!-- marketing-53 completed 2026-06-11T22:07Z → intents/archive/marketing-53.md [display: Seth Godin Marketing Learnings (Round 2); projects: virtue; type: strategy; topics: marketing,positioning,prelaunch] (Second round of Seth Godin marketing principles synthesized from Purple Cow, This is Marketing, The Practice, Linchpin, Tribes. Artifact `artifacts/marketing-53/seth-godin-marketing-learnings-round2.md`, report `reports/marketing-53/2026-06-11T2207Z-local.html`. Key: permission asset before reach, find your smallest viable market first, generosity as strategy. MARKETING_LEARNINGS.md updated with 3 new durable learnings. No external message/tracking/deploy/cost change. HTML report gate passed.) -->
<!-- marketing-52 completed 2026-06-11T10:07Z → intents/archive/marketing-52.md [display: Seth Godin Marketing Learnings; projects: virtue; type: strategy; topics: marketing,positioning] (Seth Godin marketing principles synthesized from Purple Cow, This is Marketing, The Dip, All Marketers Are Liars. Artifact `artifacts/marketing-52/seth-godin-marketing-learnings.md`, report `reports/marketing-52/2026-06-11T1007Z-local.html`. Key durable learnings promoted to MARKETING_LEARNINGS.md. No external message/tracking/deploy/cost change. HTML report gate passed.) -->
<!-- product-01 completed 2026-06-10T22:07Z → intents/archive/product-01.md [display: Virtue feature audit / prelaunch readiness; projects: virtue; type: strategy; topics: product,prelaunch,roadmap] (Virtue feature audit completed. Report `reports/product-01/2026-06-10T2207Z-local.html`. Core loop working, 5 pre-launch gaps identified (onboarding, empty state, mobile, error UX, performance). No deploy/external message/cost change. HTML report gate passed.) -->
<!-- build-08 completed 2026-06-10T10:07Z → intents/archive/build-08.md [display: Virtue build/CI audit; projects: virtue; type: ops; topics: ci,build,infra] (CI/build pipeline audit completed. Report `reports/build-08/2026-06-10T1007Z-local.html`. 3 gaps: missing staging env, no automated e2e, k8s deploy not in CI. Recommendations prepared. No deploy/external message/cost change. HTML report gate passed.) -->
<!-- marketing-51 completed 2026-06-09T22:07Z → intents/archive/marketing-51.md [display: Virtue competitive landscape; projects: virtue; type: research; topics: competitors,positioning,marketing] (Competitive landscape mapped for Virtue. Report `reports/marketing-51/2026-06-09T2207Z-local.html`. Direct: Notion AI, Craft, Mem.ai. Indirect: Linear, Obsidian+plugins. Key differentiation: agent-delegated task completion vs. AI-writing-assistance. No external message/tracking/deploy/cost change. HTML report gate passed.) -->
<!-- marketing-50 completed 2026-06-09T10:07Z → intents/archive/marketing-50.md -->
<!-- marketing-49 completed 2026-06-08T22:07Z → intents/archive/marketing-49.md -->
<!-- marketing-48 completed 2026-06-08T10:07Z → intents/archive/marketing-48.md -->
<!-- marketing-47 completed 2026-06-07T22:07Z → intents/archive/marketing-47.md -->
<!-- marketing-46 completed 2026-06-07T10:07Z → intents/archive/marketing-46.md -->
<!-- marketing-45 completed 2026-06-06T22:07Z → intents/archive/marketing-45.md -->
<!-- marketing-44 completed 2026-06-06T10:07Z → intents/archive/marketing-44.md -->
<!-- marketing-43 completed 2026-06-05T22:07Z → intents/archive/marketing-43.md -->
<!-- marketing-42 completed 2026-06-05T10:07Z → intents/archive/marketing-42.md -->
<!-- marketing-41 completed 2026-06-04T22:07Z → intents/archive/marketing-41.md -->
<!-- marketing-40 completed 2026-06-04T10:07Z → intents/archive/marketing-40.md -->
<!-- marketing-39 completed 2026-06-03T22:07Z → intents/archive/marketing-39.md -->
<!-- marketing-38 completed 2026-06-03T10:07Z → intents/archive/marketing-38.md -->
<!-- marketing-37 completed 2026-06-02T22:07Z → intents/archive/marketing-37.md -->
<!-- marketing-36 completed 2026-06-02T10:07Z → intents/archive/marketing-36.md -->
<!-- marketing-35 completed 2026-06-01T22:07Z → intents/archive/marketing-35.md -->
<!-- marketing-34 completed 2026-06-01T10:07Z → intents/archive/marketing-34.md -->
<!-- marketing-33 completed 2026-05-31T22:07Z → intents/archive/marketing-33.md -->
<!-- marketing-32 completed 2026-05-31T10:07Z → intents/archive/marketing-32.md -->
<!-- marketing-31 completed 2026-05-30T22:07Z → intents/archive/marketing-31.md -->
<!-- marketing-30 completed 2026-05-30T10:07Z → intents/archive/marketing-30.md -->
<!-- marketing-29 completed 2026-05-29T22:07Z → intents/archive/marketing-29.md -->
<!-- marketing-28 completed 2026-05-29T10:07Z → intents/archive/marketing-28.md -->
<!-- marketing-27 completed 2026-05-28T22:07Z → intents/archive/marketing-27.md -->
<!-- marketing-26 completed 2026-05-28T10:07Z → intents/archive/marketing-26.md -->
<!-- marketing-25 completed 2026-05-27T22:07Z → intents/archive/marketing-25.md -->
<!-- marketing-24 completed 2026-05-27T10:07Z → intents/archive/marketing-24.md -->
<!-- marketing-23 completed 2026-05-26T22:07Z → intents/archive/marketing-23.md -->
<!-- marketing-22 completed 2026-05-26T10:07Z → intents/archive/marketing-22.md -->
<!-- marketing-21 completed 2026-05-25T22:07Z → intents/archive/marketing-21.md -->
<!-- marketing-20 completed 2026-05-25T10:07Z → intents/archive/marketing-20.md -->
<!-- marketing-19 completed 2026-05-24T22:07Z → intents/archive/marketing-19.md -->
<!-- marketing-18 completed 2026-05-24T10:07Z → intents/archive/marketing-18.md -->
<!-- marketing-17 completed 2026-05-23T22:07Z → intents/archive/marketing-17.md -->
<!-- marketing-16 completed 2026-05-23T10:07Z → intents/archive/marketing-16.md -->
<!-- marketing-15 completed 2026-05-22T22:07Z → intents/archive/marketing-15.md -->
<!-- marketing-14 completed 2026-05-22T10:07Z → intents/archive/marketing-14.md -->
<!-- marketing-13 completed 2026-05-21T22:07Z → intents/archive/marketing-13.md -->
<!-- marketing-12 completed 2026-05-21T10:07Z → intents/archive/marketing-12.md -->
<!-- marketing-11 completed 2026-05-20T22:07Z → intents/archive/marketing-11.md -->
<!-- marketing-10 completed 2026-05-20T10:07Z → intents/archive/marketing-10.md -->
<!-- marketing-09 completed 2026-05-19T22:07Z → intents/archive/marketing-09.md -->
<!-- marketing-08 completed 2026-05-19T10:07Z → intents/archive/marketing-08.md -->
<!-- marketing-07 completed 2026-05-18T22:07Z → intents/archive/marketing-07.md -->
<!-- marketing-06 completed 2026-05-18T10:07Z → intents/archive/marketing-06.md -->
<!-- marketing-05 completed 2026-05-17T22:07Z → intents/archive/marketing-05.md -->
<!-- marketing-04 completed 2026-05-17T10:07Z → intents/archive/marketing-04.md -->
<!-- marketing-03 completed 2026-05-16T22:07Z → intents/archive/marketing-03.md -->
<!-- marketing-02 completed 2026-05-16T10:07Z → intents/archive/marketing-02.md -->
<!-- marketing-01 completed 2026-05-21 → intents/archive/marketing-01.md (add-flow telemetry merged/deployed to production after user approval. Virtue virtue-rebirth master=b28d01f, HTTP 200.) -->
<!-- housekeeping-marketing-08 completed 2026-05-19 → intents/archive/housekeeping-marketing-08.md -->
<!-- maintenance-implicit completed 2026-05-18 → intents/archive/maintenance-implicit.md -->
<!-- build-07 completed → intents/archive/build-07.md -->
<!-- build-06 completed → intents/archive/build-06.md -->
<!-- build-05 completed → intents/archive/build-05.md -->
<!-- build-04 completed → intents/archive/build-04.md -->
<!-- build-03 completed → intents/archive/build-03.md -->
<!-- build-01 cancelled 2026-04-21 → intents/archive/build-01.md (wiki already on Docsify/GitHub Pages; Jekyll not needed) -->
<!-- pages-01 completed → intents/archive/pages-01.md -->
<!-- wiki-05 completed → intents/archive/wiki-05.md -->
<!-- wiki-04 completed 2026-04-25 → intents/archive/wiki-04.md (auto-navigation.js added to shdkej/agent-wiki, approved by user) -->
<!-- wiki-03 completed 2026-04-20 → intents/archive/wiki-03.md (index.html pushed d52641c, GitHub Pages live) -->
<!-- wiki-02 completed 2026-04-19 → intents/archive/wiki-02.md (Docsify + GitHub Pages activated on shdkej/agent-wiki) -->
<!-- wiki-01 completed → intents/archive/wiki-01.md -->
<!-- monitor-01 completed → intents/archive/monitor-01.md -->
<!-- doc-01 completed → intents/archive/doc-01.md -->
<!-- research-12 completed → intents/archive/research-12.md -->
<!-- research-11 completed → intents/archive/research-11.md -->
<!-- research-10 completed → intents/archive/research-10.md -->
<!-- research-09 completed → intents/archive/research-09.md -->
<!-- research-08 completed → intents/archive/research-08.md -->
<!-- research-06 completed → intents/archive/research-06.md -->
<!-- research-05 completed → intents/archive/research-05.md -->
<!-- research-04 completed → intents/archive/research-04.md -->
<!-- research-03 completed → intents/archive/research-03.md -->
<!-- research-02 completed → intents/archive/research-02.md -->
<!-- research-01 completed → intents/archive/research-01.md -->
<!-- router-maintenance completed → intents/archive/router-maintenance.md -->
<!-- openclaw-chatroom-agent-design completed → intents/archive/openclaw-chatroom-agent-design.md -->
