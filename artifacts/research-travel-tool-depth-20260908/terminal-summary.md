# T6.1 — 최종 증거 수렴

## 결론

여행 회수 카드는 **저우선·미검증 가설**로만 유지한다. 동일 과업에서 기존 노트·사진·장소 저장보다 추가 선택 기준을 제공하는 실제 사용자 증거가 없으며, 직접 WTP·반복 사용·가격 수용성도 확인되지 않았다.

## 확인된 내부 증거

1. `evidence-gaps.md`와 `t1-close.md`: 카드 스키마, 실제 선택 기여, 기존 도구 대비 증분가치, 반복성, WTP의 공백과 Stop/Discard 영향을 고정했다.
2. `alternative-explanations.md`와 `t2-red.md`: 기존 저널·사진·장소 저장이 동일 과업을 충족하면 가설을 Discard하며, 탐색·리스트·플래너 수요로 환원되면 Stop이 우선한다.
3. `validation-design.md`, `t3-red.md`, `t3-close.md`: 실제 독립 선택·3필드 카드·수동 시간순 열람·최소수집/삭제만 사전등록했다. 실제 참여자 모집·연락·데이터 수집은 하지 않았다.
4. `prototype-decision.md`, `t4-red.md`, `t4-close.md`: 합성·로컬 fixture lifecycle만 허용하며 `no-build/hold`를 유지한다.
5. `dispatcher-regression.md`, `t5-red.md`, `t5-close.md`: pending T5/T6 leaf가 있으면 terminalization 후보가 생성되지 않는 dispatcher 분류 계약을 검증했고, T6.1 최대 30분에 대해 579분 reserve를 확인했다.

## Red 및 원격 경계

- T1.2, T2.2, T3.2, T4.2, T5.2 Red PASS가 각 문서의 범위·과장 금지·Stop 우선을 검증했다.
- T6.1 활성화 커밋 `0b4cdb386f8adaabbaea957a0a66a736e1f4a7cc`은 생성 시점에 `HEAD == origin/main`이었다.
- 이 문서는 T6.1 closing commit의 원격 일치를 주장하지 않는다. closing commit·원격 SHA는 task completion trace에서 별도로 기록해야 한다.

## 금지된 해석과 다음 경계

이 수렴은 제품 효용, 사용자 행동, 재사용, 직접 WTP, 가격, 프로토타입 승인, 배포 또는 출시 증거가 아니다. 외부 모집·결제·배포·발송은 수행하지 않았으며, Archive 전이는 별도 terminalization cycle의 계약 검토가 필요하다.
