# marketing-24 Intent Archive

- id: marketing-24
- title: Virtue AI 판정 신뢰 보정 감사표 작성
- status: archived
- priority: medium
- permission: L1 내부 문서 작성 + L2 agent-approved push
- created_at: 2026-05-28T10:00Z
- completed_at: 2026-05-28T10:07Z
- projects: [virtue]
- task_type: strategy
- topics: [activation, trust, ai-product, onboarding]
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-ai-trust-calibration.md` (Google People + AI Guidebook, Explainability + Trust / Feedback + Control 요약)

## Result Summary

**축1 (무엇이 문제였나):** Virtue의 첫 가치는 `/add` 결과 카드(`deed_judged`)에서 강하게 드러나지만, AI 판정이 "신기함"으로만 소비되면 J3 호기심형에게는 짧은 만족만 주고 J1/J2/J4에게는 저장·재방문을 설득하지 못한다. 동시에 사진 1장 + 짧은 메모라는 얕은 입력에서 나온 점수를 사용자가 정체성 피드백으로 과신하거나, mock 한 번에 불신으로 식을 위험이 prelaunch에서 점검되지 않았다.

**축2 (어떻게 해결하나):** Google People + AI Guidebook의 신뢰 보정 렌즈(과신 ↔ 불신 사이의 적정 신뢰)를 J1~J4 잡에 번역해, 잡별 **첫 가치 이벤트 → 필요한 설명 수준 → 과신 위험 → 불신 위험 → 사용자 제어(재시도/저장/무시/수정) → 정성 관찰 질문**을 **한 감사표(§2)**로 묶은 내부 문서를 작성했다. 기존 발화 이벤트만 인용, **신규 이벤트·코드·카피·제품 변경 0건**(제안은 §7 proposal-only).

핵심 구조:

- **신뢰 보정 감사표(§2, 심장):** 4행(J1~J4) × 6차원. 첫 가치(J1·J2·J4 = `deed_saved`, J3 = `deed_judged` 저장 전) / 필요 설명 수준 / 과신 위험 / 불신 위험 / 사용자 제어 / 정성 관찰 질문.
- **신뢰 보정 렌즈(§1):** 신뢰 3요소(능력/일관성/선의) · 과신(얕은 입력 점수를 정체성 피드백으로 오독) · 불신(가치 순간을 흘려보냄) · 보정(적정 신뢰, 맹신 아님) · 설명=활성화 장치. 확신도 숫자(%) 부재는 출처의 "숫자 확신도보다 행동형 문장" 권고와 우연히 정렬.
- **제어권 감사(§4):** 재시도(`한 번 더` ≤3, `deed_rerolled:149`)·저장(`deed_saved:183`, 0점도 저장 가능)·무시/되돌리기(`취소`/`onReset:153`, 미저장 `add_flow_abandoned:78`)는 실재. **출력 수정·수동 우회는 부재** — 점수/코멘트/태그 직접 수정 경로 없음. 사용자가 판정에 동의 안 할 때 쓸 수 있는 건 재시도(≤3)나 폐기뿐이라, 과신은 수동적 수용으로 불신은 이탈로 흐르기 쉽다(proposal-only 후보).
- **prelaunch 금지선(§6):** 한 명 trust 발화로 과신/불신 단정 금지, judged−saved 갭을 불신으로 단정 금지(J3 정상 종료), 확신도 숫자 도입을 정답으로 가정 금지, 신뢰=항상 높이기로 오독 금지, availability≠value(`deed_save_capped` early return 등), synthetic/mock 점수로 능력·일관성 판단 금지, 변경 금지.

**핵심 발견:** 같은 결과 카드라도 신뢰 보정 역할이 잡별로 다르다 — J1엔 통과점(낮은 설명), J2엔 일관성(누적 공정성), J3엔 본체(높은 설명·최대 과신 위험), J4엔 영구 주석(사후 수정 불가 공백). J3가 신뢰 보정의 진폭이 가장 큰 단 하나의 잡(`deed_judged`가 first value). 출력 수정·수동 우회 제어 부재로 적정 신뢰 형성 경로가 재시도(≤3)·폐기로 좁다.

앞선 5문서(first-session-jtbd-matrix / first-60-second-value-observation-script / add-input-output-balance-audit / first-session-friction-observation-protocol / onboarding-metrics-reading-table) + copy-spec 충돌 0. J3 라이브 trust-aware 관찰 큐(BASIS/FINAL CHOICE/TRUST 3축)는 60초 스크립트 §4-1이 담당하므로 본 문서는 정적 J1~J4 감사로 분리하고 중복 0으로 위임. workflow-master 파일 양 repo 부재 기록 후 Planner/Developer/Marketer/Operator 4역할 렌즈 수동 합성 + 독립 verifier(Explore, read-only) 승인 패스 분리.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `c3afb52` (이전 HEAD `808231c` fast-forward)
- path: `apps/web/docs/ai-judgment-trust-calibration-audit.md` (신규 1파일, 136줄)
- push: `808231c..c3afb52 master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 파일 존재(PASS): 136줄 신규 생성.
- Gate B 필수 정규식(PASS): `rg 'deed_judged|deed_saved|trust|신뢰|J1|J2|J3|J4'` 46매치. trust(13)·신뢰(26)·과신(20)·불신(14)·J1(17)·J2(8)·J3(14)·J4(16)·deed_judged(8)·deed_saved(12) 모두 존재.
- Gate B2 이벤트 화이트리스트(PASS): 인용 = `deed_judged`·`deed_saved`·`deed_rerolled`·`deed_save_capped`·`add_flow_abandoned`만. `deed_judge_attempted` 등 비허용 0.
- Gate C first-value 매핑(PASS): J1/J2/J4 = `deed_saved`, J3 = `deed_judged` 계승·재정의 0.
- Gate D diff 스코프(PASS): `git diff --cached --stat` = 문서 1파일(+136)만, `git status` 미추적 단일 파일.
- Gate E 충돌 마커(PASS): `rg '<<<<<<<|=======|>>>>>>>'` 0건.
- Gate F 금지어(PASS): `선행` 미사용(「앞선 문서」로 대체), copy-spec 금지어(훌륭한/멋진 인격/좋은 사람/본받을/마음이 따뜻한/모범적인/귀감/인성/미덕/베풂/봉사정신) 0건.
- Gate G 이벤트 앵커(PASS): `add/page.tsx` 23(MAX_REROLLS)/78/106/149/167/183/199 현행 코드 일치, drift 0.
- 독립 verifier(Explore, read-only) → **GO, 6/6 PASS**: 한 표 6차원 · first-value 매핑 계승(재정의 0) · 이벤트 화이트리스트(deed_judge_attempted 미인용) · 코드 앵커 + 출력 수정 제어 부재 사실 확인 · 스코프 규율(proposal-only 분리) · m20 §4-1 위임(중복 0) 모두 PASS.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인(HEAD==origin/master·clean) · 실행 후 검증 존재 → 모두 충족. force-push 아님, fast-forward(타인 작업 미덮어씀).
- report: `reports/marketing-24/2026-05-28T1007Z-local.html`

## Commits

- repo: virtue-rebirth-app, sha: `c3afb52`, note: AI 판정 신뢰 보정 감사표 신규 1파일 (push `808231c..c3afb52 master -> master`)
- repo: infinity, note: 본 archive + `INTENTS.md`(Inbox→Archive) + report를 담은 커밋. SHA는 `git log --oneline -1 -- intents/archive/marketing-24.md`로 확인.

## Next Actions

- 첫 10~20명 관찰 시 §2 감사표를 baseline 양식(`first-real-user-baseline-template.md`) + 60초 스크립트 §4-1 옆에 두고 잡별 과신/불신 발화·제어 선택을 손기록(새 컬럼 추가 없이).
- §4 출력 수정·수동 우회 공백(점수 override·코멘트 편집)을 실제 관찰에서 사용자가 원하는지 확인 후, 필요하면 별도 Intent로 제어 추가 검토(코드 변경 = 승인 대상).
- 결과 카드 신뢰 카피 후보(숫자 확신도 대신 근거/한계 문장)는 copy-spec 금지선 통과 + 사용자 관찰 비교를 거쳐 별도 Intent로 분리(승인 필요).
