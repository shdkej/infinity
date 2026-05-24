# Virtue 첫 주 활성화-리텐션 연결표 (Cloud Draft)

> 역할: Prelaunch 단계 첫 10-20명 관찰 시, 유입 문장(어떤 말에 끌렸는가)이 어떤 Job(J1-J4)과 연결되고, 그 잡의 first value → second value → 7일 내 재가치 경험으로 이어지는지를 기록하기 위한 내부 기준표.
> 주의: 이 파일은 cloud 초안이다. 정본은 virtue-rebirth-app apps/web/docs/first-week-activation-retention-bridge.md이다. local Claude Code가 source note를 읽어 보강 후 정본을 작성한다.

---

## §0 이 문서의 역할과 금지선

**역할**: 유입-가치-리텐션 연결의 관찰 기준선. 성패 판정, 전환율 계산, PMF 확인 도구가 아니다.

**근거**: Amplitude/ProductLed 연구에 따르면 신규 획득(acquisition)만으로는 리텐션이 생기지 않는다. 핵심 가치 순간(core value moment)과 활성화 지점(activation point)을 초기에 관찰해야 어떤 유입 경로가 반복 가치로 이어지는지 알 수 있다. Virtue는 prelaunch 단계이므로 수치 판정 대신 10-20명 표본에서 유입-잡-가치 연결 패턴을 정성 관찰하는 것이 목표다.

**금지선**:
- prelaunch 소수 표본(10-20명)에서 통계적 결론 도출 금지
- first/second value 경험 유무를 retention/churn의 직접 원인으로 단정 금지
- 이 표를 신규 이벤트/속성 추가, PostHog 대시보드 설정, 코드 변경의 근거로 사용 금지
- 503/가용성 이슈가 관찰을 차단한 경우, 마케팅 실패로 기록하지 않는다(§4 참조)

---

## §1 J1-J4별 First Value / Second Value 표

| 잡 | 설명 | First Value (aha moment) | 이벤트 | Second Value | 이벤트 | 7일 내 재가치 지표 |
|---|---|---|---|---|---|---|
| **J1 기록형** | 오늘 한 일을 덕행으로 기록하고 싶다 | 첫 덕행이 저장되는 순간 ("내가 기록할 수 있다") | `deed_saved` | 다음 날 또 저장하는 순간 ("습관이 된다") | `deed_saved` (distinct day) | 7일 내 3일 이상 `deed_saved` |
| **J2 누적형** | 내 덕행이 쌓여서 변화를 보고 싶다 | 첫 덕행 저장 후 레벨/덕력 변화를 확인하는 순간 | `deed_saved` → `level_up_viewed` | 두 번째 레벨업 이벤트 발생 순간 | `level_up_viewed` (2nd) | 7일 내 `level_up_viewed` 2회 이상 |
| **J3 AI 호기심형** | AI가 내 덕행을 어떻게 채점하는지 보고 싶다 | AI 채점 결과를 처음 받는 순간 ("AI가 이렇게 보는구나") | `deed_judged` | 채점 결과에 동의/저장하는 순간, 또는 재채점 시도 | `deed_saved` 또는 `deed_rerolled` | 7일 내 `deed_judged` 3회 이상 |
| **J4 회고형** | 내가 어떤 사람인지 덕행 기록을 통해 돌아보고 싶다 | 첫 덕행 저장 후 기존 기록과 함께 보이는 순간 | `deed_saved` | 다른 날 기록을 추가하며 패턴을 느끼는 순간 | `deed_saved` (3일차 이상) | 7일 내 3일 이상 방문 + `deed_saved` |

**이벤트 인용 근거** (기존 코드에서 발화, 신규 이벤트/속성 0):
- `add_flow_started`: `/add` 페이지 진입 시 (기록 의도 신호)
- `deed_judged`: AI 채점 결과 수신 시
- `deed_saved`: 덕행 저장 완료 시
- `level_up_viewed`: 레벨업 화면 조회 시
- `deed_rerolled`: 채점 결과 재시도 시
- `deed_save_capped`: 저장 한도 초과 시 (early-return, 관찰 차단 신호)

---

## §2 첫 10-20명 관찰 행 템플릿

> 한 명당 한 행. Synthetic/test traffic 제외 기준: Heartbeat/bot User-Agent, 개발자 세션, localhost 접근, 내부 테스트 계정.

| 관찰 번호 | 유입 문장/경로 | 추정 잡 | 가용성 이슈 여부 | first value 경험 | first value 이벤트 | 날짜 | second value 경험 | second value 이벤트 | 날짜 | 7일 재가치 경험 | 관찰 메모 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U01 | | | | | | | | | | | |
| U02 | | | | | | | | | | | |
| U03 | | | | | | | | | | | |
| (반복) | | | | | | | | | | | |

**유입 문장 기록 방법**: 사용자가 어떤 문장/설명에 끌려 왔는지 직접 기록하거나 인터뷰 메모로 대체. 자동 추적 아님.

**추정 잡 분류 기준**:
- J1: /add에서 기록을 바로 시작하는가 (기록 의도 우선)
- J2: 레벨/덕력 숫자에 관심을 보이는가
- J3: AI 채점에 먼저 반응하는가
- J4: 이전 기록과 비교하거나 회고 언급이 있는가
- 분류 불명: 비워두고 관찰 메모에 기록

---

## §3 Prelaunch 해석 금지선

아래 해석은 prelaunch 10-20명 표본에서 하지 않는다.

