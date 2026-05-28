# Intent Registry

> Heartbeat Agent가 주기적으로 읽고 실행하는 의도 목록.

## Inbox

## Active

### marketing-25 Virtue 트래픽 유형 판독 경계표
- id: marketing-25
- status: in_progress
- priority: medium
- permission: L1
- created: 2026-05-28T22:00Z
- projects: virtue
- type: strategy
- topics: onboarding, analytics, activation, ai-agents
- goal: prelaunch/low-signal 단계에서 deed_judged/deed_saved 이벤트에 섞이는 5종 트래픽(human real-use / maker self-test / synthetic-mock / platform-difference / future agent-API)을 판독하는 경계표를 작성한다
- success_criteria: 기존 6개 이벤트(add_flow_started, deed_judged, deed_saved, level_up_viewed, deed_rerolled, deed_save_capped)를 5종 트래픽 유형 관점으로 나눠 해석 금지선과 첫 verification gate를 문서화. 신규 이벤트·속성·코드 변경 0, 기존 문서(iOS parity/onboarding metrics/baseline/trust) 충돌 0, 충돌 마커 0
- context: virtue-rebirth-app/apps/web/docs/, source_note=/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-human-agent-onboarding-metrics.md
- mode: prepare(cloud) → execute_local(Claude Code)
- artifacts: artifacts/marketing-25/
- reports: reports/marketing-25/

## Waiting

<!-- 사용자 결정, 외부 조건, 안전 확인 대기. 같은 질문을 반복하지 않고 상태만 보존한다. -->

## Archive

<!-- marketing-24 completed 2026-05-28T10:07Z → intents/archive/marketing-24.md [projects: virtue; type: strategy; topics: activation,trust,ai-product,onboarding] (Virtue AI 판정 신뢰 보정 감사표 작성 완료. 산출물은 virtue-rebirth-app `c3afb52`의 `apps/web/docs/ai-judgment-trust-calibration-audit.md`(신규 1파일, 136줄). Google People + AI Guidebook의 신뢰 보정 렌즈(과신↔불신 사이 적정 신뢰, 무조건 신뢰 아님)를 J1~J4 잡으로 번역. 심장 표(§2)=J1~J4 × (첫 가치 이벤트 · 필요 설명 수준 · 과신 위험 · 불신 위험 · 사용자 제어(재시도/저장/무시/수정) · 정성 관찰 질문) 6차원 한 표. first value 매핑 계승(J1/J2/J4=`deed_saved`, J3=`deed_judged` 저장 전, 재정의 0). §1 신뢰 3요소(능력/일관성/선의)·설명=활성화 장치·확신도(%) 부재는 출처 "숫자보다 행동형 문장" 권고와 우연 정렬. 핵심 발견: 같은 결과 카드라도 보정 역할이 잡별로 다름 — J1 통과점(낮은 설명)·J2 일관성(누적 공정성)·J3 본체(높은 설명·최대 과신 위험)·J4 영구 주석(사후 수정 불가). J3가 신뢰 보정 진폭 최대인 단 하나의 잡. §4 제어권 감사: 재시도(`한 번 더`≤3 `deed_rerolled:149`)·저장(`deed_saved:183` 0점도 가능)·무시/되돌리기(`onReset:153`·`add_flow_abandoned:78`)는 실재이나 **출력 수정·수동 우회 부재**(점수/코멘트/태그 직접 수정 경로 없음) → 과신=수동 수용·불신=이탈로 흐르기 쉬움(proposal-only 후보). §6 금지선: 한명 trust 발화로 과신/불신 단정 금지, judged−saved 갭 불신 단정 금지(J3 정상 종료), 확신도 숫자 도입 정답 가정 금지, 신뢰=항상 높이기 오독 금지, availability≠value(`deed_save_capped` early return), synthetic/mock 점수로 능력·일관성 판단 금지, 변경 금지. 검증: 필수 정규식 46매치(trust 13/신뢰 26/과신 20/불신 14/J1~J4 전부/deed_judged 8/deed_saved 12), 이벤트 화이트리스트 준수(`deed_judge_attempted` 미인용), 코드 앵커 23/78/106/149/167/183/199 현행 일치 drift 0, diff 스코프 doc 1파일, 충돌 마커 0, 금지어 0(`선행` 대신 「앞선 문서」). 앞선 5문서(jtbd-matrix/60s-script/input-output-audit/friction-protocol/onboarding-metrics) + copy-spec 충돌 0, J3 라이브 trust-aware 3축(BASIS/FINAL CHOICE/TRUST)은 60초 스크립트 §4-1에 위임(중복 0). 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·프로덕션 데이터 변경 0, 제안은 §7 proposal-only(출력 수정 제어·결과 카드 신뢰 카피·신규 이벤트·확신도 표시). workflow-master 파일 양 repo 부재 기록 후 4역할 렌즈 수동 합성 + 독립 verifier(Explore, read-only) GO 6/6 승인 분리. L2 agent-approved push 정상 fast-forward(808231c→c3afb52, HEAD==origin/master). reports/marketing-24/2026-05-28T1007Z-local.html) -->

