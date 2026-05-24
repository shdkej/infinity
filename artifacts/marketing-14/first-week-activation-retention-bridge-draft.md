# Virtue 첫 주 활성화-리텐션 연결표

> 적용 범위: prelaunch 첫 10-20명 관찰 / 마케팅 포지셔닝·온보딩·측정 판단 기준선  
> 계승 문서: activation-milestone-ladder.md · time-to-value-observation-brief.md · first-real-user-baseline-template.md  
> 금지: 전환율·리텐션율 계산, 40% 임계값 적용, 신규 이벤트·속성·코드·PostHog 설정·배포·외부발송·비용

## 배경

획득(acquisition)만으로 리텐션이 생기지 않는다(Amplitude/ProductLed 참조 자료). Virtue prelaunch 단계에서는 전환율 판정 대신, 각 유입 문장이 어떤 잡(J1-J4)과 연결되고, first value → second value → 7일 재가치 경험으로 이어지는지 관찰 데이터를 쌓는 것이 목표다.

이 문서는 아래 세 선행 문서의 J1-J4 매핑과 이벤트 정의를 **변경 없이 계승**한다:
- `docs/activation-milestone-ladder.md` (setup→aha→habit, J1-J4별 이벤트)
- `docs/time-to-value-observation-brief.md` (first/second value, time gap, prelaunch 해석 금지선)
- `docs/first-real-user-baseline-template.md` (첫 사용자 관찰 행 양식)

---

## 1. J1-J4별 활성화-리텐션 연결표

| 잡 | 유입 신호 키워드 | Setup | First Value (Aha) | F→S gap 기준 | Second Value | 7일 재가치 기준 | 리텐션 연결 가설 |
|---|---|---|---|---|---|---|---|
| **J1 기록형** | "기록", "쌓기", "매일", "습관", "남기기" | `add_flow_started` | `deed_saved` (첫 기록 완료) | 당일~D3 | `deed_saved` ×2 (반복 기록) | D7 내 `deed_saved` ≥2 별도 날짜 | 기록 반복=습관 루프. gap > D3 이면 마찰 탐색 |
| **J2 누적형** | "성장", "레벨", "포인트", "눈에 보이는", "얼마나" | `add_flow_started` | `deed_saved` (누적 시작) | 당일~D2 | `level_up_viewed` (성장 시각화 확인) | D7 내 `level_up_viewed` ≥1 | 성장 시각화=리텐션 앵커. 레벨업 없으면 D7 이탈 위험 |
| **J3 AI 호기심형** | "AI", "채점", "어떻게 판단", "피드백", "뭐라고 해" | `add_flow_started` | `deed_judged` (AI 채점 첫 경험) | 당일~D1 | `deed_judged` + `deed_saved` 반복 | D7 내 `deed_judged` ≥2 별도 날짜 | AI 채점 호기심=재방문 유인. `deed_judged` 없이 `deed_saved`만 있으면 J1/J4로 재분류 |
| **J4 회고형** | "되돌아보기", "정리", "반성", "주간", "기억", "일지" | `add_flow_started` | `deed_saved` (회고용 첫 기록) | 당일~D7 (주기적) | `deed_saved` 재방문 기록 | D7 내 `deed_saved` ≥1 (1회도 유의미) | 주기적 의식=낮은 빈도 리텐션. D7 단 1회도 의미 있는 패턴 |

**사용 이벤트**: `add_flow_started`, `deed_judged`, `deed_saved`, `level_up_viewed`, `deed_rerolled`, `deed_save_capped` (기존 6개 외 신규 이벤트·속성 없음)

---

## 2. 유입 문장 → 잡 분류 관찰 흐름

```
유입 문장 수집 (초대/SNS/직접 URL 맥락)
    ↓
추정 잡 분류 (J1/J2/J3/J4 또는 미분류)
    ↓
add_flow_started 확인 (setup=의도 확인)
    ↓
First value 이벤트 관찰 → 잡 재확인
    ↓
F→S gap 측정 → Second value 이벤트 확인
    ↓
D7 재가치 경험 여부 기록
```

- 유입 문장 수집은 1:1 초대 대화나 첫 세션 후 짧은 대화로 파악 (PostHog 미사용, 별도 코드 변경 없음)
- 잡 분류는 유입 문장 + first value 이벤트 조합으로 결정; 단일 신호로 단정하지 않는다

---

## 3. 첫 10-20명 관찰 행 템플릿

> `first-real-user-baseline-template.md`의 기본 행에 아래 컬럼을 추가한다. 기본 템플릿의 기존 컬럼은 수정하지 않는다.

