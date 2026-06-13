# AI Pricing, Credit, and Limit Trust UX — Research Notes

Date: 2026-06-13
Scope: hybrid·credit·usage gate 모델을 쓰는 AI 제품이 수익화 이전에 어떤 trust UX 신호를 만드는가.
Use: marketing-57 — Virtue first-10 관찰표에 value unit / limit trust 컬럼을 추가하기 위한 배경 자료.

## 핵심 패턴

### Hybrid Credit / Usage Gate 모델
- ChatGPT (free tier + Plus), Claude (free + Pro), Perplexity (free searches + Pro) 등 주요 AI 제품은 credit/usage gate 방식 사용.
- cap은 가격보다 먼저 경험된다: 사용자는 결제 요청을 받기 *전*에 한계에 부딪힌다.
- cap 경험 자체가 trust signal이다: 이 제한은 공정한가? 예측 가능한가? 명확하게 설명됐는가?
- "내가 무료로 무엇을 받았는지" 이해한 사용자만 "유료 업그레이드가 가치 있는가"를 판단할 수 있다.

### Value Unit (세션당 무엇을 받았나?)
- AI 제품의 가치 단위는 흔히 불명확하다: "messages", "queries", "generations", "credits"는 모양이 제각각.
- 사용자가 자기가 받은 것을 말로 표현할 수 없으면, cap 경험은 임의적으로 느껴진다.
- 가치 단위가 명확한 제품 ("이미지 1개 생성", "문서 1개 요약")은 cap 경험이 더 깔끔하다.
- Virtue의 가치 단위 후보: 잡별로 다름 — J1/J2/J4=세션당 저장된 deed 1개, J3=판정 카드 1개.

### Limit Trust Signals
- 작업 도중 cap에 걸리는 사용자는 "방해"로 경험 (부정적 신뢰).
- 세션 시작 전 cap 경계를 미리 보는 사용자는 자발적으로 사용량을 조절하는 경향.
- 설명 없는 cap은 넉넉한 수준이라도 "숨겨진 벽" 인식을 만든다.
- cap 문구 프레임이 중요: "오늘 무료 AI 읽기 3회를 다 사용했습니다" vs "일일 한도 도달"은 신뢰 읽기가 다르다.

### 해석 금지선 (Prelaunch)
AI pricing UX 연구와 Virtue prelaunch 상태를 고려한 금지선:
1. `deed_save_capped` 관찰을 first-10 데이터 수집 전에 upgrade demand로 전환하지 않는다.
2. 사용자가 받는 것을 이해하는지 확인하기 전에 copy에 숫자 cap을 추가하지 않는다.
3. value unit 이해를 관찰하기 전에 cap 경험을 희소성 인센티브로 프레이밍하지 않는다.
4. value unit 멘탈모델이 없는 상태에서 "credit" / "billing" / "unlock" 언어를 쓰지 않는다.
5. 실제 first-10 세션 데이터 전에 가정 willingness-to-pay를 근거로 cap 정책을 조정하지 않는다.

## Virtue 특수 컨텍스트

현재 Virtue 구조:
- 외부 자율 행동 없음 (deed 저장은 사용자가 직접 실행)
- cap (`deed_save_capped`)은 availability signal이지 value signal이 아님 [MARKETING_LEARNINGS: Availability And Friction Are Not Value]
- value unit: J1/J2/J4는 세션당 저장된 deed 1개, J3는 AI 판정 카드 1개
- prelaunch: first-10 사용자, 수기 관찰, pricing/tracking 변경 금지

trust calibration 연결:
- Virtue의 trust 질문은 "AI가 자율적으로 행동했는가"가 아니라 "사용자가 AI 출력을 조언으로 읽었는가, 판결로 읽었는가" [MARKETING_LEARNINGS: No Autonomous Action Bounds The Trust Question]
- value unit 이해는 "무료 deed 3개 cap"이 공정하게 느껴지는가(3개를 받았다) 대 임의적으로 느껴지는가(막혔다)에 직접 영향.

## 참조
- MARKETING_LEARNINGS.md (marketing-21, marketing-28, marketing-38, marketing-41)
- 기존 Virtue activation artifacts: marketing-54, marketing-55, marketing-56
- AI freemium 모델 패턴 (industry common knowledge)