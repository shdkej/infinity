# marketing-59: Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- status: archived
- completed_at: 2026-06-14T13:00Z
- projects: [virtue]
- task_type: strategy
- topics: [plg, activation, measurement, prelaunch]
- result_summary: PLG 신호 위계를 Virtue prelaunch 3열 게이트(지금/보류/launch-after)로 번역하고 first-10 수기 review checklist를 완성했다. J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑 유지.
- artifacts:
  - path: artifacts/marketing-59/virtue-plg-signal-gate.md
    role: strategy
    note: 3열 신호 게이트 표 + first-10 수기 review checklist
- reports:
  - path: reports/marketing-59/2026-06-14T1300Z-heartbeat.html
    role: final
- source_note: source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md
- commits:
  - repo: infinity
    branch: claude/gifted-bohr-qpcsgc
    note: heartbeat cloud docs-only completion
- urls: []
- next_actions:
  - first-10 관찰 시 이 게이트 표를 수기 체크리스트로 사용한다
  - 어떤 신호도 이 표의 분류 없이 activation rate / PMF / retention% / PQL로 환산하지 않는다
  - PostHog 접근 및 프로젝트 ID 확보 시 별도 intent로 계측 readiness 확인

## Result

`marketing-59`는 최신 PLG 신호 위계 개념을 Virtue prelaunch 관찰 계약에 L1 docs-only로 통합했다.

핵심 산출물은 **3열 신호 게이트 표**:

| 지금 볼 신호 | 보류할 신호 | launch 이후 볼 신호 |
|---|---|---|
| first value 도달 (잡별) | activation rate % | PQL 확정 (반복+재방문 묶음) |
| 트래픽 분류 (human vs mock) | D7/D30 retention 비율 | Correlation: activation vs D7 retention |
| 가용성 차단 여부 | PMF 수치 | 재활성화 후보 분류 |
| 사용자 언어 원문 | PQL 단일이벤트 환산 | Monetization 신호 |
| 결정-위임 인지 | 외부 벤치마크 복사 | 공개 카피 / 발송 전략 |
| guided break 위치 | judged-saved 갭 → 이탈 단정 | dashboard / tracking |
| B-분류 | D1/D3/D7 미방문 → churn 단정 | |

그리고 **first-10 수기 review checklist**:
```
□ Human 실사용인가? (mock/synthetic → 제외)
□ first value 이벤트 발화? (J1/J2/J4: deed_saved | J3: deed_judged)
□ 가용성 차단 있었나? (deed_save_capped / 503 / 지연)
□ 사용자 언어 원문 기록했나?
□ 결정-위임 인지 기록했나?
□ B-분류 표시했나? (B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL)
□ guided break 위치 표시했나?
→ 모든 체크 완료 전에 비율/PMF/retention 결론 없음
```

## Verification

- Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` 생성됨
- conflict markers: 0
- 선행 marketing-55/56/58: first-value 매핑(J1/J2/J4=`deed_saved`, J3=`deed_judged`) 계승, 충돌 없음
- production code / tracking / privacy / dashboard / public copy / deploy / external message / cost 변경: 0
- HTML report gate: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함

## Learning

`MARKETING_LEARNINGS.md` 승격 후보 없음 — 이 게이트는 기존 기준들의 통합 응용이며 새 durable learning을 추가하지 않는다. (기존 [[Measurement Readiness Is A Separate Gate]], [[PQL Is A Bundle, Not A Single Event]], [[Prelaunch Decision Boundary]]로 모두 커버됨)
