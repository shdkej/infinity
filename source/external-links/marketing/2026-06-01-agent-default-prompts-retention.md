# Agent Default Prompts & Retention (2026-06-01)

> Source type: external-link · marketing
> Topics: onboarding, activation, retention, ai-product, default-prompts
> Added: 2026-06-01
> Related intent: marketing-32

## 핵심 인사이트

Amplitude 사례 분석: 앱의 **첫 입력 유도 문구(agent default prompts / placeholder text)**가 사용자의 첫 경험과 후속 행동(저장·재판정·이탈)에 크게 영향을 미친다.

## 핵심 관찰

### "기능 구경형" 기본값 (Feature-Exploring Default)
- 특징: "뭐든 해봐", "AI에게 물어봐", "한번 써봐" 류의 중립·탐색형 문구
- 사용자가 먼저 AI 기능을 체험/검증하고 싶게 유도
- 예상 흐름: 입력 → AI 결과 확인(deed_judged) → 저장 없이 종결
- Retention 예측력: 낮음. 호기심 충족 후 이탈로 이어질 수 있음
- 적합 잡: J3(AI 호기심형). J1/J2/J4에는 잡 불일치

### "잡 수행형" 기본값 (Job-Performing Default)
- 특징: 사용자가 원래 하려던 작업을 직접 수행하게 유도하는 구체적 문구
- 실제 덕행·행동 기록 맥락을 먼저 제시
- 예상 흐름: 입력 → AI 판정(deed_judged) → 저장(deed_saved) first value 도달
- Retention 예측력: 높음. 잡을 완수한 사용자는 돌아옴
- 적합 잡: J1/J2/J4 (deed_saved 목표). J3도 잡 맥락 문구면 deed_judged first value 도달 가능

## Virtue 적용 맥락

Virtue `/add`의 현재 placeholder/예시/CTA가:
1. 어느 잡(J1~J4)을 우선 호출하는가
2. "기능 구경형"인가 "잡 수행형"인가
3. J3(AI 호기심형)를 의도적으로 부르는가, 우연히 부르는가
4. J1/J2/J4 사용자가 deed_saved first value에 자연스럽게 도달하는 입력을 유도하는가

를 내부 감사표로 분류하면, prelaunch 첫 사용자 관찰 시 손기록 품질이 높아진다.

## 원칙

- 기본값 변경은 관찰 후 proposal-only. 코드 diff 없이 분류 먼저
- 작은 표본(첫 1~3명) 결과로 "기본값이 잡 불일치" 확정하지 않음
- deed_judged 후 deed_saved 없음을 무조건 기능 구경형 이탈로 읽지 않음 (J3 정상 종료)
- synthetic/mock 테스트 입력을 사람 사용자 첫 입력 증거와 혼용하지 않음
