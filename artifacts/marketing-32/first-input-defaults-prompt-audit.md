# Virtue `/add` 첫 입력 기본값/예시 감사표

> prelaunch 전에 `/add`의 placeholder, 예시, 첫 입력 유도 문구가 J1~J4 중 어느 잡을 부르는지,
> "기능 구경형"(deed_judged 종결)인지 "잡 수행형"(deed_saved/deed_judged first value 도달)인지 내부 감사표.

**Status:** cloud draft — §4 심장표 [CODE_CHECK] 칸은 local Claude Code가 virtue-rebirth-app 코드 확인 후 채울 것

Source: `source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md`

선행 문서:
- `apps/web/docs/first-session-jtbd-matrix.md` (marketing-06)
- `apps/web/docs/add-input-output-balance-audit.md` (marketing-21)
- `apps/web/docs/first-session-friction-observation-protocol.md` (marketing-17)
- `apps/web/docs/product-body-vs-bumper-boundary-table.md` (marketing-31)
- `apps/web/docs/onboarding-metrics-reading-table.md` (marketing-23)
- `apps/web/docs/home-screen-fae-audit.md` (marketing-19)
- `apps/web/docs/first-60-second-value-observation-script.md` (marketing-20)

---

## §1 목적 및 배경

Amplitude의 agent default prompt 사례: 앱의 첫 입력 유도 문구가 사용자의 첫 경험과 후속 행동을 크게 좌우한다. "기능 구경형" 기본값과 "잡 수행형" 기본값을 구분하지 않으면:

- 같은 앱에서 J3 경로 사용자(AI 호기심형, deed_judged first value)가 의도치 않게 J1/J2/J4 경로 기대값(deed_saved)으로 유도될 수 있다
- 또는 J1/J2/J4 기대 사용자가 "기능 구경형" 기본값에 혼란을 느껴 첫 세션을 이탈할 수 있다

prelaunch 첫 사용자 관찰 전에 현재 `/add`의 기본값이 어느 잡을 유도하는지 분류해 두면, 첫 세션 activation 손기록 품질이 높아진다.

---

## §2 잡(Job) 정의 및 first value 매핑

| 잡 | 잡 이름 | 사용자 핵심 목적 | first value event | first value 설명 |
|----|---------|----------------|-------------------|------------------|
| J1 | 기록형 | "덕행을 기록해 두고 싶다" | `deed_saved`:183 | 저장 완료 |
| J2 | 누적형 | "덕행을 쌓아 성장을 보고 싶다" | `deed_saved`:183 | 저장 완료 (누적 payoff는 후속 세션 `level_up_viewed`:199) |
| J3 | AI 호기심형 | "AI가 내 덕행을 어떻게 판정하는지 궁금하다" | `deed_judged`:106 | 결과 카드 도달 (저장은 선택) |
| J4 | 회고형 | "과거 덕행을 돌아보고 싶다" | `deed_saved`:183 | 저장 완료 |

이 매핑은 marketing-06~marketing-31 전체에서 일관되게 계승. 재정의 없음.

---

## §3 기존 6 발화 이벤트 매핑

| 이벤트 | 코드 앵커 | 발화 조건 | 잡별 의미 | 기본값 감사 관련성 |
|--------|-----------|-----------|----------|-----------------|
| `add_flow_started` | :72 | `/add` 진입 | 모든 잡: TTV 시작점 | 기본값이 이 이벤트를 유발하는 첫 화면까지만 연결 |
| `deed_judged` | :106 | AI 판정 완료 | **J3**: first value. J1/J2/J4: 통과점 | J3 잡 유도 기본값의 목표 이벤트 |
| `deed_saved` | :183 | 저장 완료 | **J1/J2/J4**: first value. J3: 선택적 | J1/J2/J4 잡 유도 기본값의 목표 이벤트 |
| `deed_rerolled` | :149 | 재판정 요청 | J3: AI 호기심 확장 (최대 3회). 다른 잡: 마찰 가능성 | "기능 구경형" 기본값이 J3 재판정을 유도할 수 있음 |
| `deed_save_capped` | :167 | 저장 상한 early-return | availability/friction 신호. first value 아님 | 기본값 분류와 무관. 가용성 문제 |
| `level_up_viewed` | :199 | 레벨업 화면 도달 | 누적 payoff (J2 특히 유효) | 기본값 직접 연결 없음 (후속 세션) |

