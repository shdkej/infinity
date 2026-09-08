# T5.2 — 마감 전 Archive 방지 Red 검증

## 판정

**PASS.** `test_pending_replan_leaves_prevent_early_terminalization`은 격리 temporary fixture에서 pending `T5.2`·`T5.3`·`T6.1`이 있을 때 `terminalization_candidates=[]`이며, 활성화 후보가 단 하나의 `work-1 / T5.2`임을 확인한다.

## 수정 반영

- 단위 테스트가 Archive writer·terminal notifier 호출을 확인한다고 했던 표현을 제거했다. 이 테스트의 범위는 dispatcher **plan classification**이다.
- 활성화 후보의 유일성을 명시적으로 assertion했다.
- trace의 중복 top-level `events` 키를 하나의 배열로 합치고, 다음 결정도 T5.2 검토로 갱신했다.

## 범위 한계

이 PASS는 제품 효용, 사용자 행동, 재사용, 직접 WTP, 프로토타입, 배포 또는 release 증거가 아니다. 실제 Archive 전이는 남은 explicit leaf와 Archive 계약을 별도로 통과해야 한다.