<!-- research-10 completed 2026-05-28T16:07Z → intents/archive/research-10.md [projects: knowledge-lab,infinity; type: research; topics: content,wiki] (PC·인터넷 시대 전환사 리서치 완료. 산출물은 artifacts/research-10/pc-internet-transition-history.md. 메인프레임/연구망→개인 단말→웹/브라우저→브로드밴드→모바일 상시 인프라로 이어진 장기 전환과 인식 변화(특수 도구→생산성 도구→정보 고속도로→생활 인프라→사회 기본값)를 정리. 주요 변곡점 1946 ENIAC, 1969 ARPANET, 1981 IBM PC, 1984 Macintosh, 1989-1993 WWW/Mosaic, 1995 Windows 95/Netscape, 2007-2008 iPhone/Android, 2020 팬데믹 포함. 출처는 Computer History Museum, CERN, Web Foundation, NCSA, Pew, ITU, World Bank, U.S. Census, NTIA. 공개 사이트·코드·외부발송·비용·시크릿·권한 변경 0. reports/research-10/2026-05-28T1607Z.html) -->

<!-- marketing-23 completed 2026-05-27T22:07Z → intents/archive/marketing-23.md [projects: virtue; type: strategy; topics: activation,retention,analytics] (Virtue 온보딩 지표 운영 판독표 작성 완료. 산출물은 virtue-rebirth-app `808231c`의 `apps/web/docs/onboarding-metrics-reading-table.md`(신규 1파일, 168줄). Appcues 온보딩 지표 루프(activation/TTV/funnel drop-off/retention + vanity completion 분리)를 Virtue prelaunch 기준으로 번역해 흩어진 선행 문서(m06 first value·m10 TTV·m20 60초 라이브·m22 depth/D7)를 한 운영 판독표로 정렬. first value 매핑 계승(J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106 저장 전, 재정의 0). workflow-master 파일 양 repo 부재 기록 후 4역할 렌즈 수동 합성 + 독립 verifier(GO 6/6) 승인 분리. L2 agent-approved push 정상 fast-forward(179ca70→808231c, HEAD==origin/master). reports/marketing-23/2026-05-27T2207Z-local.html) -->

<!-- marketing-22 completed 2026-05-27T10:07Z → intents/archive/marketing-22.md (Virtue 리텐션 예측 활성화 브리프 작성 완료. 산출물은 virtue-rebirth-app `179ca70`의 `apps/web/docs/retention-predictive-activation-brief.md`(신규 1파일, 166줄). L2 agent-approved push 정상 fast-forward(95cc836→179ca70, HEAD==origin/master). reports/marketing-22/2026-05-27T1007Z-local.html) -->

<!-- marketing-21 completed 2026-05-26T22:07Z → intents/archive/marketing-21.md (Virtue `/add` 입력-결과 균형 감사표 작성 완료. 산출물은 virtue-rebirth-app `95cc836`의 `apps/web/docs/add-input-output-balance-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward(993547f→95cc836, HEAD==origin/master). reports/marketing-21/2026-05-26T2207Z-local.html) -->

<!-- marketing-20 completed 2026-05-26T15:07Z → intents/archive/marketing-20.md (Virtue 첫 60초 가치 관찰 스크립트 작성 완료. 산출물은 virtue-rebirth-app `993547f`의 `apps/web/docs/first-60-second-value-observation-script.md`(신규 1파일, 248줄). L2 agent-approved push 정상 fast-forward(3d90648→993547f, HEAD==origin/master). reports/marketing-20/2026-05-26T1507Z-local.html) -->

<!-- marketing-19 completed 2026-05-26T10:07Z → intents/archive/marketing-19.md (Virtue 신규 사용자 홈 화면 FAE 감사표 작성 완료. 산출물은 virtue-rebirth-app `3d90648`의 `apps/web/docs/home-screen-fae-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward(f74cf59→3d90648, HEAD==origin/master). reports/marketing-19/2026-05-26T1007Z-local.md) -->

<!-- marketing-18 completed 2026-05-26T00:07Z → intents/archive/marketing-18.md (Virtue AEO / Agent-ready 공개 표면 감사표 작성 완료. 산출물은 virtue-rebirth-app `f74cf59`의 `apps/web/docs/aeo-agent-ready-surface-audit.md`(신규 1파일). L2 agent-approved push 정상 fast-forward(2a8c694→f74cf59, HEAD==origin/master). reports/marketing-18/2026-05-26T0007Z-local.md) -->