---

## §4 심장표 — J1~J4 × `/add` 첫 입력 유도 감사

> ⚠️ **TODO (local Claude Code)**: 아래 [CODE_CHECK] 표시 칸은
> `virtue-rebirth-app/apps/web/app/add/page.tsx` (또는 관련 component)를
> 확인하여 실제 값을 채운다.
>
> 확인해야 할 요소:
> - `placeholder` props (입력 필드 안내 텍스트)
> - example / helper text (입력 아래 예시 문구)
> - CTA 버튼 label
> - 입력 전 화면 안내 문구 (있을 경우)

| 잡 | 기대 입력 유형 | 현재 placeholder | 현재 예시/helper | 이 기본값이 유도하는 잡 | 기능 구경형 vs 잡 수행형 | first value 경로 | 잡 불일치 시 위험 |
|----|--------------|-----------------|-----------------|---------------------|---------------------|----------------|----------------|
| **J1 기록형** | 구체적 행동 기록 ("어려운 사람 도왔다") | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | `deed_saved`:183 | 추상적 기본값이면 AI 판정만 받고 저장 안 함 |
| **J2 누적형** | 반복 가능한 행동 ("매일 아침 스트레칭") | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | `deed_saved`:183 | 일회성 예시면 J1 유도, 누적 동기 부재 |
| **J3 AI 호기심형** | AI 판정이 흥미로운 애매한 행동 ("오늘 좀 친절했나?") | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | `deed_judged`:106 | 명확한 기본값이면 J1 유도, J3 본체 약함 |
| **J4 회고형** | 과거 행동 회고 ("지난 주 했던 일") | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | [CODE_CHECK] | `deed_saved`:183 | 현재형 기본값이면 J1 유도, 회고 맥락 부재 |

### §4-1 이미 알려진 컨텍스트 (선행 문서 기반)

- 입력 표면은 이미 얇음: 사진1 + 선택메모(≤120자) + 1탭 (marketing-21)
- J3 앞단 AI 약속이 `/add` 이전 홈 화면에서 사실상 부재 (marketing-19, marketing-16 three-screen §3-A)
- output strength 정점은 저장(E)이 아니라 결과 카드(D, `deed_judged`) (marketing-21)
- J3에 저장 유도 범퍼를 무조건 붙이면 J3 첫 가치 흐름 방해 (marketing-31)

---

## §5 "기능 구경형" vs "잡 수행형" 분류 기준

### 기능 구경형 (Feature-Exploring Default)

특징:
- AI가 어떻게 반응하는지 테스트/탐색하는 성격의 문구
- "뭐든 입력해보세요", "AI에게 판정받아보세요", "한번 써보세요" 류
- 사용자가 자신의 덕행 맥락을 연결하기 전에 AI를 먼저 시험
- 결과: `deed_judged` 후 저장 없이 종결 가능성 높음
- 유도 잡: J3 경로 강하게 유발. J1/J2/J4에는 잡 불일치
- Retention 예측력: 낮음 (호기심 충족 후 이탈 가능)

### 잡 수행형 (Job-Performing Default)

특징:
- 사용자가 원래 하려던 잡을 수행하게 유도하는 문구
- "오늘 선하게 행동한 순간을 기록하세요", "덕행을 남겨두세요" 류
- 사용자의 실제 덕행 맥락과 연결
- 결과: 잡별 first value(`deed_saved` or `deed_judged`) 도달 가능성 높음
- 유도 잡: 잡 명시 정도에 따라 J1/J2/J3/J4 중 특정 잡 호출
- Retention 예측력: 높음 (잡을 완수한 사용자는 돌아옴)

### 혼합형 기본값

- 현재 기본값이 양쪽 성격을 동시에 가질 수 있음
- "오늘 어떤 덕행을 했나요? AI가 판정합니다" = J1/J3 중립
- 이 경우 사용자 트래픽 분류 후 어느 잡 사용자가 더 많은지 관찰 필요

---

## §6 첫 세션 activation 영향 분류표

기본값 유형과 예상 activation 흐름:

