# marketing-17 Intent Archive

- id: marketing-17
- title: Virtue 첫 세션 정성 마찰 관찰 프로토콜
- status: archived
- priority: medium
- permission: L1 문서 작성 + L2 agent-approved push
- created_at: 2026-05-25T22:07Z
- completed_at: 2026-05-25T22:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-25-first-session-friction-evidence.md`

## Result Summary

Virtue 첫 실사용자 표본이 작을 때(첫 10~20명) `deed_judged`/`deed_saved` 전환율보다 **미완료 세션의 첫 가시적 막힘(first visible blockage)**을 먼저 행동 증거로 기록하기 위한 내부 관찰 프로토콜을 작성했다. Goldcast/LogRocket(세션 행동이 이벤트가 놓치는 마찰을 드러냄) + Arise GTM/Hi-Books(pre-value 단계를 value-critical/value-adjacent/non-critical로 분류) + 세스 고딘(마찰=약속이 충분히 구체적이지 않거나 다음 행동 의미가 안 닿았다는 신호) 렌즈를 합성했다.

문서는 (1) J1~J4 첫 가치 경로를 기존 경로 `/` 대시보드 → `/add` 입력 → 결과 카드 → 저장 → `/` 복귀 위에 매핑하고, (2) 수기 정성 마찰 태그 F1~F9(반복 클릭/입력 보류/입력 이탈/결과 카드 이해 못 함/저장 보류·건너뜀/대시보드 payoff 못 알아챔/AI 약속 공백/누적 payoff 공백/카피·의미 불일치)를 Intent 지정 9종과 1:1로 정의하고, (3) 각 단계를 잡별 `value-critical`/`value-adjacent`/`non-critical at activation`으로 분류하며, (4) 신규 계측 없는 첫 3명/첫 10명 검증 게이트를 정리했다.

핵심 정합: F7(AI 약속 공백)=`three-screen-value-path-audit` §3-A J3 앞단 끊김, F8+F6(누적/대시보드 payoff 공백)=§3-B J2 뒷단 누출. "AI 채점 대기"는 잡별 부호 반전 *처분* 대상이라 별도 태그로 만들지 않고 `activation-path-friction-audit`(처분 렌즈)에 위임 — 본 문서는 관찰 렌즈로 역할 분리.

## Artifact

- repo: `virtue-rebirth-app`
- branch: `master`
- commit: `2a8c694` (이전 HEAD `87b8877` fast-forward)
- path: `apps/web/docs/first-session-friction-observation-protocol.md` (신규 1파일 +289)

## Scope

- 신규 이벤트/속성/PostHog 설정/대시보드/세션 리플레이: 0
- 코드/카피/런타임 변경: 0
- 배포/외부 발송/비용/시크릿/권한/개인정보 변경: 0
- 기존 4개 이벤트(`add_flow_started`, `deed_judged`, `deed_saved`, `level_up_viewed`)만 인용
- iOS·`/deeds`·`/dex` 마찰 관찰: 범위 밖, 별도 Intent 후보

## Verification

- 변경이 `apps/web/docs/` 문서 1개로 한정 (`git status --short` 신규 doc만)
- `apps/web/src`·`apps/ios` 변경 0건 (`git diff --stat` 빈 출력)
- 실제 충돌 마커 0 (라인시작 앵커 무매치; 느슨한 검색 유일 매치는 self-check 명령 자기참조, 선행 marketing-16과 동일 관례)
- 지정 선행 3문서(`first-session-jtbd-matrix`/`three-screen-value-path-audit`/`ios-activation-event-parity-brief`) 충돌 0 (§9-2)
- target repo push 후 local HEAD `2a8c694` == `origin/master` `2a8c694`, 워킹트리 clean

## workflow-master

- target repo에 workflow-master 파일 부재 → 부재 기록 후 게이트 수동 적용
- 복잡도 중간 분류, Planner/Developer/Marketer/Operator 4역할 병렬 합성

## Reports

- `reports/marketing-17/2026-05-25T2207Z-local.md`
