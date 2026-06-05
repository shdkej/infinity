# Virtue 막힘 지점 넛지 경계표

> **문서 역할**: prelaunch 첫 10명 관찰 전, 기존 이벤트 조합별 "도움을 줄 수 있는 시점"과
> "건드리지 말아야 할 시점"을 미리 고정해 저장 강요·J3 정상 종료 오독·cap/availability 구간
> 전환 압박을 줄이는 내부 경계표.
> **금지선**: 신규 이벤트·속성·카피·tracking/privacy·PostHog dashboard·코드·배포·공개발송·비용 변경 0.
> **계승 원장**: `MARKETING_LEARNINGS.md`, `marketing-31`(Product Body vs Bumper),
> `marketing-39`(Human-AI Readiness Trace), `marketing-33`(Activation Candidate Registry).

---

## §0 계승한 기준

| 기준 | 내용 | 출처 |
|---|---|---|
| First value 매핑 | J1/J2/J4 = `deed_saved`:183 / J3 = `deed_judged`:106 | marketing-06, MARKETING_LEARNINGS.md |
| J3 정상 종료 | `deed_judged` 후 `deed_saved` 없이 닫힘 = 정상 (이탈 아님) | marketing-21, marketing-31 |
| `deed_save_capped` 의미 | 30덕 상한 early-return = availability/friction. upgrade demand·monetization intent 아님 | marketing-28, MARKETING_LEARNINGS.md |
| 막힘 4분류 | B-LOST(길 잃음) / B-MISMATCH(결과 불일치) / B-AVAIL(가용성 차단) / B-NORMAL(정상 종료) | marketing-31 |
| 범퍼 원칙 | B-NORMAL에는 범퍼 금지. B-AVAIL은 availability 안내만. B-MISMATCH는 제품 문제(범퍼 불가) | marketing-31 |
| `deed_rerolled` 해석 | 탐색·학습 행동 (불신 단정 금지, 최대 3회) | marketing-30, MARKETING_LEARNINGS.md |

**Amplitude/Lenny 렌즈 적용 (source note 요지)**:
- 넛지는 팝업 형식이 아니라 행동 기반 막힘 지점의 도움이어야 한다
- prelaunch에서는 먼저 정상 종료(B-NORMAL)와 나쁜 마찰(B-LOST/B-MISMATCH)을 분리해야 한다
- 저장 강요, J3 정상 종료 오독, cap/availability 구간 conversion 압박을 줄여야 한다
- source note 원본은 로컬 경로 `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-05-behavior-triggered-onboarding-nudges.md` (본 Heartbeat에서 미확인 → rationale 요지로 대체)

---

## §1 막힘 분류 라우팅 (넛지 판단 선행 단계)

넛지 후보를 결정하기 전에 반드시 아래 순서로 막힘을 분류한다.

```
이탈/미완료 감지
    ↓
B-AVAIL? (deed_save_capped:167 early-return · 503 오류 · deed_judge_attempted:135 후 무응답)
    → YES: availability 상태 안내만. upgrade 유도·conversion 압박 금지.
    → NO: 다음 단계
    ↓
J3이고 deed_judged:106 후 deed_saved 없이 종료?
    → YES: B-NORMAL. 아무것도 하지 않는다. 저장 유도 절대 금지.
    → NO: 다음 단계
    ↓
어디서 멈췄는지 확인
    add_flow_started:72 이후 /add 미진입
        → B-LOST (방향 안내 후보)
    /add 진입 이후 입력 중단
        → B-LOST (입력 안내 후보)
    결과 카드 이해 못함/기대 불일치
        → B-MISMATCH (제품 약속 문제, 범퍼로 가릴 수 없음)
    J1/J2/J4에서 deed_judged 후 deed_saved 없이 종료
        → 저장 전 이탈 후보 (prelaunch: 즉각 범퍼 금지, 수기 관찰 우선)
```

---

## §2 심장표 — 이벤트 조합별 넛지 경계