| 기본값 유형 | 예상 이벤트 흐름 | first value 도달 확률 | 손기록 관찰 포인트 |
|-----------|----------------|---------------------|------------------|
| 기능 구경형 | `add_flow_started`:72 → `deed_judged`:106 (저장 없이 종결) | J3에서는 높음. J1/J2/J4에서는 낮음 | deed_judged 후 세션 종결 빈도 |
| 잡 수행형 (J1/J2/J4) | `add_flow_started`:72 → `deed_judged`:106 → `deed_saved`:183 | J1/J2/J4에서 높음 | deed_saved 도달 빈도 |
| 잡 수행형 (J3) | `add_flow_started`:72 → `deed_judged`:106 [→ `deed_rerolled`:149] | J3에서 높음 | deed_judged 후 표정/반응 (손기록) |
| 잡 불일치 | `add_flow_started`:72 → `add_flow_abandoned`:78 (미입력 이탈) | 낮음 | 입력 시작 후 중단 빈도 |

---

## §7 prelaunch 감사 금지선

- **코드 변경 없음**: 이 문서는 내부 감사표이며 placeholder/CTA 텍스트를 직접 변경하지 않는다
- **신규 이벤트/속성 0**: 기존 6 발화 이벤트만 인용. 신규 이벤트·속성·계측·대시보드·세션리플레이 추가 없음
- **공개 카피 변경 없음**: 기본값 개선 제안은 proposal-only. 배포·외부 발송 없음
- **비용 없음**: 신규 인프라·외부 서비스·권한 변경 없음
- **단정 금지**:
  - 한 명 사용자의 첫 입력으로 "기본값이 잡 불일치다"고 단정하지 않는다
  - `deed_judged` 후 `deed_saved` 없음을 무조건 이탈로 읽지 않는다 (J3 정상 종료)
  - synthetic/mock 입력 테스트 결과를 사람 사용자 첫 입력 증거에 섞지 않는다
  - 기본값 변경이 즉시 activation rate를 높인다고 가정하지 않는다
  - 소표본에서 "잡 수행형 기본값이 더 낫다"고 확정하지 않는다

---

## §8 선행 문서 계승 확인

| 선행 문서 | 계승한 내용 | 충돌 |
|----------|-----------|------|
| `first-session-jtbd-matrix.md` (m06) | J1~J4 정의, first value 매핑 (J1/J2/J4=deed_saved, J3=deed_judged) | 없음 |
| `add-input-output-balance-audit.md` (m21) | output strength 정점 = deed_judged, 입력 표면은 이미 얇음, J3 저장 전 정상 종료 | 없음 |
| `first-session-friction-observation-protocol.md` (m17) | F7 = J3 앞단 끊김, 마찰 관찰 방법 | 없음 |
| `product-body-vs-bumper-boundary-table.md` (m31) | J3는 결과 카드가 본체, 저장 유도 범퍼가 J3 방해 | 없음 |
| `onboarding-metrics-reading-table.md` (m23) | J3: deed_judged-deed_saved 갭 = 정상 종료. J1/J2/J4: 저장 전 이탈 후보 | 없음 |
| `home-screen-fae-audit.md` (m19) | J3 앞단 AI 약속이 /add 이전 홈에서 부재 | 없음 |
| `first-60-second-value-observation-script.md` (m20) | 60초 안에 first value에 닿는지 기본값이 영향 | 없음 |

재정의: 없음. 기존 J1~J4 first-value 매핑 그대로.

---

## §9 검증 게이트 (local 실행 시 확인)

- [ ] 코드 diff 0 (문서 파일만 신규, 코드 변경 없음)
- [ ] 신규 이벤트/속성 0
- [ ] conflict marker 0
- [ ] source note 경로 (`source/external-links/marketing/2026-06-01-agent-default-prompts-retention.md`) 인용
- [ ] first value 매핑 명시 (J1/J2/J4=`deed_saved`:183, J3=`deed_judged`:106)
- [ ] §4 심장표 [CODE_CHECK] 칸이 실제 코드 값으로 채워짐
- [ ] 기존 이벤트 앵커 drift 없음 (72/106/149/167/183/199 현행 일치)
- [ ] HEAD == origin/master (virtue-rebirth-app)
