# marketing-25 Intent Archive

- id: marketing-25
- title: Virtue human/test/agent 트래픽 판독 경계표 작성
- status: archived
- priority: medium
- permission: L1 내부 문서 작성 + L2 agent-approved push
- created_at: 2026-05-28T22:00Z
- completed_at: 2026-05-28T22:07Z
- projects: [virtue]
- task_type: strategy
- topics: [onboarding, analytics, activation, ai-agents]
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-human-agent-onboarding-metrics.md` (Userpilot 2026 / Appcues 2026 onboarding metrics notes)

## Result Summary

**축1 (무엇이 문제였나):** 선행 Virtue activation 문서는 잡 축(J1~J4)과 플랫폼 축(web/iOS)을 분리했지만, `누가/무엇이 만든 트래픽인가`라는 출처 축이 비어 있었다. 사람 실사용자, 메이커 self-test, synthetic/mock, 플랫폼 차이, 장래 agent/API 호출이 aggregate activation에 섞이면 `deed_judged`/`deed_saved` 의미가 오염되고 첫 10~20명 baseline을 과대해석하기 쉽다.

**축2 (어떻게 해결하나):** Userpilot/Appcues 2026 온보딩 지표 가이드를 Virtue prelaunch 판독 경계로 번역해, 트래픽 종류별 **식별 단서 → 기존 이벤트 나타남 → 사람과 같은 판독 규칙인가 → 집계 처리 → 해석 금지선**을 한 경계표로 묶은 내부 문서를 작성했다. 기존 6개 발화 이벤트만 인용했고, 신규 이벤트·코드·카피·제품 변경은 0건이다.

핵심 구조:

- **트래픽 판독 경계표(§2):** A 사람 실사용(baseline 본행), B 메이커 self-test(표시 후 제외), C synthetic/mock(J3 first value 부적합), D 플랫폼 차이(`platform` 분리 후 최소공약수 비교), E 장래 agent/API(미발생, 생기면 별도 규칙).
- **분류 선행 원칙(§3/§5):** 트래픽 종류가 정해지기 전에는 activation/TTV/retention 칸을 읽지 않는다. aggregate 합산 전환율·completion rate·retention rate를 먼저 말한 뒤 나중에 제외하는 방식 금지.
- **first value 매핑 계승(§4):** J1/J2/J4 = `deed_saved`, J3 = `deed_judged` 저장 전을 그대로 유지했고 재정의 0.
- **장래 agent/API 경계(§6):** agent activation·retention은 사람과 다른 규칙(첫 작업 무오류 완료 / 설정자 재호출)으로 분리하는 proposal-only 후보로만 남겼다. 구현·계측·대시보드 변경 0.

**핵심 발견:** 같은 이벤트 수라도 `누가/무엇이` 만들었는지가 다르면 같은 activation으로 묶지 않는다. A만 baseline 본행으로 읽고, B·C는 표시 후 제외한다. D는 플랫폼 분리 후 공통 명명 이벤트만 비교하며, E는 아직 미발생이므로 사람이 만든 activation과 합산하지 않는다. 한 세션이 여러 분류에 걸치면 더 강한 제외 사유(B·C)가 D보다 앞선다.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `f5fde73` (이전 HEAD `c3afb52` fast-forward)
- path: `apps/web/docs/traffic-source-reading-boundary-table.md` (신규 1파일, 177줄)
- push: `c3afb52..f5fde73 master -> master`, HEAD == origin/master, 워킹트리 clean

## Verification

- Gate A 파일 존재(PASS): 177줄 신규 생성.
- Gate B 5개 트래픽 종류(PASS): A 사람 실사용 · B 메이커 self-test · C synthetic/mock · D 플랫폼 차이 · E 장래 agent/API.
- Gate B2 6개 이벤트(PASS): `add_flow_started`, `deed_judged`, `deed_saved`, `level_up_viewed`, `deed_rerolled`, `deed_save_capped` 모두 문서에 존재.
- Gate C first-value 매핑(PASS): J1/J2/J4 = `deed_saved`, J3 = `deed_judged` 계승·재정의 0.
- Gate D no-read/금지선(PASS): 분류 전 숫자 읽기 금지와 aggregate 합산 금지선 명시.
- Gate E 충돌 마커(PASS): 라인 시작 실제 conflict marker 0.
- Gate F 이벤트 앵커(PASS): `add/page.tsx` 72/106/149/167/183/199 현행 코드 일치, drift 0. iOS `platform=ios` `Analytics.swift:23` 일치.
- Gate G 코드 변경 0(PASS): `apps/web/src`, `apps/ios/Sources` diff 없음.
- Gate H 타 문서 미변경(PASS): repo 전체 변경은 신규 doc 1파일뿐.
- workflow-master 파일 양 repo 부재 기록 후 Planner/Developer/Marketer/Operator 4역할 렌즈 수동 합성.
- L2 self-approval(agent-approved): intent 직결 · 되돌림 가능 · 비용 0 · 프로덕션 데이터/운영 권한/시크릿 변경 0 · 타인 메시지 0 · 실행 전 상태 확인(HEAD==origin/master·clean) · 실행 후 검증 존재 → 모두 충족. force-push 아님, fast-forward(타인 작업 미덮어씀).
- report: `reports/marketing-25/2026-05-28T2207Z-local.html`

## Commits

- repo: virtue-rebirth-app, sha: `f5fde73`, note: traffic-source reading boundary table 신규 1파일 (push `c3afb52..f5fde73 master -> master`)
- repo: infinity, note: 본 archive + `INTENTS.md`(Inbox→Archive) + report를 담은 커밋. SHA는 `git log --oneline -1 -- intents/archive/marketing-25.md`로 확인.

## Next Actions

- 첫 10~20명 baseline 판독 전에 §2 경계표로 트래픽 종류를 먼저 분류하고, B/C/D/E를 aggregate activation에서 섞지 않는다.
- 장래 agent/API 호출이 실제로 생기면 사람 activation과 합산하지 말고 별도 Intent로 계측/대시보드 경계를 검토한다.
