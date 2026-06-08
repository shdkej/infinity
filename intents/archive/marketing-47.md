# marketing-47 Virtue 첫 10명 design-user ask script

- id: marketing-47
- status: archived
- completed_at: 2026-06-08T22:07
- projects: [virtue]
- task_type: strategy
- topics: [prelaunch, first-users, onboarding]
- result_summary: 정식 출시 전 첫 10명에게 보여주기 전 단계의 내부 초대·질문·기록 스크립트를 한 장으로 고정했다. 잡별 초대 문장(J1~J4), 사용 전 2문항, 첫 세션 후 3문항, "사용자가 자기 말로 설명한 Virtue" 기록 칸, 승인 필요선을 docs-only로 정리하고 외부 행동 0.
- artifacts:
  - path: artifacts/marketing-47/virtue-first-10-design-user-ask-script.md
    role: strategy
    note: Virtue 앱 레포가 로컬에 없어 ARTIFACT_RULES에 따라 Infinity artifact로 생성. 초대·질문 문장은 전부 proposal-only 내부 후보, 신규 계측·코드·공개 카피 0.
- reports:
  - path: reports/marketing-47/2026-06-08T2207Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: TBD
    note: artifact, report, learning promotion, archive
- urls: []
- next_actions:
  - 첫 10명 또는 첫 7일 관찰에서 비율 결론 없이 잡별 first value 위치·자기 말 가치·결정-위임 인지 세 언어가 손기록으로 모이는지만 확인한다.
  - 실제 초대 발송·공개 카피·기록표 자동 컬럼 추가는 approval-needed로 별도 게이트에 둔다.

## Result

첫 사용자 학습 루프를 **초대(§A) → 사용 전 2문항(§B) → 첫 세션 후 3문항(§C) → 자기 말 기록 칸(§D)** 4지점 손기록으로 고정했다. 산출의 목표는 작은 표본을 성패율이 아니라 (a) 반복 문제 언어 (b) 자기 말로 설명한 가치 (c) 결정-위임 인지 세 언어로 읽는 것이다.

잡별 초대 문장은 각 잡의 first value를 미리 가리키게 했다 — J1/J2/J4는 `deed_saved`(기록·누적·회고 재료로 남음), J3는 `deed_judged`(AI 결과 카드 도착 자체가 가치, 무저장 종료 정상). AI 결과 질문(§C-3)은 m45 동사 프레임을 따라 사용자가 출력을 판결로 읽는지 조언으로 읽는지를 본다. 성찰형 제품 특성상 도움의 목표를 "결정 대행"이 아니라 "사용자가 자기 말로 가치를 말하게"로 고정했다.

## Verification

- HTML report gate: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함 + details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함.
- docs-only: Infinity artifact 1파일 + report 1파일 + 원장/INTENTS/archive만. Virtue 앱 레포 로컬 부재로 코드 접근·변경 0.
- first value 매핑 재정의 0 (J1/J2/J4=`deed_saved`, J3=`deed_judged`). 앱 미접근으로 line-anchor 인용은 범위 밖, 이벤트명만 사용.
- 신규 이벤트·속성·tracking·privacy·dashboard·session replay·공개 발송·프로덕션 카피·배포·비용·권한 변경: 0.
- 선행 산출물(first-real-user-baseline-template·first-60-second-value-observation-script·ai-promise-decision-control-audit-table) 충돌 0 — 층이 다른 추가.

## Learning

`MARKETING_LEARNINGS.md`에 durable learning candidate `First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation`를 승격했다.
