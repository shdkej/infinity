# Virtue 첫 결과 공유성 판독 기준

> prelaunch 첫 10~20명 관찰에서 AI 결과 카드를 보고 "공유하거나 추천하고 싶다"는 신호를
> 어떻게 읽을지를 정의한 내부 브리프.
> 신규 이벤트·계측·카피·코드·배포·외부 발송 변경 없음. 기존 6개 이벤트 관찰만.

## §0 이 문서가 필요한 이유

ProductLed의 AI 온보딩 렌즈는 60초 가치(time-to-value)와 낮은 입력 대비 강한 출력(low-input high-output)뿐 아니라 **"공유하거나 추천하고 싶은 첫 경험(shareworthy first result)"**을 activation의 핵심 신호로 본다.

Virtue는 `deed_judged`(106)와 `deed_saved`(183)라는 활동량 신호를 이미 갖고 있지만, 이것만으로는 아래 두 가지를 구분하지 못한다:

1. "사용자가 결과를 수용했다(acceptance)" — 저장했거나 긍정 반응을 보였다
2. "결과를 타인에게 전달하고 싶었다(shareworthy)" — 한 층 더 강한 인정 반응

이 문서는 prelaunch 손기록 관찰에서 공유성 신호를 식별하는 기준을 J1~J4 잡별로 정리한다.
특히 J3 저장 전 정상 종료가 shareworthy 부재인지 J3 first value 달성인지를 혼동하지 않도록 명시한다.

## §1 공유성(Shareworthy) 정의와 proxy 층

공유성은 사용자가 결과를 받고 **타인에게 전달하거나 추천하고 싶다는 인정 반응**이다.
활동량(AI가 실행됐다)과 다르고, 수용(사용자가 결과를 받아들였다)보다 한 층 더 강한 신호다.

| proxy 층 | 설명 | 대표 신호 |
|---|---|---|
| **Activity** | AI가 작동했다 | `deed_judged`(106) 발화 |
| **Acceptance** | 사용자가 결과를 수용했다 | `deed_saved`(183) 발화, 또는 J3에서 저장 없이 긍정 반응 |
| **Shareworthy** | 타인에게 전달하거나 추천하고 싶다 | 발화·행동 증거 (§2 표 참조) |

공유성은 §2의 행동 증거로만 판독하며, 이벤트 수로 추산하지 않는다.

## §2 J1~J4 × 첫 결과 공유성 관찰 기준 (심장 표)

| 잡 | 첫 가치 이벤트 | shareworthy 판단 기준 | 행동 증거 예시 | 기존 이벤트 매핑 | 오독 위험 |
|---|---|---|---|---|---|
| **J1** 기록형 | `deed_saved`(183) | 저장 후 결과 카드를 다시 확인하거나 오래 바라본다; "이 평가 맞다" 발화 | 카드 재열람, 저장 후 홈 복귀 지연, 소리 내어 읽기, 스크린샷 시도 | `deed_saved`→카드 응시, `deed_rerolled`(149) 후 저장 | `deed_saved` 1회를 공유 의도로 단정 금지 — 저장=기록 행위이지 추천 의도가 아닐 수 있다 |
| **J2** 누적형 | `deed_saved`(183) | 누적 진행(`level_up_viewed`)을 타인에게 보여주려는 반응 | `level_up_viewed`(199) 후 탭 전환(공유 앱 시도), 누적 화면 캡처, "이만큼 모았어" 발화 | `level_up_viewed`→공유 앱 전환, 반복 `deed_saved` 패턴 | `level_up_viewed` 1회만으로 공유 의향 확정 금지 — 누적 패턴이 여러 세션에 걸쳐 보일 때만 신호 |
| **J3** AI 호기심형 | `deed_judged`(106) (저장 전) | 결과 카드를 받고 "이 판정 맞아" 긍정 발화; 저장 없이 세션 종료해도 얼굴 표정·발화가 긍정적 | 결과 카드 응시 시간 증가, 긍정 감탄, 스크린샷 시도, `deed_rerolled` 없이 만족 표현 | `deed_judged`→반응 관찰, `deed_rerolled`(149) 여부 | **핵심**: `deed_judged` 후 `deed_saved` 없음을 shareworthy 실패로 읽지 말 것 — J3는 저장 전 정상 종료가 first value; judged-without-saved 갭을 이탈·비공유 단정 금지 |
| **J4** 회고형 | `deed_saved`(183) | 저장 후 오래된 카드를 다시 꺼내 보거나 "이거 다시 봐도 좋다" 발화; 타인에게 과거 덕행을 보여주려는 반응 | 오래된 저장 카드 반복 열람, 시간 흐름 확인 행동, "이런 거 남겨뒀네" 발화 | `deed_saved` 기록 재접근 패턴 | 회고 shareworthy는 첫 세션이 아닌 반복 세션(D7+)에서 주로 발생 — 초기 absence를 공유성 없음으로 읽지 않는다 |

