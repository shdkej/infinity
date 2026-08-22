# marketing-128 첫 실행 세트

상태: `HOLD_UNTIL_ITEM_SPLIT` · 공개 게시/공개 링크/계정 조작 없음

이번 피드백으로 기존 첫 실행 세트의 상품 묶음 초안은 폐기한다. 구매 기록에 함께 적힌 항목을 그대로 한 게시물로 쓰지 않으며, 관련성이 있다는 이유만으로도 자동으로 묶지 않는다.

## 실행 전 필수 작업

1. 원본 구매·준비 기록에서 실제 개별 상품명과 옵션을 다시 확인한다.
2. 개별 상품마다 별도 `candidate_id`를 만든다. 구매 기록의 묶음명은 후보명이 아니다.
3. 개별 상품의 실제 사용 장면 또는 사용 근거를 확인한다. 확인 전에는 구매·준비 사실만 기록하고 훅을 만들지 않는다.
4. 서로 다른 상품을 한 글에 묶으려면 같은 문제와 같은 장면을 공유한다는 근거를 별도로 남긴다.
5. 상품·옵션·가격·재고·Sharelink 동일성을 게시 직전에 재확인하고, 공개 게시 승인을 별도로 받는다.

## 현재 보류 중인 원본 기록

| source_record | 원본 기록 | 현재 상태 | 다음 확인 |
|---|---|---|---|
| C01 | `여행용 파우치, 칫솔 등 (무인양품)` | 묶음 기록만 확인 | 파우치·칫솔의 실제 개별 상품명과 근거 분리 |
| C02 | `여행용 멀티플러그, 종이세제 (쿠팡)` | 묶음 기록만 확인 | 멀티플러그·종이세제의 실제 개별 상품명과 근거 분리 |
| C03 | `Travel prep · 손톱깎이/수건/빨랫줄` | 준비 묶음만 확인 | 각 항목의 실제 상품·사용 근거 분리 |

현재는 위 세 기록에서 개별 상품 후보를 확정하지 않았으므로 게시 초안, 훅, Sharelink URL을 만들지 않는다.

## 내부 후보 등록부 요약

| candidate_id | identity_confidence | usage_evidence | affiliate_match | decision |
|---|---|---|---|---|
| C01-item-pending | grouped_pending_identity | purchase_only | mismatch/unverified | hold |
| C02-item-pending | grouped_pending_identity | purchase_only | mismatch/unverified | hold |
| C03-item-pending | grouped_pending_identity | purchase_only | mismatch/unverified | hold |

발급된 제휴 상품이 실제 구매품과 다르면 링크를 넣지 않는다. 대체 후보로 사용할 때도 “비슷한 문제를 위한 대체 후보”라고 명시하며, 공개 실행 전에는 사용자 승인을 받는다.
