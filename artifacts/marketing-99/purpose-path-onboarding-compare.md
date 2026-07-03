# Virtue 홈 첫 진입 `목적별 첫 길` 3안 비교

- id: marketing-99
- created: 2026-07-03
- type: strategy · comparison
- permission: L1 docs-only
- 기준: marketing-19 홈 FAE 감사, marketing-70 empty-state proof, marketing-93 J1 판독표, marketing-98 관찰표, MARKETING_LEARNINGS.md

## 배경: 현재 홈 진입 상태

현재 홈(`apps/web/src/app/page.tsx`) 진입 구조:
- **주 CTA** `오늘 덕 쌓기` (`:106-112`) → `/add`로 연결. J1/J2/J4에 최적화.
- **빈 상태** `최근 덕행` (`:125-131`) → `count===0`, `recent.length===0`일 때 아무것도 없음.
- **AI 신호 없음** → J3 (AI 호기심형) 사용자는 홈에서 Virtue가 AI 제품임을 알 수 없다. (marketing-19 Gap G3)
- **첫 방문자 부담** → J1은 빈 화면에서 `오늘 덕 쌓기`를 눌러야 하는데, 눌렀을 때 무엇이 생기는지 예고가 없다.
- marketing-93 확인: "홈 language-market fit은 J1 중심, J3는 `/add` 진입 후 늦게 나타남."

계승 기준:
- J1/J2/J4 first value = `deed_saved`, J3 first value = `deed_judged` (First Value Mapping)
- 전역 예시/placeholder 최적화 금지 (First-Input Defaults Steer The Job)
- 동사 프레임: `채점`/`판정` 판결 프레임 금지, `보기`/`읽기` 관점 프레임 사용 (Decision-Delegation Risk Rides The Verb)
- 단일 케이스, 작은 표본에서 결론 확정 금지 (Prelaunch Decision Boundary)

---

## 3안 비교표

| 항목 | A. 단일 CTA 유지 | B. J1/J3 2갈래 시작선 | C. 샘플 결과 preview |
|------|-----------------|----------------------|---------------------|
| **핵심** | 현재 그대로. `오늘 덕 쌓기` 1개 CTA | 두 버튼: `오늘 기록하기` + `AI로 먼저 보기` | 홈 빈 상태에 정적 결과 카드 예시 1개 삽입 |
| **코드 앵커** | `page.tsx:106-112` 유지 | `page.tsx:106-112` 교체 필요 | `page.tsx:125-131` 영역 교체 필요 |
| **J1 부담** | 빈 화면 그대로 | `오늘 기록하기` 문구로 방향 명료화 | preview로 "이런 결과가 나온다" 예고 가능 |
| **J3 신호** | 홈에서 AI 신호 0 (Gap G3 미해결) | `AI로 먼저 보기` 버튼으로 AI 신호 추가 | preview 카드가 AI 판정 결과물임을 보여줌 |
| **장점** | 변경 없음, 리스크 0 | J3 Gap G3 직접 해소; 잡 자기 선택 유도 | 코드 변경 최소화; 양쪽 잡에 동시 신호 |
| **단점** | J3 Gap G3 미해결; J1 빈 화면 부담 지속 | 2 CTA 선택 장애 가능; J1/J3 경계 불명확 사용자 혼란 | preview가 "가짜처럼" 느껴질 위험; 유지보수 필요 |
| **금지선** | — | 동사 `AI 채점`/`AI 판정` 금지; 전역 placeholder 동시 수정 금지 | 실 사용자 데이터 금지; mock 레이블 노출 금지 |
| **실험 비용** | 없음 | 높음 (UX 설계 + 코드 변경 + 관찰 후 재설계 가능성) | 낮음 (정적 카드 1개 삽입, 코드 최소 변경) |
| **관찰 조건** | 첫 10명 이후 J3·J1 마찰 없음 | J3 Gap G3가 실제 이탈 원인임을 관찰 후 | 빈 화면 부담이 주요 마찰로 관찰된 후 |

---

## 우선 실험 순서

```
0. 관찰 먼저 (필수 선행 게이트)
   - 첫 10명 세션에서 marketing-98 관찰표 작성
   - J3 사용자가 홈에서 AI 신호를 못 찾아 이탈하는 패턴 확인
   - J1 사용자가 빈 화면에서 오늘 덕 쌓기를 누르지 못하고 이탈하는 패턴 확인
   - 둘 다 없으면 A(유지)로 충분

1순위 실험 후보: C. 샘플 결과 preview
   조건: J1 빈 화면 부담이 관찰로 확인된 경우
   구현: page.tsx:125-131 영역에 정적 예시 카드 1개 삽입
   금지: 실 데이터 사용, mock/임시 레이블 노출, J3 저장 강요 힌트 추가
   검증: 홈→/add 진입률 변화 (정성 관찰 우선)

2순위 실험 후보: B. J1/J3 2갈래 시작선
   조건: J3 Gap G3가 관찰로 확인된 경우 (J3가 홈에서 실제로 혼란)
   구현: page.tsx:106-112 CTA 교체, 동사 관점 프레임 준수
   금지: AI 채점/AI 판정 동사, 2 CTA 동시에 J1/J3 모두 유도하는 예시 추가
   주의: B를 먼저 만들고 관찰하지 않는다. 관찰 근거 없이 실험하면 J1/J2를 혼란에 빠뜨릴 위험.

유지(A): 관찰에서 J3 Gap G3와 J1 빈 화면 부담 둘 다 주요 마찰로 안 나오면 현 상태 유지.
```

---

## 금지선 종합

1. **코드 배포**: 이 문서는 docs-only 비교다. 코드 변경 및 배포는 별도 approval-needed.
2. **판결 프레임 동사**: `AI 채점`, `AI 판정`, `채점해드립니다` 금지. 관점 프레임(`AI가 본`, `AI 관점`, `보기`)만.
3. **전역 예시/placeholder**: 잡별 검증 후에만 적용.
4. **실 사용자 데이터 preview**: mock/synthetic 데이터를 실 사용자 증거로 제시 금지.
5. **관찰 없는 B 구현**: 관찰 증거 없이 2갈래 시작선을 먼저 배포하지 않음.
6. **소규모 표본 결론 확정**: 첫 10명 결과를 activation rate, PMF, conversion으로 환산하지 않음.

---

## 다음 마케터에게 넘길 규칙

- **계승한 기준**: First Value Mapping, Decision-Delegation Risk (판결→관점 프레임), First-Input Defaults (전역 최적화 금지), Prelaunch Decision Boundary
- **이번에 새로 배운 것**: J3 Gap G3 해소 실험 비용은 B > C 순이며, 관찰 없이 B 실험은 J1 혼란 위험이 높다.
- **다음 작업에 넘길 규칙**: 1순위(C) 실험 전에 반드시 첫 10명 관찰표(marketing-98 양식)를 완성하고 J3 Gap G3 또는 J1 빈 화면 부담이 관찰되는지 확인한다.
