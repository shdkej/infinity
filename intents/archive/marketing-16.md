# marketing-16 Intent Archive

- id: marketing-16
- title: Virtue 첫 세션 3-스크린 가치 경로 감사표
- status: archived
- priority: medium
- permission: L1 + L2 agent-approved push
- created_at: 2026-05-25T10:07Z
- completed_at: 2026-05-25T10:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-25-three-screen-value-onboarding.md`

## Result Summary

Virtue 첫 세션을 S1 `/` 대시보드, S2 `/add` 입력, S3 `/add` 결과 카드의 3개 개념 화면으로 고정하고, J1 기록형/J2 누적형/J3 AI 호기심형/J4 회고형 각각의 `첫 약속 -> 첫 행동 -> 첫 가치 확인` 경로를 내부 감사표로 작성했다.

핵심 결론은 "닫히지 않음"을 두 형태로 분리한 것이다. J3는 `deed_judged`로 S3에서 가치를 확인하지만 S1에 AI 약속이 없어 앞단이 끊긴다. J2는 `deed_saved`로 저장은 닫히지만 누적/진화 payoff가 `/` 복귀 또는 조건부 `level_up_viewed`에 의존해 첫 세션 세 화면 밖으로 샌다. J1과 J4의 첫 세션 가치는 `deed_saved`로 S3에서 닫힌다.

## Artifact

- repo: `virtue-rebirth-app`
- commit: `87b8877`
- path: `apps/web/docs/three-screen-value-path-audit.md`

## Scope

- 신규 이벤트/속성/PostHog 설정/대시보드: 0
- 코드/카피/런타임 변경: 0
- 배포/외부 발송/비용/시크릿/권한 변경: 0
- iOS 화면 수 감사: 범위 밖, 별도 Intent 후보

## Verification

- 기존 문서 `first-session-jtbd-matrix`, `activation-milestone-ladder`, `ios-activation-event-parity-brief`와 직접 충돌 0
- 지정 이벤트 4개(`add_flow_started`, `deed_judged`, `deed_saved`, `level_up_viewed`)만 매핑에 사용
- `apps/web/src`, `apps/ios/Sources` 변경 0건
- 충돌 마커 0건
- `virtue-rebirth-app` push 후 local HEAD `87b8877` == `origin/master` `87b8877`

## Reports

- `reports/marketing-16/2026-05-25T1007Z-local.md`
