# Virtue Recovery-over-Streak 리텐션 렌즈 — Cloud Prepare 초안

> **상태**: cloud prepare 단계 초안. 로컬 Claude Code가 source note를 읽어 보완 후 virtue-rebirth-app에 반영한다.
> **목표 경로**: `apps/web/docs/recovery-over-streak-retention-lens.md` (신규 1파일)
> **source note**: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-29-streak-flexibility-recovery-retention.md`

---

# Virtue Recovery-over-Streak 리텐션 렌즈

> **목적**: 연속일(streak) 압박·shame pressure 대신 "빠진 뒤 회복 가능성"으로 J1-J4 첫 7일 재방문 루프를 읽는 내부 렌즈.
> **대상**: 기획·마케팅 내부 사용 (public copy/feature 변경 금지, §7 proposal-only 참조).
> **선행 문서**: `seven-day-deed-loop.md` · `first-week-activation-retention-bridge.md` · `retention-predictive-activation-brief.md`

---

## 0. 왜 Recovery-over-Streak인가

**문제**: Duolingo·HabitBoard 등 streak 장치는 retention에 유효하지만, 강한 streak reset이나 shame pressure는 오히려 이탈을 촉진한다.

**Virtue 리스크**: 덕행 기록의 연속성 신호가 "연속일 깨짐 = 실패"로 읽히면 첫 7일 재방문 루프가 의도와 다르게 작동할 수 있다. `deed_saved` / `deed_judged` 이벤트는 streak 달성 도구가 아니라 잡별 고유 가치 확인 순간이다.

**렌즈 목적**: 이벤트 데이터를 streak 달성이 아닌 "오늘 복귀했는가, 빠졌다가 다시 올 수 있는가"로 읽는다.

---

## 1. 외부 사례: 연속성 장치의 양면

<!-- TODO: source note 읽어 Duolingo/Reforge/HabitBoard 구체 데이터 보완 -->

| 제품 | 연속성 장치 | 회복 장치 | 리텐션 영향 |
|------|-----------|---------|----------|
| Duolingo | streak counter | streak shield / freeze | 회복 가능성이 streak 포기를 막음; shame 설계 → 이탈 가속 |
| HabitBoard | daily ring / chain | flexible skip marking | strict chain 해제 후 재방문율 향상 사례 |
| Reforge (리서치) | — | habit recovery loop | 습관 회복 속도 > streak 길이 (장기 retention 예측력) |

**핵심 교훈**: 연속일 보호보다 "빠졌다가 돌아오는 경로의 마찰"이 장기 retention을 결정한다.

---

## 2. J1-J4 × Recovery-over-Streak 렌즈

first value 매핑 계승 — 재정의 0: J1·J2·J4 = `deed_saved` | J3 = `deed_judged` (저장 전)

| 잡 | first value event | 빠진 날 읽기 | skip 해석 | monthly completion 해석 | comeback session 읽기 |
|---|---|---|---|---|---|
| **J1 기록형** | `deed_saved` | 공백 = 기록 없음 (실패 아님; prelaunch 단정 금지) | 의도적 pause 가능 — 기록 의지 소멸인지 확인 필요 | 월간 총 `deed_saved` 수 > 연속일 (완성도보다 밀도) | `deed_saved` 재발화 = comeback 행동 증거 |
| **J2 누적형** | `deed_saved` | 누적 chain 끊김 위험 — `level_up_viewed` 발화 여부가 단서 | streak 중단보다 누적 payoff 신호 부재가 이탈 원인 가능 | `level_up_viewed` 조건부 발화 = 월간 경계 payoff 증거 | `deed_saved` + `level_up_viewed` 재발화 패턴 관찰 |
| **J3 AI 호기심형** | `deed_judged` (저장 선택) | skip = AI 판정 자극 미발생 (저장 여부 무관) | `deed_judged` 없음 = 호기심 미트리거; `deed_saved` 없음은 J3 정상 종료 가능 | `deed_judged` 월간 횟수 > `deed_saved` (J3 정상 패턴) | `deed_judged` 재발화 = comeback 행동 증거 |
| **J4 회고형** | `deed_saved` | 회고 공백 — 이탈인지 회고 시점 이동인지 불분명 | 주기가 일별이 아닐 수 있음 (배치 기록형) | `deed_saved` 월간 분포가 균등 vs 배치형인지 관찰 | 복수 `deed_saved` 짧은 시간 내 = comeback 배치 증거 |

---

## 3. Recovery 렌즈 읽기 원칙

1. **빠진 날 단정 금지**: `deed_saved` 공백 = "이탈"이 아니라 "공백"이다. 잡별 skip 해석을 먼저 확인한다.
2. **judged-saved 갭 이탈 단정 금지**: J3는 `deed_judged` 후 `deed_saved` 없이 세션 종료가 정상 완료다.
3. **comeback = 재발화**: 공백 후 `deed_saved` 또는 `deed_judged` 재발화가 comeback session의 행동 증거다.
4. **streak 압박이 아닌 복귀 마찰 측정**: "왜 빠졌는가"보다 "다시 오는 경로에서 무엇이 막히는가"를 관찰한다.
5. **prelaunch 소표본 제약**: comeback 비율·전환율·PMF 결론 도출 금지 (소표본 통계적 유의성 없음).

---

## 4. 첫 7일 재방문 루프와의 연결 (`seven-day-deed-loop.md` 계승)

> **역할 분리**: 이 문서는 recovery 렌즈만 추가한다. D1/D7 이벤트 정의·second value 정의는 `first-week-activation-retention-bridge.md` · `retention-predictive-activation-brief.md`에 위임한다.

| 루프 포인트 | recovery 렌즈 추가 읽기 |
|-----------|---------------------|
| D0 first value | 이후 skip 시 복귀 기준선 (잡별 `deed_saved`/`deed_judged`) |
| D1-D6 재방문 | 재발화 = comeback; 공백 = "아직 안 옴" (이탈 단정 금지) |
| D7 재방문 | 7일 내 comeback 경험 유무 > 연속 7일 달성 여부 |
| D7 이후 | comeback session 패턴 주기 관찰 (배치형 vs 일별형) |

---

## 5. 기존 이벤트만 (신규 이벤트명 0)

| 이벤트 | 코드 앵커 | recovery 렌즈 역할 |
|--------|---------|------------------|
| `add_flow_started` | :72 | comeback session 시작 의도 신호 |
| `deed_judged` | :106 | J3 comeback 증거; J1/J2/J4 comeback 중간 단계 |
| `deed_saved` | :183 | J1/J2/J4 comeback 확인 이벤트 |
| `level_up_viewed` | :199 | J2 누적 payoff 확인 = comeback 강화 신호 |
| `deed_rerolled` | :149 | comeback 후 재탐색 (재참여 지속 신호) |
| `deed_save_capped` | :167 | early return = `deed_saved` 미발화, comeback 판정 제외 |

---

## 6. 금지선 (Verification Gate)

- conflict marker 0
- 신규 이벤트명 0 (기존 6개 이외 인용 금지)
- 코드 diff 0 (순수 내부 문서)
- 기존 first value 매핑 유지: J1/J2/J4=`deed_saved`, J3=`deed_judged`
- streak reset/shame pressure 단정 금지
- 전환율·리텐션·PMF·% 산출 금지
- synthetic/mock 트래픽 포함 금지 (임시판정·641 데모시드·메이커 self-test 제외)
- 선행 3문서 충돌 금지: `seven-day-deed-loop.md`, `first-week-activation-retention-bridge.md`, `retention-predictive-activation-brief.md`

---

## 7. Proposal-only (승인 필요 후보)

> 아래는 내부 렌즈에서 파생된 제안이며, 적용 전 별도 승인 필요. 현재 코드·카피 변경 0.

- **streak 표시 유연화**: `/` 대시보드에서 연속일 강조 → "최근 활동" 표현으로 전환 (카피 변경, 승인 필요)
- **comeback 메시지**: 공백 후 복귀 시 "다시 왔네요" 계열 메시지 (신규 UX, 승인 필요)
- **monthly completion 경계 표시**: `level_up_viewed` 조건부 발화를 월간 완료 신호로 명시화 (기능 변경, 승인 필요)

---

*Infinity Heartbeat Agent cloud prepare 초안 — 2026-05-29T10:00Z*
*로컬 실행 전 source note 보완 필요: §1 외부 사례 구체 데이터, §2 잡별 관찰 세부 사항*
