# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox


## Active

### marketing-31 — Virtue 첫 세션 제품 본체/범퍼 경계표 작성
- id: marketing-31
- status: in_progress
- priority: high
- permission: L1/L2
- project: virtue
- goal: J1~J4 × 첫 세션 표면 × 본체/범퍼 역할 × 정상 종료/막힘 판독 기준 표를 virtue-rebirth-app docs에 추가
- success_criteria: apps/web/docs/first-session-product-bumper-boundary.md 생성, 기존 first value 매핑 재정의 0, conflict marker 0, 코드 diff 0
- next_action: 로컬 Claude Code가 artifacts/marketing-31/first-session-product-bumper-boundary-draft.md를 virtue-rebirth-app에 복사·커밋·푸시
- started: 2026-05-31T10:07Z

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-31 in_progress 2026-05-31T10:07Z — cloud prepare 완료 (초안 artifacts/marketing-31/, 로컬 실행 대기) -->

<!-- marketing-30 completed 2026-05-31T10:07Z → reports/marketing-30/2026-05-31T1007Z-local.html [projects: virtue; type: strategy; topics: onboarding,activation,ai-product,prelaunch] (Virtue 첫 결과 공유성 판독 기준 작성 완료. 산출물은 virtue-rebirth-app의 `apps/web/docs/shareworthy-first-result-observation-criteria.md`(신규 1파일). ProductLed AI 온보딩 렌즈의 세 신호 중 ③ "공유하거나 추천하고 싶은 첫 경험"만 잡별로 번역(①60초 가치·②입력 대비 결과 강도는 m20/m21이 이미 소유). 핵심 신규 판독: 공유성(shareworthiness)을 first value·acceptance와 구분되는 별도 축(resonance/advocacy)으로 정의 — "첫 결과"를 (a)가치 도달 (b)공유성 (c)저장 후 누적 payoff 세 층으로 분리. 저장 없이 공유성 있음(J3 결과 읽고 보여 주고 닫음=정상)·저장 있으나 공유성 없음(J1 묵묵한 저장) 모두 가능하므로 공유성은 항상 저장 전 시점에서 따로 기록. §2 행동 증거 사전 B1~B6(웃음/놀람/반박/다르게 보기 재시도/보여 주기/재전달) 중 B4만 on-instrument(`deed_rerolled`:149), 나머지 5종 off-instrument → 저장수·재판정수로 공유성 환산 금지, 손기록 전용. §3 심장표 J1~J4 × first value × 공유성 관찰 순간 × 기대 행동 증거 × 누적 payoff 분리 × 기존 이벤트 매핑 × misread. §4 Inform/Guide/Execute/Orchestrate 감사: `/add`는 `deed_judged`:106 결과 카드 생성으로 이미 Execute 도달(기존 증거), 단 Execute≠자동 shareworthy이고 그 손기록 양식 부재가 본 문서 공백. first value 매핑 J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(앵커 72/106/149/167/183/199 drift 0), `deed_save_capped`:167은 availability/friction(upgrade 환산 금지) 계승. §5 prelaunch 금지선(전환율/PMF/벤치마크 산출·1명 단정·저장수=공유성 환산·cap=공유/upgrade 신호·J3 judged−saved 갭=가치 부재·synthetic 혼입·신규 이벤트/코드/카피/계측/배포/외부발송/비용/권한 변경 금지). §6 계승/변경/충돌/승격 분리: 선행 6문서(jtbd-matrix/proxy-dictionary/input-output-balance/60s-script/monetization-boundary/copy-spec) 충돌 0. 검증 게이트 PASS: conflict marker 0, virtue 코드 diff 0(doc 1파일만), HTML 보고서 <html/<body/axis ax1/axis ax2/<details 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함, HEAD==origin/master. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. durable learning "Shareworthiness Is A Separate Axis"를 MARKETING_LEARNINGS.md에 승격. Infinity EVALUATION_NOTES.md는 staging 제외. L2 agent-approved push.) -->

