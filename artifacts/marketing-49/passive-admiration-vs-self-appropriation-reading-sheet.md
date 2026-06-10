# 수동 감탄 vs 자기화 행동 판독표 (Virtue 결과 카드 직후)

> docs-only · 신규 계측 0 · approval-needed 경계 명시
> 출처: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-09-ai-passive-activation-retention.md`

## 배경

ChartMogul AI activation/retention 노트(2026-06-09): AI가 빠른 첫 가치를 만들수록 사용자가 수동적으로 감탄만 하고 반복 맥락을 만들지 못할 위험을 지적한다.

Virtue의 J3(`deed_judged`)는 결과 카드가 first value 도착점이라 저장 없이 종료해도 정상이다. 그런데 "저장 없는 종료" 버킷에 세 가지가 섞여 있다:
- J3 정상 완료 (무저장 정상 종료)
- 수동 감탄 (passive admiration — 감탄 반응만, 반복 맥락 없음)
- 마찰·가용성 (deed_save_capped, 503, 지연)

이 세 가지를 더 선명하게 분리하는 수기 판독 칸이 이 문서의 목적이다.

## 기존 매핑 보존 (변경하지 않음)

- J1/J2/J4 first value: `deed_saved` (저장)
- J3 first value: `deed_judged` (AI 결과 카드 도달)
- J3 무저장 종료: **정상** — 저장 없이 닫힘이 이탈 신호가 아님

## 결과 카드 직후 행동 분류 (수기 판독 칸)

prelaunch 첫 10명 관찰 시 결과 카드(`deed_judged`) 이후 관찰자가 손기록으로 체크한다.

**한 세션에서 복수 체크 가능. 모두 미체크 시 "기타" 칸에 메모.**

---

### 칸 1: 저장 / 재작성 / 선택 (자기화 행동 A)

- [ ] **저장했다** (`deed_saved`) — 결과를 기록으로 남겼다
- [ ] **재작성/재판정 요청** (`deed_rerolled`) — 다른 입력으로 다시 시도했다
- [ ] **선택·편집** — 결과 일부를 골라서 옮기거나 수정했다

*근거: 자기 맥락에 결과를 집어넣는 행동. 반복 방문의 씨앗.*

---

### 칸 2: 자기 말로 설명했다 (자기화 행동 B)

- [ ] **소리 내어 읽거나 재해석** — "아 이게 이런 거구나"처럼 자기 말로 바꿔 읽었다
- [ ] **타인에게 보여주거나 설명** — 옆 사람에게 화면을 돌려 보여주거나 말로 설명했다

*근거: 수동 감탄과 구별하는 핵심 신호. 자기 말 설명 = 자기화 진입 신호.*

---

### 칸 3: 무저장 정상 종료 (J3 정상)

- [ ] **무저장으로 닫았다 — 정상 종료** — 결과를 보고 특별한 마찰 없이 그냥 닫았다

*적용: J3에서만 정상. J1/J2/J4에서 체크되면 "저장 전 이탈 보류"로 별도 메모.*

---

### 칸 4: 수동 감탄 (ChartMogul 경고 대상)

- [ ] **"오" / "맞다" 반응만 했다** — 감탄·동의 표현만 하고 저장/재작성/자기 말 설명 없이 닫았다

*근거: ChartMogul 노트의 핵심 위험 신호. 빠른 AI 가치 → 감탄에 머뭄 → 반복 맥락 없음.*
*J3에서도 이 칸이 체크되면 다음 세션 재방문 여부를 별도 주시.*

---

### 칸 5: 마찰 / 가용성

- [ ] **기술적 차단** — 버튼이 안 눌렸다, 화면이 느렸다, `deed_save_capped`, 503, 지연

*근거: 이 칸은 가치/이탈 신호가 아니라 availability/friction 신호로 분류한다.*

---

### 기타

- [ ] 기타: ___________________________________

---

## 판독 기준 요약

| 관찰된 행동 | 분류 | 반복 맥락 형성 여부 |
|------------|------|-------------------|
| 저장/재작성/선택 | 자기화 행동 A | ✓ (직접 형성) |
| 자기 말 설명/공유 | 자기화 행동 B | ✓ (언어로 형성) |
| 무저장 종료 (J3) | 정상 종료 | — (이탈 신호 아님) |
| 감탄 반응만 | 수동 감탄 (주시) | △ (형성 미확인) |
| 기술적 차단 | 마찰·가용성 | ✗ (인프라 문제) |

## 연결 문서

- **first-real-user-baseline-template**: 세션 전체 관찰 기록지
- **marketing-47 산출물** (`artifacts/marketing-47/virtue-first-10-design-user-ask-script.md`): 초대 → pre → post → 자기 말 기록 루프
- **ai-promise-decision-control-audit-table** (marketing-45): 결과 카드 전 단계 — 동사 프레임
- **출처 노트**: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-09-ai-passive-activation-retention.md`

## 적용 범위 및 제약

**적용 범위 (docs-only):**
- prelaunch 첫 10명 관찰 시 손기록 판독 칸으로 사용
- first-user baseline / design-user ask script 관찰 지점 4번(자기 말 기록 칸)과 연결
- Infinity artifact로 보관 (Virtue 앱 레포 로컬 부재)

**신규 계측 0:** 이 문서는 신규 이벤트·속성·tracking을 정의하지 않는다. 모든 관찰은 손기록이다.

**Approval-needed:**
- 공개 카피, 온보딩 UX 변경, 결과 카드 후 affordance 변경
- 신규 이벤트/속성/tracking/privacy/dashboard/session replay
- 발송, 배포, 가격/결제, 외부 액션 일체

## 계승한 기준

1. **[Post-Response Flow Reveals Value, Not The Result Event] (m44)**: 결과 카드 직후 30초를 세션 전체와 분리된 수기 관찰 프레임으로 두고, 먼저 카드가 도착점인가 통과점인가를 묻는다.
2. **[First-User Learning Loop Reads Language, And Help Means Articulation Not Delegation] (m47)**: 자기 말 설명 칸은 수집 대상. 손기록만(신규 계측 0).
3. **[Availability And Friction Are Not Value] (m21)**: 마찰/가용성은 value 신호가 아님 — 칸 5에서 분리.

## 이번에 새로 배운 것

ChartMogul 노트의 "수동 감탄 함정"을 Virtue 첫 사용자 관찰로 번역하면: J3 무저장 정상 종료와 수동 감탄을 구별하는 유일한 관찰 가능 신호는 **"자기 말로 재해석했는가 또는 타인에게 설명했는가"**다. 저장 없음 단독으로는 구별이 안 된다.

## 다음 Marketer에게 넘길 규칙

- 수동 감탄 칸(칸 4)에 체크가 많아도 즉시 UX 변경 제안하지 않는다. 관찰 언어를 먼저 수집한 뒤 판단한다.
- J3 정상 종료(칸 3)와 수동 감탄(칸 4)은 on-instrument로 구별 불가. 손기록이 단일 근거다.
- 승격 후보: **"Passive Admiration Is Distinguished From Normal Completion By Self-Articulation"** — 단일 사례라 report 보류, 첫 10명 관찰 후 재검토.
