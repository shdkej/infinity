# Virtue 트래픽 유형 판독 경계표 — 초안

**Human Real-use / Maker Self-test / Synthetic-mock / Platform-difference / Future Agent-API**

> **적용 범위**: prelaunch/low-signal 단계, 첫 10~20명 실사용자 기간
> **대상 이벤트**: `add_flow_started` · `deed_judged` · `deed_saved` · `level_up_viewed` · `deed_rerolled` · `deed_save_capped`
> **변경 범위**: 신규 이벤트·속성·코드·계측·대시보드·배포·외부발송·비용·개인정보 변경 0

---

## 1. 목적

prelaunch 단계의 활성화 집계(`deed_judged`, `deed_saved`)에는 여러 성격의 트래픽이 섞인다. 이를 구별하지 않으면:

- 메이커 자가 테스트를 제품 수요로 오인한다
- 합성·목업 이벤트가 첫 baseline을 오염시킨다
- iOS와 웹의 속성 불일치를 무시하고 통합 집계한다
- 미래 에이전트/API 호출이 사용자 행동으로 기록된다

이 문서는 **집계 전 유형을 판독하는 경계표**다. 신규 계측을 설치하지 않고 기존 속성과 맥락으로만 판별한다.

---

## 2. 트래픽 유형 정의

| 코드명 | 유형 | 정의 |
|--------|------|------|
| `human-real` | 실사용자 | 제품을 자신의 필요로 사용하는 실제 사용자. 알려진 테스트 신호 없음 |
| `maker-test` | 메이커 자가 테스트 | 제작자·팀이 기능 확인을 위해 사용하는 이벤트. 알려진 계정 또는 비정형 반복 패턴 |
| `synthetic-mock` | 합성/목업 | 자동 시드·데모(641)·localStorage 반복·CI 환경에서 발화된 이벤트 |
| `platform-diff` | 플랫폼 차이 | iOS/웹 이벤트 속성 불일치로 인한 집계 왜곡 (미발화 이벤트, 속성 수 차이) |
| `future-agent` | 미래 에이전트/API | Claude Code 등 API 호출로 생성될 자동화 이벤트. 현재 prelaunch에서는 가능성 낮음 |

---

## 3. 핵심 표: 이벤트 × 트래픽 유형 판독 경계표

| 이벤트 | 코드 앵커 | human-real | maker-test | synthetic-mock | platform-diff | future-agent |
|--------|----------|------------|------------|----------------|---------------|--------------|
| `add_flow_started` | :72 | 진입 의도 신호 (낮은 예측력, vanity) | 단시간 반복 진입은 테스트 의심 | 641 데모시드 진입 → 제외 | **iOS 미발화** → 웹 단독 집계 시 분모 왜곡 주의 | 자동 진입 속도 패턴으로 추후 구별 |
| `deed_judged` | :106 | J3 잡 충족 또는 중간 단계 | 결과 무관 반복이면 테스트 의심 | `MOCK` 속성 또는 641 → 제외 | 웹 9속성/iOS 7속성 차이 — 비교 시 목록 통일 | 비인간적 속도(< 1초 flow 완료)로 추후 구별 |
| `deed_saved` | :183 | J1·J2·J4 first value, J3 선택적 저장 | 알려진 계정 수기 제외 | 641 시드 저장 → 제외 | 웹 12속성/iOS 3속성 — 통합 시 속성 정규화 필요 | 비인간적 저장 패턴으로 추후 배제 |
| `level_up_viewed` | :199 | 누적 payoff 인지 신호 (J2 depth) | 빠른 반복은 테스트 의심 | 합성 deed_saved 누적으로 인한 level_up → 제외 | iOS 발화 여부 미확인 — 웹 전용 해석 가능 여부 확인 필요 | 자동 뷰 패턴으로 추후 구별 |
| `deed_rerolled` | :149 | 호기심·양면 신뢰, 최대 3회 | 상한 없는 반복은 테스트 의심 | 목업에서 제한 없이 reroll 가능 → 제외 | **iOS 미발화** — 웹 전용 지표 | 자동 reroll 속도로 추후 구별 |
| `deed_save_capped` | :167 | 의도된 마찰, early return, 저장 미발화 | cap 도달 확인 반복이면 테스트 의심 | 합성에서 cap 반복 → 제외 | iOS 발화 여부 미확인 | cap 패턴이 자동화 구분 지점 |

---

## 4. 유형별 판독 가이드

### 4-1. 합성/목업 (synthetic-mock) — 집계 전 제외

집계에서 제외하되 **데이터를 삭제하지 않는다** (관찰용 보존):

| 제외 조건 | 판별 방법 |
|-----------|----------|
| `user_id == 641` | PostHog 필터 `user_id != 641` |
| 이벤트 속성에 `MOCK` 포함 | 속성 문자열 검색 |
| localStorage 기반 반복 | 동일 세션 내 비정형 반복 패턴 (수기 판단) |
| CI·테스트 환경 | 환경 속성 또는 테스트 계정 여부 |

> **기존 문서 정합**: `onboarding-metrics-reading-table.md §5 synthetic/test 제외` 기준을 계승한다.

### 4-2. 메이커 자가 테스트 (maker-test) — 수기 제외

