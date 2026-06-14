# PLG Signal Hierarchy for Prelaunch Products

> 내부 참조 노트 — marketing-59 (Virtue Launch-Ready PLG Signal Gate) 작성을 위한 개념 기반.
> 날짜: 2026-06-14

## 핵심 인사이트

PLG 프레임워크(OpenView PLG Index, activation-to-monetization hierarchy)의 공통 원칙:

1. **Activation이 항상 먼저다**: "사용자가 first value에 도달했는가"가 모든 후속 신호의 전제 조건이다.
2. **PQL은 activation 이후다**: qualified lead 신호는 *반복* 활성화 + 재방문 행동 묶음에서 나오지, 단일 이벤트에서 나오지 않는다.
3. **Monetization 신호는 실제 사용자의 반복 행동이 쌓인 뒤에야 읽을 수 있다.**
4. **Prelaunch**: 에너지를 전부 first value 이해에 쓴다. conversion/churn을 측정하는 단계가 아니다.

## 신호 위계 (Prelaunch → Launch → Post-Launch)

### 지금 (Prelaunch) — First-Value 신호
- 누가 first value에 도달했는가? (잡별 정의 필요)
- 잡별 first value는 어떤 모양인가?
- first value 이전에 무엇이 막는가?
- 도달 후 사용자는 어떤 언어를 쓰는가?

### 보류 — 시기상조 신호
- 전환율 / PQL rate: N 부족, 대조군 없음
- Viral coefficient: 볼륨 필요
- Retention %: 단일 코호트 신호 잡음 너무 큼
- PMF threshold (40% "very disappointed"): 실사용자 40명+ 필요

### Launch 이후 — Correlation 신호
- Activation vs D7 retention: activation이 재방문을 예측하는가?
- PQL bundle: 반복 activation + D7 재방문 → upgrade readiness
- 채널 품질: 어떤 acquisition 채널이 활성화된 사용자를 만드는가?
- Monetization readiness: 반복 가치 이후 어떤 가격 모델이 맞는가?

## Virtue 적용 메모

- Virtue는 prelaunch, 한 자리 수 사용자
- `deed_save_capped`는 availability/friction — value나 upgrade intent가 아님
- J3의 `deed_judged` 후 무저장 종료는 정상 종료 (churn 아님)
- `deed_saved`는 AI 판정 동의/승인이 아님
- PostHog 접근 가능하지만 prelaunch는 수기 관찰 먼저

## 선행 노트와의 관계

- `marketing-55`: activation measurement contract — first-value gate 고정
- `marketing-56`: first reliable value observation columns — 수기 컬럼 4개
- `marketing-58`: first successful output contract — J1-J4 화면 증거 + agent-readable 품질 기준
- **이 노트**: 어떤 신호를 *언제* 읽어야 하는지의 위계 — 이벤트를 세는 방법이 아니라 단계별 우선순위
