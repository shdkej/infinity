# marketing-22 Intent Archive

- id: marketing-22
- title: Virtue 리텐션 예측 활성화 브리프 작성
- status: archived
- priority: medium
- permission: L1 내부 문서 작성 + L2 agent-approved push
- created_at: 2026-05-27T10:00Z
- completed_at: 2026-05-27T10:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-27-retention-predictive-activation.md` (Amplitude 7% Retention Rule / Lenny Distilled 활성화 메모 요약)

## Result Summary

**축1 (무엇이 문제였나):** prelaunch 첫 10~20명에서 첫 행동 클릭(`add_flow_started`)을 활성화로 오인하거나 D7 복귀 수치를 외부 벤치마크로 베끼면 작은 표본을 과대 해석한다. 선행 문서는 first→second value를 이었으나 "이 클릭이 vanity인가 리텐션 예측 depth 신호인가"를 잡별로 가르는 분리 렌즈가 없었다.

**축2 (어떻게 해결하나):** 활성화를 **첫 행동(intent) → first value(aha) → retention-predictive depth signal** 세 층으로 분리하고, 잡(J1~J4)별 first value·depth·**D7 재가치 질문(손기록, 숫자 아님)**을 한 표로 묶은 내부 문서를 작성했다. 기존 6개 발화 이벤트만 인용, **신규 이벤트·코드·카피·대시보드·계측 변경 0건**.

핵심 구조:

- **3층 분리표(§2)**: 첫 행동(`add_flow_started` `:72`, 낮은 예측력·vanity 위험) / first value(J1·J2·J4 = `deed_saved` `:183`, J3 = `deed_judged` `:106` 저장 전) / depth(반복 `deed_saved`·`level_up_viewed` `:199`·`deed_rerolled` `:149`·D7 내 second value, 높을 가능성이나 작은 표본은 정성). 시간순 층이지 통과 관문 아님.
- **잡별 심장 표(§3)**: J1~J4 × (first value · retention-predictive depth signal · D7 재가치 질문 · 기존 이벤트 증거). J1 즉시 만족 / J2 누적감+`level_up_viewed` / J3 반복 판정·`deed_rerolled` 또는 저장 전환 / J4 지연 가치. 같은 `deed_saved`라도 depth 가치 방향이 다르므로 묶지 않음. J3는 저장 없는 판정 반복도 정상 depth.
- **D7 재가치 질문 5선(§5)**: D0 first value · D7 return(본인 표현) · D7 second value evidence · same-job continuity · source promise fit. 모두 baseline·first-week-bridge 양식의 기존 칸 재사용, 새 표/컬럼 0, 손기록.
- **작은 표본 depth 읽기(§4)**: `level_up_viewed`는 비율 아닌 "누적 payoff 알아챘는가" 정성, depth는 D0 단발이 아니라 "다시·더" 신호, availability≠value(503·지연·`deed_save_capped` `:167` early return 제외).
- **prelaunch 금지선(§6)**: D7 수치 외부 벤치마크 베끼기 금지, 첫 행동 지표 승격 금지, 전환율·리텐션·PMF·% 산출 금지, judged−saved 갭 이탈 단정 금지(J3 정상 종료), availability≠value, 한 명 신호 확정 금지, depth 1회로 리텐션 확보 단정 금지, synthetic/mock 제외, 변경 금지.

**핵심 발견:** 같은 이벤트라도 *층*이 다르다 — `add_flow_started`는 intent(낮은 예측력), 단발 `deed_saved`/`deed_judged`는 first value, "다시·더"(반복 저장·`level_up_viewed`·`deed_rerolled`·D7 재가치)만이 retention-predictive depth. D7는 prelaunch에서 비율이 아니라 "같은 잡 가치가 D7에 한 번 더 닿았는가"를 묻는 손기록 질문으로 다룬다.

선행 8문서(jtbd-matrix / activation-milestone-ladder / seven-day-deed-loop / first-week-activation-retention-bridge / add-input-output-balance-audit / first-real-user-baseline-template / time-to-value-observation-brief / copy-spec) 충돌 0. copy-spec 금지어 신규 카피 0(`선행`은 「선행 문서」 동음이의 메타 맥락만). workflow-master 파일 양 repo 부재 기록 후 Planner/Developer/Marketer/Operator 4역할 렌즈 수동 합성 + 독립 verifier 승인 패스 분리.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `179ca70` (이전 HEAD `95cc836` fast-forward)
- path: `apps/web/docs/retention-predictive-activation-brief.md` (신규 1파일, 166줄)
- push: `95cc836..179ca70 master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 파일 존재(PASS): 166줄 신규 생성.
- Gate B 필수 문자열(PASS): `deed_judged`(15), `deed_saved`(25), `level_up_viewed`(8), `D7`(34), `prelaunch`(11) 모두 존재.
- Gate C 스코프(PASS): Virtue `git status --porcelain` = 신규 doc 1개만. `src`·이벤트·대시보드·카피 변경 0.
- Gate D 충돌 마커(PASS): doc 내 git 충돌 마커 0.
- Gate E 금지어(PASS): `선행`은 「선행 문서」(preceding documents) 동음이의 메타 맥락만, 사용자 노출 카피 0. 그 외 금지어 0.
- Gate F 이벤트 앵커(PASS): `add/page.tsx` 6이벤트 72/106/149/167/183/199 현행 코드 일치, 선행 문서와 drift 0.
- 독립 verifier(Explore, read-only) → **GO, 5/5 PASS**: 필수 내용 5종 · 앵커 일치 · 잡→이벤트 매핑 계승(재정의 0) · 금지어 메타만 · 1파일 스코프.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인(HEAD==origin/master·clean) · 실행 후 검증 존재 → 모두 충족. force-push 아님, fast-forward(타인 작업 미덮어씀).
- report: `reports/marketing-22/2026-05-27T1007Z-local.html`

## Commits

- repo: virtue-rebirth-app, sha: `179ca70`, note: 리텐션 예측 활성화 브리프 신규 1파일 (push `95cc836..179ca70 master -> master`)
- repo: infinity, note: 본 archive + `INTENTS.md`(Inbox→Archive) + report를 담은 커밋. SHA는 `reports/marketing-22/2026-05-27T1007Z-local.html` 동시 커밋과 동일하며 `git log --oneline -1 -- intents/archive/marketing-22.md`로 확인.

## Next Actions

- 첫 10~20명 관찰 시 §3 D7 재가치 질문과 §5 5선을 baseline·first-week-bridge 양식 칸에 손기록(새 컬럼 추가 없이).
- PostHog 접근 확인 후에도 D7 수치만 보지 말고 `deed_judged`/`deed_saved`/`level_up_viewed` 조합을 잡별 코호트 정성으로 읽는 쿼리 후보 검토(별도 Intent).
- 첫 10~20명 양식에 `D7 return reason`·`same job continued`·`second value evidence` 컬럼을 신설할지 여부는 Waiting(본 Intent 범위 밖, 기존 칸 재사용으로 충당).
