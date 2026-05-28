# Virtue Human/Test/Agent 트래픽 판독 경계표

> prelaunch/low-signal 단계에서 PostHog `deed_judged`·`deed_saved`를 안전하게 해석하기 위한 트래픽 유형 분류 경계표.  
> 신규 이벤트·속성·코드 변경 0. 읽기·해석 금지선·검증 게이트만 문서화.

## 1. 이 문서의 목적

Virtue prelaunch(첫 10~20명)에서 PostHog에 쌓이는 이벤트는 단일 신호가 아니다. 같은 `deed_judged` 이벤트라도 발화 주체와 맥락에 따라 해석이 완전히 달라진다. 이 경계표는 **집계 activation 수치를 해석하기 전에 반드시 확인해야 할 판독 전처리 체크리스트**다.

선행 문서들(`onboarding-metrics-reading-table.md` §5, `first-real-user-baseline-template.md` §4)이 synthetic/test 제외를 권고했으나, 트래픽 유형별 경계를 이벤트 단위로 명시한 문서가 없었다. 본 문서가 그 공백을 채운다.

## 2. 5가지 트래픽 유형 정의

| 코드 | 이름 | 정의 | 식별 단서 |
|------|------|------|----------|
| **H** | human-real-use | 실제 사용 목적이 있는 외부 사용자의 자발적 행동 | J1~J4 중 하나로 분류 가능한 사용 맥락 존재 |
| **M** | maker-self-test | 개발자·메이커가 기능 확인 목적으로 직접 사용 | 특정 계정에서 짧은 간격 반복 발화, 빌드 직후 패턴 |
| **S** | synthetic-mock | 테스트 데이터·모의 입력·seed 데이터 | `641` 시드 ID, `MOCK` 폴백, localStorage 반복, 데모 seed |
| **P** | platform-difference | 웹 vs iOS 구조적 차이로 인한 이벤트 부재·속성 값 차이 | `platform=ios` super-property, iOS 미발화 이벤트 |
| **A** | future-agent-api | 미래 자동화 에이전트·API 호출·CI 봇 | 현재 prelaunch 미발생, 출시 후 API 연동 시 해당 |

## 3. 이벤트 × 트래픽 유형 경계표

| 이벤트 | H (human) | M (maker) | S (synthetic) | P (platform) | A (agent) | 해석 주의 |
|--------|-----------|-----------|---------------|--------------|-----------|----------|
| `add_flow_started` (:72) | ✅ 의도 진입 신호 | ⚠️ 기능 테스트 진입과 구분 어려움 | ❌ mock 폴백 시 미발화 가능 | ❌ iOS 미발화 | ⚠️ 미래 봇 자동 진입 가능 | M과 H를 동일 계정 반복 패턴으로 구분. iOS는 이 이벤트 없으므로 웹 전용 퍼널 입구로만 읽어야 함 |
| `deed_judged` (:106) | ✅ AI 채점 완료 (J3 first value) | ⚠️ 채점 결과 확인용 반복 테스트 가능 | ❌ `641` seed 판정은 S | ⚠️ iOS: 속성 7개 (웹: 9개) | ⚠️ API 자동화 채점 가능 | J3 저장 전 종료는 정상(이탈 아님). 641 seed·mock 폴백 판정은 집계 제외. iOS 속성 차이는 P로 기록 |
| `deed_save_capped` (:167) | ✅ 한도 도달, 의도된 early return | ⚠️ 한도 확인 테스트 가능 | ❌ seed 완료 시에도 발화 가능 | ❌ iOS 미발화 | ❌ API 호출 시 발화 가능 | availability≠value. early return이라 TTV 종료·재가치 집계 제외. iOS 미발화는 P |
| `deed_saved` (:183) | ✅ J1/J2/J4 first value | ⚠️ 저장 기능 확인용 반복 테스트 가능 | ❌ seed 저장은 S | ⚠️ iOS: 속성 3개 (웹: 12개) | ⚠️ 자동화 저장 가능 | 속성 수 웹/iOS 차이는 P. 동일 user_id 반복 저장(M) vs 새 flow 진입 후 저장(H) 구분 |
| `deed_rerolled` (:149) | ✅ 재시도 호기심·양면 신뢰 (최대 3회) | ⚠️ 재시도 기능 확인 테스트 가능 | ❌ seed 재시도는 S | ❌ iOS 미발화 | ❌ 봇 반복 가능 | 최대 3회 제한. iOS 미발화는 P. 동일 계정 3회 연속은 M 가능성 높음 |
| `level_up_viewed` (:199) | ✅ 누적 payoff 인지 (조건부 발화) | ⚠️ 레벨업 화면 확인 테스트 가능 | ❌ seed 레벨업은 S | ❌ iOS 미발화 | ❌ 봇 조건 충족 시 발화 가능 | 조건부 발화 — 누적 기준 미달이면 미발화. iOS 미발화는 P |

