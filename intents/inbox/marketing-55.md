# marketing-55: Virtue Prelaunch Activation Measurement Contract

- id: marketing-55
- status: inbox
- projects: [virtue]
- task_type: strategy
- topics: [activation, measurement, onboarding, prelaunch, plg]
- owner: SAM
- display_name: Virtue Prelaunch Activation Measurement Contract
- created_at: 2026-06-12T10:00Z
- source: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-12-plg-activation-measurement.md`
- permission_level: L1 docs-only

## Rationale

Mixpanel의 2026 PLG 글은 가입/페이지뷰보다 activation, PQL, expansion 같은 행동 신호가 중요하다고 설명한다. Virtue는 아직 prelaunch라 후단 지표를 계산할 단계가 아니므로, 먼저 잡별 first value와 출시 전 판단 금지 지표를 문서로 계약해야 한다.

## Expected Impact

정식 출시 전 작은 이벤트 숫자를 과대해석하지 않고, 첫 10명 관찰과 기존 PostHog 이벤트를 같은 언어로 읽게 한다. 특히 J3의 `deed_judged` 정상 완료와 J1/J2/J4의 `deed_saved` 중심 완료를 섞어 판단하는 위험을 줄인다.

## First Useful Action

Virtue activation measurement contract 문서를 만든다. 표에는 잡(J1-J4), first value, 기존 이벤트, 수기 관찰 질문, `count now`, `observe manually`, `do not judge yet`, launch-after gate를 포함한다.

## Success Criteria

- 기존 first value 매핑을 재정의하지 않는다: J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- 신규 이벤트, tracking/privacy 변경, PostHog 대시보드 생성, 공개 카피, 배포, 외부 발송, 비용 발생이 없다.
- PQL, paid conversion, expansion, viral coefficient는 prelaunch 판단 금지 또는 launch-after gate로 분리한다.
- 산출물에 출처 노트 경로와 Mixpanel PLG 측정 렌즈를 명시한다.

## First Verification Gate

문서 작성 후 `rg '<<<<<<<|=======|>>>>>>>'`로 충돌 마커 0건을 확인하고, `rg 'deed_saved|deed_judged|do not judge yet|count now|observe manually'`로 필수 판독 용어가 포함됐는지 확인한다.

## Approval Boundary

L1 docs-only 작업이다. 신규 추적 이벤트/속성, 개인정보·tracking 설정, 대시보드 생성, 프로덕션 코드, 공개 카피, 외부 메시지, 광고, 비용, 배포는 별도 승인 전까지 실행하지 않는다.
