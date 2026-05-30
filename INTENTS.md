# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-28 — Virtue prelaunch monetization boundary brief
- status: in_progress
- priority: medium
- permission: L1 (docs-only); paywall/AI cap/결제/배포는 L2 approval-required
- goal: Virtue prelaunch 단계에서 "무엇을 지금 잠그지 말아야 하는가"를 한 문서로 정리 — 가격/제한 논의를 activation 학습과 분리
- context:
  - source: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-30-plg-pricing-triggers.md`
  - target: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/prelaunch-monetization-boundary-brief.md`
  - cloud_draft: `artifacts/marketing-28/prelaunch-monetization-boundary-brief-draft.md`
- success_criteria:
  - J1-J4별 첫 가치 이전 금지 제한이 명시됨
  - 첫 가치 이후 확장 트리거 후보가 포함됨
  - `deed_save_capped` 오독 금지 원칙이 포함됨
  - 승인 필요 경계가 명시됨
  - 기존 first-value 매핑 재정의 없음 (J1/J2/J4=`deed_saved`, J3=`deed_judged`)
  - 신규 이벤트/카피/결제/배포 변경 없음 (docs-only diff)
- mode: execute_local
- next_action: Local Claude Code가 source note를 읽고 artifacts/marketing-28/ cloud draft를 참고해 virtue-rebirth-app/apps/web/docs/prelaunch-monetization-boundary-brief.md 작성 후 커밋 & push


## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. 산출물은 virtue-rebirth-app `f69f309`의 `apps/web/docs/first-user-message-confusion-log.md`(신규 1파일, 159줄). Wynter/April Dunford 포지셔닝 혼란 렌즈를 Virtue prelaunch 내부 관찰표로 축소해, 사용자가 붙인 제품명/대체재·되물은 문장·가장 먼저 이해한 가치·J1~J4 해석·후속 카피 후보 여부를 한 행에 기록하는 message confusion log를 추가. 기존 first-real-user baseline, first-60-second observation, first-session friction protocol, traffic-source boundary와 연결. 핵심 경계: 사용자 언어는 증거이지 결정 자체가 아니며, 작은 표본을 activation rate/conversion/retention/PMF/benchmark로 읽지 않는다. traffic-source를 먼저 분리하고 synthetic/mock/self-test 언어를 사람 메시지 증거에 섞지 않는다. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑 계승. 신규 이벤트·코드·카피·계측·dashboard·session replay·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 직전 cron의 Claude 위임 timeout 이후 수동 직접 처리. L2 agent-approved push 정상 fast-forward, HEAD==origin/master.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. 산출물은 virtue-rebirth-app `7372aab`의 `apps/web/docs/recovery-over-streak-retention-lens.md`(신규 1파일, 166줄). Duolingo/Reforge/HabitBoard source note를 Virtue prelaunch 첫 7일 판독 렌즈로 번역해, recovery/skip/monthly completion/comeback session을 J1~J4 표로 정리. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승. 핵심: 연속일/streak reset보다 빠진 뒤 돌아오는 세션을 정성 신호로 보되, skip·comeback·monthly completion을 KPI/전환율/합격선으로 읽지 않는다. J3는 저장 없이 `deed_judged`에서 가치가 닫힐 수 있으므로 saved-deed loop에 섞지 않는다. 공개 카피·기능·운영 후보는 proposal-only로 분리하고 반영 0. 신규 이벤트·코드·카피 반영·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증: conflict marker 0, 코드 diff 0, 기존 이벤트 범위만 인용, HEAD==origin/master. L2 agent-approved push 정상 fast-forward(virtue commits `4ff2b96`, `7372aab`). reports/marketing-26/2026-05-29T1107Z-local.md) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판독 경계표 작성 완료. 산출물은 virtue-rebirth-app `f5fde73`의 `apps/web/docs/traffic-source-reading-boundary-table.md`(신규 1파일, 177줄). Userpilot/Appcues 2026 온보딩 지표 가이드를 Virtue prelaunch 트래픽 출처 축으로 번역해, A 사람 실사용(baseline 본행) / B 메이커 self-test(표시 후 제외) / C synthetic/mock(J3 first value 부적합) / D 플랫폼 차이(platform 분리 후 최소공약수 비교) / E 장래 agent/API(미발생, 생기면 별도 규칙) 5행 경계표를 작성. 핵심 원칙: 분류가 판독에 선행하며, 트래픽 종류가 정해지기 전에는 activation/TTV/retention 칸을 읽지 않는다. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 기존 6개 발화 이벤트(`add_flow_started`,`deed_judged`,`deed_saved`,`level_up_viewed`,`deed_rerolled`,`deed_save_capped`)만 인용. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. workflow-master 파일 양 repo 부재 기록 후 4역할 렌즈 수동 합성. 검증: 5개 트래픽 종류 존재, 6개 이벤트 존재, first-value 매핑 계승, no-read/aggregate 합산 금지선, conflict marker 0, 이벤트 앵커 drift 0, 코드 diff 0, 기존 iOS parity/onboarding metrics/baseline/trust 문서 충돌 0. L2 agent-approved push 정상 fast-forward(c3afb52→f5fde73, HEAD==origin/master). reports/marketing-25/2026-05-28T2207Z-local.html) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. 산출물은 virtue-rebirth-app `c3afb52`의 `apps/web/docs/ai-judgment-trust-calibration-audit.md`(신규 1파일, 136줄). Google People + AI Guidebook의 신뢰 보정 렌즈(과신↔불신 사이 적정 신뢰, 무조건 신뢰 아님)를 J1~J4 잡으로 번역. 심장 표(§2)=J1~J4 × (첫 가치 이벤트 · 필요 설명 수준 · 과신 위험 · 불신 위험 · 사용자 제어(재시도/저장/무시/수정) · 정성 관찰 질문) 6차원 한 표. first value 매핑 계승(J1/J2/J4=`deed_saved`, J3=`deed_judged` 저장 전, 재정의 0). 검증: 필수 정규식 46매치(trust 13/신뢰 26/과신 20/불신 14/J1~J4 전부/deed_judged 8/deed_saved 12), 이벤트 화이트리스트 준수. L2 agent-approved push 정상 fast-forward(808231c→c3afb52, HEAD==origin/master). reports/marketing-24/2026-05-28T1007Z-local.html) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료. 산출물은 artifacts/research-10/pc-internet-transition-history.md. reports/research-10/2026-05-28T1607Z.html) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. 산출물은 virtue-rebirth-app `808231c`의 `apps/web/docs/onboarding-metrics-reading-table.md`. L2 agent-approved push 정상 fast-forward. reports/marketing-23/2026-05-27T2207Z-local.html) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. 산출물은 virtue-rebirth-app `179ca70`의 `apps/web/docs/retention-predictive-activation-brief.md`. L2 agent-approved push. reports/marketing-22/2026-05-27T1007Z-local.html) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. 산출물은 virtue-rebirth-app `95cc836`의 `apps/web/docs/add-input-output-balance-audit.md`. L2 agent-approved push. reports/marketing-21/2026-05-26T2207Z-local.html) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. 산출물은 virtue-rebirth-app `993547f`의 `apps/web/docs/first-60-second-value-observation-script.md`. L2 agent-approved push. reports/marketing-20/2026-05-26T1507Z-local.html) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. 산출물은 virtue-rebirth-app `3d90648`의 `apps/web/docs/home-screen-fae-audit.md`. L2 agent-approved push. reports/marketing-19/2026-05-26T1007Z-local.md) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. 산출물은 virtue-rebirth-app `f74cf59`의 `apps/web/docs/aeo-agent-ready-surface-audit.md`. L2 agent-approved push. reports/marketing-18/2026-05-26T0007Z-local.md) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. 산출물은 virtue-rebirth-app `2a8c694`의 `apps/web/docs/first-session-friction-observation-protocol.md`. L2 agent-approved push. reports/marketing-17/2026-05-25T2207Z-local.html) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치. 산출물 artifacts/research-09/solopreneur-strength-vs-limits.md. reports/research-09/2026-05-25T1230Z.html) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. 산출물은 virtue-rebirth-app `87b8877`의 `apps/web/docs/three-screen-value-path-audit.md`. L2 agent-approved push. reports/marketing-16/2026-05-25T1007Z-local.md) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료. 산출물은 virtue-rebirth-app `10e3fa2`의 `apps/web/docs/ios-activation-event-parity-brief.md`. reports/marketing-15/2026-05-24T2207Z-local.md) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료. 산출물은 virtue-rebirth-app `ff6a769`의 `apps/web/docs/first-week-activation-retention-bridge.md`. reports/marketing-14/2026-05-24T1107Z-local.md) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프 작성 완료. 산출물은 virtue-rebirth-app `dc0ce55`의 `apps/web/docs/competitive-alternatives-positioning-brief.md`. L2 agent-approved push. reports/marketing-13/2026-05-23T2207Z.md) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표 작성 완료. 산출물은 virtue-rebirth-app `c32033f`의 docs/time-to-value-observation-brief.md. reports/marketing-10/2026-05-23T1607Z.md) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표 작성 완료. 산출물은 virtue-rebirth-app `fc08cf4`의 docs/activation-path-friction-audit.md. reports/marketing-12/2026-05-23T1007Z.md) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료. reports/research-08/...) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿 작성 완료. 산출물은 virtue-rebirth-app `ebd5781`의 docs/first-real-user-baseline-template.md. reports/marketing-11/...) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리 작성 완료. docs/activation-milestone-ladder.md) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 처리 완료) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 작성 완료) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표 작성 완료) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 작성 완료) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표 작성 완료) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 작성 완료) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성 완료) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안) -->

<!-- research-07 completed 2026-05-13T12:00 → intents/archive/research-07.md -->

<!-- product-01 completed 2026-05-15T11:44Z → intents/archive/product-01.md -->

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
