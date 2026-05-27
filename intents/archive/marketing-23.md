# marketing-23 Intent Archive

- id: marketing-23
- title: Virtue 온보딩 지표 운영 판독표 작성
- status: archived
- priority: medium
- permission: L1 내부 문서 작성 + L2 agent-approved push
- created_at: 2026-05-27T22:00Z
- completed_at: 2026-05-27T22:07Z
- projects: [virtue]
- task_type: strategy
- topics: [activation, retention, analytics]
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-27-onboarding-metrics-practice.md` (Appcues User Onboarding Metrics & KPIs 요약)

## Result Summary

**축1 (무엇이 문제였나):** 선행 문서들이 first value(m06)·TTV(m10)·60초 라이브 판독(m20)·리텐션 예측 depth/D7(m22)을 각각 잘게 정의하면서 "좋은 지표 후보는 많아졌지만 운영 리듬이 흐려지는" 위험이 커졌다. prelaunch 첫 10~20명에서 completion·첫 클릭·전환율·retention %·PMF를 결론으로 만들면 작은 표본을 과대 해석한다.

**축2 (어떻게 해결하나):** Appcues 온보딩 지표 루프(activation/TTV/funnel drop-off/retention + vanity completion 분리)를 Virtue prelaunch 기준으로 번역해, 잡(J1~J4)별 **activation event → TTV 시작/종료 → drop-off 해석 주의 → D1/D7 재가치 질문 → synthetic/test 제외**를 **한 운영 판독표(§2)**로 묶은 내부 문서를 작성했다. 기존 6개 발화 이벤트만 인용, **신규 이벤트·코드·카피·대시보드·계측 변경 0건**.

핵심 구조:

- **운영 판독표(§2, 심장):** 한 표가 6개 차원을 모두 덮는다 — activation event(J1·J2·J4 = `deed_saved`, J3 = `deed_judged` 저장 전) / TTV 시작(`add_flow_started`) → 종료(잡별 first value) / drop-off 해석 주의(잡별) / D1·D7 재가치 질문(손기록) / synthetic·test 제외 단서.
- **drop-off 단계·해석 주의(§4):** `/` land → `add_flow_started` → `deed_judged` → `deed_saved` → 조건부 `level_up_viewed`. 각 갭은 "이탈"이 아니라 "어디서 멈췄나"의 진단. `deed_judged`−`deed_saved` 갭은 잡별로 부호가 뒤집힌다(J1/J2/J4 저장 전 이탈 후보 vs J3 정상 종료). `add_flow_abandoned`(:78)는 코드상 미저장 이탈 위치 표시 짝으로 사실만 인용.
- **synthetic/test 제외(§5):** mock 폴백·데모 시드 641·localStorage 반복·메이커 self-test → 표시 후 집계 제외(삭제 아님). mock 점수 품질 판단 금지.
- **운영 리듬(§6):** 주간 activation·drop-off / 월간(또는 launch 직전) retention·재가치를 손기록으로 본다. 대시보드·자동 집계·알림 없음.
- **prelaunch 금지선(§7):** completion을 결론으로 만들기·첫 클릭 승격·conversion 산출·retention % 외부 벤치마크 판정·PMF 계산 금지, judged−saved 갭 이탈 단정 금지(J3 정상 종료), availability≠value, 한 명 신호 확정 금지, 단계 도달을 세그먼트 크기로 읽기 금지, 변경 금지.

**핵심 발견:** 같은 `deed_saved`라도 가치 방향이 다르다(J1 즉시 / J2 누적 / J4 지연)이고, J3만 `deed_judged`가 first value이며 저장 없는 종료가 정상 경로다. `deed_save_capped` 발화 시도는 early return으로 `deed_saved`가 발화하지 않아 TTV 종료·D1/D7 재가치 집계에서 제외된다. drop-off는 멈춤 위치를 찾는 진단 도구이지 온보딩 합격/불합격 판정이 아니다.

선행 6문서(first-session-jtbd-matrix / time-to-value-observation-brief / first-60-second-value-observation-script / retention-predictive-activation-brief / seven-day-deed-loop / first-real-user-baseline-template) + copy-spec 충돌 0. 본 판독표는 정의를 재정의하지 않고 TTV 정밀 계산은 m10에, 60초 현장 시계는 m20에, depth/D7 상세는 m22에 위임한다. workflow-master 파일 양 repo 부재 기록 후 Planner/Developer/Marketer/Operator 4역할 렌즈 수동 합성 + 독립 verifier(Explore, read-only) 승인 패스 분리.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `808231c` (이전 HEAD `179ca70` fast-forward)
- path: `apps/web/docs/onboarding-metrics-reading-table.md` (신규 1파일, 168줄)
- push: `179ca70..808231c master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 파일 존재(PASS): 168줄 신규 생성.
- Gate B 필수 용어(PASS): `activation event`(4), `TTV`(23), `drop-off`(13), `D1`(15), `D7`(22), `synthetic`(8), `test`(8) 모두 존재. 과대해석 금지 용어 `completion`(8)·`conversion`(2)·`retention`(14)·`PMF`(5)도 명시.
- Gate B2 6개 이벤트(PASS): `add_flow_started`(12), `deed_judged`(15), `deed_saved`(21), `level_up_viewed`(7), `deed_rerolled`(4), `deed_save_capped`(5).
- Gate C first-value 매핑(PASS): J1/J2/J4 = `deed_saved`, J3 = `deed_judged` 유지·재정의 0.
- Gate D 충돌 마커(PASS): `rg '<<<<<<<|=======|>>>>>>>'` 0건.
- Gate E 금지어(PASS): `선행`은 「선행 문서」(preceding documents) 동음이의 메타 맥락만, 사용자 노출 카피 0. 그 외 금지어 0.
- Gate F 이벤트 앵커(PASS): `add/page.tsx` 6이벤트 72/106/149/167/183/199 현행 코드 일치, 선행 문서와 drift 0.
- 독립 verifier(Explore, read-only) → **GO, 6/6 PASS**: 한 표 6차원 · 6이벤트 앵커 일치 · 잡→이벤트 매핑 계승(재정의 0) · 과대해석 금지선 5종(completion/first click/conversion/retention%/PMF) · 신규 이벤트 제안 0 · 금지어 메타만.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인(HEAD==origin/master·clean) · 실행 후 검증 존재 → 모두 충족. force-push 아님, fast-forward(타인 작업 미덮어씀).
- report: `reports/marketing-23/2026-05-27T2207Z-local.html`

## Commits

- repo: virtue-rebirth-app, sha: `808231c`, note: 온보딩 지표 운영 판독표 신규 1파일 (push `179ca70..808231c master -> master`)
- repo: infinity, note: 본 archive + `INTENTS.md`(Inbox→Archive) + report를 담은 커밋. SHA는 `git log --oneline -1 -- intents/archive/marketing-23.md`로 확인.

## Next Actions

- 첫 10~20명 관찰 시 §2 판독표를 baseline 양식(`first-real-user-baseline-template.md`) 옆에 두고 잡별 first value·TTV·drop-off·D1/D7을 손기록(새 컬럼 추가 없이).
- §6 운영 리듬(주간 activation·drop-off / 월간 retention)을 실제 주간 리뷰에 한 번 돌려보고 판독표 칸이 손기록에 맞는지 점검(별도 Intent 후보).
- launch 후 PostHog 잡별 코호트가 가능해지면 본 판독표의 정성 칸을 쿼리 후보로 옮길지 검토(D7 수치 단독 판정은 계속 보류).
