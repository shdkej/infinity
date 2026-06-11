# Virtue task-completion 감사표

- intent: marketing-53
- based_on: MARKETING_LEARNINGS.md, marketing-52, marketing-51, marketing-49, marketing-44
- scope: docs-only / no public copy / no event / no tracking
- permission: L1 docs-only
- status: completed 2026-06-11T10:00Z

## Purpose

Virtue 첫 입력/결과 직후를 `사용자 의도 → AI가 수행한 작업 → 사용자가 선택한 다음 행동` 3축으로 읽는 손기록 감사표.

목적:
- `deed_judged` 과대평가 방지 (J1/J2/J4에서 deed_judged는 통과점, J3에서만 도착점)
- 신규 계측 없이 첫 10명 관찰 기준 선명화
- 잡별 first-value 행동 증거 보강

## 상속한 기준

| 기준 | 규칙 | 이 감사표에서 적용 |
|---|---|---|
| First Value Mapping | J1/J2/J4=`deed_saved`, J3=`deed_judged` | 잡별 task completion 판단 기준 |
| Post-Response Flow Reveals Value (m44) | 결과 직후 행동이 가치 전달 여부를 읽는 창 | 축3(다음 행동) 설계 근거 |
| Guided First-Value Is A Four-Stage Handoff (m51) | 4구간 handoff | 구간 분류 근거 |
| Session Value Is Read By Job (m42) | 잡별 first value 도달 여부 우선 | 잡별 감사표 분리 근거 |
| Prelaunch Decision Boundary (m08) | 작은 표본은 방향 재료 | 감사표 결과를 율로 환산 금지 |

## 이벤트 기준 (신규 없음, 기존 6개만)

| 이벤트 | 의미 | 잡별 역할 |
|---|---|---|
| `add_flow_started` | `/add` 흐름 진입 | 첫 입력 전 구간 시작 |
| `deed_judged` | AI 판정 결과 표시 | J3 first value (도착점) / J1·J2·J4 통과점 |
| `deed_saved` | 저장 완료 | J1/J2/J4 first value (도착점) |
| `deed_rerolled` | 재판정 요청 | 의도 관찰 보류 신호 |
| `deed_save_capped` | 저장 상한 도달 | 가용성/마찰 신호 (value 아님) |
| `level_up_viewed` | 레벨업 확인 | J2 두 번째 가치 신호 후보 |

---

## Task-Completion 감사표

### J1 — 기록 (Record)

**사용자 의도:** 오늘 한 일을 기록으로 남기고 싶다

| 구간 | AI 작업 | 사용자 다음 행동 | 손기록 |
|---|---|---|---|
| 첫 입력 전 | — | 메모/사진 입력 | □ 망설임 있음 □ 없음 |
| AI 대기 | 행동을 잡/덕 유형으로 분류, 점수·맥락 제시 | 결과 확인 | □ 기대한 결과 □ 예상 외 |
| 결과 직후 | — | `deed_saved` / `deed_rerolled` / 종료 | □ saved □ rerolled □ 종료 |
| task completion | `deed_saved` 발화 여부 | — | □ 완료 □ 미완료 |

**정상 완료:** 저장 후 홈 이동  
**보류:** 재판정 반복, 저장 없는 종료  
**마찰:** `deed_save_capped`, 503, `deed_judged` 발화 후 미저장 장시간 체류  
**미완료 성격:** B-LOST □ / B-MISMATCH □ / B-AVAIL □ / B-NORMAL □

---

### J2 — 누적 (Accumulation)

**사용자 의도:** 꾸준함이 쌓이는 흐름에 오늘을 추가하고 싶다

| 구간 | AI 작업 | 사용자 다음 행동 | 손기록 |
|---|---|---|---|
| 첫 입력 전 | — | 메모/사진 입력 | □ 망설임 있음 □ 없음 |
| AI 대기 | 누적 맥락에서 오늘 항목 분류·추가 | 결과 확인 | □ 기대한 결과 □ 예상 외 |
| 결과 직후 | — | `deed_saved` / `level_up_viewed` / 종료 | □ saved □ level_up □ 종료 |
| task completion | `deed_saved` 발화 여부 | — | □ 완료 □ 미완료 |

**정상 완료:** 저장 후 누적 카운트 확인  
**보류:** 저장 없는 종료 (누적 기대 충족 불확실)  
**마찰:** `deed_save_capped`  
**미완료 성격:** B-LOST □ / B-MISMATCH □ / B-AVAIL □ / B-NORMAL □

---

### J3 — AI 호기심 (AI Curiosity)

**사용자 의도:** AI가 내 행동을 어떻게 읽는지 확인하고 싶다

| 구간 | AI 작업 | 사용자 다음 행동 | 손기록 |
|---|---|---|---|
| 첫 입력 전 | — | 메모/사진 입력 | □ 망설임 있음 □ 없음 |
| AI 대기 | 행동 의미·패턴·관점을 AI 시각으로 제시 | 결과 읽기 | □ 기대한 결과 □ 예상 외 |
| 결과 직후 | — | 종료(정상) / `deed_saved`(선택) / `deed_rerolled` | □ judged+종료 □ judged+saved □ rerolled □ 미판정 |
| task completion | `deed_judged` 발화 여부 | — | □ 완료 □ 미완료 |

