# Virtue Launch-Ready PLG Signal Gate

- id: marketing-59
- date: 2026-06-14
- predecessor_intents: [marketing-55, marketing-56, marketing-57, marketing-58, marketing-60]
- permission: L1 docs-only
- jobs: [J1 업무관리, J2 생활루틴, J3 자기평가, J4 기록저장]

## 목적

Virtue prelaunch(첫 10명) 단계에서:
1. 지금 볼 신호
2. 나중으로 미룰 신호
3. launch 이후에 볼 신호

를 한 표로 정리하여, acquisition/activation/measurement-too-early 혼동을 방지한다.

## 신호 위계 표

| 신호 | 카테고리 | 타이밍 | Virtue 연결 | 관찰 방법 |
|------|---------|--------|------------|----------|
| 첫 deed_saved/deed_judged | First Win | **지금** | J1/J2/J4=saved, J3=judged | 수기 관찰 |
| 첫 세션에서 뭔가 완성했는가 | First Win | **지금** | deed 완료 여부 | 수기 체크 |
| time_to_first_value | First Win | **지금** | 가입→첫 deed까지 | 수기 기록 |
| value_unit_heard | First Win | **지금** | 사용자가 뭘 "쓸 만하다"고 했나 | 대화/피드백 |
| limit_trust_signal | First Win | **지금** | 플랜 제한에 어떻게 반응 | 수기 관찰 |
| 두 번째 방문 여부 | Activation | **지금** | D1-D7 내 재방문 | 수기 추적 |
| 같은 job 반복 성공 | Activation | **보류** | D7-D14 | 10명 이후 |
| 7일 retention | Retention | **보류** | D7 | 측정 도구 필요 |
| support_phrase_needed | UX 개선 | **보류** | 어떤 도움이 필요한가 | 10명 이후 |
| reproducibility_understanding | Activation | **보류** | 반복 사용 이해도 | 10명 이후 |
| plan_page_visit | PQL | **launch 이후** | 유료 플랜 페이지 | 계측 도구 필요 |
| limit_hit → upgrade | PQL | **launch 이후** | 한도 도달→결제 | Stripe/billing |
| viral_coefficient | Viral | **launch 이후** | 초대/공유 | 계측 도구 필요 |
| NPS | Satisfaction | **launch 이후** | 순추천지수 | 30일 이후 |
| expansion (multi-job) | Expansion | **launch 이후** | 여러 job type | 측정 도구 필요 |
| paid conversion rate | Revenue | **launch 이후** | 유료 전환율 | billing 연동 |

## First-10 수기 Review Gate

### 관찰표 (10명 × 신호)

| 사용자 | deed_saved/judged | 두번째방문 | value_unit_heard | limit_trust | 첫 불평/찬사 |
|--------|------------------|-----------|-----------------|-------------|-------------|
| U01 | □ | □ | | | |
| U02 | □ | □ | | | |
| U03 | □ | □ | | | |
| U04 | □ | □ | | | |
| U05 | □ | □ | | | |
| U06 | □ | □ | | | |
| U07 | □ | □ | | | |
| U08 | □ | □ | | | |
| U09 | □ | □ | | | |
| U10 | □ | □ | | | |

### Review Gate 판정 기준

| 결과 | 조건 | 다음 행동 |
|------|------|----------|
| Activation Pass | 7/10명 이상 deed 완료 | acquisition 집중 (더 많은 사람 불러오기) |
| Activation Warn | 5-6/10명 deed 완료 | onboarding 단계 검토 (시작 마찰 점검) |
| Activation Fail | 4/10명 이하 deed 완료 | product 수정 우선 (첫 deed까지 경로 개선) |
| Return Visit Gate | 5/10명 이상 재방문 | activation 개선 (습관 루프 형성 확인) |

### 선행 인텐트와의 충돌 방지

- **marketing-55**: count now/observe manually/do not judge yet 분류와 일치 — First Win/Activation = now, PQL+ = do not judge yet
- **marketing-56**: accepted_output/useful_result_time 컬럼이 deed_saved와 동일 맥락 → 통합 유지
- **marketing-57**: value_unit_heard/limit_trust_signal이 First Win 지금 볼 신호에 포함됨
- **marketing-58**: first successful output (deed_saved/deed_judged) = First Win 최상위 신호
- **marketing-60**: outcome-readable 판독 기준이 이 gate 판정 후 실행됨 (순서: signal gate → outcome docs)

## 금지선 (conflict markers = 0)

- 신규 이벤트 정의 없음
- tracking/privacy 변경 없음
- production code 변경 없음
- public copy 변경 없음
- deploy/external message/cost 없음
