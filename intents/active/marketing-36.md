# marketing-36 · Virtue prelaunch 분석 skill sheet 작성

- id: marketing-36
- status: in_progress
- priority: medium
- permission: L1/L2 doc-only
- projects: [virtue]
- goal: 에이전트와 내부 분석자를 위한 Virtue prelaunch 분석 1-page 참조 sheet를 작성한다. J1~J4 first value 매핑, activation 후보 묶음 A1~A4, prelaunch 금지선, synthetic 제외, availability 분리를 한 문서에 통합한다.
- success_criteria: `apps/web/docs/virtue-prelaunch-analysis-skill-sheet.md` 생성, 기존 first value 문서 충돌 0, 신규 이벤트/속성 0, conflict marker 0
- mode: prepare (cloud, 완료) → execute_local (virtue-rebirth-app docs, 대기)
- context: artifacts/marketing-36/virtue-prelaunch-analysis-skill-sheet-draft.md
- prepare_report: reports/marketing-36/2026-06-03T0600Z.html

## 다음 액션 (로컬 Claude Code 실행)

```
Infinity Intent: marketing-36 Virtue prelaunch 분석 skill sheet 작성
Mode: execute_local
Workflow: simple-doc (단일 문서 생성)
Goal: apps/web/docs/virtue-prelaunch-analysis-skill-sheet.md 생성
Context:
  - infinity/artifacts/marketing-36/virtue-prelaunch-analysis-skill-sheet-draft.md (초안)
  - infinity/MARKETING_LEARNINGS.md (기준 원장)
  - apps/web/docs/ 기존 문서들
Prepared findings: cloud prepare 완료. §0~§7 구조로 초안 작성됨. 계승 기준: First Value Mapping, Availability And Friction Are Not Value, Prelaunch Decision Boundary, Traffic Source Before Metrics, Measurement Readiness Is A Separate Gate.
Allowed: L1 doc-only (새 파일 1개 생성, 기존 파일 변경 없음)
Forbidden: 코드·이벤트 속성·공개 카피·계측·배포·외부발송·비용·권한·개인정보 변경
Verification:
  1. rg '<<<<<<<|=======|>>>>>>>' → 0 확인
  2. git diff --stat apps/web/src apps/ios/Sources → 빈 출력
  3. git status → docs/virtue-prelaunch-analysis-skill-sheet.md 1파일만
  4. 기존 *activation*, *onboarding*, *jtbd*, *baseline* 문서 충돌 없음
Report back to: infinity/reports/marketing-36/2026-06-03T0600Z-local.html (HTML 필수)
```
