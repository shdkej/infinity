# marketing-20 Intent Archive

- id: marketing-20
- title: Virtue 첫 60초 가치 관찰 스크립트 작성
- status: archived
- priority: medium
- permission: L1 내부 문서/관찰표 + L2 agent-approved push
- created_at: 2026-05-26T15:00Z
- completed_at: 2026-05-26T15:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-ai-agent-product-marketing-trends.md` (후보 C)

## Result Summary

prelaunch/low-signal 단계 Virtue에서 **첫 10~20명이 사용 시작 후 60초 안에 "첫 가치"에 닿는지를 사람이 실시간으로 판독하는 현장 대본**을 내부 문서로 작성했다. ProductLed의 2026 PLG 신호(time-to-value 60초 이하, 출처 노트 §3)를 첫 사용자의 말·행동으로 직접 확인하는 최우선 학습 입력이다. **신규 계측·코드·카피·대시보드·세션리플레이·외부발송·정책·비용 0**, 기존 6개 이벤트만 육안 관찰의 인지 보조로 인용.

핵심 구조:

- **J → 60초 첫 가치 매핑(인용)**: J1 기록형/J2 누적형/J4 회고형 → `deed_saved`, J3 AI 호기심형 → `deed_judged`(저장은 선택, judged-without-saved는 정상 종료). `first-session-jtbd-matrix`·`activation-milestone-ladder` 정의를 재정의 없이 계승.
- **문서의 심장(§3)**: J1~J4 × (60초 첫 가치 순간 / 화면에서 보아야 할 증거 / 대응 이벤트) 표. 모든 화면 증거는 현재 코드의 인지 앵커를 file:line으로 인용 — `/` CTA "오늘 덕 쌓기"(`page.tsx:106-112`), 결과 카드 헤더 "AI가 본 오늘"/"임시 판정 결과"(`add/page.tsx:319`), 저장 토스트 "저장됐어요. +N덕"(`add/page.tsx:204`).
- **60초 시계 메커닉(§2)**: start = `/` 첫 land, stop = 첫 가치 도달 OR 60초 경과(먼저). 무계측 측정(벽시계/스톱워치 손기록). **가용성 ≠ 가치 분리** — 503·judge 타임아웃·네트워크 사건은 시계에서 제외하고 `availability-blocked`로 표시, 미도달로 집계하지 않음(friction-protocol §6-3 계승).
- **관찰자 셋업(§1)**: 메이커 본인 + 이미 동의된 지인. 허용 4방법(옆에서 보기/동의된 화면공유/self-observation(test 제외)/사후 회고), 금지(은밀 녹화·신규 리플레이 도구·계측 설치·외부 모집). 새 프라이버시 정책 제안 0.
- **관찰 질문(§4·§4-1)**: 잡별 [조용한 관찰] vs [소리내어·허용된 대화 한정] 구분, 유도질문 금지. J3 trust-aware 3축(BASIS 근거 가시성 / FINAL CHOICE 최종 선택권 / TRUST 태도) — trusted AI 트렌드(출처 노트 §1) 정렬.
- **기록 필드(§5)**: baseline-template 컬럼 재사용, 신설은 `60초 도달 여부`·`도달 순간(초)`·`본 증거` 3칸뿐(새 표/텔레메트리 0, 중복 방지).
- **해석 경계(§6·§7)**: pass/hold/follow-up을 잡별로 정의. 전환율·리텐션·PMF·세그먼트 크기·% 산출·한 명 신호 확정 전면 금지. "60초 미도달 ≠ 제품 실패"를 (a)첫 막힘 (b)가용성 사건 (c)지연 가치(J4)로 분해. judgment-hold를 대신 기록.
- **synthetic/mock 제외(§9)**: "임시 판정"/"mock" 배지/폴백 토스트/매직넘버 641(데모 시드)/localStorage 반복 테스트를 식별해 60초 집계에서 제외(삭제 아닌 표시).

**핵심 발견(계승·재정의 없음):** 60초 창은 사용자의 페이스가 아니라 **관찰자의 렌즈 폭**이다 — 미도달은 관찰창이 짧았거나(J4 지연 가치) 인프라 사건일 수 있어 실패로 단정 금지. 이 문서는 TTV brief와 **역할 분리**(라이브 정성 판독 vs 타임스탬프 정량 계산)되어 중복이 아니며, "도달 순간(초)"는 체감 대략값으로만 적고 정밀 계산은 TTV에 위임. J3 앞단 끊김(`/`에 AI 신호 부재)·J2 뒷단 누출(누적 payoff가 `/` 복귀/`level_up_viewed`에 의존)을 three-screen·friction-protocol과 모순 없이 계승.

선행 7문서(jtbd-matrix / three-screen / time-to-value / first-real-user-baseline / friction-protocol / activation-ladder / copy-spec) 충돌 0. copy-spec 금지어 0건(사용자 노출 카피 신규 0; 금지어 명단은 §10 메타 맥락으로만 등장). workflow-master 파일 양 repo 부재 기록 후 4역할 병렬 합성.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `993547f` (이전 HEAD `3d90648` fast-forward)
- path: `apps/web/docs/first-60-second-value-observation-script.md` (신규 1파일, 248 라인)
- push: `3d90648..993547f master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 충돌 마커 0(PASS): 변경 파일에 git 충돌 마커(7연속 부등호/등호) 없음, rg 빈 출력.
- Gate B 스코프(PASS): 신규 doc 1개로 한정. `apps/web/src`·iOS·이벤트·대시보드·카피 파일 변경 0.
- Gate C 금지 경로 0(PASS): 코드/카피/이벤트/스키마/대시보드/세션리플레이/배포/외부발송/비용/시크릿/권한/개인정보 변경 0.
- Gate D Infinity 선택적 스테이징(PASS): `INTENTS.md`·`intents/archive/marketing-20.md`·`reports/marketing-20/`만 스테이징, 무관한 `EVALUATION_NOTES.md` 인덱스 제외.
- Gate E 양 repo HEAD == origin(PASS): Virtue `993547f`, Infinity push 후 `origin/main` 일치.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인 · 실행 후 검증 존재 → 모두 충족. force-push 아님, 타인 작업 덮어쓰지 않음(fast-forward).
- report: `reports/marketing-20/2026-05-26T1507Z-local.html`
