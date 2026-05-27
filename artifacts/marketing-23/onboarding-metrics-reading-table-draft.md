# [Draft] Virtue 온보딩 지표 운영 판독표

> **Cloud 준비 초안** — Local Claude Code가 출처 노트 반영 후 최종 작성.
> 정본 위치: `virtue-rebirth-app/apps/web/docs/onboarding-metrics-reading-table.md`
> 출처 노트: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-27-onboarding-metrics-practice.md`

---

# Virtue 온보딩 지표 운영 판독표

> **용도**: prelaunch 첫 10-20명 관찰 시, 「어느 이벤트를 볼지」가 아니라 「어떤 가치 증거로 해석할지」를 한 표에서 읽는다.
> **기반**: Appcues 온보딩 지표 루프(Activation → TTV → Engagement → Retention)를 Virtue prelaunch 기준에 번역. 신규 계측 0.

## 검증 게이트 (작업 전 확인 — archive 기준 PASS)

| 확인 항목 | 결과 |
|-----------|------|
| `add_flow_started` 발화 위치 | :72 ✓ |
| `deed_judged` 발화 위치 | :106 ✓ |
| `deed_rerolled` 발화 위치 | :149 ✓ |
| `deed_save_capped` 발화 위치 | :167 ✓ |
| `deed_saved` 발화 위치 | :183 ✓ |
| `level_up_viewed` 발화 위치 | :199 ✓ |
| `first-session-jtbd-matrix` 충돌 | 없음 ✓ |
| `time-to-value-observation-brief` 충돌 | 없음 ✓ |
| `first-60-second-value-observation-script` 충돌 | 없음 ✓ |
| `retention-predictive-activation-brief` 충돌 | 없음 ✓ |

## 판독표 — 잡별 온보딩 지표 해석

| 지표 영역 | 정의 | J1 기록형 | J2 누적형 | J3 AI 호기심형 | J4 회고형 |
|-----------|------|-----------|-----------|----------------|----------|
| **Activation Event** | 의도 진입 신호 | `add_flow_started` | `add_flow_started` | `add_flow_started` | `add_flow_started` |
| **First Value (aha)** | 처음으로 가치를 느끼는 순간 | `deed_saved` (저장 후) | `deed_saved` (저장 후) | `deed_judged` (AI 채점, 저장 전) | `deed_saved` (저장 후) |
| **TTV 시작점** | 시계 시작 | `add_flow_started` | `add_flow_started` | `add_flow_started` | `add_flow_started` |
| **TTV 종료점** | 시계 종료 (first value 도달) | `deed_saved` | `deed_saved` | `deed_judged` | `deed_saved` |
| **Drop-off 해석** | `deed_judged` 후 `deed_saved` 없이 종료 | 이탈 후보 | 이탈 후보 | **정상 종료** ← J3 잡 충족 | 이탈 후보 |
| **D1 재가치 신호** | 다음날 재진입 증거 | `deed_saved` 재발생 | `deed_saved` 재발생 | `deed_judged` 재방문 | `deed_saved` 재발생 |
| **D7 재가치 질문** | D7까지 가치 확인 (손기록, 숫자 산출 금지) | D7 내 두 번째 `deed_saved` 있는가? | D7 내 `level_up_viewed` 있는가? | D7 내 `deed_rerolled` 있는가? | D7 내 `level_up_viewed` + `deed_saved` |
| **Depth Signal** | 습관화 가능성 징조 | distinct-day `deed_saved` 횟수 | `level_up_viewed` + 반복 `deed_saved` | `deed_rerolled` 존재 (최대 3회) | `level_up_viewed` + `deed_saved` 조합 |

## 보조 이벤트 해석 가이드

| 이벤트 | 해석 가이드 |
|--------|-------------|
| `deed_save_capped` (:167) | 의도된 early return (저장 캡 도달). **이탈 아님**. |
| `deed_rerolled` (:149) | 호기심·양면 신뢰 신호 (J3 주요 Depth Signal). 최대 3회. |
| `level_up_viewed` (:199) | 누적 payoff를 알아챘는가의 증거 (J2/J4 Depth Signal). |

## 해석 금지선 (prelaunch 엄금)

| 금지 항목 | 이유 |
|-----------|------|
| `deed_save_capped`를 이탈로 단정 | 의도된 마찰 (캡 = 설계된 조기 반환) |
| J3의 `deed_judged` without `deed_saved`를 이탈로 단정 | J3 잡 충족 자연 종료 |
| 503·지연·가용성 차단 중 이벤트를 가치 신호로 계산 | availability ≠ value |
| D7 외부 벤치마크(예: "D7 30%") 목표로 설정 | prelaunch 표본으로 통계 불가 |
| 전환율·리텐션·PMF·% 수치 산출 | 첫 10-20명은 정성 관찰 단계 |
| 한 명 신호로 패턴 확정 | 단일 사례는 신호 아님 |
| `level_up_viewed` 1회로 리텐션 확보 단정 | depth 1회로 충분하지 않음 |

## Synthetic/Test 제외 원칙

- `641`로 시작하는 사용자 ID: 테스트 계정, 제외
- `MOCK` 포함 이벤트: 개발 환경 발화, 제외
- 비정상적으로 빠른 세션 (봇/자동화): 제외

## 이벤트 코드 앵커 (변경 시 재확인)

| 이벤트 | 코드 위치 (archive 기준) | 역할 요약 |
|--------|--------------------------|----------|
| `add_flow_started` | :72 | 의도 진입, TTV 시작점, Activation event |
| `deed_judged` | :106 | AI 채점 완료, J3 First Value |
| `deed_rerolled` | :149 | 재채점 요청, J3 Depth Signal |
| `deed_save_capped` | :167 | 저장 캡 도달 (Early return, 의도된 마찰) |
| `deed_saved` | :183 | 저장 완료, J1/J2/J4 First Value |
| `level_up_viewed` | :199 | 레벨업 확인, J2/J4 Depth Signal |

## 선행 문서 정렬 — 이 판독표가 계승하는 정의

| 선행 문서 | 계승 내용 |
|-----------|----------|
| `first-session-jtbd-matrix` | J1/J2/J4=deed_saved, J3=deed_judged 정의 |
| `time-to-value-observation-brief` | TTV 시작/종료점, first/second value 구분 |
| `first-60-second-value-observation-script` | TTV<60s, add_flow_started 시작, 가용성≠가치 |
| `retention-predictive-activation-brief` | depth signal = 반복 deed_saved, D7 재가치 |
| `activation-milestone-ladder` | setup=add_flow_started, aha=deed_saved/judged, habit=반복 |
| `first-week-activation-retention-bridge` | D1-D7 second value 연결 |
| `first-session-friction-observation-protocol` | drop-off 마찰 태그 F7/F8 |

## 운영 리듬 (관찰 사이클)

1. **첫 세션 중**: `add_flow_started` → `deed_judged`/`deed_saved` 경로 추적 (TTV 측정)
2. **세션 직후**: drop-off 여부 확인 (잡별 해석 금지선 적용)
3. **D1**: 재방문 신호 확인 (판독표 D1 행 참조)
4. **D7**: 정성 D7 재가치 질문 수행 (판독표 D7 행, 숫자 산출 금지, 손기록)
5. **Synthetic 제외**: 관찰 시작 전 `641`/`MOCK` 필터링

---

## Local Claude Code 실행 프롬프트

```
Infinity Intent: marketing-23 Virtue 온보딩 지표 운영 판독표 작성
Mode: execute_local
Required workflow: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present before doing implementation work.
Goal: Appcues 온보딩 지표 루프를 Virtue prelaunch 기준에 번역해 activation/TTV/drop-off/D1-D7 retention을 한 판독표로 묶은 내부 문서 작성
Context:
  - 출처 노트 (필독): /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-27-onboarding-metrics-practice.md
  - 초안 artifact: infinity 레포 artifacts/marketing-23/onboarding-metrics-reading-table-draft.md
  - 정본 위치: virtue-rebirth-app/apps/web/docs/onboarding-metrics-reading-table.md
  - 선행 문서 (충돌 확인용): apps/web/docs/first-session-jtbd-matrix.md, time-to-value-observation-brief.md, first-60-second-value-observation-script.md, retention-predictive-activation-brief.md
Prepared findings:
  - 이벤트 발화 위치 (archive 기준): add_flow_started:72, deed_judged:106, deed_rerolled:149, deed_save_capped:167, deed_saved:183, level_up_viewed:199
  - J1/J2/J4=deed_saved, J3=deed_judged 정의 유지
  - 판독표 초안 (activation/TTV/drop-off/D1/D7/depth signal × J1-J4) 준비됨
  - 선행 4문서 충돌 없음 확인됨
Allowed: L0/L1 actions only (internal-doc only)
Forbidden: 새 이벤트, 코드, 카피, 대시보드, 배포, 외부발송, 비용, 개인정보/트래킹 변경
Verification:
  1. 출처 노트 내용이 판독표에 반영됐는가
  2. 선행 4문서와 J 정의·이벤트 앵커 충돌 없음 확인
  3. 6개 이벤트만 인용 (신규 0)
  4. copy-spec 금지어 신규 카피 없음
  5. git status clean, HEAD==origin 확인 후 L2 agent-approved push
Report back to: infinity 레포 reports/marketing-23/{timestamp}-local.html (결론 2축 양식)
```
