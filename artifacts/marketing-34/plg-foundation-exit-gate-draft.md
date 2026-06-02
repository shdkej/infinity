# Virtue PLG Foundation Exit Gate — 초안

> 이 파일은 cloud prepare 단계 산출물이다.
> 로컬 Claude Code에서 virtue-rebirth-app의 `apps/web/docs/plg-foundation-exit-gate.md`로 복사 후 검증·커밋한다.

## 로컬 실행 프롬프트

```
Infinity Intent: marketing-34 Virtue PLG Foundation exit gate 문서 작성
Mode: execute_local (simple-doc)
Goal: artifacts/marketing-34/plg-foundation-exit-gate-draft.md의 본문(--- 아래)을
      virtue-rebirth-app/apps/web/docs/plg-foundation-exit-gate.md 로 복사하고
      아래 검증 게이트를 통과한 뒤 커밋·push한다.

Allowed: L1 (doc 1파일 추가, 커밋·push)
Forbidden: 코드/이벤트/속성/카피/계측/대시보드/배포/외부발송/비용/시크릿/권한 변경

Verification:
  1. git diff --stat apps/web/src apps/ios/Sources  → 빈 출력 (코드 변경 0)
  2. git diff --name-only                           → apps/web/docs/plg-foundation-exit-gate.md 1파일만
  3. grep -rn '^<<<\|^===\|^>>>' apps/web/docs/plg-foundation-exit-gate.md → 출력 없음 (conflict marker 0)
  4. grep -c 'deed_saved\|deed_judged' apps/web/docs/plg-foundation-exit-gate.md → 양수 (기존 이벤트 인용 확인)
  5. HEAD == origin/master (fast-forward만)

Report back to: infinity repo reports/marketing-34/{timestamp}.html
  (HTML report contract 준수: <html, <body, axis ax1, axis ax2, <details 포함)
```

---

# Virtue PLG Foundation Exit Gate

> Virtue prelaunch 문서 체계가 완비된 상태와 첫 사용자 데이터를 읽을 수 있는 상태 사이에
> 반드시 통과해야 할 최소 조건 목록이다.
> 이 게이트를 통과한 뒤에야 activation bundle, D7 second value, source promise fit을
> 첫 10~20명 또는 7일 데이터와 단일 기준으로 대조할 수 있다.

## §0 이 문서의 역할

PLG 단계 모델에서 **Foundation**은 "측정 가능한 상태와 해석 금지선을 잠그는" 준비 단계다.
Foundation이 완비되지 않으면 첫 사용자 데이터를 받더라도:

- 어떤 기준으로 "활성화됐다"고 볼지 문서마다 달라진다
- 작은 표본을 어느 기준으로 읽어야 할지 몰라 과대해석하거나 방치한다
- "Foundation → Activation"이 아닌 "Foundation 도중에 결론 내리기"가 일어난다

이 게이트는 "좋은 숫자를 만든다"가 아니라 **"읽을 준비가 됐는가"** 를 묻는다.

## §1 단계 정의

| 단계 | 설명 | 완료 신호 |
|------|------|----------|
| Foundation | 첫 사용자 데이터가 오기 전 내부 기준을 잠그는 단계. 코드·이벤트·문서·관찰 양식을 고정한다 | 이 게이트 체크리스트 통과 |
| Activation | 첫 10~20명 또는 7일 관찰 데이터를 기준 대비 손기록으로 읽는 단계. 숫자 산출보다 정성 질문이 먼저 | 첫 관찰 세션 완료 |
| Interpretation | Activation 관찰 완료 후 기준 대비 이상/정상 판단을 시작하는 단계. PMF/전환율/retention% 확정은 이 단계 이후 별도 Intent | 관찰 완료 + 금지선 확인 |

> **주의**: 첫 10명 데이터가 도착했다고 Foundation이 자동으로 완료되지 않는다.
> 아래 체크리스트를 모두 통과했을 때만 Activation 단계로 진입한다.

## §2 Foundation Exit Gate 체크리스트

아래 7개 항목이 **모두** YES여야 게이트를 통과한 것이다.
하나라도 NO이면 해당 항목을 먼저 완비한다.

### G1. First Value Mapping 고정

- [ ] J1/J2/J4 first value = `deed_saved`(183)로 문서화됨
  - 참조: `activation-candidate-registry.md` §2 등록부, `first-session-jtbd-matrix.md`
- [ ] J3 first value = `deed_judged`(106)로 문서화됨 (저장 없이 닫힘 = 정상 종료 명시)
- [ ] J3 judged−saved 갭을 이탈로 단정하지 않는다는 금지선이 최소 1개 문서에 명시됨

### G2. Activation Bundle 등록 완료

- [ ] J1~J4별 activation bundle(A1~A4)이 `activation-candidate-registry.md`에 등록됨
- [ ] 관찰 window W-IMM(첫 세션)과 W-CONF(D7)가 구분돼 있음
- [ ] 각 bundle이 기존 발화 이벤트 6종 이내에서만 구성됨 (신규 이벤트 0)
  - 허용 이벤트: `add_flow_started`(72) · `deed_judged`(106) · `deed_rerolled`(149) · `deed_save_capped`(167) · `deed_saved`(183) · `level_up_viewed`(199)

