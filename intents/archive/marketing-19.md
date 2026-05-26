# marketing-19 Intent Archive

- id: marketing-19
- title: Virtue 신규 사용자 홈 화면 FAE 감사표 작성
- status: archived
- priority: medium
- permission: L1 내부 문서/감사표 + L2 agent-approved push
- created_at: 2026-05-26T10:00Z
- completed_at: 2026-05-26T10:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-26-home-dashboard-fae.md`

## Result Summary

신규 사용자가 도착하는 홈 화면 `/`이 **일반 기능 메뉴판이 아니라 First Activation Event(FAE)로 향하는 방향판인지**를 감사하는 내부 문서를 작성했다. ProductQuant/Skene/Delivering Value 공통 렌즈(첫 홈 화면을 중립 대시보드가 아닌 첫 가치 행동 방향판으로 보라)를 채택하되, **공개 카피·코드·이벤트·대시보드·배포는 하나도 바꾸지 않고** 가설 평가/인용으로만 기록했다.

핵심 구조:

- **J → 첫 활성화 행동 매핑(인용)**: J1 기록형/J2 누적형/J4 회고형 → `deed_saved`, J3 AI 호기심형 → `deed_judged`. setup 진입 = `add_flow_started`, J2 누적 부가 = `level_up_viewed`(첫 세션 대개 부재). `activation-milestone-ladder`·`first-session-jtbd-matrix` 정의를 재정의 없이 계승.
- **문서의 심장(§2)**: `/`의 네 요소(주 CTA `오늘 덕 쌓기` `page.tsx:106-112` / 빈 상태 `최근 덕행` `:125-131` / 최근 덕행 영역 `:114-143` / 누적·환생종 신호 `:55-104`)를 세 질문("무엇을 먼저 / 왜 지금 / 하면 무엇이 생기나")으로 **J1/J2/J4 vs J3** 강·약 평가. 모든 셀은 `apps/web/src/app/page.tsx` 실제 렌더 트리 근거.
- **signpost gap G1~G5**: 빈 덕력 숫자(`count===0`)·경쟁 모듈 다수·**J3 홈 AI 훅 부재(가장 큰 갭)**·CTA after-state 미예고·환생종 카드 양면성(positioning R2).
- **관찰 게이트(§4)**: 이벤트 4개를 "닿음" 이진 관찰 보조로만 한정. `/`은 커스텀 이벤트 미발화(autocapture만) → 이정표 효과는 정성 관찰 전용. 전환율 환산·닫힘 단정·J3 judged−saved 갭 이탈 단정 금지.

**핵심 발견:** 홈 화면은 J1/J2 약속에 강하고 **J3에는 구조적으로 약하다** — J3가 찾는 AI 신호는 `/add` 진입 전까지 홈에 사실상 없고, 첫 진입엔 `ScorePill` 점수 칩조차 빈 상태라 부재. `three-screen-value-path-audit` §3-A(J3 앞단 끊김)·positioning R3·jtbd-matrix §3 J3 메모와 모순 없이 일치. 커버한 코드 사실: 신규 사용자 홈은 `count===0`·`recent.length===0`이며 네 named 이벤트(`add_flow_started`/`deed_judged`/`deed_saved`/`level_up_viewed`)는 전부 `add/page.tsx`에서만 발화(홈 `page.tsx`엔 posthog import 없음).

선행 8문서(three-screen / empty-state / friction-protocol / activation-ladder / seven-day-loop / jtbd-matrix / first-impression / copy-spec) 충돌 0. 범위는 "홈 화면 FAE 방향판" 단일 축으로 한정 — 경로 닫힘 재감사(three-screen)·빈 상태 카피 결정(empty-state ES-2)·마찰 태그 처분(friction F1~F9)은 명시적으로 각 문서 소관으로 위임. copy-spec 금지어 0건(사용자 노출 카피 신규 0). workflow-master 파일 양 repo 부재 기록 후 4역할 병렬 합성.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `3d90648` (이전 HEAD `f74cf59` fast-forward)
- path: `apps/web/docs/home-screen-fae-audit.md` (신규 1파일)
- push: `f74cf59..3d90648 master -> master`, HEAD==origin/master, 워킹트리 clean

## Verification

- Gate A 충돌 마커 0(PASS), Gate B 스코프 신규 doc 1개·추적 수정 0(PASS), Gate C 금지 경로 0(PASS), Gate D Infinity 선택적 스테이징·`EVALUATION_NOTES.md` 인덱스 제외(PASS), Gate E 양 repo HEAD==origin(PASS).
- 코드/카피/이벤트/스키마/대시보드/배포/외부발송/비용/시크릿/권한/개인정보 변경 0.
- L2 agent-approved push 2건(Virtue master, Infinity main) 모두 정상 fast-forward.
- report: `reports/marketing-19/2026-05-26T1007Z-local.md`
