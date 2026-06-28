# Virtue 온보딩 상태 언어 매핑표

- intent: marketing-91
- status: complete
- created_at: 2026-06-28T2229Z
- scope: L1 docs-only
- source_note:
  - /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-28-onboarding-state-language.md
- supporting_notes:
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/first-session-jtbd-matrix.md
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/activation-candidate-registry.md
  - /home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-28-first-session-three-gates.md
  - /home/ubuntu/workspace/knowledge-lab/infinity/intents/archive/marketing-89.md
  - /home/ubuntu/workspace/knowledge-lab/infinity/intents/archive/marketing-90.md

## 목적

프리런치 Virtue에서는 작은 이벤트 수보다, 이미 존재하는 이벤트 조합과 홈 반환 사례를 어떤 상태 이름으로 읽을지 먼저 고정하는 편이 더 중요하다. 이 문서는 `정상 진행 / 자연 종료 / 마찰 / 상태 모순` 4개 상태 언어를 한 장으로 고정해, 이후 관찰 기록과 implementation handoff가 같은 판독 기준을 쓰게 만든다.

## 판독 원칙

1. 이벤트 수보다 상태 이름을 먼저 읽는다. 같은 `deed_judged` 이후 미저장도 잡 맥락에 따라 자연 종료일 수도 있고 마찰일 수도 있다.
2. 첫 세션 잡 가설을 덮어쓰지 않는다. J1/J2/J4는 `deed_saved`가 가치 닫힘이고, J3만 `deed_judged`가 저장 전 가치 닫힘이다.
3. 반환 홈은 별도 게이트로 읽는다. 홈에서 retained proof와 first-visit empty-state가 함께 보이면 카피 문제가 아니라 `상태 모순`이다.
4. 이 문서는 새 이벤트, 새 카피, 배포 변경을 요구하지 않는다. 기존 이벤트와 이미 관찰된 표면만 재분류한다.

## 4상태 매핑표

| 상태 | 정의 | 대표 이벤트/표면 조합 | Virtue 예시 | 판독 메모 |
|---|---|---|---|---|
| 정상 진행 | 현재 잡이 약속한 가치가 닫히고 다음 표면도 그 결과와 충돌하지 않는 상태 | `add_flow_started -> deed_judged -> deed_saved`, 또는 저장 후 홈/덕행록이 누적 상태로 일관되게 보임 | J1/J2/J4 사용자가 저장까지 끝내고 홈에서 누적 수치·최근 덕행이 맞게 보이는 경우 | 기본 성공 경로. 이후 세부 friction은 별도 메모 가능하지만 상태 이름은 우선 정상 진행으로 둔다. |
| 자연 종료 | 가치가 이미 닫혀 사용자가 더 진행하지 않아도 되는 상태 | `deed_judged` 후 저장 없음, 단 J3 AI 호기심형 맥락에서 해석 | J3 사용자가 AI 판정만 보고 떠난 경우 | `judged - saved` 갭을 자동으로 이탈로 읽지 않는다. J3만 이 상태를 정상적으로 가질 수 있다. |
| 마찰 | 가치 닫힘 전 멈추거나, 좋은 의도는 있었지만 기대 대비 마찰이 커져 진행이 끊긴 상태 | `add_flow_started` 후 저장 전 이탈, J1/J4에서 `deed_judged` 후 미저장, `deed_save_capped`, 입력 기대 부족으로 저장 직전 중단 | 기록형/회고형 사용자가 저장 전에 멈춘 경우, 30덕 상한에 막혀 저장이 중단된 경우 | 이 상태는 실패 낙인이 아니라 개선 후보다. 잡 맥락 없이 수치만 보고 판정하지 않는다. |
| 상태 모순 | 이미 보여준 사용자 상태와 다음 표면이 서로 다른 이야기를 하는 상태 | retained proof 존재 + first-visit empty-state 동시 노출, `stats.count > 0`인데 첫 방문 카피 유지 | 홈에서 `612덕` retained proof와 `아직 비어있어요`/`아직 기록이 없어요`가 함께 보인 사례 | 현재 최우선 보수 대상. 이벤트 부족보다 반환 상태 계약 불일치가 핵심이다. |

## 사례별 빠른 분류

### 1. `deed_judged` 후 미저장

- J3 AI 호기심형이면 `자연 종료`
- J1 기록형, J2 누적형, J4 회고형이면 우선 `마찰`
- 판독 질문: "이 사용자는 저장 자체보다 AI 판정을 보러 왔는가?"

### 2. `deed_save_capped`

- 기본 분류는 `마찰`
- 다만 J2 누적형에서 의도된 제한으로 보일 수 있으므로, 반복 빈도와 저장 맥락을 함께 본다
- 판독 질문: "건강한 제한으로 느껴졌는가, 아니면 가치 닫힘 전 차단처럼 느껴졌는가?"

### 3. 반환 홈 empty-state와 retained proof 동시 노출

- 무조건 `상태 모순`
- `stats.total` 같은 누적치가 남아 있어도, 반환 상태 게이트는 `stats.count > 0` 기준으로 first-visit 카피를 막아야 한다
- 판독 질문: "방금 남긴 것이 정말 남았다는 증거와 첫 방문 문구가 동시에 존재하는가?"

## 운영용 2문장 검증

- `deed_judged` 후 미저장은 J3에선 AI 판정이 가치 닫힘이므로 `자연 종료`가 될 수 있지만, J1/J2/J4에선 저장 전 중단이므로 우선 `마찰`로 읽는다.
- retained proof와 empty-state가 함께 보이는 홈은 수치 부족이 아니라 반환 상태 계약이 깨진 `상태 모순`이다.

## 다음 handoff에 넘길 최소 규칙

1. 관찰표, report, implementation note에서 `이탈` 같은 넓은 단어 대신 위 4개 상태 이름을 먼저 붙인다.
2. 반환 홈 self-audit는 retained proof와 first-visit empty-state 동시 노출을 만나면 자동으로 `상태 모순`으로 분류한다.
3. 이후 구현 intent는 카피 수정, 이벤트 추가, 홈 반환 게이트 보수를 한 intent에 섞지 말고 어느 상태를 줄이려는지 기준으로 자른다.

## Out of Scope

- 새 PostHog 이벤트/속성 추가
- Virtue 코드 수정 또는 배포
- 사용자-facing 카피 반영
- 표본 수치 평가나 전환율 판단