<!-- marketing-29 completed 2026-05-30T22:07Z → reports/marketing-29/2026-05-30T2207Z-local.html [projects: virtue; type: strategy; topics: ai-product,activation,trust,measurement,prelaunch] (Virtue AI outcome proxy 사전 작성 완료. 산출물은 virtue-rebirth-app `22f3aea`의 `apps/web/docs/ai-outcome-proxy-dictionary.md`(신규 1파일). Intercom outcome-based value framing + Reforge North Star quality 렌즈를 Virtue prelaunch 내부 판독 사전으로 번역해, "AI가 무언가 했다"는 활동량과 "사용자가 인정했는가"라는 사용자 인정 가치 proxy를 분리. §1 proxy type 5종 사전(activity/acceptance/curiosity/friction/retention) 정의. §2 심장표1=6개 발화 이벤트 × 지배적 proxy type × quality condition × misread warning(코드 앵커 72/106/149/167/183/199 인용). §3 심장표2=J1~J4 × 이벤트 × proxy 판독 × quality condition × misread warning, 같은 `deed_judged`가 J3엔 curiosity first value·다른 잡엔 통과점으로 부호 전환. §4 misread 7종(활동량=가치, judged−saved 갭=이탈, cap=유료수요, reroll=불신, level_up 1회=리텐션, 저장수=만족도, synthetic=인정 금지). §5 prelaunch decision-grade 금지선(전환율/PMF/벤치마크 산출·1명 단정·activity 승격·cap monetization 환산 금지). first value 매핑 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 기존 6 발화 이벤트만 인용(보조 add_flow_abandoned:78·deed_judge_attempted:135 사실만 참조, 신규 invented 0). 선행 m06/m28/m25/m22/copy-spec 충돌 0. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·공개카피·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증 게이트 7종 PASS: 코드 diff 0, 신규 이벤트/속성 0, 6개 이벤트 이름 drift 0(started6/judged13/saved21/level_up8/rerolled5/capped7), conflict marker 0, first-value 매핑 1, decision-grade 금지선 포함, HEAD==origin/master. Infinity dirty 무관 파일(EVALUATION_NOTES.md·workflows/heartbeat.md) staging 제외. L2 agent-approved push 정상 fast-forward(c0dcf7d→22f3aea). Legacy Markdown log도 보존.) -->

<!-- marketing-28 completed 2026-05-30T10:07Z → reports/marketing-28/2026-05-30T1007Z-local.html [projects: virtue; type: strategy; topics: monetization,pricing,activation,prelaunch] (Virtue prelaunch 유료화 경계 브리프 작성 완료. 산출물은 virtue-rebirth-app `c0dcf7d`의 `apps/web/docs/prelaunch-monetization-boundary-brief.md`(신규 1파일, 136줄). Stripe PLG pricing 2026/Growth Unhinged monetization source note를 Virtue prelaunch 내부 경계표로 번역해, J1~J4별 first value 이전 do-not-lock 제한과 first value 이후 확장/유료화 trigger candidate를 분리. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 핵심 경계: 가격·플랜·금액 결정 0, 첫 가치 이전 결제정보/계정강제/핵심행동 0회 잠금 금지, §3 후보는 반복 가치 관찰 전 확정/구현 금지. `deed_save_capped`는 30덕 상한 early-return으로 `deed_saved` 미발화하는 availability/friction 신호이며 monetization intent/upgrade demand로 환산 금지. 공개 가격표·결제 연동·트래킹 변경·paywall 실험·트리거 확정·배포·외부발송·비용·시크릿·권한 변경은 Waiting/approval-needed로 명시. 신규 이벤트·코드·카피·결제·트래킹·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증: doc-only diff, 코드 diff 0, conflict marker 0, HEAD==origin/master. L2 agent-approved push 정상 fast-forward. Legacy Markdown log도 보존.) -->

<!-- marketing-27 completed 2026-05-29T22:25Z → reports/marketing-27/2026-05-29T2225Z-local.md [projects: virtue; type: strategy; topics: positioning,messaging,activation,prelaunch] (Virtue 첫 사용자 메시지 혼란 로그 작성 완료. 산출물은 virtue-rebirth-app `f69f309`의 `apps/web/docs/first-user-message-confusion-log.md`(신규 1파일, 159줄). Wynter/April Dunford 포지셔닝 혼란 렌즈를 Virtue prelaunch 내부 관찰표로 축소해, 사용자가 붙인 제품명/대체재·되물은 문장·가장 먼저 이해한 가치·J1~J4 해석·후속 카피 후보 여부를 한 행에 기록하는 message confusion log를 추가. 기존 first-real-user baseline, first-60-second observation, first-session friction protocol, traffic-source boundary와 연결. 핵심 경계: 사용자 언어는 증거이지 결정 자체가 아니며, 작은 표본을 activation rate/conversion/retention/PMF/benchmark로 읽지 않는다. traffic-source를 먼저 분리하고 synthetic/mock/self-test 언어를 사람 메시지 증거에 섞지 않는다. J1/J2/J4=`deed_saved`, J3=`deed_judged` first value 매핑 계승. 신규 이벤트·코드·카피·계측·dashboard·session replay·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 직전 cron의 Claude 위임 timeout 이후 수동 직접 처리. L2 agent-approved push 정상 fast-forward, HEAD==origin/master.) -->