### G3. D7 Second Value 관찰 양식 준비

- [ ] D7 재가치 질문이 `first-week-activation-retention-bridge.md` 또는 `retention-predictive-activation-brief.md`에 있음
- [ ] D7 복귀를 retention 확보 단정으로 읽지 않는다는 금지선이 명시됨
- [ ] small sample depth를 비율이 아닌 정성으로 읽는 규칙이 명시됨

### G4. Traffic Source 분류 준비

- [ ] `traffic-source-reading-boundary-table.md`에 A(사람 실사용)/B(메이커 self-test)/C(synthetic·mock)/D(플랫폼 차이)/E(agent·API) 5행이 있음
- [ ] 분류가 판독에 선행한다는 원칙이 명시됨
- [ ] synthetic/mock/self-test를 사람 데이터에 섞지 않는 금지선이 있음

### G5. Source Promise Fit 정의

- [ ] J1~J4 각 잡에 대해 "이 잡을 부르는 진입 경로"가 최소 1개 문서에 명시됨
  - 참조: `first-session-jtbd-matrix.md` · `minimum-viable-audience-brief.md` · `traffic-source-reading-boundary-table.md` 중 1개 이상
- [ ] 유입 경로 × first value 매핑을 기록할 칸이 `first-real-user-baseline-template.md`에 있음
- [ ] "유입 문장 ≠ activation" 금지선이 명시됨 (클릭·방문만으로 PMF/전환율 확정 불가)

### G6. Availability/Friction 분리 준비

- [ ] `deed_save_capped`(167), 503, 지연을 availability/friction으로 읽는 규칙이 문서화됨
- [ ] availability 구간을 activation window 집계에서 제외한다는 규칙이 있음
- [ ] cap = monetization/upgrade demand로 읽지 않는다는 금지선이 있음
  - 참조: `prelaunch-monetization-boundary-brief.md` · `onboarding-metrics-reading-table.md`

### G7. 해석 금지선 목록 최종 확인

Foundation Exit Gate를 통과하기 직전, 아래를 한 번 더 확인한다:

- [ ] 첫 10~20명 관찰을 전환율/리텐션/PMF/activation%로 산출하지 않는다
- [ ] 외부 벤치마크(타사 activation rate 등)를 Virtue 합격선으로 쓰지 않는다
- [ ] 한 명의 신호를 잡 전체 결론으로 확정하지 않는다
- [ ] J3 judged−saved 갭을 가치 부재로 단정하지 않는다
- [ ] activation bundle·window 구성을 사후에 바꾸지 않는다 (cherry-pick 금지)

## §3 게이트 통과 후 Activation 진입 순서

G1~G7이 모두 통과되면 아래 순서로 진행한다:

1. `first-real-user-baseline-template.md`의 첫 관찰 행 준비 (사람 실사용 A 분류 확인)
2. `first-60-second-value-observation-script.md`로 60초 관찰 대본 사전 숙지
3. `first-session-friction-observation-protocol.md`의 F1~F9 태그 인지
4. 첫 세션 직후: traffic source 분류 → activation bundle 대조 → 60초 도달 여부 → F 태그 기록
5. D7 도달 시: `first-week-activation-retention-bridge.md` D7 질문 대조

> Activation 단계 데이터는 결론이 아니라 다음 Foundation 개선 재료다.

## §4 참조 문서

이 문서에서 인용하는 기존 문서 목록이다. 신규 이벤트·속성·카피·계측·대시보드 변경은 없다.

| 문서 | 게이트 | 역할 |
|------|--------|------|
| `activation-candidate-registry.md` | G1, G2 | activation bundle A1~A4, window W-IMM/W-CONF |
| `first-session-jtbd-matrix.md` | G1, G5 | J1~J4 first value/성공 지표/마찰 |
| `first-real-user-baseline-template.md` | G5, §3 | 첫 10~20명 기록 양식, 유입 경로 칸 |
| `time-to-value-observation-brief.md` | G1 | TTV 관찰 기준, first/second value 정의 |
| `first-week-activation-retention-bridge.md` | G3, §3 | D7 second value 연결표 |
| `onboarding-metrics-reading-table.md` | G3, G6 | D1/D7 재가치 질문, drop-off 해석 주의 |
| `retention-predictive-activation-brief.md` | G3 | D7 depth 정성 읽기 |
| `traffic-source-reading-boundary-table.md` | G4, G5 | 트래픽 분류 5행 |
| `minimum-viable-audience-brief.md` | G5 | 첫 10명 후보 조건, 진입 경로 |
| `prelaunch-monetization-boundary-brief.md` | G6 | cap/availability 분리 |
| `first-60-second-value-observation-script.md` | §3 | 60초 관찰 대본 |
| `first-session-friction-observation-protocol.md` | §3 | F1~F9 마찰 태그 |

---

> 이 문서는 internal-doc. 공개 카피·코드·이벤트·대시보드·배포·외부 발송 변경 0.
> 신규 이벤트·속성·카피·계측·대시보드 0. 외부 벤치마크 수치를 Virtue 합격선으로 쓰지 않음.
