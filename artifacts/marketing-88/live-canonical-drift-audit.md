# marketing-88 Virtue 홈 반환 상태 live/canonical drift audit

- intent: marketing-88
- date: 2026-06-27
- scope: home hero, 누적 카드, 최근 덕행, CTA
- method: live HTML read-only + local home code + prior canonical marketing proposals
- status: completed

## 계승한 기준

- marketing-80: 누적/요약 신호와 `아직 비어있어요` empty-state가 함께 보이면 저장 성공 뒤 신뢰를 깎는다.
- marketing-83: 최근 덕행 섹션은 `전체 이력 0건`과 `오늘 이력 0건`을 구분해야 하며, J3는 `deed_judged`, J1/J2/J4는 `deed_saved` 게이트가 다르다.
- marketing-84 / marketing-86: J1/J2/J4의 canonical return surface는 홈 `최근 덕행`, J3는 `/add` 결과 카드다.

## 비교 표

| Surface | Live 2026-06-27 | Local code | Canonical prior guidance | Drift | Recommended source of truth |
|---|---|---|---|---|---|
| Home hero | `오늘 1덕만 쌓아볼까요?` | `Greeting` 컴포넌트 사용 | recent proposals focus on return-state continuity rather than replaying a first-action push | 반환 세션에서도 첫 행동 유도 톤이 전면에 남아, 이미 가치가 있었던 사용자 상태를 약하게 만든다 | return-state wording should follow the same saved/judged gates used elsewhere; home should not read like a blank first session when value already exists |
| 누적 카드 | `나의 덕력` + `612덕` + `아직 비어있어요. 오늘 1덕만 시작해볼까요?` | `나의 덕력` + `이번 달 +{month}덕 · 어제 +{yesterday}덕` | marketing-80/81/83 all flag that cumulative proof must not coexist with zero-history language | 가장 큰 충돌. live는 누적 proof와 zero-state 보조문구를 한 카드 안에서 동시에 보여 준다 | when `stats.count > 0`, cumulative card should speak from real retained proof, not a blank-state prompt |
| 최근 덕행 | title `아직 기록이 없어요.` + `오늘 사소한 거 하나, 카메라로 콕.` | title `첫 기록이 여기에 쌓여요.` + `오늘 덕 하나만 남기면 결과와 함께 바로 돌아와요.` | marketing-83 says this surface must distinguish new vs return states and act as the primary J1/J2/J4 return surface | live and local are both still empty-state variants, but live regresses further by claiming no record despite visible accumulated score | this surface is the primary source of truth for J1/J2/J4 return state and should reflect saved-history presence before any generic encouragement copy |
| CTA | `오늘 덕 쌓기` | `오늘 덕 쌓기` | marketing-84/86 keep home CTA as next action helper, not primary proof surface | 문구 자체 drift는 없지만, surrounding proof state makes the CTA read like recovery from emptiness instead of a next step after remembered value | CTA can stay secondary; proof/return surfaces must resolve first so the button reads as next action, not contradiction cover |

## 핵심 판단

1. 현재 가장 위험한 drift는 copy 차이보다 상태 규칙 차이다. live 홈은 `612덕`라는 retained proof가 있는데도 zero-history 문장을 두 군데에서 반복한다.
2. local code는 최소한 누적 카드 보조문구를 실제 월/어제 기록 기반으로 바꿨지만, `최근 덕행`은 여전히 `recent.length === 0`만 보고 empty-state를 렌더링한다. 즉 local도 canonical proposal을 완전히 따라가진 못했다.
3. canonical guidance is already stable: J1/J2/J4 return truth belongs on home `최근 덕행`, while J3 keeps `/add` result card as its primary surface. The live page still behaves as if one global empty-state can serve everyone.
4. safest next step is not new copy ideation. It is one implementation/verification slice that makes home return-state gating consistent across hero, cumulative helper, and recent-deeds state.

## 권장 후속 범위

- next implementation intent should inspect the state source behind `stats.total`, `stats.count`, and `recent.length`, then align return-state rendering without changing tracking, privacy, or public messaging beyond the already approved home surfaces.
- verification gate: a return session with retained score must no longer show any sentence semantically equivalent to `아직 기록이 없어요.` unless the product can prove total saved history is truly zero.

## Evidence

- Live home: `https://virtue.oracle.shdkej.com` observed 2026-06-27 10:07 UTC
- Local code: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`
- Prior canonical notes: `marketing-80`, `marketing-81`, `marketing-83`, `marketing-84`, `marketing-86`
