# Virtue value-per-session 판독표

> Mixpanel 2026 AI/product analytics 렌즈: AI 제품에서 fewer actions ≠ less value.  
> Virtue prelaunch 첫 10명/첫 7일 관찰에서 세션당 이벤트 수 대신 세션당 가치를 읽는 내부 판독 기준.
>
> **이 파일은 Infinity cloud prepare 초안이다.**  
> 목적지: `virtue-rebirth-app/apps/web/docs/value-per-session-reading-table.md`

## §0 전제 · 이벤트 앵커

이 문서는 파생물이다. 결론 충돌 시 아래 원본 문서가 우선한다:
- `first-session-jtbd-matrix.md` (J1~J4 잡 정의, first value mapping)
- `ai-outcome-proxy-dictionary.md` (proxy 5종 정의)
- `activation-candidate-registry.md` (A1~A4 activation 후보 묶음)
- `MARKETING_LEARNINGS.md` (durable learning 원장)

이벤트 앵커 (현행, drift 0 기준):

| 이벤트 | 줄 번호 | 비고 |
|---|---|---|
| `add_flow_started` | :72 | 흐름 진입 |
| `add_flow_abandoned` | :78 | 미저장 이탈 |
| `deed_judged` | :106 | AI 판정 완료 |
| `deed_judge_attempted` | :135 | 판정 시도 |
| `deed_rerolled` | :149 | 재판정 (최대 3회) |
| `deed_save_capped` | :167 | 30덕 상한 early-return |
| `deed_saved` | :183 | 저장 완료 |
| `level_up_viewed` | :199 | 레벨업 확인 |

First value 매핑 (재정의 없음):
- **J1(기록형), J2(누적형), J4(회고형)** = `deed_saved`:183
- **J3(AI 호기심형)** = `deed_judged`:106 (저장 없이 닫힘 = 정상 종료)

## §1 왜 "세션당 이벤트 수"로 읽으면 안 되나

Mixpanel 2026 AI/product analytics 핵심 렌즈:

> AI 제품에서 fewer actions가 빠른 가치 도달일 수 있다.  
> raw usage volume보다 workflow 안의 measurable value가 중요하다.

| 일반 앱 오독 | AI 제품에서의 실제 의미 |
|---|---|
| 이벤트 수 많음 = 참여 높음 | AI가 빠르게 답하면 fewer actions로 가치 도달 |
| 짧은 세션 = 나쁨 | J3는 결과 카드 1번 확인 후 종료도 first value 닫힘 |
| 저장 없음 = 이탈 | J3 judged-without-saved = 정상 종료 (V-DONE) |
| 재시도 많음 = 불만 | `deed_rerolled` = curiosity/exploration 신호 가능 |
| 클릭 많음 = 참여 높음 | availability 차단(503/지연/cap)으로 발생한 재시도일 수 있음 |

핵심: **측정 단위를 "이벤트 수"에서 "가치 도달 여부"로 전환한다.**

## §2 세션 가치 4분류

| 분류 | 기호 | 정의 |
|---|---|---|
| 성공 (Value-Yes) | V-YES | 잡별 first value 이벤트에 도달함 |
| 정상 종료 (Value-Done) | V-DONE | J3에서 `deed_judged` 후 저장 없이 종료. 잡 충족. 이탈 아님. |
| 보류 (Value-Pending) | V-PEND | First value 미도달, 단 availability/외부 차단 원인. 판독 보류. |
| 마찰 (Value-Lost) | V-LOST | First value 미도달, availability 외 원인. 잡별 검토 필요. |

> **V-DONE은 V-YES와 다른 별도 분류다.** J3 외의 잡(J1/J2/J4)에서 저장 없이 끝나면 V-YES가 아닌 V-LOST 후보다.

## §3 심장 표 — 잡 × 세션 패턴 × 가치 판독

| 잡 | 세션 패턴 | 기존 이벤트 증거 | 가치 분류 | 오독 경고 |
|---|---|---|---|---|
| **J1** 기록형 | 입력 후 `deed_saved` 즉시 | `add_flow_started`→`deed_saved` | **V-YES** | 없음. J1 정상 성공 |
| **J1** | `deed_judged` 후 저장 없이 종료 | `deed_judged` 있음, `deed_saved` 없음 | **V-LOST** 후보 | J3 판독 기준 적용 금지. J1 first value = 저장 |
| **J1** | `deed_save_capped` 후 종료 | `deed_save_capped`:167 | **V-PEND** | availability (30덕 상한). monetization 수요로 읽지 않음 |
| **J2** 누적형 | `deed_saved` 후 `level_up_viewed` | `deed_saved`:183→`level_up_viewed`:199 | **V-YES** (depth) | 없음 |
| **J2** | `deed_saved` 후 `level_up_viewed` 없이 종료 | `deed_saved` 있음 | **V-YES** (기본) | `level_up_viewed`는 depth signal이지 first value 조건 아님 |
| **J2** | `deed_save_capped` 후 종료 | `deed_save_capped`:167 | **V-PEND** | J2 누적 payoff 도달 전 availability 차단. upgrade 수요 환산 금지 |
| **J3** AI 호기심형 | `deed_judged` 후 저장 없이 종료 | `deed_judged`:106, `deed_saved` 없음 | **V-DONE** | J1/J2/J4 기준 적용 금지. J3 저장 전 종료 = 정상 |
| **J3** | `deed_rerolled` 1~3회 후 종료 | `deed_rerolled`:149 | **V-DONE** 또는 curiosity depth | `deed_rerolled` = 불만 단정 금지. 호기심/탐색 가능 |
| **J3** | `deed_judged` 없이 종료 | `add_flow_started`:72, `deed_judged` 없음 | **V-LOST** 후보 | AI 판정 전 이탈. first value 미도달 |
| **J4** 회고형 | `deed_saved` | `deed_saved`:183 | **V-YES** | 없음 |
| **J4** | `deed_save_capped` 후 종료 | `deed_save_capped`:167 | **V-PEND** | availability |

