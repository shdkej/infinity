# Virtue 웹/iOS 활성화 이벤트 패리티 브리프

> cloud-draft: 2026-05-24. 로컬 코드 grep 검증 필요.
> 최종 산출물 경로: apps/web/docs/ios-activation-event-parity-brief.md (virtue-rebirth-app)
> 권한 경계: 문서 작성만. 코드·PostHog·대시보드·배포 변경 0.

## 목적

Virtue는 pre-launch 단계로, 첫 10~20명 관찰 시 웹과 iOS의 활성화 이벤트가 어긋나면 "활성화 실패"와 "플랫폼 계측 불일치"를 구분하지 못해 오판이 생긴다. 이 문서는:

- 웹과 iOS 이벤트의 발화 위치 및 속성 차이를 명시하고
- J1~J4 잡별 활성화 후보 묶음을 플랫폼 패리티 기준으로 정의하며
- prelaunch 해석 금지선과 출시 후 첫 검증 게이트를 한 곳에 정리한다.

---

## 1. 이벤트 발화 위치 대조표

> ⚠️ 아래 표는 Inbox 메모 및 선행 마케팅 문서 기반 초안.
> 로컬에서 `rg 'posthog.capture|Analytics.capture' apps/web/src apps/ios/Sources -S` 실행 후 대조 필수.

| 이벤트 | 웹 | iOS | 설명 | 패리티 |
|--------|:--:|:---:|------|:------:|
| `add_flow_started` | ✅ | ❌ | 덕행 추가 플로우 진입 | 웹 전용 |
| `add_flow_abandoned` | ✅ | ❌ | 덕행 추가 플로우 이탈(중간 포기) | 웹 전용 |
| `deed_judge_attempted` | ❌ | ✅ | AI 채점 버튼 탭(채점 요청 직전) | iOS 전용 |
| `deed_judged` | ✅ | ✅ | AI 채점 완료(결과 수신) | **공통** |
| `deed_saved` | ✅ | ✅ | 덕행 저장/누적 완료 | **공통** |
| `level_up_viewed` | ✅ | ❌ | 레벨업 화면 조회 | 웹 전용 |

**공통 이벤트**: `deed_judged`, `deed_saved` (2종)  
**웹 전용**: `add_flow_started`, `add_flow_abandoned`, `level_up_viewed` (3종)  
**iOS 전용**: `deed_judge_attempted` (1종)

### 1-1. 속성 차이 (로컬 grep 검증 필요)

| 속성 | 웹 예상 | iOS 예상 | 비고 |
|------|---------|---------|------|
| `deed_judged` 점수/결과 필드 | 미확인 | 미확인 | 필드명·타입 플랫폼 간 일치 여부 확인 |
| `deed_saved` 잡 분류 속성 | 미확인 | 미확인 | J1~J4 구분용 속성 존재 여부 확인 |
| `add_flow_started.source` | 웹 전용 | — | 플로우 진입 경로 |
| `deed_judge_attempted.deed_id` | — | iOS 전용 | 채점 대상 식별자 |

> 로컬 grep 후 실제 속성명·타입·존재 여부로 이 표를 업데이트할 것.

---

## 2. J1~J4 잡별 활성화 후보 묶음

PostHog 권장: 단일 이벤트보다 3~5개 이벤트 묶음 + 장기 리텐션 검증.  
Virtue prelaunch 단계에서는 **묶음 정의만** 하고 전환율 판정은 금지.

### J1 기록형 — 오늘 한 일을 기록하고 싶다

| 단계 | 웹 | iOS | 패리티 |
|------|----|----|--------|
| 의도 포착 | `add_flow_started` | ❌ 없음 | 웹만 관찰 가능 |
| aha moment | `deed_saved` | `deed_saved` | ✅ 공통 |
| 보조 신호 | `deed_judged` | `deed_judged` | ✅ 공통 |
| 누적 확인 | `level_up_viewed` | ❌ 없음 | 웹만 관찰 가능 |

**J1 패리티 묶음** (플랫폼 공통 최소): `deed_judged` + `deed_saved`  
**웹 추가 신호**: `add_flow_started` (의도 포착), `level_up_viewed` (누적 시각화 도달)

### J2 누적형 — 덕행이 쌓이는 것을 보고 싶다

| 단계 | 웹 | iOS | 패리티 |
|------|----|----|--------|
| 반복 저장 | `deed_saved` × 2+ | `deed_saved` × 2+ | ✅ 공통 |
| 누적 시각화 | `level_up_viewed` | ❌ 없음 | 웹만 관찰 가능 |
| 채점 결과 | `deed_judged` | `deed_judged` | ✅ 공통 |

**J2 패리티 묶음**: `deed_saved` × 2+ (distinct session 기준) + `deed_judged`  
**웹 추가 신호**: `level_up_viewed` (J2의 핵심 aha가 웹에서 더 직접 관찰 가능)

