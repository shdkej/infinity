# T5.1 — 조기 완료 재계획 회귀 테스트

## 목표

마감 전 다수 leaf가 완료됐더라도 명시된 T5/T6 leaf가 남아 있으면 dispatcher가 terminalization 또는 Archive 후보를 만들지 않는지 격리 fixture로 검증한다.

## 결정적 fixture

- `T1.1`, `T4.3`, `T5.1`: `done`
- `T5.2`: `pending`, 의존 `T5.1`
- `T5.3`: `pending`, 의존 `T5.2`
- `T6.1`: `pending`, 의존 `T5.3`
- future deadline을 가진 Active intent

## 기대 결과

1. `terminalization_candidates=[]`
2. `plan_activation_candidates`는 `T5.2`를 가리킨다.
3. handoff는 Active intent를 유지하며 Archive writer·terminal notifier를 호출하지 않는다.
4. 실제 T5/T6 계획이 끝나기 전에는 리서치·제품·사용자 효용·WTP·출시 완료를 주장하지 않는다.

## 범위와 한계

이 회귀는 dispatcher 계획 분류만 검증한다. fixture-only lifecycle, 실제 사용자 행동, 재사용, 직접 WTP, 결제, 프로토타입, 배포 또는 외부 발송의 증거·승인이 아니다.

## 실행

`python3 scripts/test_prepare_dispatch_cycle.py`의 `test_pending_replan_leaves_prevent_early_terminalization`로 격리 temporary fixture에서 실행한다. canonical `INTENTS.md`, Archive lane, 원격 상태는 테스트가 변경하지 않는다.
