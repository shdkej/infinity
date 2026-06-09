# Virtue 결과 카드 직후 행동 판독표 (내부용)

> deed_judged 직후 행동을 4칸 수기 판독표로 구분한다.
> 목적: prelaunch 첫 10명 관찰에서 자기화 완료 / J3 정상 종료 / 수동 감탄 / 마찰·가용성을 선명하게 읽는다.
> 출처노트: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-09-ai-passive-activation-retention.md (ChartMogul AI activation/retention)

- id: marketing-49
- permission: L1/L2 docs-only
- first value 매핑(기본값, 재정의 없음): J1·J2·J4 = `deed_saved`, J3 = `deed_judged`
- 연결: first-user ask script (m47 §C), first-real-user-baseline-template
- 신규 계측: 0 (손기록만)

---

## 핵심 맥락: 왜 이 판독표가 필요한가

ChartMogul AI activation/retention 노트(출처노트)의 핵심 경고:
> AI가 빠른 첫 가치를 만들수록 사용자가 수동적으로 감탄만 하고 반복 맥락을 만들지 못할 위험이 있다.

Virtue에서 이 위험은 다음처럼 나타난다:

- `deed_judged`는 J3에서 first value 도착점이다.
- 그러나 같은 `deed_judged` 이후 "저장 없이 닫힘"이 세 가지 전혀 다른 의미일 수 있다:
  1. **J3 정상 종료** — first value를 얻었고 끝. 성공.
  2. **수동 감탄** — AI 출력에 감탄했지만 자기 것으로 만들지 않음. 반복 맥락 미형성.
  3. **마찰·가용성** — 시스템 문제나 B-LOST로 중단.

이 세 가지를 on-instrument 신호만으로 구분할 수 없다. 수기 판독 칸이 필요한 이유다.

---

## 4칸 수기 판독표

| 칸 | 이름 | 발화 이후 행동 | on-instrument 신호 | 수기 단서 (손기록) | first-user ask script 연결 |
|---|---|---|---|---|---|
| **칸 1** | **자기화 완료** | 결과를 자기 것으로 만듦 | `deed_saved`, `deed_rerolled`(다듬기) | 자기 말로 설명, 결과를 보여주며 맥락 제공, 다음 행동으로 연결 | §C-1 first value 위치 = 결과 카드 or 저장 후; §C-3 "정리해준 것" 응답 |
| **칸 2** | **J3 정상 종료** | `deed_judged` = first value. 저장 불요. | `deed_judged`, 미저장, 짧은 세션 | 차분한 종료, 만족 표정, "봤어요" 반응 | §C-1 first value 위치 = 결과 카드 도착 자체; J3에서 저장 넛지 금지 |
| **칸 3** | **수동 감탄** | 감탄했으나 자기 것으로 만들지 않음 | `deed_judged`, 미저장, 빠른 닫기 | "신기하다/재밌다" 반응 후 자기 말 설명 불가; 보여줘도 "왜 그게 중요한지" 설명 못함 | §C-3 "대신 정해준 것"에 가까운 응답 → 수동 감탄 신호 |
| **칸 4** | **마찰·가용성** | 흐름이 차단됨 | `deed_save_capped`, 503, B-LOST, `deed_rerolled` 반복 | 혼란/표정 변화, "왜 이래요?" 반응, 여러 번 재시도 | §C-2 friction 질문으로 확인 |

### 칸 2 vs 칸 3 구분 기준 (핵심 판독 포인트)

칸 2와 칸 3은 on-instrument로 거의 동일하게 보인다 (`deed_judged`, 미저장, 빠른 종료).
**손기록으로만 구분 가능**:

| 구분 질문 | 칸 2: J3 정상 종료 | 칸 3: 수동 감탄 |
|---|---|---|
| "어떤 결과를 봤어요?" | 자기 말로 설명 가능 | "신기하다"고만 함 |
| "이 결과로 뭘 할 것 같아요?" | "딱히 없어도 됨" 또는 자연스러운 다음 행동 | "모르겠어요" |
| §C-3 "대신 정해준 것 vs 정리해준 것" | 관점("정리해준 것")으로 읽음 | 판결("대신 정해준 것") 경향 |
| 표정/반응 | 차분, 완결감 | 놀람·감탄 후 망설임 |