## §4 수기 관찰 판독 순서

출시 후 첫 10명 / 첫 7일 관찰 시 아래 순서로 읽는다 (신규 계측 없음).

1. **traffic 분리 먼저**: 사람 실사용(A) / 메이커 self-test(B) / synthetic/mock(C). C는 집계 제외.
2. **잡 추정**: 첫 세션 맥락으로 J1~J4 추정. 명확하지 않으면 "미분류"로 기록.
3. **availability 먼저 확인**: `deed_save_capped` 발화 또는 503/지연 흔적 → V-PEND. 이후 진행.
4. **first value 도달 확인**: 잡별 기준으로 V-YES / V-DONE / V-LOST 분류.
5. **오독 금지선 대조** (§5 참고).

## §5 오독 금지선

1. `deed_save_capped`:167 = availability/friction. monetization intent / upgrade 수요로 읽지 않는다.
2. J3 judged-without-saved = V-DONE. V-LOST로 읽지 않는다.
3. `deed_rerolled`:149 최대 3회 = curiosity 가능성 포함. "불만" 단정 금지.
4. 짧은 세션 = J3는 V-DONE일 수 있음. "짧음=나쁨" 단정 금지.
5. 이벤트 수 많음 = availability 반복 재시도일 수 있음. "많음=참여 높음" 단정 금지.
6. 세션 가치 분류는 10명 미만 / 7일 미만에서 전환율·% 산출로 이어지지 않는다.
7. synthetic/mock 세션(`641` 데모시드, `MOCK` 모드, localStorage 반복, 메이커 자체 테스트)을 사람 세션과 합산하지 않는다.
8. **이 문서는 판독 렌즈이지 계측 변경 지시가 아니다.** 신규 이벤트·속성·tracking·privacy·대시보드·코드·배포·외부발송·비용·권한 변경 0.

## §6 선행 문서와의 연결

| 이 문서의 질문 | 선행 문서 |
|---|---|
| J1~J4 잡 정의 | `first-session-jtbd-matrix.md` |
| Proxy 타입(activity/acceptance/curiosity/friction/retention) | `ai-outcome-proxy-dictionary.md` |
| Activation 후보 묶음(A1~A4), W-IMM/W-CONF window | `activation-candidate-registry.md` |
| 세션당 수기 관찰 타이밍, 60초 체크 | `first-60-second-value-observation-script.md` |
| 막힘 4분류(B-LOST/B-MISMATCH/B-AVAIL/B-NORMAL) | `product-body-vs-bumper-boundary-table.md` |
| PQL/upgrade 신호 경계 | `post-launch-pql-upgrade-signal-boundary-table.md` |
| AI 판정 신뢰/제어 | `ai-judgment-trust-control-observation-boundary-table.md` |
| Human-AI readiness trace | `human-ai-readiness-trace-map.md` |

## §7 prelaunch 금지선

이 판독표는 아래를 산출하거나 결정하지 않는다:

- 전환율 (V-YES / 전체)
- activation rate / D7 retention / PMF 점수
- PQL 후보 확정
- 업그레이드 수요 / 유료화 트리거 확정
- 새 이벤트 / 속성 / tracking / privacy / 대시보드 변경
- 공개 카피 / 가격표 / 외부 발송
- 코드 / 배포 / 비용 / 권한 변경

**이 표의 유일한 역할**: 기존 이벤트를 기반으로 첫 관찰에서 "이벤트 수 = 가치"라는 오독을 막는 렌즈 제공.

---

## 로컬 실행 지침 (Infinity → virtue-rebirth-app)

```
Infinity Intent: marketing-42 Virtue value-per-session 판독표 작성
Mode: execute_local
Goal: 이 파일을 virtue-rebirth-app/apps/web/docs/value-per-session-reading-table.md로 복사·커밋·push
Allowed: docs 1파일 추가만. 코드/tracking/privacy/copy/배포/비용 변경 0.
Verification gate:
  - conflict marker 0
  - 신규 이벤트/속성 0
  - 이벤트 앵커 drift 0 (rg 72/78/106/135/149/167/183/199)
  - 코드 diff 0 (git diff --stat apps/web/src apps/ios 빈 출력)
  - source note path 인용 포함
Marketing learning: MARKETING_LEARNINGS.md 먼저 읽고 승격 후보 "Value Per Session Is Classification First, Count Never" 판단
Report back: reports/marketing-42/{timestamp}.html (ARTIFACT_RULES.md 양식, HTML report 필수)
로컬 실행 전 §0 앵커를 현재 코드와 대조할 것 (drift 있으면 업데이트 후 진행)
```

*출처 노트: `source/external-links/marketing/2026-06-06-ai-value-per-session.md` (로컬 부재 — Intent rationale 요지와 선행 문서 근거로 작성)*