| # | 유입 문장 요약 | 추정 잡 | add_flow_started | First Value 이벤트·날짜 | F→S gap | Second Value 이벤트·날짜 | D7 재가치 (○/✗) | 503·가용성 차단 | 메모 |
|---|---|---|---|---|---|---|---|---|---|
| U-01 | | J? | ○/✗ · 날짜 | | | | | ○/✗ | |
| U-02 | | J? | ○/✗ · 날짜 | | | | | ○/✗ | |
| U-03 | | J? | ○/✗ · 날짜 | | | | | ○/✗ | |
| … | | | | | | | | | |

**기록 지침**:
- `#`: 익명 순번 (개인 식별 정보 최소화)
- `유입 문장 요약`: 초대/SNS/직접 URL 맥락 1-2문장
- `추정 잡`: 초기 추정 → first value 이벤트 후 재확인, 불확실하면 `J?`로 유지
- `503·가용성 차단`: 서버 오류/배포 롤백으로 접속 불가였던 날짜 기록

---

## 4. Prelaunch 해석 금지선

| 금지 행동 | 이유 |
|---|---|
| `add_flow_started` / 전체 방문자 로 퍼널 전환율 계산 | 표본 < 20명은 비율 판정 불가 |
| D7 리텐션율 X% 집계 | 관찰이지 통계가 아님 |
| PMF "매우 아쉽다" 40% 기준 적용 | 표본 부족, prelaunch 단계 부적합 |
| `judged−saved` 갭으로 이탈 단정 | J3 외에서는 탐색 행동일 수 있음 |
| 유입 문장-잡 가설을 카피/광고로 확정 | 관찰 데이터 10-20명은 가설 검증용 |
| `deed_rerolled` 多를 부정 신호로 단정 | 재추첨=참여의 다른 형태일 수 있음 |

---

## 5. 운영 경계: 503/가용성 이슈 분리

| 상황 | 분류 | 기록 방법 |
|---|---|---|
| 접속 시 503·타임아웃 응답 | **관찰 차단** (마케팅·제품 실패 아님) | 행 `503·가용성 차단` 컬럼에 날짜 기록 |
| 배포 롤백 구간 중 비활동 | 관찰 차단 | 동일 |
| `add_flow_started` 없이 세션 종료 | 원인 불명 (인프라 로그 대조 필요) | 차단 여부 확인 후 재분류 |
| 사용자가 스스로 재방문하지 않음 | 리텐션 부재 (제품·마케팅 문제) | 잡·first value 경험 재검토 |
| `deed_save_capped` 발생 | UX 마찰이나 활발한 사용 신호 | 저장 한도 도달=리텐션 가능성 높음 |

> **원칙**: 인프라 장애 중 발생한 비활동은 사용자 이탈이 아닌 **관찰 차단**으로 기록한다. 두 원인을 구분하지 않으면 첫 10-20명 데이터가 오염된다.

---

## 검증 게이트 (local 실행 전 확인)

```bash
# 충돌 마커 없음
rg '<<<<<<<|=======|>>>>>>>' docs/first-week-activation-retention-bridge.md || true

# 기존 이벤트만 인용 (신규 이벤트명 미포함 확인)
rg 'add_flow_started|deed_judged|deed_saved|level_up_viewed|deed_rerolled|deed_save_capped' docs/first-week-activation-retention-bridge.md

# 계승 문서 경로 존재 확인
ls docs/first-real-user-baseline-template.md docs/time-to-value-observation-brief.md docs/activation-milestone-ladder.md

# git 클린 확인
git status --short
```

> 위 파일에서 J1-J4 정의 또는 이벤트명이 이 문서와 다르다면 선행 문서를 기준으로 맞춘다.

---

## Local 실행 프롬프트 (Claude Code 위임용)

```markdown
Infinity Intent: marketing-14 Virtue 첫 주 활성화-리텐션 연결표 작성
Mode: execute_local
Required workflow: Use workflow-master first. Read and follow WORKFLOW-MASTER.md before doing implementation work.
Goal: virtue-rebirth-app/docs/first-week-activation-retention-bridge.md 파일 생성
Context:
  - 현재 작업 디렉토리: /home/ubuntu/dev/virtue-rebirth-app
  - 참조 파일: docs/first-real-user-baseline-template.md, docs/time-to-value-observation-brief.md, docs/activation-milestone-ladder.md
  - Cloud draft: infinity repo artifacts/marketing-14/first-week-activation-retention-bridge-draft.md
Prepared findings: 위 draft 파일의 전체 내용
Allowed: L0/L1 actions only (내부 문서 작성, 커밋, push)
Forbidden: 신규 이벤트·속성·PostHog 설정·코드·대시보드·외부발송·비용·시크릿·권한 변경
Verification:
  rg '<<<<<<<|=======|>>>>>>>' docs/first-week-activation-retention-bridge.md || true  (빈 결과)
  ls docs/first-real-user-baseline-template.md docs/time-to-value-observation-brief.md docs/activation-milestone-ladder.md
  git status --short  (draft 파일 1개만)
Report back to: infinity repo reports/marketing-14/{timestamp}-local.md
```