**정상 완료:** `deed_judged` 후 저장 없이 종료 (저장은 선택 범퍼)  
**보류:** 미판정 종료, `deed_rerolled` 반복  
**⚠️ J3 특이점:** `deed_judged` 후 무저장 종료는 이탈이 아니다. judged-saved 갭을 실패로 읽지 않는다.  
**미완료 성격:** B-LOST □ / B-MISMATCH □ / B-AVAIL □ / B-NORMAL □

---

### J4 — 회고 (Reflection)

**사용자 의도:** 이 행동이 내게 어떤 의미인지 AI 시각으로 보고 싶다

| 구간 | AI 작업 | 사용자 다음 행동 | 손기록 |
|---|---|---|---|
| 첫 입력 전 | — | 메모/사진 입력 | □ 망설임 있음 □ 없음 |
| AI 대기 | 행동의 회고적 가치·의미 해석 제시 | 결과 확인 | □ 기대한 결과 □ 예상 외 |
| 결과 직후 | — | `deed_saved` / `deed_rerolled` / 종료 | □ saved □ rerolled □ 종료 |
| task completion | `deed_saved` 발화 여부 | — | □ 완료 □ 미완료 |

**정상 완료:** 저장 후 홈 이동  
**보류:** 재판정 반복 (회고 결과가 기대에 못 미침)  
**마찰:** `deed_save_capped`, AI 결과 표시 실패  
**미완료 성격:** B-LOST □ / B-MISMATCH □ / B-AVAIL □ / B-NORMAL □

---

## deed_judged 과대평가 방지 체크

| 상황 | 올바른 읽기 | ❌ 잘못된 읽기 |
|---|---|---|
| J1/J2/J4에서 `deed_judged` 발화 후 미저장 종료 | 보류 후보 (first value 미도달) | ~~"AI 판정 받았으니 완료"~~ |
| J3에서 `deed_judged` 후 무저장 종료 | 정상 완료 (J3 first value = judged) | ~~"저장 안 했으니 이탈"~~ |
| 모든 잡 `deed_save_capped` | 가용성/마찰 신호 | ~~"더 원해서 막혔다 = upgrade 수요"~~ |
| J3 `deed_rerolled` | 의도 관찰 보류 | ~~"AI 결과 불신"~~ |
| J3 judged-saved 갭 | J3 정상 종료 패턴 | ~~"가치 전달 실패"~~ |

---

## 첫 10명 손기록 양식

세션별 기록:

```
관찰일: ___________   사용자 번호: #___

[추정 잡]  J1 □   J2 □   J3 □   J4 □   모름 □

[구간별 관찰]
  첫 입력 전: ___________________________________________________
  AI 대기 중: ___________________________________________________
  결과 직후 30초: ________________________________________________

[다음 행동]
  deed_saved □   deed_judged □   deed_rerolled □
  deed_save_capped □   종료(무저장) □

[자기화 신호]
  AI가 결정했다고 읽었나?  □ 그렇게 보였다  □ 아니다  □ 모름
  자기 행동의 연장으로 읽었나?  □ 그렇게 보였다  □ 아니다  □ 모름
  자기 말로 설명한 가치: ________________________________________

[task completion 판정]
  □ 완료 (first value 도달)
  □ 보류 — 성격: B-LOST □  B-MISMATCH □  B-AVAIL □  B-NORMAL □
  □ 마찰 (capped / 503 / 지연)
```

---

## 기존 문서와의 관계

| 문서 | 관계 | 충돌 |
|---|---|---|
| marketing-52 (prompt design audit) | 보완 — 첫 입력 표면 프롬프트 렌즈 | 없음 |
| marketing-51 (4-stage handoff) | 상위 프레임 — 4구간 중 결과 직후 집중 | 없음 |
| marketing-49 (post-result self-appropriation) | 병렬 — 동일 시점을 자기화 행동 렌즈로 | 없음 |
| marketing-47 (first-user learning loop) | 상위 프레임 — 첫 사용자 손기록 루프 | 없음 |

**conflict marker: 0건**

---

## 변경 없음 확인

| 항목 | 변경 |
|---|---|
| 신규 이벤트 | 0 |
| tracking/privacy | 0 |
| 공개 카피 | 0 |
| 배포 | 0 |
| 외부 발송 | 0 |
| 비용 | 0 |
| 권한 | 0 |

---

## MARKETING_LEARNINGS.md 승격 후보 (보류)

**Task-Completion Lens Reads Intent, Not Output Event**
- `deed_judged` 발화는 J3에서만 task completion 기준이고, J1/J2/J4에서는 저장 전 통과점이다.
- 후속 첫 10명 관찰로 보강 후 승격 여부 결정한다.