## §3 공유성 proxy 유형 분류

| proxy 유형 | 설명 | Virtue 관찰 형태 |
|---|---|---|
| **Direct** | 스크린샷·공유 버튼·링크 복사 등 직접 공유 행동 | 현재 공유 버튼 없음 → 스크린샷 시도 행동 관찰만 가능 |
| **Verbal** | 긍정 발화·감탄·타인 소환 | "이거 맞아", "이거 봐봐", 소리 내어 읽기 |
| **Intensified Saving** | 저장 강화 — 재시도 후 저장, 결과 카드 오래 보기 | `deed_rerolled`(149)→`deed_saved`(183) 연속; 카드 응시 시간 길어짐 |
| **Return Intent** | "다음에도 하고 싶다" 또는 D7 자발 복귀 | D7 return 여부를 손기록 (기존 baseline 양식 재사용) |

## §4 prelaunch 관찰 방법

1. **신규 계측 없음.** 기존 6개 이벤트(`add_flow_started`·`deed_judged`·`deed_saved`·`level_up_viewed`·`deed_rerolled`·`deed_save_capped`) 발화 타이밍과 사용자 반응을 함께 손기록한다.
2. **잡 분류 먼저**: J3의 경우 "저장 없이 세션 종료"가 shareworthy 부재인지 first value 달성인지는 **잡을 먼저 분류한 뒤** 판독한다.
3. **D7 칸 추가**: 첫 세션이 아니라 D7 재방문 때 공유 시도가 나타날 수 있다. 기존 `first-week-activation-retention-bridge` 양식에 shareworthy 관찰 칸(공유 시도 여부, 발화 내용)을 손으로 추가한다. 새 표 불필요.
4. **관찰 기록 형식**: `[잡] [이벤트] [shareworthy proxy 유형] [관찰 내용]`
   - 예: `J3 deed_judged(106) Verbal "AI 판정이 맞네" 발화, 저장 없이 종료 → J3 정상 종료`
   - 예: `J1 deed_saved(183) Intensified Saving 카드를 3번 다시 열람, 저장 후 홈 이동 지연`

## §5 prelaunch 금지선

- `deed_saved` 횟수 또는 `deed_judged` 횟수로 **공유율·추천 의향·NPS** 추정 금지
- J3의 judged-without-saved 갭을 **공유성 실패**로 단정 금지 — J3 저장 전 정상 종료
- `deed_save_capped`(167) early-return을 **공유 욕구 좌절**로 읽지 않는다 — availability/friction 신호
- 1명 발화로 **공유성 높다/낮다** 결론 확정 금지
- synthetic/mock/self-test/메이커 세션 반응을 사람 공유성 신호에 혼입 금지
- 첫 10~20명 완료 이전에 **공유 기능 구현·카피 반영·외부 발송·배포** 결정 금지
- 활동량(`deed_judged`/`deed_saved` 발화 수)을 공유성 proxy로 **승격** 금지

## §6 기존 문서 연결 · 충돌 확인

| 선행 문서 | 연결 지점 | 충돌 여부 |
|---|---|---|
| `ai-outcome-proxy-dictionary.md` | Acceptance proxy 위에 Shareworthy를 추가 층으로 얹음 (proxy type 재정의 없음) | 없음 |
| `add-input-output-balance-audit.md` | output strength 정점 D 결과 카드(`deed_judged`) — 이 강도가 shareworthy 신호의 시작점 | 없음 |
| `first-60-second-value-observation-script.md` | 60초 시계 안 공유 반응 = 강력한 first-result 신호로 손기록 | 없음 |
| `first-session-friction-observation-protocol.md` | F7(AI 약속 공백)/F8(누적 payoff 공백) 해소가 shareworthy 예비조건 | 없음 |
| `first-real-user-baseline-template.md` | D7 shareworthy 관찰 칸을 기존 baseline 양식에 손 추가 (새 표 불필요) | 없음 |

first value 매핑 계승: J1/J2/J4=`deed_saved`(183), J3=`deed_judged`(106) — 재정의 0.

## §7 검증 게이트

- [ ] first value 매핑 재정의 없음 (J1/J2/J4=`deed_saved`, J3=`deed_judged`)
- [ ] 신규 이벤트·속성·코드·카피·계측·대시보드·세션리플레이·배포·외부발송·비용·시크릿·권한·개인정보 변경 없음
- [ ] 기존 6개 이벤트만 인용 (앵커 72/106/149/167/183/199)
- [ ] conflict marker 없음
- [ ] J3 judged-without-saved 갭 shareworthy 실패 단정 금지선 포함
- [ ] prelaunch 금지선 7항 포함