| # | 이벤트 조합 (막힘 지점) | 막힘 분류 | 적용 잡 | 도움 후보 | 띄우지 말아야 할 경우 | 수기 관찰 질문 |
|---|---|---|---|---|---|---|
| N1 | `add_flow_started`:72 후 `/add` 미진입 이탈 | B-LOST | J1/J2/J3/J4 | 홈 화면 기존 CTA 재확인. "오늘 한 일 기록하러 왔어요? →" (기존 UI 활용 우선, 신규 팝업 금지) | J3 탐색(홈을 먼저 살펴보는 B-NORMAL) / 첫 방문 단순 둘러보기 / CTA가 이미 명확한 경우 추가 팝업 금지 | 첫 화면에서 무엇을 하려고 했나? 어떤 행동을 찾았나? 버튼 중 의미가 불명확했나? |
| N2 | `/add` 진입 후 사진·메모 미입력 이탈 | B-LOST | J1/J2/J4 | 기존 placeholder 재확인. "한 줄이면 충분해요" — 신규 팝업 금지, 기존 placeholder가 없는 경우에만 강화 (기존 `:277`에 이미 있음, proposal-only) | 이미 placeholder가 있는 경우 추가 팝업 금지. IS_AI_MODE=false 상태에서 J3 도움 혼입 금지 | 입력 화면에서 무엇이 걸렸나? 뭘 써야 할지 몰랐나, 쓸 말이 없었나? 사진이 없어서였나? |
| N3 | `deed_judge_attempted`:135 후 응답 지연 | B-AVAIL (AI 지연) | J3 | 기존 로딩 인디케이터 여부 먼저 확인 후 보완. "AI가 판정 중이에요" 상태 안내 (기존 UI 없을 때만) | 정상 응답 시간 내 개입 금지. "빠르게 해드릴게요" 약속 카피 금지. 신규 이벤트 추가 금지 | 판정 대기 중에 무엇을 했나? 얼마나 기다렸나? 그냥 닫았나? |
| N4 | `deed_judged`:106 후 `deed_saved` 없이 종료 (J3) | **B-NORMAL** | J3 | **아무것도 하지 않는다** | 어떤 조건에서도 J3 저장 유도 범퍼 금지. J3의 이 종료 패턴은 first value 도달의 정상 흐름 | (저장 없이 닫은 직후 손기록) 결과를 보고 어떤 생각이 들었나? 다른 사람에게 보여주고 싶었나? |
| N5 | `deed_judged`:106 후 `deed_saved` 없이 종료 (J1/J2/J4) | 저장 전 이탈 후보 | J1/J2/J4 | prelaunch 관찰 단계: 즉각 범퍼 금지. 수기 관찰 우선. 충분 관찰 후 별도 Intent로 판단 | 팝업·체크리스트·저장 유도 즉각 배치 금지. J3와 J1/J2/J4 데이터 합산 금지 | 저장 전에 무엇이 걸렸나? 결과가 기대와 달랐나? 저장하고 싶지 않았나? |
| N6 | `deed_save_capped`:167 (30덕 상한 early-return) | B-AVAIL | J1/J2/J4 | "오늘 저장 한도에 도달했어요" — 상태 안내만 (기존 UI 있는지 먼저 확인 후 보완) | "더 저장하려면 업그레이드" 유도 절대 금지. "한도 초과" 부정적 프레이밍 금지. monetization intent·upgrade demand·TTV 종료로 읽지 않는다 | 한도 안내를 보고 어떻게 반응했나? 계속 쓰고 싶었나? 내일 다시 올 것 같나? |
| N7 | `deed_rerolled`:149 (재판정 1~3회) | 탐색·학습 (B-MISMATCH 가능성 있으나 단정 금지) | J3 | **아무것도 하지 않는다** (재판정 자체가 탐색·학습 행동) | "결과가 마음에 안 드시나요?" 팝업 금지. 불신 신호로 읽고 설명 추가 금지. 3회 재판정 후 강제 저장 유도 금지 | 재판정 후 어떤 결과를 기대했나? 다른 입력을 시도했나? 결과가 달라졌을 때 어떻게 했나? |
| N8 | `add_flow_abandoned`:78 (미저장 이탈 이벤트) | B-LOST / B-MISMATCH / B-NORMAL 가능 | J1/J2/J3/J4 | 먼저 잡과 이탈 직전 화면으로 B-분류 후 N1~N7 라우팅 적용 | 이 이벤트 단독으로 막힘 성격 단정 금지. J3 B-NORMAL 포함 가능. 이 이벤트 발화만으로 즉각 개입 금지 | 이 이벤트 직전에 어떤 화면이었나? 결과를 봤는가, 아직 결과 전이었는가? |
| N9 | 첫 세션 종료 후 D1 내 재방문 없음 | 불명확 (관찰 필요) | J1/J2/J3/J4 | prelaunch: 수기 관찰 기록만. 외부 발송 일체 금지 | push 알림·이메일 리마인더 즉각 배치 금지 (approval-needed). prelaunch 소표본으로 이탈 확정 금지 | (손기록) 다시 오지 않은 이유가 있나? 앱이 생각났나? |

