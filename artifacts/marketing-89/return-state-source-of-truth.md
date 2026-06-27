# marketing-89 Virtue 홈 반환 상태 source-of-truth 및 empty-state 게이트

## 목적

- `stats.total`, `stats.count`, `recent.length`가 서로 다른 질문에 답하고 있다는 점을 명시적으로 고정한다.
- retained proof 세션에서 empty-state가 언제 허용되고 언제 금지되는지 1페이지 계약으로 만든다.
- 후속 구현/검증 intent가 이 문서를 source-of-truth로 삼게 한다.

## 관측 근거

| 근거 | 확인 내용 |
| --- | --- |
| `apps/web/src/lib/store.ts` | `stats.total = INITIAL_VIRTUE + stored deed score sum`, `stats.count = deeds.length`, `useDeeds()`는 localStorage의 deeds를 최신순으로 반환 |
| `apps/web/src/lib/mock-data.ts` | `INITIAL_VIRTUE = 612` |
| `apps/web/src/app/page.tsx` | 홈은 `isFirstVisit = stats.count === 0`로 hero/CTA/첫 안내를 분기하고, 최근 덕행은 `recent.length === 0`으로 empty-state를 분기 |
| `intents/archive/marketing-88.md` | 라이브에서 `612덕` retained proof와 empty-state 계열 문구가 동시에 보여 drift가 기록됨 |
| `source/external-links/marketing/2026-06-27-return-state-verification-gate.md` | 문제를 카피 부족이 아니라 return-state gating mismatch로 정의함 |

## 값별 역할 고정

| 값 | 진짜로 말하는 것 | 단독 사용 가능 여부 | 금지되는 오해 |
| --- | --- | --- | --- |
| `stats.total` | 기본 덕력(`INITIAL_VIRTUE`)과 저장된 덕행 점수 합산 결과 | 누적 점수/종 진행도 표면에는 가능 | "기록이 하나 이상 있다"의 증거로 사용하면 안 됨 |
| `stats.count` | 저장된 덕행 개수 | first-visit / returning 판정의 기준으로 사용 | 누적 덕력 존재 여부를 대신 설명하면 안 됨 |
| `recent.length` | 홈에 노출할 최근 덕행 카드 개수 | 최근 덕행 리스트 렌더링 기준으로 사용 | 전체 계정이 empty-state인지 판정하면 안 됨 |

## canonical gating 계약

### 1. first-visit 상태

- 기준: `stats.count === 0`
- 허용 표면
  - hero 라벨 `오늘의 첫 환생 기록`
  - 첫 기록 유도 카피
  - CTA `첫 덕 기록해보기`
  - 최근 덕행 empty-state
- 전제
  - `recent.length === 0`
  - `stats.total`이 612 이상이어도 first-visit 판정을 뒤집지 않는다. 기본 덕력은 retained proof가 아니라 baseline이다.

### 2. returning 상태

- 기준: `stats.count > 0`
- 허용 표면
  - hero 라벨 `나의 덕력`
  - 월/어제 증감 노출
  - CTA `오늘 덕 쌓기`
  - 최근 덕행 리스트 또는, 필요 시 "최근 항목 로딩 실패" 같은 비-empty 복구 상태
- 금지 표면
  - `아직 기록이 없어요`, `첫 기록이 여기에 쌓여요`, `첫 덕 기록해보기`처럼 first-visit 전용 문구
  - `stats.total > INITIAL_VIRTUE` 또는 `stats.count > 0`인데도 전체 홈이 새 사용자처럼 보이는 조합

### 3. mixed-signal 예외 처리

- `stats.count > 0`인데 `recent.length === 0`이면, 이는 "최근 3개 목록 렌더링/동기화 문제"이지 first-visit가 아니다.
- 이 경우 홈 전체를 empty-state로 내리면 안 되고, 문제 표면은 최근 덕행 섹션에 국한해야 한다.
- 검증 문장: "누적 proof는 살아 있고 최근 리스트만 비었다"를 설명할 수 있어야 한다.

## retained proof 세션 검증 게이트

### empty-state 허용 조건

- 오직 `stats.count === 0`이고 `recent.length === 0`일 때
- 이때 `stats.total`은 baseline으로만 읽고, 기록 존재 증거로 취급하지 않는다.

### empty-state 금지 조건

- `stats.count > 0`
- `recent.length > 0`
- live surface에서 저장 이력이 존재한다고 이미 다른 표면이 주장하는 경우
  - 예: 누적 proof를 baseline이 아닌 retained history처럼 보이게 카피한 상태

## 구현 전 검증 질문

1. home hero가 first-visit / returning을 무엇으로 판정하는가
2. 최근 덕행 섹션이 비어도 홈 전체 상태를 바꿀 권한이 있는가
3. `stats.total`이 baseline인지 retained proof인지 사용자가 3초 안에 구분 가능한가

세 질문 중 하나라도 "아니다"면 반환 상태 드리프트로 실패 처리한다.