<!-- marketing-17 completed 2026-05-25T22:07Z → intents/archive/marketing-17.md (Virtue 첫 세션 정성 마찰 관찰 프로토콜 작성 완료. 산출물은 virtue-rebirth-app `2a8c694`의 `apps/web/docs/first-session-friction-observation-protocol.md`(신규 +289). L2 agent-approved push 정상 fast-forward(87b8877→2a8c694, HEAD==origin/master). reports/marketing-17/2026-05-25T2207Z-local.html) -->

<!-- research-09 completed 2026-05-25T12:30Z → intents/archive/research-09.md (1인기업 강점 살리기 vs 한계 조기 규정 리서치. 산출물 artifacts/research-09/solopreneur-strength-vs-limits.md. 공개 사이트/코드 변경 0) -->

<!-- marketing-16 completed 2026-05-25T10:07Z → intents/archive/marketing-16.md (Virtue 첫 세션 3-스크린 가치 경로 감사표 작성 완료. 산출물은 virtue-rebirth-app `87b8877`의 `apps/web/docs/three-screen-value-path-audit.md`. L2 push는 agent-approved 조건 확인 후 정상 fast-forward push. reports/marketing-16/2026-05-25T1007Z-local.md) -->

<!-- marketing-15 completed 2026-05-24T22:07Z → intents/archive/marketing-15.md (Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성 완료. 산출물은 virtue-rebirth-app `10e3fa2`의 `apps/web/docs/ios-activation-event-parity-brief.md`. 신규 이벤트·속성·코드·카피·대시보드·외부발송·비용·시크릿·권한 변경 0. reports/marketing-15/2026-05-24T2207Z-local.md) -->

<!-- marketing-14 completed 2026-05-24T15:56Z → intents/archive/marketing-14.md (Virtue 첫 주 활성화-리텐션 연결표 작성 완료. virtue-rebirth-app `ff6a769`. reports/marketing-14/2026-05-24T1107Z-local.md, 2026-05-24T1556Z-archive.md) -->

<!-- marketing-13 completed 2026-05-23T22:07Z → intents/archive/marketing-13.md (Virtue 경쟁 대안 기반 포지셔닝 브리프. virtue-rebirth-app dc0ce55. reports/marketing-13/2026-05-23T2207Z.md) -->

<!-- marketing-10 completed 2026-05-23T16:07Z → intents/archive/marketing-10.md (Virtue Time-to-Value 관찰 기준표. virtue-rebirth-app c32033f, reports/marketing-10/2026-05-23T1607Z.md) -->

<!-- marketing-12 completed 2026-05-23T10:18Z → intents/archive/marketing-12.md (Virtue 활성화 경로 마찰 감사표. virtue-rebirth-app fc08cf4. reports/marketing-12/2026-05-23T1007Z.md) -->

<!-- research-08 completed 2026-05-23T10:30Z → intents/archive/research-08.md (GEO/LLMO 체크리스트 조사 완료. 공개 사이트 변경 0) -->

<!-- marketing-11 completed 2026-05-22T22:17Z → intents/archive/marketing-11.md (Virtue 첫 실사용자 기준선 템플릿. virtue-rebirth-app ebd5781 push 완료) -->

<!-- marketing-09 completed 2026-05-21T22:07Z → intents/archive/marketing-09.md (Virtue 활성화 마일스톤 사다리. docs/activation-milestone-ladder.md 추가) -->

<!-- marketing-01 completed 2026-05-21T10:17Z → intents/archive/marketing-01.md (Virtue add-flow telemetry 승인 처리 완료. HEAD==origin/master) -->

<!-- marketing-08 completed 2026-05-21T10:07Z → intents/archive/marketing-08.md (Virtue PMF 응답 분석 루브릭. docs/pmf-response-analysis-rubric.md 추가) -->

<!-- marketing-07 completed 2026-05-20T22:07Z → intents/archive/marketing-07.md (Virtue 최소 생존 오디언스 기준표. docs/minimum-viable-audience-brief.md 추가) -->

<!-- marketing-06 completed 2026-05-20T10:07Z → intents/archive/marketing-06.md (Virtue 첫 세션 JTBD 매트릭스. docs/first-session-jtbd-matrix.md sha 38af1be) -->

<!-- marketing-05 completed 2026-05-19T22:07Z → intents/archive/marketing-05.md (Virtue 빈 상태/첫 행동 감사표) -->

<!-- marketing-04 completed 2026-05-19T10:07Z → intents/archive/marketing-04.md (Virtue 첫인상 포지셔닝 스냅샷) -->

<!-- marketing-03 completed 2026-05-18T22:20Z → intents/archive/marketing-03.md (Virtue 첫 7일 deed_saved 루프 정의서 작성) -->

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