<!-- marketing-26 completed 2026-05-29T11:07Z → intents/archive/marketing-26.md [projects: virtue; type: strategy; topics: retention,habit,recovery,copy] (Virtue recovery-over-streak 리텐션 렌즈 작성 완료. 산출물은 virtue-rebirth-app `7372aab`의 `apps/web/docs/recovery-over-streak-retention-lens.md`(신규 1파일, 166줄). Duolingo/Reforge/HabitBoard source note를 Virtue prelaunch 첫 7일 판독 렌즈로 번역해, recovery/skip/monthly completion/comeback session을 J1~J4 표로 정리. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승. 핵심: 연속일/streak reset보다 빠진 뒤 돌아오는 세션을 정성 신호로 보되, skip·comeback·monthly completion을 KPI/전환율/합격선으로 읽지 않는다. J3는 저장 없이 `deed_judged`에서 가치가 닫힐 수 있으므로 saved-deed loop에 섞지 않는다. 공개 카피·기능·운영 후보는 proposal-only로 분리하고 반영 0. 신규 이벤트·코드·카피 반영·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. 검증: conflict marker 0, 코드 diff 0, 기존 이벤트 범위만 인용, HEAD==origin/master. L2 agent-approved push 정상 fast-forward(virtue commits `4ff2b96`, `7372aab`). reports/marketing-26/2026-05-29T1107Z-local.md) -->