---

## §3 잡별 넛지 가능 구간 요약

| 잡 | first value 이벤트 | B-NORMAL 구간 | 넛지 가능 구간 | 절대 금지 구간 |
|---|---|---|---|---|
| J1 기록형 | `deed_saved`:183 | 없음 | N1(방향 안내), N2(입력 안내), N6(cap 상태 안내) | N5 즉각 저장 유도, N6 upgrade 유도 |
| J2 누적형 | `deed_saved`:183 | 없음 | N1(방향 안내), N6(cap 상태 안내) | N6 upgrade·monetization 유도, 저장 전 전환 압박 |
| J3 AI 호기심형 | `deed_judged`:106 | N4(deed_judged 후 미저장 종료) | N3(AI 지연 상태 안내만) | N4 저장 유도(어떤 경우도), N7 불신 개입, N8에서 J3 미저장=이탈 단정 |
| J4 회고형 | `deed_saved`:183 | 없음 | N1(방향 안내), N2(입력 안내) | N5 즉각 저장 유도 |

---

## §4 Prelaunch 넛지 금지선

1. **J3 저장 유도 금지** — `deed_judged`:106 후 저장을 유도하는 팝업·체크리스트·힌트·카피를 붙이지 않는다. J3 저장 없는 종료는 first value 도달의 정상 흐름이다.
2. **B-AVAIL 구간 conversion 압박 금지** — `deed_save_capped`:167·503·지연 구간에서 "업그레이드", "더 쓰려면", "한도 초과" 전환 압박을 하지 않는다. `deed_save_capped` = monetization intent·upgrade demand 아님.
3. **deed_rerolled 개입 금지** — 재판정은 탐색·학습 행동이다. "결과가 마음에 안 드시나요?" 팝업, 추가 설명, 불신 개입을 하지 않는다.
4. **B-MISMATCH를 범퍼로 가리는 시도 금지** — 결과 기대 불일치는 제품 약속·결과 품질 문제이며 체크리스트·툴팁으로 해결할 수 없다.
5. **외부 발송 금지** — prelaunch 넛지는 세션 내 도움에 한정한다. push 알림·이메일 리마인더는 approval-needed다.
6. **신규 이벤트·속성·계측 금지** — 넛지 트리거를 위한 신규 이벤트, 속성, PostHog 설정을 추가하지 않는다. 기존 6개 이벤트(`add_flow_started`, `deed_judged`, `deed_saved`, `deed_rerolled`, `deed_save_capped`, `add_flow_abandoned`)만 사용한다. (`deed_judge_attempted` 참조는 B-AVAIL 상태 안내용 사실 참조만.)
7. **prelaunch 표본으로 전환율/activation%/retention% 판단 금지** — 넛지 추가 후 소표본으로 conversion, activation, retention 비율을 읽지 않는다.
8. **synthetic/mock 세션 혼입 금지** — mock 모드(`임시 판정`, 641 데모시드) 세션의 막힘을 실사용 마찰로 읽지 않는다.

---

## §5 수기 관찰 질문 후보 (prelaunch 손기록용)

**B-LOST 구간 (N1/N2)**:
- 첫 화면에서 무엇을 하려고 했나? 어떤 행동을 찾았나?
- 버튼/라벨 중 의미가 불명확한 것이 있었나?
- `/add`로 가는 경로가 불명확했나, 아니면 `/add`까지 왔는데 입력이 막혔나?

**B-MISMATCH 구간 (N5/N8 일부)**:
- AI 판정 결과를 보고 어떤 생각이 들었나?
- 기대와 다른 결과가 나왔을 때 어떻게 했나? (재시도·저장·무시·이탈)
- 다시 시도하고 싶은 마음이 들었나?

**B-AVAIL (deed_save_capped 후, N6)**:
- 저장 한도 안내를 보고 어떻게 반응했나?
- 계속 사용하고 싶었나, 아니면 그냥 닫았나?
- 내일 다시 와서 쓸 것 같나?

**J3 B-NORMAL (저장 없이 종료 후, N4)**:
- 결과를 보고 어떤 느낌이었나? (저장 여부와 무관)
- 다른 사람에게 결과를 보여주고 싶었나?
- 나중에 다시 와서 써보고 싶었나?

