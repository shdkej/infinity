# marketing-21 Intent Archive

- id: marketing-21
- title: Virtue `/add` 입력-결과 균형 감사표 작성
- status: archived
- priority: medium
- permission: L1 내부 문서 감사 + L2 agent-approved push
- created_at: 2026-05-26T22:00Z
- completed_at: 2026-05-26T22:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-ai-onboarding-input-output.md` (ProductLed AI 온보딩 60초 / TTV / Wave FAE 요약)

## Result Summary

Virtue의 AI 가치가 처음 드러나는 `/add` 경로를 **입력 부담(input burden) / 결과 강도(output strength) / 불필요 단계(click tax)** 세 렌즈로 단계별로 감사하고, J1~J4 잡별 "첫 가치"가 닫히는 이벤트를 **저장 전(`deed_judged`) vs 저장 후(`deed_saved`)**로 명시 분리한 내부 문서를 작성했다. **신규 이벤트·코드·카피·계측·대시보드·배포·외부발송·비용·시크릿·권한 변경 0**, 기존 발화 중 이벤트만 관찰 보조로 인용.

핵심 구조:

- **세 렌즈 정의(§0-2)**: `input burden`=첫 결과까지의 수고, `output strength`=수고 대비 결과 풍부함·신뢰, `click tax`=결과에 기여 안 하는 단계(사용자 아닌 제품이 흡수). ProductLed "낮은 입력·높은 결과·제품이 흡수하는 세금" 기준 정렬.
- **단계 지도(§1)**: A 사진 → B 한 줄 메모(선택, ≤120자) → C 판정 트리거 → D 결과 카드 → E 저장. 모든 단계 `apps/web/src/app/add/page.tsx` file:line 앵커. **결과 카드는 저장 전에 보이고 `deed_judged`(`:106`)는 `deed_saved`(`:183`)보다 항상 먼저 발화**.
- **심장 표(§2)**: 단계 × (input burden / output strength / click tax / 기존 이벤트 증거). 요지 — 입력 표면은 이미 얇고(사진1+선택메모+1탭), output strength 정점은 저장(E)이 아니라 **결과 카드(D, `deed_judged`)**, `/add` 내부 click tax는 낮고 진짜 세금은 앞단(J3 약속 부재)·뒷단(J2 누적 누출)에 있음.
- **잡별 첫 가치(§3)**: J1 기록형/J2 누적형/J3 AI 호기심형/J4 회고형 정의 인용. **J3 첫 가치 = `deed_judged`(저장 전), J1/J2/J4 첫 가치 = `deed_saved`(저장 후)** 명시 분리. `J3 저장 전 정상 종료` = J3가 `deed_judged` 후 `deed_saved` 없이 끝내는 것은 이탈이 아니라 잡 충족 후 자연 종료 / 같은 judged-without-saved가 J1/J2/J4엔 저장 전 이탈 후보.
- **보조 이벤트(§4)**: `deed_rerolled`(`:149`, 최대 3회) = 결과 더 보고 싶은 호기심 신호(J3 가치·양면적 신뢰), `deed_save_capped`(`:167`, 발화 후 early return 미저장) = 일일 상한 의도된 마찰. capped 세션도 J3 기준 첫 가치(판정)엔 도달 가능.
- **prelaunch 금지선(§5)**: availability ≠ value(503·judge 지연·캡은 input burden/이탈 집계 제외), judged−saved 갭 잡 분리 없이 이탈 단정 금지, 전환율·리텐션·PMF·% 산출 금지, 한 명 신호 확정 금지, synthetic/mock 제외, 변경 금지.

**핵심 발견:** 같은 "판정은 봤으나 저장 안 함(`deed_judged` 있고 `deed_saved` 없음)" 사건이 잡에 따라 정반대로 해석된다 — J3엔 `J3 저장 전 정상 종료`, J1/J2/J4엔 저장 전 이탈 후보. J3 분리 없이 갭을 일괄 이탈로 읽으면 활성화를 과소 측정한다(activation-ladder 계승). output strength의 정점이 저장이 아니라 판정 결과 카드라는 점이 입력-결과 균형의 중심.

선행 5문서(jtbd-matrix / three-screen / friction-audit / 60s-script / copy-spec) 충돌 0. copy-spec 금지어 신규 카피 0건(금지어는 §0-3 메타 맥락에만). workflow-master 파일 양 repo 부재 기록 후 Planner/Developer/Marketer/Operator 4역할 렌즈 합성.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `95cc836` (이전 HEAD `993547f` fast-forward)
- path: `apps/web/docs/add-input-output-balance-audit.md` (신규 1파일)
- push: `993547f..95cc836 master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 충돌 마커 0(PASS): 변경 파일에 git 충돌 마커 없음, rg 빈 출력.
- Gate B 필수 문자열(PASS): `input burden`(8), `output strength`(7), `click tax`(9), `deed_judged`(18), `deed_saved`(16), `J3 저장 전 정상 종료`(4) 모두 명시. 보조 `deed_rerolled`(7)·`deed_save_capped`(6) 참조.
- Gate C 스코프(PASS): 신규 doc 1개로 한정. `apps/web/src`·iOS·이벤트·대시보드·카피 파일 변경 0.
- Gate D 금지 경로 0(PASS): 코드/카피/이벤트/계측/프라이버시/배포/외부발송/비용/시크릿/권한 변경 0.
- Gate E Infinity 선택적 스테이징(PASS): `INTENTS.md`·`intents/archive/marketing-21.md`·`reports/marketing-21/`만 스테이징, 무관한 `EVALUATION_NOTES.md` 변경 제외.
- Gate F 양 repo HEAD == origin(PASS): Virtue `95cc836`, Infinity push 후 `origin/main` 일치.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인 · 실행 후 검증 존재 → 모두 충족. force-push 아님, 타인 작업 덮어쓰지 않음(fast-forward).
- report: `reports/marketing-21/2026-05-26T2207Z-local.html`

## Next Actions

- 첫 10~20명 관찰 시 §3-3을 적용해 J3 `deed_judged`-only 세션을 `J3 저장 전 정상 종료`로, J1/J2/J4 동일 패턴을 저장 전 이탈 후보로 분리 기록.
- §2 심장 표의 가설(앞단 click tax = 홈 J3 약속 부재 / 뒷단 = J2 누적 누출)을 후속 관찰로 갱신.
- 공개 카피·추적 변경·배포는 별도 승인(Waiting) 경계 유지.