| 금지 해석 | 이유 |
|---|---|
| "J3의 전환율이 낮다" | 표본 크기 부족, J3 유입 문장 자체가 아직 미개발 |
| "first value 미경험자가 50%니 이탈 위험" | 방문 의도/컨텍스트가 달라 분모 동일 비교 불가 |
| "second value까지 간 사람이 0명이니 제품 실패" | prelaunch 단계에서 second value는 시간 문제, 반복 방문 기회 자체가 적음 |
| "7일 재가치가 없다 = 리텐션 0" | 7일을 채우지 못한 신규 가입자 포함, 첫 사용자 시간 보정 필요 |

**허용 해석 예시**: "J1 기록형으로 온 U01은 first value(deed_saved)를 경험했고, 3일 후 재방문해 second value도 경험했다. 유입 문장 A가 J1 잡과 연결되는 신호를 보인다."

---

## §4 운영 경계: 503/가용성 이슈 vs. 마케팅 실패 분리

**원칙**: 사용자가 앱에 도달하지 못했거나 핵심 기능이 동작하지 않은 경우, 이는 마케팅 실패(유입 문장 문제)가 아니라 **관찰 차단(observability block)**이다.

| 상황 | 분류 | 기록 방법 |
|---|---|---|
| 앱 503/404로 접근 불가 | 관찰 차단 | §2 "가용성 이슈 여부" 컬럼에 기록, 유입/잡/가치 분석 제외 |
| `/add` 페이지 로딩 실패 | 관찰 차단 | add_flow_started 미발화 → 관찰 불가로 분류 |
| AI 채점 서비스 오류 | 부분 차단 (J3만 영향) | deed_judged 미발화 → J3 관찰 가능 범위 축소 기록 |
| deed_save_capped (저장 한도 초과) | 부분 차단 | 저장 의도 있었으나 완료 못 함, 관찰 메모에 기록 |
| 정상 동작 중 사용자 이탈 | 마케팅/제품 신호 | 잡/가치 분석 대상 |

---

## §5 선행 문서와의 역할 분리

| 문서 | 역할 | 본 문서와의 관계 |
|---|---|---|
| `activation-milestone-ladder.md` | setup/aha/habit 사다리 정의, J1-J4 매핑 기준 | 본 문서의 first/second value는 ladder의 aha/habit을 계승 |
| `time-to-value-observation-brief.md` | first/second value 시간 간격 계산 기준 | 본 문서 §2의 날짜 기록란의 계산 방식은 TTV brief를 따름 |
| `first-real-user-baseline-template.md` | 첫 사용자 기준선 수기 기록 양식 | 본 문서 §2는 유입-가치 연결에 특화한 확장 템플릿 (중복 아님) |
| `competitive-alternatives-positioning-brief.md` | 포지셔닝 앵커 | 유입 문장의 출처/가설은 이 문서의 §1에서 참조 |

**충돌 없음 확인**:
- J1/J4의 aha = `deed_saved` (ladder §1과 동일)
- J3의 aha = `deed_judged` (ladder §1과 동일)
- J2의 habit = `level_up_viewed` 반복 (ladder §1과 동일)
- `deed_save_capped` = early-return 코드 사실 반영 (ladder §1 일치)
- 신규 이벤트·속성·코드·대시보드·외부발송·비용 0

---

## §6 다음 단계 (이 문서의 사용법)

1. 첫 실사용자 방문 시 §2 템플릿에 즉시 기록 시작
2. 가용성 이슈 발생 시 §4 기준으로 먼저 분류, 마케팅 원인 단정 금지
3. 7일 후 §1 표와 대조해 어떤 유입-잡 조합이 second value까지 이어졌는지 정성 검토
4. 포지셔닝/온보딩/측정 기준 변경은 §3 금지선을 확인한 뒤 별도 Intent로 진행

---

## Local 실행 지시 (execute_local 위임)

```
Infinity Intent: marketing-14 Virtue 첫 주 활성화-리텐션 연결표 작성
Mode: execute_local
Required workflow: Use workflow-master first. Read .agent/workflows/workflow-master.md or WORKFLOW-MASTER.md before doing implementation work.
Goal: apps/web/docs/first-week-activation-retention-bridge.md 작성 및 virtue-rebirth-app master에 push
Context:
  - /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-24-week-one-activation-plg.md (source note, cloud 접근 불가 → local 보강 필수)
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/first-real-user-baseline-template.md
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/time-to-value-observation-brief.md
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/activation-milestone-ladder.md
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/competitive-alternatives-positioning-brief.md
Prepared findings: infinity/artifacts/marketing-14/first-week-activation-retention-bridge.md (cloud 초안)
Allowed: L0/L1 actions only (doc 작성, git commit/push to master non-force)
Forbidden: 신규 이벤트/속성, 코드 변경, PostHog 설정, 대시보드, 외부발송, 비용, 시크릿, L2/L3 without approval
Verification:
  - rg '<<<<<<<|=======|>>>>>>>' apps/web/docs/first-week-activation-retention-bridge.md || true  → 출력 없어야 함
  - rg 'add_flow_started|deed_judged|deed_saved|level_up_viewed' apps/web/docs/first-week-activation-retention-bridge.md → PASS
  - 선행 3문서(first-real-user-baseline-template/time-to-value-observation-brief/activation-milestone-ladder)와 J1-J4 이벤트 매핑 충돌 0 확인
  - git status --short → clean after commit
Report back to: infinity/reports/marketing-14/{timestamp}.md
```
