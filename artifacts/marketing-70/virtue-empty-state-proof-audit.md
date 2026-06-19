# Virtue Empty-State Proof Audit
> marketing-70 | docs-only | prelaunch | 2026-06-19

Lens: 홈 `최근 덕행` 빈 상태의 seeded proof gap을 J1-J4별로 감사.
선행 문서: marketing-31 (Product Body vs Bumper), marketing-45 (Verb Frame), marketing-66 (J1-J4 Context Map), marketing-68 (Agent-Readable Surface Audit).

## 전제 (계승)

- **Product Body vs Bumper By Job** (marketing-31): 홈 feed는 J2에게는 본체(누적 payoff), J1에게는 범퍼(다음 행동 안내)
- **Decision-Delegation Risk Rides The Verb** (marketing-45): 버튼 `AI 채점`(판결) vs 헤더 `AI가 본 오늘`(관점) 불일치 기 확인 — proof 추가 전 정렬 선행 필요
- **Prelaunch Decision Boundary**: 코드 변경보다 docs-only 기준 고정이 우선

## 감사 범위

- 표면: 홈 `최근 덕행` 빈 상태 (empty state)
- 모드: read-only 분석 (컨텍스트 기반 추론)
- 제약: prelaunch L1 docs-only (production/code/deploy/tracking 변경 없음)

## 현재 Empty-State 구조 (컨텍스트 기반 추론)

- `/add` CTA만 존재
- 기록 후 어떤 카드가 쌓이는지 보여주는 proof preview 없음
- 기존 확인된 문제: 버튼 `AI 채점` vs 헤더 `AI가 본 오늘` 동사 프레임 불일치 (m45)

## Gap 분석 (기존 노트 대비)

| # | Gap | 선행 문서 | 비고 |
|---|-----|----------|------|
| G1 | 동사 프레임 감사(m45)는 있으나 empty-state proof preview 감사 없었음 | marketing-45 | 이번에 채움 |
| G2 | J1-J4 context_before_output(m66) 정의됐으나 job별 proof preview 필요도 매핑 없었음 | marketing-66 | 이번에 채움 |
| G3 | Agent-readable surface 감사(m68)는 있으나 human-facing empty-state proof surface 감사 없었음 | marketing-68 | 이번에 채움 |

## J1-J4 x Seeded Proof 감사표

### J1 — 기록형

- **방문자 의도**: 오늘 한 일을 AI 관점에서 보고 저장하고 싶다
- **first value**: deed_saved
- **홈 feed 역할**: 범퍼 (다음 행동 안내)
- **seeded proof 필요도**: 중상 — 단일 카드 예시가 payoff 상상에 도움
- **현재 empty-state**: CTA만, proof 없음
- **oops risk**: 예시 카드가 실제 내 데이터처럼 보임
- **안전 표시**: "예시 카드" 레이블 or 연한 배경 처리 필요
- **preview 후보**: 행동명 + AI가 본 짧은 관점 + 저장 표시 (단일 카드)
- **production 변경**: 코드 변경 필요 (approval-needed)

### J2 — 누적형 (최우선 gap)

- **방문자 의도**: 반복 기록이 쌓여 패턴/레벨이 어떻게 되는지 보고 싶다
- **first value**: deed_saved x 2 + level_up_viewed
- **홈 feed 역할**: 본체 (누적 payoff) — 가장 큰 gap job
- **seeded proof 필요도**: 높음 — 3-5개 카드 스택 + 레벨 뱃지 예시가 핵심
- **현재 empty-state**: CTA만, 누적 시각화 없음
- **oops risk**: 여러 예시 카드가 "이미 내가 기록한 것" 오해 가능
- **안전 표시**: "예시 흐름" 레이블 + 시각적 구분 (점선 테두리 등)
- **preview 후보**: 3-5개 카드 스택 + 레벨 뱃지 예시 (날짜 흐름 있으면 효과적)
- **production 변경**: 코드 변경 필요 (approval-needed)

### J3 — AI 호기심형

