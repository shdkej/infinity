# Virtue Recovery-over-Streak 리텐션 렌즈 — Cloud Draft

> **Internal draft only.** Public copy/feature 변경은 §8 proposal-only로 분리.
> Permission: L1 internal-doc only. 신규 이벤트·코드·카피·외부발송·비용·개인정보 변경 금지.
> Source: `knowledge-lab/source/external-links/marketing/2026-05-29-streak-flexibility-recovery-retention.md`
> 상태: Cloud prepare 완료. 로컬 Claude Code가 source note 읽고 §1 데이터 반영 후 최종 파일 작성.

---

## §1 렌즈 배경: Streak → Recovery 전환 논거

### 외부 연구 핵심 (source note에서 구체 수치 반영 필요)

Duolingo/Reforge/HabitBoard 선행 연구 공통 관찰:
- **Streak 순기능**: 매일 앱을 열게 만드는 단기 행동 동기
- **Streak 역기능**: 끊기면 shame pressure → 이탈 가속. 연속 streak 보유자가 끊기는 날 더 높은 이탈률
- **Streak 유연성(Freeze/Grace period) 효과**: 복구 가능성 인지 → D7/D30 리텐션 개선
- **HabitBoard 관찰**: habit loop는 streak length보다 **회복 속도**와 상관이 더 높을 수 있음

> 로컬 실행 시: source note에서 구체적 데이터 포인트와 인용 출처를 §1에 반영할 것.

### Virtue 적용 번역

Virtue의 덕행 기록은:
- 일일 의무가 아닌 **자발적 실천**이다
- streak reset이나 "오늘 안 했음" 강조는 shame pressure로 작동할 수 있다
- 첫 7일 재방문 루프(`seven-day-deed-loop.md`)를 "연속일 보호"가 아닌 **"빠진 뒤 회복 가능성"**으로 읽는 것이 J1/J2/J4 `deed_saved`와 J3 `deed_judged` 혼선을 줄인다

> **Prelaunch 제약**: 이 렌즈는 관찰 도구다. 신규 계측·이벤트·코드·카피 변경 없이 기존 이벤트로만 읽는다.

---

## §2 핵심 표: J1-J4 × Recovery-over-Streak 4시나리오

> First value 매핑 계승 (재정의 0):
> - J1/J2/J4: `deed_saved`(:183) — 저장 완료가 first value
> - J3: `deed_judged`(:106) — AI 판정 완료가 first value (저장 전 정상 종료 가능)

| 잡 | 유형 | skip 해석 | recovery 신호 | monthly completion 의미 | comeback session 패턴 |
|----|------|-----------|---------------|------------------------|----------------------|
| **J1** | 기록형 | `deed_saved` 없는 날 = 기록 공백. shame 금지; 기회로 읽는다 | 공백 후 첫 `deed_saved` = recovery 시작 | 해당 월 `deed_saved` 있는 날 수 (밀도 관찰, % 금지) | gap ≥ 3일 후 `/add` 진입 → `deed_saved` 완료 |
| **J2** | 누적형 | 하루 skip = 누적 level 손실 없음. level 보존이 복귀 동기가 될 수 있다 | 공백 후 `deed_saved` + `level_up_viewed`(:199) 재확인 | 월 누적 `deed_saved` 수 → level 진행 속도 가늠 | gap 후 복귀 시 level 여전히 존재 확인이 comeback 신호 |
| **J3** | AI 호기심형 | `deed_judged` 없는 날 = AI 판정 기회 skip. **J3 정상 종료(deed_judged 후 저장 안 함)와 구별 필수** | 공백 후 `/add` 재진입 → `deed_judged` = AI 호기심 재점화 | 월 `deed_judged` 세션 수 (저장 여부 무관한 참여 밀도) | gap 후 새 덕행으로 `deed_judged` 받는 것이 comeback 신호 |
| **J4** | 회고형 | skip이 아닌 사후 기록 가능. 과거 덕행을 회고하는 것이 J4 정상 흐름 | `deed_saved` (회고 포함) = recovery의 다른 이름 | 월 회고 기록 완성도 (밀도보다 의미 정성 관찰) | gap 후 복귀 → 밀린 기간 회고 deed_saved = comeback |

---

## §3 이벤트 근거 (기존 6개만, 신규 0)

| 이벤트 | 코드 위치 | Recovery 렌즈 역할 |
|--------|-----------|-------------------|
| `add_flow_started` | :72 | /add 진입 = recovery 시도의 첫 신호 |
| `deed_judged` | :106 | J3 comeback 신호; skip vs 정상종료 구별 기준점 |
| `deed_saved` | :183 | J1/J2/J4 recovery/first value; 공백 후 재발화 = recovery |
| `level_up_viewed` | :199 | J2 comeback 동기 (level 보존 인지) |
| `deed_rerolled` | :149 | recovery 시도 중 재시도 (최대 3회) |
| `deed_save_capped` | :167 | early return; recovery 시도가 availability 제한으로 끊길 수 있음 |

---

## §4 Skip vs. 정상 종료 구별

J3 전용 주의사항:

| 상황 | 이벤트 패턴 | 해석 |
|------|------------|------|
| J3 정상 종료 | `deed_judged` 있음 + `deed_saved` 없음 | 이탈 아님, J3 잡 충족 자연 종료 |
| J3 진행 중 이탈 | `add_flow_started` 있음 + `deed_judged` 없음 | 이탈 후보 또는 availability block |
| J3 skip | 해당 날 모든 이벤트 없음 | 해당 잡 skip (recovery 관찰 대상) |
| J1/J2/J4 이탈 후보 | `deed_judged` 있음 + `deed_saved` 없음 | J3와 반대 부호: 저장 전 이탈 |

> `deed_judged`(:106)는 항상 `deed_saved`(:183)보다 먼저 발화 → 갭 식별 가능

---

## §5 Monthly Completion 밀도 렌즈

Monthly completion을 "몇 일 연속"이 아닌 **습관 밀도**로 읽는다:

| 밀도 | 월 deed_saved 있는 날 | Recovery 렌즈 해석 |
|------|---------------------|-------------------|
| 탐색기 | 1-5일 | 실험적 참여. streak 관점 "실패" → recovery 관점 "관심 존재" |
| 형성기 | 6-15일 | 습관 형성 중. J2 level 진행 확인 구간 |
| 정착기 | 16일+ | 습관 정착 신호. J3는 deed_judged 빈도로 별도 측정 |

> prelaunch 제약: 밀도는 정성 관찰 기준. % 계산·외부 벤치마크 비교 금지.

---

## §6 Comeback Session 정의 및 관찰 포인트

Gap 기준 (첫 10-20명 관찰용, 계측 변경 없음):

| Gap 유형 | 기준 | 연계 선행 문서 |
|----------|------|--------------|
| Short gap | 2-3일 공백 후 복귀 | `seven-day-deed-loop.md`: D1/D3 리듬 확인 |
| Medium gap | 4-7일 공백 후 복귀 | `first-week-activation-retention-bridge.md`: 첫 주 연결 |
| Long gap | 8일+ 공백 후 복귀 | streak reset 아닌 "돌아온 것"으로 관찰 |

Comeback 시 관찰 포인트:
1. 복귀 후 첫 이벤트: `add_flow_started`? `deed_saved`? (직접 기록?)
2. same-job으로 복귀했나, 다른 잡으로 전환했나?
3. J2의 경우: level 보존을 인지했나 (`level_up_viewed` 유무)?

---

## §7 선행 3문서 충돌 확인

| 선행 문서 | 본 문서와의 관계 | 충돌 |
|-----------|----------------|------|
| `seven-day-deed-loop.md` | D1/D3/D7 루프 정의. 본 문서의 Short/Medium gap comeback과 연계 | 없음. 루프를 recovery 렌즈로 보완 |
| `first-week-activation-retention-bridge.md` | J1-J4 × first value→7일 second value 연결. 본 문서는 그 이후 복귀 경우 추가 | 없음. 연속 보완. first value 매핑 계승 |
| `retention-predictive-activation-brief.md` | depth signal(반복 deed_saved, level_up_viewed, D7 재가치). 본 문서의 monthly/comeback이 depth 신호와 연계 | 없음. first value 매핑 계승. % 금지선 동일 |

**검증 게이트 (로컬 실행 시 확인):**
- conflict marker: **0** (`<<<<<<<` 없음)
- 신규 이벤트명: **0** (whitelist: add_flow_started/deed_judged/deed_saved/level_up_viewed/deed_rerolled/deed_save_capped만)
- 코드 diff: **0** (apps/web/docs/ 외 파일 변경 없음)
- first value 매핑 변경: **0** (J1/J2/J4=deed_saved:183, J3=deed_judged:106)

---

## §8 Proposal-Only (공개 카피/기능 변경 후보 — 미반영)

> 아래는 제안이다. 코드·카피·이벤트·배포·외부발송·비용·시크릿·권한 변경은 이 문서에서 발생하지 않는다.

| 번호 | 제안 | 이유 | 승인 수준 |
|------|------|------|----------|
| P1 | gap ≥ 3일 후 첫 /add 진입 시 "돌아왔네요" 카피 (shame-free tone) | Short gap comeback을 recovery 축하로 읽는 UX | L2: 코드+카피 변경 |
| P2 | 월 달력에 deed_saved 있는 날만 표시, 빈 날은 "기회"로 읽는 시각화 | streak 시각화 대신 밀도 시각화로 shame pressure 제거 | L2: UI 코드 변경 |
| P3 | recovery achievement: 3일 gap 후 comeback deed_saved에 별도 신호 | deed_rerolled 유사 패턴. comeback 동기 강화 | L3: 신규 이벤트 필요, 사용자 명시 승인 |

---

## §9 Prelaunch 금지선

- recovery % 계산 금지 (표본 10-20명 prelaunch)
- gap 길이로 retention 실패 단정 금지
- J3 judged-without-saved를 streak break로 분류 금지 (J3 정상 종료)
- monthly completion을 외부 벤치마크와 비교 금지
- 신규 이벤트·속성·코드·카피·계측·대시보드·외부발송·비용·시크릿·권한·개인정보 변경 금지
- 한 명 데이터로 comeback pattern 확정 금지
- `deed_save_capped`(:167) early return을 recovery 실패로 단정 금지 (availability 제한)
- availability≠value: 앱 오류·지연으로 인한 이벤트 미발화는 recovery 분석에서 제외