<!-- marketing-25 completed 2026-05-28T22:07Z → intents/archive/marketing-25.md [projects: virtue; type: strategy; topics: onboarding,analytics,activation,ai-agents] (Virtue human/test/agent 트래픽 판독 경계표 작성 완료. 산출물은 virtue-rebirth-app `f5fde73`의 `apps/web/docs/traffic-source-reading-boundary-table.md`(신규 1파일, 177줄). Userpilot/Appcues 2026 온보딩 지표 가이드를 Virtue prelaunch 트래픽 출처 축으로 번역해, A 사람 실사용(baseline 본행) / B 메이커 self-test(표시 후 제외) / C synthetic/mock(J3 first value 부적합) / D 플랫폼 차이(platform 분리 후 최소공약수 비교) / E 장래 agent/API(미발생, 생기면 별도 규칙) 5행 경계표를 작성. 핵심 원칙: 분류가 판독에 선행하며, 트래픽 종류가 정해지기 전에는 activation/TTV/retention 칸을 읽지 않는다. first value 매핑은 J1/J2/J4=`deed_saved`, J3=`deed_judged` 그대로 계승, 재정의 0. 기존 6개 발화 이벤트(`add_flow_started`,`deed_judged`,`deed_saved`,`level_up_viewed`,`deed_rerolled`,`deed_save_capped`)만 인용. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 0. workflow-master 파일 양 repo 부재 기록 후 4역할 렌즈 수동 합성. 검증: 5개 트래픽 종류 존재, 6개 이벤트 존재, first-value 매핑 계승, no-read/aggregate 합산 금지선, conflict marker 0, 이벤트 앵커 drift 0, 코드 diff 0, 기존 iOS parity/onboarding metrics/baseline/trust 문서 충돌 0. L2 agent-approved push 정상 fast-forward(c3afb52→f5fde73, HEAD==origin/master). reports/marketing-25/2026-05-28T2207Z-local.html) -->

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. 산출물은 virtue-rebirth-app `c3afb52`의 `apps/web/docs/ai-judgment-trust-calibration-audit.md`(신규 1파일, 136줄). Google People + AI Guidebook의 신뢰 보정 렌즈(과신↔불신 사이 적정 신뢰, 무조건 신뢰 아님)를 J1~J4 잡으로 번역. 심장 표(§2)=J1~J4 × (첫 가치 이벤트 · 필요 설명 수준 · 과신 위험 · 불신 위험 · 사용자 제어(재시도/저장/무시/수정) · 정성 관찰 질문) 6차원 한 표. first value 매핑 계승(J1/J2/J4=`deed_saved`, J3=`deed_judged` 저장 전, 재정의 0). §1 신뢰 3요소(능력/일관성/선의)·설명=활성화 장치·확신도(%) 부재는 출처 "숫자보다 행동형 문장" 권고와 우연 정렬. 핵심 발견: 같은 결과 카드라도 보정 역할이 잡별로 다름 — J1 통과점(낮은 설명)·J2 일관성(누적 공정성)·J3 본체(높은 설명·최대 과신 위험)·J4 영구 주석(사후 수정 불가). J3가 신뢰 보정 진폭 최대인 단 하나의 잡. §4 제어권 감사: 재시도(`한 번 더`≤3 `deed_rerolled:149`)·저장(`deed_saved:183` 0점도 가능)·무시/되돌리기(`onReset:153`·`add_flow_abandoned:78`)는 실재이나 출력 수정·수동 우회 부재(점수/코멘트/태그 직접 수정 경로 없음) → 과신=수동 수용·불신=이탈로 흐르기 쉬움(proposal-only 후보). §6 금지선. 검증: 필수 정규식 46매치, 이벤트 화이트리스트 준수, 코드 앵커 23/78/106/149/167/183/199 현행 일치 drift 0, diff 스코프 doc 1파일, 충돌 마커 0. 앞선 5문서+copy-spec 충돌 0. 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·프로덕션 데이터 변경 0. L2 agent-approved push 정상 fast-forward(808231c→c3afb52, HEAD==origin/master). reports/marketing-24/2026-05-28T1007Z-local.html) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료. 산출물은 artifacts/research-10/pc-internet-transition-history.md. 메인프레임/연구망→개인 단말→웹/브라우저→브로드밴드→모바일 상시 인프라로 이어진 장기 전환과 인식 변화를 정리. 공개 사이트·코드·외부발송·비용·시크릿·권한 변경 0. reports/research-10/2026-05-28T1607Z.html) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. 산출물은 virtue-rebirth-app `808231c`의 `apps/web/docs/onboarding-metrics-reading-table.md`(신규 1파일, 168줄). Appcues 온보딩 지표 루프를 Virtue prelaunch 기준으로 번역해 흩어진 선행 문서를 한 운영 판독표로 정렬. first value 매핑 계승. L2 agent-approved push 정상 fast-forward. reports/marketing-23/2026-05-27T2207Z-local.html) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. 산출물은 virtue-rebirth-app `179ca70`의 `apps/web/docs/retention-predictive-activation-brief.md`. reports/marketing-22/2026-05-27T1007Z-local.html) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. 산출물은 virtue-rebirth-app `95cc836`의 `apps/web/docs/add-input-output-balance-audit.md`. reports/marketing-21/2026-05-26T2207Z-local.html) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. 산출물은 virtue-rebirth-app `993547f`의 `apps/web/docs/first-60-second-value-observation-script.md`. reports/marketing-20/2026-05-26T1507Z-local.html) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. 산출물은 virtue-rebirth-app `3d90648`의 `apps/web/docs/home-screen-fae-audit.md`. reports/marketing-19/2026-05-26T1007Z-local.md) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. 산출물은 virtue-rebirth-app `f74cf59`의 `apps/web/docs/aeo-agent-ready-surface-audit.md`. reports/marketing-18/2026-05-26T0007Z-local.md) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. 산출물은 virtue-rebirth-app `2a8c694`의 `apps/web/docs/first-session-friction-observation-protocol.md`. reports/marketing-17/2026-05-25T2207Z-local.html) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치. 산출물 artifacts/research-09/solopreneur-strength-vs-limits.md) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. 산출물은 virtue-rebirth-app `87b8877`의 `apps/web/docs/three-screen-value-path-audit.md`. reports/marketing-16/2026-05-25T1007Z-local.md) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료. 산출물은 virtue-rebirth-app `10e3fa2`의 `apps/web/docs/ios-activation-event-parity-brief.md`. reports/marketing-15/2026-05-24T2207Z-local.md) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료. reports/marketing-14/2026-05-24T1556Z-archive.md) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프 작성 완료. 산출물은 virtue-rebirth-app `dc0ce55`의 `apps/web/docs/competitive-alternatives-positioning-brief.md`. reports/marketing-13/2026-05-23T2207Z.md) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표 작성 완료. virtue-rebirth-app c32033f, reports/marketing-10/2026-05-23T1607Z.md) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표 작성 완료. reports/marketing-12/2026-05-23T1007Z.md) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿 작성 완료. virtue-rebirth-app ebd5781) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리 작성 완료) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 처리 완료) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭 작성 완료) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표 작성 완료) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스 작성 완료) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표 작성 완료) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷 작성 완료) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성 완료) -->

<!-- marketing-02 completed 2026-05-16T14:00Z → intents/archive/marketing-02.md (마찰점 4개 특정, 개선 후보 3개 초안) -->

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
