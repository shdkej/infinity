# marketing-49: Virtue 결과 카드 직후 행동 판독표 (수동 감탄 vs 자기화)

> Source: ChartMogul AI activation/retention 노트 (2026-06-09)
> Path: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-09-ai-passive-activation-retention.md
>
> 이 문서는 Virtue 결과 카드(`deed_judged`) 직후 30초 관찰용 수기 판독 칸을 제안한다.
> 기존 잡 매핑(J1/J2/J4=`deed_saved`, J3=`deed_judged`)은 그대로 유지한다.
> 신규 계측, 이벤트, 속성, tracking, dashboard, session replay를 만들지 않는다.

## 판독 프레임: 결과 카드 직후 30초

결과 직후를 세션 전체와 분리된 별도 수기 관찰 단위로 둔다.
on-instrument 신호는 `deed_saved`, `deed_rerolled`, `deed_save_capped`, 종료뿐이며,
그 외 근거 읽기·보여주기·망설임·감탄은 손기록으로만 남긴다.

## 관찰 칸 (3-5개 수기 판독)

### 칸 1: 결과 카드 도착점 vs 통과점

| 잡 | 카드 위치 | 정상 종료 판단 기준 |
|----|----------|-------------------|
| J3 | **도착점** (first value) | `deed_judged` 발화 = 완료. 저장 없이 닫혀도 정상. |
| J1/J2/J4 | **통과점** (저장 전) | `deed_saved` 발화 여부로 완료 판단. |

수기 기록: 이 세션의 잡은? → J3 / J1 / J2 / J4 / 불명

---

### 칸 2: 결과 직후 첫 행동 분류

7가지 행동 중 관찰된 것을 손기록한다. (복수 가능, on-instrument에 없는 항목은 직접 관찰)

| 코드 | 행동 | 설명 |
|------|------|------|
| **A-SAVE** | 저장 | `deed_saved` 발화. J1/J2/J4에서는 first value 도달. |
| **A-REWRITE** | 재작성 / 다시 입력 | 다른 내용으로 다시 제출. 기대 불일치 또는 탐색 신호. |
| **A-SELECT** | 선택/강조 | 결과 일부를 직접 선택하거나 가리킴. 특정 부분에 주의 집중. |
| **A-VOICE** | 자기 말로 읽기/설명 | 결과를 읽고 다른 사람에게 자기 말로 풀어 설명함. 공유성(m30) 신호. |
| **A-CLOSE** | 저장 없이 정상 종료 | 무저장으로 닫기. J3에서는 정상 완료. J1/J2/J4에서는 보류 후보. |
| **A-ADMIRE** | 수동 감탄 | 결과를 보고 "오~" 반응만. 저장·재시도·공유 없이 닫힘. ChartMogul 위험 지점. |
| **A-FRICTION** | 마찰/가용성 차단 | 저장 상한(`deed_save_capped`), 로딩, UI 혼란 등. |

수기 기록: 관찰된 행동 코드? → _______

---

### 칸 3: 수동 감탄 vs 자기화 판별 기준

이 칸은 A-CLOSE와 A-ADMIRE를 구분하기 위한 보조 관찰이다.

| 신호 | 수동 감탄 쪽 | 자기화 쪽 |
|------|------------|----------|
| 결과를 읽은 시간 | 빠르게 스캔 후 닫기 | 꼼꼼히 읽음 |
| 결과에 대한 언급 | "신기하다", "맞네" (감탄) | "이걸 어떻게 씀" (활용 탐색) |
| 재방문 의도 | "나중에 또 써볼까" 수준 | "오늘 한 일에 쓰겠다" 수준 |
| 저장 의향 | 없음 | 있음 (나중에라도) |

수기 기록: 어느 쪽에 더 가까운가? → 수동 감탄 / 자기화 / 판별 불가

---

### 칸 4: 판단 귀속 신호 (결정-위임 인지 여부)

