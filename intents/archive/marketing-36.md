# marketing-36 Virtue Prelaunch 분석 Skill Sheet

- id: marketing-36
- status: archived
- completed_at: 2026-06-03T10:07
- projects: [virtue]
- task_type: strategy
- topics: [ai-agent, activation, measurement, prelaunch]
- result_summary: Virtue prelaunch 분석의 taxonomy, first value 매핑, 이벤트 어휘, availability 분리, 막힘 4분류, activation 측정 가능 상태, 금지선, 코퍼스 소유 문서를 읽기 전용 참조 1장에 인덱싱했다. 시트는 파생물이며 충돌 시 원본과 원장이 우선이다.
- artifacts:
  - path: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/virtue-prelaunch-analysis-skill-sheet.md
    role: strategy
    note: prelaunch 분석 재발견 방지용 단일 lookup 시트. 새 결론/이벤트/정의 0.
- reports:
  - path: reports/marketing-36/2026-06-03T1007Z-local.html
    role: final
- commits:
  - repo: virtue-rebirth-app
    sha: 6303e36
    note: docs-only prelaunch analysis skill sheet.
  - repo: infinity
    sha: self
    note: Archive registry, intent index, and HTML report.
- urls: []
- next_actions:
  - 다음 Virtue prelaunch 분석 intent는 이 시트 → MARKETING_LEARNINGS.md → 주제 원본 순으로 읽고 시작한다.
  - file:line 앵커는 실행 전 rg로 drift 재확인하고 어긋나면 코드를 따른다.
  - 다음 분석이 실제로 시트를 참조해 재발견 비용이 줄었음이 확인되면 "Prelaunch Analysis Skill Sheet As A Single Lookup" durable 승격을 검토한다.

## Axis

- 축1: prelaunch 판단 기준(first value 매핑·이벤트 앵커·금지선·activation 묶음·코퍼스 소유 문서)이 12개 이상 문서에 분산돼 분석 intent마다 같은 재발견 비용과 저신호 과해석 위험이 반복된다.
- 축2: 읽기 전용 Skill Sheet 1장에 모두 인덱싱하고, 시트를 파생물로 두어 충돌 시 원본 file:line과 MARKETING_LEARNINGS.md가 우선이라는 우선순위를 명시했다.

## Verification

- HTML report gate passed: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details`(4).
- Conflict marker: line-start regex `^(<<<<<<<|=======|>>>>>>>)` NONE. 단일 `rg -c` 매치는 §8에 문서화한 검증 명령 줄.
- Virtue 코드 diff 0: `git diff --stat apps/web/src apps/ios` 빈 출력. git status = docs 1파일만 untracked.
- 신규 이벤트·속성·카피·tracking/privacy·PostHog 설정·dashboard·session replay·코드·배포·외부발송·비용·시크릿·권한·개인정보 변경 0.
- First value mapping preserved: J1/J2/J4 = `deed_saved`:183, J3 = `deed_judged`:106. `deed_save_capped`:167 = availability/friction.
- J3 저장 미강제, judged−saved 갭 = 정상 종료 가능. synthetic/mock/self-test 비결정 등급.
- Source note(`source/external-links/marketing/2026-06-03-agent-first-product-surfaces.md`) 로컬 부재 → intent rationale 요지만 근거.

## Learning Loop

- 계승한 기준: First Value Mapping, Availability And Friction Are Not Value, Traffic Source Before Metrics, Prelaunch Decision Boundary, Measurement Readiness Is A Separate Gate, Product Body vs Bumper By Job, 외 원장 전 항목.
- 이번에 새로 배운 것: 판단 기준이 12개 이상 문서에 분산돼 분석마다 재발견 비용이 든다. 단일 읽기 전용 시트로 모으면 "참조 후 대조"로 전환되고, 충돌 시 원본 우선 우선순위를 명시해야 stale 위험을 막는다.
- 다음 Marketer에게 넘길 규칙: 분석은 시트→원장→원본 순으로 시작; 앵커는 rg로 drift 재확인 후 코드 우선; 시트에 새 결론을 추가하지 말고 원본에 쓴 뒤 인덱스만 갱신; J3 저장 미강제·synthetic 제외·availability 분리·judged−saved 갭=정상을 분석 전 확인.
- MARKETING_LEARNINGS.md 승격 후보: "Prelaunch Analysis Skill Sheet As A Single Lookup" remains report-only until reused by another analysis intent.