---

## 수기 기록 양식

> deed_judged 직후 30초 관찰 (m44 Post-Response Flow 연결)

| 관찰 항목 | 수기 메모 |
|---|---|
| 결과 카드 도착 후 첫 반응 | (원문 그대로 손기록) |
| on-instrument 신호 | `deed_saved` / `deed_rerolled` / 미저장 종료 / `deed_save_capped` / 503 |
| 자기 말 설명 시도 여부 | 가능 / 불가(감탄만) / 없음 |
| 결과를 어떻게 읽나 (§C-3) | 관점("정리해준 것") / 판결("대신 정해준 것") / 명확하지 않음 |
| 판독 칸 최종 배정 | 1(자기화) / 2(J3 정상) / 3(수동 감탄) / 4(마찰·가용성) |

**기록 원칙**: on-instrument + 손기록 같이 보고 최종 배정. 신규 이벤트/속성/tracking 0.

---

## 이 판독표가 연결되는 문서들

| 선행 문서 | 이 판독표의 관계 |
|---|---|
| `first-real-user-baseline-template` | 수기 기록 양식이 이 기록표로 흘러든다 |
| `design-user ask script (m47) §C` | §C-1(first value 위치) / §C-2(friction) / §C-3(결정-위임 인지)가 칸 배정에 직결 |
| `ai-promise-decision-control-audit-table (m45)` | 칸 3 vs 칸 2 구분에 동사 프레임(판결 vs 관점)이 단서로 쓰임 |
| `Post-Response Flow Reveals Value (m44)` | deed_judged 직후 30초 관찰 프레임이 이 판독표의 관찰 시간 단위 |

---

## 가정·충돌·학습 분리

### 계승한 가정 (inherited)

- first value 매핑: J1·J2·J4=`deed_saved`, J3=`deed_judged` (재정의 0, m06)
- J3 deed_judged 후 미저장 = 정상 종료 (judged−saved 갭=정상, m47)
- `deed_save_capped`·503·지연 = availability/friction, value 아님 (m22)
- 비자율 AI → 위험은 행동적 해가 아니라 자기인식 오보정, 결정-위임 위험은 동사 프레임에 실림 (m38·m45)
- 성찰형 제품에서 도움의 목표 = 자기 말로 말하게 하기, 결정 대행 아님 (m47)
- 작은 표본은 방향 재료, decision-grade 아님 (Prelaunch Decision Boundary)

### 변경한 가정 (changed)

없음. 기존 경계 재정의 0. "수동 감탄" 칸을 J3 정상 종료와 분리한 새 관찰 칸 추가.

### 선행 산출물과의 충돌 (conflicts)

없음. m44 / m47 / m45 / baseline-template과 층이 다르고 같은 방향.

### durable learning 후보 (단일 사례 — report에 보류)

- "Passive Admiration And J3 Normal Completion Are Only Distinguishable By Hand-Written Signal": AI 빠른 첫 가치 제품에서 deed_judged 직후 미저장 종료는 on-instrument로 동일하게 보이지만, 자기 말 설명 가능 여부(손기록)로만 정상 종료와 수동 감탄을 구분할 수 있다. → 단일 사례. MARKETING_LEARNINGS.md 승격은 실사용 관찰 후 확인.

---

## 승인 필요선 (approval-needed)

이 문서 범위 = 내부 준비물 작성까지(L1/L2 docs-only). 아래는 별도 승인 없이 실행하지 않는다.

- 신규 이벤트·속성·tracking·privacy·dashboard·session replay
- 공개 카피·온보딩·버튼·헤더 문구 변경
- 배포·가격·결제·권한 변경
- 공개 발송·DM·광고
- 코드 접근·변경