AI 판정 결과를 어떻게 받아들이는지 직접 관찰한다.

| 유형 | 예시 표현 | 해석 |
|------|----------|------|
| **확인형** | "맞아, 나도 그랬어" | AI를 자기 판단의 확인 도구로 사용. 건강한 보정. |
| **위임형** | "AI가 그러니까 그런가 봐" | 자기 판단 없이 수용. 과의존 주의. |
| **중립형** | "그냥 봤어" | 판단 귀속 없음. |

수기 기록: 어떤 유형? → 확인형 / 위임형 / 중립형 / 불명

---

### 칸 5: first-user baseline / design-user ask script 연결 포인트

이 칸은 m47 First-User Learning Loop와 연결된다.

**pre-session 질문 (2문항, proposal-only):**
- 지금 이 일을 어떻게 기록하고 있어요? (현재 행동)
- AI가 이걸 판단해 준다면 어떻게 쓰실 것 같아요? (기대)

**post-session 질문 (3문항, proposal-only):**
- 결과 카드를 보고 가장 먼저 뭘 했어요? (→ 칸2 코드 확인)
- 결과를 저장했거나 하려고 했나요? (→ A-SAVE / A-CLOSE / A-ADMIRE)
- 이 AI 판정이 '내 판단'이라고 느껴졌나요, '참고'라고 느껴졌나요? (→ 칸4)

수기 기록 칸: ___________________________________________________

---

## 검증 게이트 (신규 계측 없음 확인)

- [x] 기존 J1/J2/J4=`deed_saved`, J3=`deed_judged` 매핑을 재정의하지 않았다.
- [x] 새로운 이벤트, 속성, tracking, dashboard, session replay를 만들지 않았다.
- [x] 모든 관찰 칸은 손기록(수기) 전용이다.
- [x] source note 경로 인용: /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-09-ai-passive-activation-retention.md
- [x] 결과 직후 행동을 저장/재작성/선택/자기말설명/무저장정상종료/수동감탄/마찰 7가지로 구분함.
- [x] approval-needed 경계 명시: 신규 계측·이벤트·tracking·dashboard·session replay·공개 카피·발송·가격/결제·배포·외부 액션

## 상속한 기준 (MARKETING_LEARNINGS.md)

- **Post-Response Flow Reveals Value, Not The Result Event** (m44): 결과 카드 직후 30초를 수기 관찰 프레임으로 분리, on-instrument 외는 손기록만
- **First Value Mapping** (m06+): J3=`deed_judged`, J1/J2/J4=`deed_saved` 기본값 유지
- **Shareworthiness Is A Separate Axis** (m30): A-VOICE 칸은 공유성 수기 관찰
- **AI Outcome Proxy Separation** (m24): activity vs acceptance 분리 (수동 감탄 vs 자기화가 이 축에 해당)
- **First-User Learning Loop Reads Language** (m47): pre/post 질문 연결 칸(칸5) — 초대·질문 문장은 proposal-only

## 이번에 새로 배운 것 / 다음 작업에 넘길 규칙

- **수동 감탄(A-ADMIRE)과 정상 종료(A-CLOSE)를 구분하는 기준은 재방문 의도와 활용 탐색 언어다.** on-instrument로는 구분 불가. 손기록 필수.
- **결과 직후 판독은 세션 전체와 분리해야 한다.** J3에서는 저장 없는 종료가 정상이므로, 전체 세션 지표(저장률, 이벤트 수)와 혼합하면 A-ADMIRE를 정상 종료로 놓친다.
- **칸2(결과 직후 첫 행동)의 7가지 분류는 m44 프레임과 일치하며 재사용 가능하다.** 다음 Marketer가 first-user observation 설계 시 이 코드를 그대로 쓸 수 있다.
- **durable learning 후보:** "Post-Result Action Is Read By Job — A-CLOSE Is Normal For J3, Hold For J1/J2/J4" — 단일 사례 미발생 단계라 report에 보류.