---

## §6 검증 게이트

1. conflict marker 없음: `rg '<<<<<<<|=======|>>>>>>>'` → 0 matches
2. 코드 diff 없음: `git diff --stat apps/web/src apps/ios` → 빈 출력
3. 신규 이벤트 없음: 기존 6개 발화 이벤트 이외의 이름 0 (`deed_judge_attempted` 는 B-AVAIL 사실 참조용, 신규 계측 아님)
4. first value 매핑 계승 확인: J1/J2/J4=`deed_saved`, J3=`deed_judged` 명시 (§0, §3)
5. J3 저장 유도 범퍼 금지선 명시 확인: §4.1, §3 J3 행
6. B-AVAIL 구간 upgrade 유도 금지 명시 확인: §4.2, N6
7. deed_rerolled 개입 금지 명시 확인: §4.3, N7

---

## §7 계승/변경/충돌 분리

- **계승**: first value 매핑(m06/m21/m31), 막힘 4분류(m31), 범퍼 원칙(m31), deed_save_capped=availability(m28), deed_rerolled=탐색(m30), J3 정상 종료(m21/m31/m39), 기존 6개 이벤트 인용(m36 skill-sheet)
- **변경**: 없음
- **충돌**: 없음 (기존 activation/readiness 문서와 J3 정상 종료 경계 일치 확인)
- **durable learning 후보**: "Nudge Boundary Is Classified Before Triggered" — 넛지는 발동 조건보다 막힘 분류가 먼저이며, B-NORMAL은 어떤 넛지도 붙이지 않는 별도 게이트가 필요하다. 단일 실행이므로 관찰 후 승격 판단.

---

## §8 제안(Proposal-Only)

관찰 후 별도 Intent로 처리:
- J3 전용 "저장 없이 결과 공유" 버튼 (`deed_judged` 후 share CTA)
- B-LOST 구간 잡별 맞춤 placeholder 강화 (J3 전용 `/add` 진입 copy)
- D1 이후 리마인더 (approval-needed, 외부 발송 포함)
- mock 모드(`임시 판정`) 라벨 정책 변경 (런타임 모드 정책, 코드 변경 포함)
- B-MISMATCH 후 결과 품질 개선 연구 (별도 Intent)

---

## §9 로컬 실행 지시 (Heartbeat → Local Claude Code)

```
Infinity Intent: marketing-40 Virtue 막힘 지점 넛지 경계표 작성
Mode: execute_local (simple-doc)
Invocation: Prefer existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result. Fall back to bounded `claude --dangerously-skip-permissions -p` if no usable pt pane.
Workflow: simple-doc — direct lightweight prompt acceptable.

Goal: virtue-rebirth-app/apps/web/docs/에 아래 초안을 그대로 복사 후 커밋/푸시.

Source draft: /home/user/infinity/artifacts/marketing-40/friction-point-nudge-boundary-table.md
Target: /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/friction-point-nudge-boundary-table.md

Prepared findings: Heartbeat cloud draft 완료. 기존 이벤트 9개 조합 경계표(N1~N9), 막힘 4분류 라우팅,
잡별 요약, prelaunch 금지선 8개, 수기 관찰 질문, 검증 게이트 7개 포함.

Marketing learning context:
- MARKETING_LEARNINGS.md의 First Value Mapping, Product Body vs Bumper By Job, Availability And Friction 기준 계승
- J3 first value = deed_judged:106 (저장 없는 종료 = 정상)
- J1/J2/J4 first value = deed_saved:183
- deed_save_capped:167 = availability/friction (upgrade demand 아님)

Allowed: L1 actions only (docs-only, 코드 diff 0)
Forbidden: 신규 이벤트·속성·코드·카피·PostHog·배포·외부발송·비용·권한 변경

Verification:
  rg '<<<<<<<|=======|>>>>>>>'  → 0 matches
  git diff --stat apps/web/src apps/ios  → 빈 출력
  git diff --stat apps/web/docs/friction-point-nudge-boundary-table.md  → 1파일만
  first value 매핑 명시 확인 (J1/J2/J4=deed_saved, J3=deed_judged)
  J3 저장 유도 금지 명시 확인

Report back to: /home/user/infinity/reports/marketing-40/{timestamp}-local.html
HTML report contract: <html, <body, axis ax1, axis ax2, <details 포함 필수.
```