| 제외 조건 | 판별 방법 |
|-----------|----------|
| 알려진 이메일/user_id | 수기 목록 대조 (prelaunch 단계 주기적 갱신) |
| 하루 내 동일 이벤트 10+ 발화 | 비정형 반복 플래그 (수기 판단) |
| 업무 시간 외 집중 반복 | 패턴 관찰 |

### 4-3. 플랫폼 차이 (platform-diff) — 분리 집계

| 이벤트 | 웹 속성 수 | iOS 속성 수 | iOS 미발화 |
|--------|-----------|------------|----------|
| `deed_saved` | 12 | 3 | — |
| `deed_judged` | 9 | 7 | — |
| `add_flow_started` | 발화 | — | ✓ |
| `deed_rerolled` | 발화 | — | ✓ |
| `deed_save_capped` | 발화 | 미확인 | ? |
| `level_up_viewed` | 발화 | 미확인 | ? |

> 웹/iOS 통합 집계 시 iOS 미발화 이벤트가 포함된 비율 계산은 분모 왜곡을 낳는다. 세부는 `ios-activation-event-parity-brief.md` 참조.

### 4-4. 미래 에이전트/API (future-agent) — 현재 예상 0건, 대비용

| 판별 신호 | 내용 |
|-----------|------|
| 비인간적 속도 | `add_flow_started` → `deed_judged` → `deed_saved` < 1초 완료 |
| user-agent 헤더 | 봇/에이전트 표식 |
| 서비스 계정 | 특정 API 키 또는 시스템 계정 |

---

## 5. 첫 검증 게이트 (First Verification Gate)

| 게이트 | 확인 항목 | 통과 기준 |
|--------|-----------|----------|
| G1 | 신규 이벤트·속성·코드 변경 없음 | diff = doc 1파일 |
| G2 | iOS parity / onboarding metrics / baseline / trust 문서와 충돌 없음 | 충돌 마커 0 |
| G3 | synthetic/mock 제외 기준이 `onboarding-metrics-reading-table.md §5`와 정합 | 기준 동일 확인 |
| G4 | J1~J4 first value 매핑 변경 없음 | `deed_saved`(J1/J2/J4), `deed_judged`(J3) 계승 |
| G5 | iOS 속성 수 현행 일치 | `ios-activation-event-parity-brief.md` 앵커와 일치 |

---

## 6. 해석 금지선

1. **단일 신호로 유형 확정 금지**: `user_id=641` 외에는 단 하나의 신호로 트래픽 유형을 확정하지 않는다. 복수 신호로 판단한다.
2. **실사용자 확정 금지**: "이건 실사용자"라고 확정하지 않는다. "알려진 테스트 신호 없음 → 실사용자 추정"만 허용한다.
3. **`deed_saved` 미발화를 J3 이탈로 단정 금지**: J3 잡에서 `deed_judged` 후 `deed_saved` 없는 종료는 정상 종료다.
4. **합성/플랫폼 차이 무시 후 집계 금지**: 첫 baseline은 반드시 유형 분리 후 집계한다.
5. **미래 에이전트 트래픽을 현재 baseline에 포함 금지**: API 호출이 발생하면 별도 집계한다.
6. **% 비율·PMF·리텐션 판정 금지**: 소표본에서 비율 계산은 금지한다. 유형 판독은 이진(포함/제외) 분류만.
7. **`deed_save_capped`(:167) 발화를 TTV 종료·재가치로 집계 금지**: early return은 저장 미발화다.

---

## 7. 관련 문서

- `onboarding-metrics-reading-table.md` — synthetic/test 제외 §5, J1~J4 TTV 매핑
- `ios-activation-event-parity-brief.md` — 플랫폼 속성 상세
- `ai-judgment-trust-calibration-audit.md` — 잡별 신뢰 보정
- `first-real-user-baseline-template.md` — 수기 제외 운영
- `first-session-jtbd-matrix.md` — J1~J4 정의

---

## 로컬 실행 프롬프트 (Claude Code용)

```
Infinity Intent: marketing-25 Virtue 트래픽 유형 판독 경계표
Mode: execute_local
Required workflow: workflow-master 우선 사용. 부재 시 4역할 렌즈(Planner/Developer/Marketer/Operator) 수동 합성.
Goal: 이 초안(artifacts/marketing-25/human-agent-traffic-boundary-draft.md)을 바탕으로
      virtue-rebirth-app/apps/web/docs/human-agent-traffic-boundary-table.md를 신규 작성한다.
Context:
  - source_note=/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-human-agent-onboarding-metrics.md
    먼저 읽고 초안과 비교·보완
  - 기존 docs: onboarding-metrics-reading-table.md / ios-activation-event-parity-brief.md /
    ai-judgment-trust-calibration-audit.md / first-real-user-baseline-template.md / first-session-jtbd-matrix.md
Allowed: L0/L1 actions only (doc 1파일 추가)
Forbidden: 신규 이벤트·속성·코드·계측·대시보드·배포·외부발송·비용·개인정보 변경
Verification:
  G1: diff = doc 1파일만
  G2: 충돌 마커 0, 기존 문서 충돌 0
  G3: onboarding-metrics-reading-table.md §5 synthetic/mock 제외 기준과 정합
  G4: J1~J4 first value 매핑 변경 없음 (deed_saved J1/J2/J4, deed_judged J3)
  G5: iOS 속성 수 현행 일치 확인
Report back to: reports/marketing-25/{timestamp}-local.html (결론 2축 양식, ARTIFACT_RULES.md 참조)
```