### J3 AI 호기심형 — AI가 내 덕행을 어떻게 평가하는지 궁금하다

| 단계 | 웹 | iOS | 패리티 |
|------|----|----|--------|
| 채점 의도 | `add_flow_started` | `deed_judge_attempted` | 각 플랫폼 고유 신호 |
| aha moment | `deed_judged` | `deed_judged` | ✅ 공통 핵심 |
| 저장 여부 | `deed_saved` | `deed_saved` | ✅ 공통 (선택적) |

**J3 패리티 묶음**: `deed_judged` (J3의 aha는 채점 결과 수신 자체 — `deed_saved` 없이도 성립)  
**iOS 추가 신호**: `deed_judge_attempted`→`deed_judged` funnel (시도 대비 완료율, 웹에서는 분모 불명)  
**주의**: J3는 `deed_saved` 없이 `deed_judged`만 발생할 수 있음 — 미저장을 이탈로 단정 금지

### J4 회고형 — 지난 덕행을 돌아보고 싶다

| 단계 | 웹 | iOS | 패리티 |
|------|----|----|--------|
| 반복 저장 | `deed_saved` × 2+ | `deed_saved` × 2+ | ✅ 공통 |
| 회고 트리거 | `level_up_viewed` | ❌ 없음 | 웹만 관찰 가능 |

**J4 패리티 묶음**: `deed_saved` × 2+  
**웹 추가 신호**: `level_up_viewed` (회고형 aha 직접 관찰)  
**주의**: J2와 J4는 `deed_saved` 반복이라는 공통 신호를 공유 — 사용자 인터뷰 없이 PostHog만으로 잡 분리 불가

---

## 3. Prelaunch 해석 금지선

| 금지 해석 | 이유 |
|----------|------|
| 웹 활성화율 vs iOS 활성화율 직접 비교 | 이벤트 비대칭 (3종 차이) — 분모 정의가 다름 |
| `add_flow_started` 기반 funnel 전환율 | iOS에 해당 이벤트 없어 플랫폼 간 분모 불일치 |
| `level_up_viewed` 기반 J2/J4 활성화율 | iOS에 이벤트 없음 |
| `deed_judge_attempted`→완료율 웹 적용 | 웹에 해당 이벤트 없음 |
| "활성화 달성" 판정 (40% 임계값 등) | 소표본 prelaunch — 관찰만, 판정 금지 |
| `deed_judged` − `deed_saved` 갭을 이탈로 단정 | J3에서는 채점 후 미저장이 정상 패턴 |
| J2 vs J4 사용자 비율 PostHog에서 계산 | 두 잡이 동일 이벤트 시퀀스 — 분리 불가 |

---

## 4. 출시 후 첫 검증 게이트

출시 후 PostHog에서 아래 순서로 확인한다.

```
1. 이벤트 수신 확인
   - deed_judged, deed_saved 웹/iOS 모두 수신 여부
   - add_flow_started, add_flow_abandoned, level_up_viewed 웹만 수신 여부
   - deed_judge_attempted iOS만 수신 여부

2. 속성 일관성 확인 (공통 이벤트)
   - deed_judged의 주요 속성명이 웹/iOS에서 동일한 키로 전달되는지
   - deed_saved의 주요 속성명 일치 여부

3. J1~J4 묶음 수동 관찰 (첫 10명)
   - 각 사용자의 이벤트 시퀀스를 직접 확인
   - 어느 패리티 묶음 도달 여부만 기록 (전환율 계산 금지)
   - 플랫폼별 이벤트 미수신 시 "계측 누락"과 "사용자 미도달" 분리 기록

4. 이 문서 작업 이후 변경 0건 확인
   - src/ 코드 변경 0건
   - iOS Sources 변경 0건
   - PostHog 설정 변경 0건
```

---

## 5. 로컬 검증 명령어

```bash
# 이벤트 발화 위치 전수 검색
rg 'posthog.capture|Analytics.capture' apps/web/src apps/ios/Sources -S

# 이벤트명 직접 검색 (속성 컨텍스트 포함)
rg 'deed_judged|deed_saved|deed_judge_attempted|add_flow_started|add_flow_abandoned|level_up_viewed' apps/web/src apps/ios/Sources -S

# 이 문서 작성 후 변경 파일 없는지 확인
git diff --name-only HEAD
git status --short
```

이 명령어 결과와 섹션 1 표가 일치하면 검증 게이트 PASS.

---

*이 문서는 Inbox 메모 + 선행 마케팅 문서(marketing-06~14) 기반 cloud draft.*  
*섹션 1 속성 표와 섹션 5 명령어 결과는 로컬 grep 후 업데이트 필요.*  
*코드·PostHog·대시보드·배포·외부발송·비용·시크릿·권한 변경 금지.*
