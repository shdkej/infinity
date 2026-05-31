# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-31: Virtue 첫 세션 제품 본체/범퍼 경계표 작성

- id: marketing-31
- status: in_progress
- priority: medium
- permission: L1
- project: virtue
- goal: virtue-rebirth-app 내부 docs에 J1~J4 × 첫 세션 5개 표면 × 본체/범퍼 역할 × 정상 종료/막힘 판독 기준 표 작성
- success_criteria:
  - docs/first-session-product-body-bumper-map.md 생성 (virtue-rebirth-app)
  - J1~J4 × 5개 표면 × 본체/범퍼 역할 × 정상종료/막힘 판독 기준 표 포함
  - 기존 first value 매핑(deed_saved, deed_judged) 재정의 없음
  - conflict marker 0, 코드 diff 0, 신규 이벤트/속성/카피/배포 0
- context:
  - source: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-05-31-product-led-onboarding-bumpers.md
  - target: virtue-rebirth-app/apps/web/docs/first-session-product-body-bumper-map.md
  - related: m06/m16/m17/m19/m21 (apps/web/docs/ 내 선행 문서)
- mode: prepare (cloud, done) → execute_local (대기)
- prepared_artifact: artifacts/marketing-31/first-session-product-body-bumper-map-draft.md
- prepared_report: reports/marketing-31/2026-05-31T0830Z-prepare.html
- next_action: Local Claude Code → virtue-rebirth-app/apps/web/docs/에 draft 기반 문서 작성 후 커밋·push

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 결과 공유성 판독 기준 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/shareworthy-first-result-observation-criteria.md`(신규 1파일). ProductLed AI 온보딩 렌즈의 세 신호 중 ③ "공유하거나 추천하고 싶은 첫 경험"만 잡별로 번역(①60초 가치·②입력 대비 결과 강도는 m20/m21이 이미 소유). 핵심 신규 판독: 공유성(shareworthiness)을 first value·acceptance와 구분되는 별도 축(resonance/advocacy)으로 정의 — "첫 결과"를 (a)가치 도달 (b)공유성 (c)저장 후 누적 payoff 세 층으로 분리. 저장 없이 공유성 있음(J3 결과 읽고 보여 주고 닫음=정상)·저장 있으나 공유성 없음(J1 묵묵한 저장) 모두 가능하므로 공유성은 항상 저장 전 시점에서 따로 기록. §2 행동 증거 사전 B1~B6(웃음/놀람/반박/다르게 보기 재시도/보여 주기/재전달) 중 B4만 on-instrument(`deed_rerolled`:149), 나머지 5종 off-instrument → 저장수·재판정수로 공유성 환산 금지, 손기록 전용. §3 심장표 J1~J4 × first value × 공유성 관찰 순간 × 기대 행동 증거 × 누적 payoff 분리 × 기존 이벤트 매핑 × misread. §4 Inform/Guide/Execute/Orchestrate 감사: `/add`는 `deed_judged`:106 결과 카드 생성으로 이미 Execute 도달(기존 증거), 단 Execute≠자동 shareworthy이고 그 손기록 양식 부재가 본 문서 공백. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(앵커 72/106/149/167/183/199 drift 0), `deed_save_capped`:167은 availability/friction(upgrade 환산 금지) 계승. §5 prelaunch 금지선(전환율/PMF/벤치마크 산출·1명 단정·저장수=공유성 환산·cap=공유/upgrade 신호·J3 judged−saved 갭=가치 부재·synthetic 혼입·신규 이벤트/코드/카피/계측/배포/외부발송/비용/권한 변경 금지). §6 계승/변경/충돌/승격 분리: 선행 6문서(jtbd-matrix/proxy-dictionary/input-output-balance/60s-script/monetization-boundary/copy-spec) 충돌 0. 검증 게이트 PASS: conflict marker 0, virtue 코드 diff 0(doc 1파일만), HTML 보고서 포함, HEAD==origin/master. durable learning "Shareworthiness Is A Separate Axis"를 MARKETING_LEARNINGS.md에 승격. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,trust,measurement,prelaunch] (Virtue AI outcome proxy 사전 작성 완료. 산출물은 virtue-rebirth-app `22f3aea`의 `apps/web/docs/ai-outcome-proxy-dictionary.md`(신규 1파일). first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,pricing,activation,prelaunch] (Virtue prelaunch 유료화 경계 브리프 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판독 경계표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료.) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. L2 agent-approved push 정상 fast-forward.) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치 완료.) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. L2 agent-approved push.) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료.) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료.) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프 작성 완료.) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표 작성 완료.) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표 작성 완료.) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료.) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿 작성 완료.) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리 작성 완료.) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 배포 완료.) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 작성 완료.) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표 작성 완료.) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 작성 완료.) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표 작성 완료.) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 작성 완료.) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성 완료.) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안 완료.) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md (Virtue 최신 상태, 후속 개선은 별도 Intent로 분리) -->

<!-- build-02 completed 2026-05-13 → intents/archive/build-02.md (https://infinity.oracle.shdkej.com 배포 완료) -->

<!-- research-06 completed 2026-05-05T08:00 → intents/archive/research-06.md -->

<!-- wiki-05 completed 2026-04-25T09:00 → intents/archive/wiki-05.md -->

<!-- wiki-04 completed 2026-04-25T10:15 → intents/archive/wiki-04.md -->

<!-- wiki-02 completed 2026-04-19T02:45 → intents/archive/wiki-02.md -->
<!-- wiki-03 completed 2026-04-20T13:30 → intents/archive/wiki-03.md -->
<!-- research-05 completed 2026-04-21T00:00 → intents/archive/research-05.md -->
<!-- wiki-01 completed 2026-04-21T00:00 → intents/archive/wiki-01.md -->
<!-- build-01 completed 2026-04-21T00:30 → intents/archive/build-01.md -->
<!-- research-05 re-run completed 2026-04-23T10:00 → intents/archive/research-05.md (3차) -->