## 4. 해석 금지선

### 4.1 집계 전 제외 기준

| 제외 유형 | 식별 방법 | 처리 |
|-----------|-----------|------|
| S: `641` 데모 seed | user_id·deed_id에 `641` 포함 | PostHog 필터 후 집계 |
| S: `MOCK` 폴백 | 서버 응답에 MOCK 태그 | 필터 후 집계 |
| S: localStorage 반복 | 동일 기기·짧은 간격 반복 발화 | 메이커 기기 ID 별도 관리 |
| M: 메이커 자체 테스트 | 개발자 계정(이메일) 발화 | 개발자 계정 목록 관리·제외 |
| P: iOS 미발화 이벤트 | `platform=ios` super-property | iOS/웹 분리 집계 |

### 4.2 절대 금지 해석

1. **`deed_judged` 수치로 activation 단정 금지** — J3는 저장 없이 종료가 정상. J1/J2/J4에서만 `deed_saved`가 activation이다.
2. **`deed_judged`−`deed_saved` 갭을 이탈로 단정 금지** — J3 정상 종료 + S/M 트래픽 혼재 가능.
3. **iOS와 웹 통합 집계 전환율 비교 금지** — 발화 이벤트 수가 구조적으로 다름(iOS: add_flow_started/deed_rerolled/deed_save_capped/level_up_viewed 미발화).
4. **S/M 트래픽 제거 전 activation 비율 산출 금지** — prelaunch 소표본에서 S/M 1건이 전환율을 크게 왜곡.
5. **A (agent-api) 트래픽을 H (human) 신호로 계산 금지** — 현재 미발생이나, API 출시 후 자동화 호출이 섞이면 즉시 분리.
6. **단건 이벤트로 트래픽 유형 확정 금지** — M·S 여부는 패턴으로 판단, 단건으로 단정하지 않는다.

### 4.3 availability ≠ value

- `deed_save_capped`(:167): early return이라 저장 미발화 → TTV 종료·재가치 집계 제외
- 503·서버 지연: 채점 지연 ≠ 사용자 이탈 의사 — 가용성 차단 플래그로 별도 기록
- `level_up_viewed`(:199) 미발화: 누적 기준 미달이거나 iOS — payoff 없음과 다르다

## 5. 첫 번째 Verification Gate

prelaunch 첫 10~20명 수집 후 activation 수치를 해석하기 전에 아래를 순서대로 확인한다.

### Gate V1: 트래픽 분류 점검
```
□ S: PostHog에서 641·MOCK 발화 건수 확인 → 0이면 제외 불필요, >0이면 필터 적용
□ M: 개발자 계정 발화 건수 확인 → 제외 목록과 대조
□ P: iOS vs 웹 발화 분리 집계 완료 여부 확인
□ A: 현재 0 확인 후 기록 (미발생)
```

### Gate V2: 이벤트 해석 전 체크
```
□ deed_judged 수치: J3 first value용으로만 읽음 (J1/J2/J4 activation 아님)
□ deed_saved 수치: S/M 제거 후 H만 집계 확인
□ level_up_viewed: iOS 분리 후 웹 전용 조건부 발화로 해석
□ add_flow_started: iOS 부재로 웹 전용 퍼널 입구
```

### Gate V3: 표본 크기 확인
```
□ H 트래픽 N ≥ 3 이상이어야 비율 산출 가능 (1~2명은 정성 관찰만)
□ 단일 계정 반복 deed_saved ≥ 3회 → M 가능성 재확인
□ deed_rerolled 3회 연속 동일 계정 → M 가능성 재확인
```

## 6. 선행 문서 연결

| 선행 문서 | 연결 포인트 | 충돌 |
|-----------|-------------|------|
| `ios-activation-event-parity-brief.md` | P 유형 근거 (이벤트 부재·속성 차이 상세) | 없음 |
| `onboarding-metrics-reading-table.md` | S/M 제외 원칙 계승 (§5) | 없음 |
| `first-real-user-baseline-template.md` | H 트래픽 기록 행 템플릿 재사용 | 없음 |
| `ai-judgment-trust-calibration-audit.md` | J3 저장 전 정상 종료 원칙 계승 | 없음 |
| `add-input-output-balance-audit.md` | 코드 앵커(72/106/149/167/183/199) 현행 일치 | 없음 |

## 7. 제한 사항 (변경 금지)

- 신규 이벤트·속성 추가: **0**
- 코드·계측·대시보드·배포 변경: **0**
- 외부 발송·비용·개인정보 변경: **0**
- 기존 6개 이벤트 앵커(72/106/149/167/183/199) 재정의: **0**
- 기존 선행 문서의 J1~J4 first value 매핑 변경: **0** (J1/J2/J4=`deed_saved`, J3=`deed_judged` 저장 전 계승)