- **방문자 의도**: AI가 이 행동을 어떻게 볼지 궁금하다 — 저장은 선택
- **first value**: deed_judged
- **홈 feed 역할**: 무관 (J3 첫 가치는 /add 결과 카드)
- **seeded proof 필요도**: 낮음 — 홈 feed proof는 J3 전환에 직접 기여 낮음
- **현재 empty-state**: CTA만 (홈이 J3 진입점이 아닐 수 있음)
- **oops risk**: 홈 proof 추가해도 J3 동기에 실질 영향 없음
- **안전 표시**: 해당 없음
- **preview 후보**: /add flow의 결과 카드 자체 미리보기 (별도 검토)
- **production 변경**: /add flow 수정 필요 (별도 approval-needed)

### J4 — 회고형

- **방문자 의도**: 중요한 기록에 AI 주석을 영구적으로 달고 싶다
- **first value**: deed_saved (영구 주석)
- **홈 feed 역할**: 본체 (영구 보존 확인)
- **seeded proof 필요도**: 중 — 영구성 느낌을 주는 카드 형태가 중요
- **현재 empty-state**: CTA만, 영구성 표현 없음
- **oops risk**: 카드가 너무 가볍게 보이면 "이게 정말 영구 보존이 맞나" 의심
- **안전 표시**: 날짜·아카이브 아이콘·진지한 텍스트 예시 필요
- **preview 후보**: 의미 있는 기억 카드 + AI 주석 + 날짜 표시
- **production 변경**: 코드 변경 필요 (approval-needed)

## 구현 권장 순서 (prelaunch 후)

1. **동사 프레임 정렬** (m45 권고): 버튼 `AI 채점` → 관점 프레임 문구 — approval-needed
2. **J2 누적 카드 스택** seeded proof: 홈 empty-state에 예시 3-5개 카드 + 레벨 뱃지 — approval-needed
3. **J1 단일 카드** seeded proof: 행동명 + AI 관점 단일 카드 예시 — approval-needed
4. **J4 영구성 카드**: 날짜+아카이브 있는 예시 카드 — approval-needed
5. **J3 /add preview**: 별도 검토 (홈 empty-state 범위 밖)

## Prelaunch 허용 범위

이 문서 자체가 이번 heartbeat의 산출물이다.

**허용:** proof preview 기준 문서화, J1-J4별 형태 명세, 오해 위험 정리
**approval-needed:** 위 1-5번 구현 항목 모두 (production code, deploy, public copy 변경)

## 충돌 점검

| 선행 문서 | 확인 항목 | 충돌 여부 |
|-----------|----------|-----------|
| marketing-31 | Product Body vs Bumper By Job | 없음 — 계승 |
| marketing-45 | verb frame mismatch | 없음 — 선행 조건으로 명시 |
| marketing-66 | J1-J4 context map | 없음 — 보완 (proof dimension 추가) |
| marketing-68 | agent-readable surface audit | 없음 — 보완 (human-facing empty-state 추가) |

Conflict markers: 0

## Marketer 인수인계

**계승한 기준:**
1. Product Body vs Bumper By Job (marketing-31): 홈 feed J2=본체, J1=범퍼
2. Decision-Delegation Risk Rides The Verb (marketing-45): 동사 프레임 정렬 우선
3. Prelaunch Decision Boundary: docs-only 선행

**이번에 새로 만든 것:**
- J1-J4 x seeded proof 필요도 매핑 (기존 미존재)
- 오해 위험 x 안전 표시 방법 명세
- G1/G2/G3 gap 정리 (m45/m66/m68 대비)

**다음 작업에 넘길 규칙:**
- J2가 seeded proof 우선 job이다 (누적 payoff 시각화)
- seeded proof 구현 전 반드시 동사 프레임 정렬(m45)을 먼저 완료한다
- "예시" 레이블은 UI에서 필수 (실제 데이터 오해 방지)
- J3는 홈 proof보다 /add 결과 카드 자체 미리보기가 더 효과적

## 금지선 (prelaunch 적용)

- production code · deploy · tracking/privacy · PostHog · public copy · external message · cost · 권한 변경: 0
- 이 문서 자체는 내부 docs-only — 공개 발행 불가
