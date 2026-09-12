# 첫 6편 적용 예시 — 추상 소재 카드 (내부 `hold` 검증용)

> 이 문서는 사용자가 승인한 범위 정정입니다. ‘첫 6편’은 실제 인물·장소·브랜드·상품을 추천하거나, 대본·촬영·게시를 제안하는 목록이 아닙니다. 모든 카드는 식별 불가능한 **추상 소재**이며, 정보가 부족할 때 같은 상태 규칙이 `hold`로 작동하는지를 검증합니다.

## 공통 판정

- 카드 수: 6개 — 사람·공간·물건 각 2개
- 모든 카드: `decision: hold`, `evidence: []`, `relationship_status: unknown`, `rights_status: unknown`, `privacy_status: unknown`, `asset_status: unknown`, `external_action: none`
- 금지: 실명, 상호, URL, 가격, 이미지, 위치, 성능·사실 주장, 순위, CTA, 대본, 촬영·게시·연락·구매
- 공통 재개 기준: 대상 식별을 목적으로 하지 않는 내부 검증 기록에, 열린 근거와 locator, 관계 고지/관계 없음 확인, 권리·프라이버시·자산 상태 확인이 모두 채워진 경우에만 재판정한다. 이 문서 자체는 재개를 실행하지 않는다.

## P1 — 공개 동의가 확인되지 않은 대화형 인물 기록

```yaml
card_id: KR-ABSTRACT-P1
axis: person
scene: "일상 선택의 이유를 말하는 비식별 인물 기록"
constraint: "발화·초상·관계와 공개 동의가 확인되지 않음"
decision: hold
decision_reason: "대상 적합성보다 동의·관계·권리 정보가 먼저 필요함"
hold_reason: "열린 근거와 locator가 없고, 공개 동의·관계·권리·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 공개 동의, 관계 고지 또는 관계 없음, 사용 권리와 자산 상태를 확인해 남김"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: unknown
public_access_status: not_applicable
safety_route_status: not_applicable
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## P2 — 작업 방식이 미확인인 관찰형 인물 기록

```yaml
card_id: KR-ABSTRACT-P2
axis: person
scene: "반복 작업의 제약을 관찰하는 비식별 인물 기록"
constraint: "관찰 근거·동의·관계·자산 상태가 확인되지 않음"
decision: hold
decision_reason: "관찰을 추천이나 해석으로 바꾸는 근거가 없음"
hold_reason: "근거·locator·공개 동의가 없고 관계·권리·프라이버시·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 관찰 근거와 locator, 공개 동의, 관계 고지 또는 관계 없음, 권리·프라이버시·자산 상태를 확인함"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: unknown
public_access_status: not_applicable
safety_route_status: not_applicable
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## S1 — 공개 접근 여부가 미확인인 조용한 작업 공간 기록

```yaml
card_id: KR-ABSTRACT-S1
axis: space
scene: "집중을 위해 소음과 동선을 줄이는 비식별 공간 기록"
constraint: "공개 접근·안전 경로·정확 위치·촬영 권한이 확인되지 않음"
decision: hold
decision_reason: "공간의 미감보다 접근·안전·권리 확인이 선행돼야 함"
hold_reason: "열린 근거와 locator가 없고 공개 접근·안전 경로·권리·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 공개 접근 가능 여부, 안전·동선 검토, 촬영 권리·자산 상태를 확인하되 정확 위치는 불필요하게 기록하지 않음"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: unknown
public_access_status: unknown
safety_route_status: unknown
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## S2 — 임시 보관 문제를 다루는 비식별 공간 기록

```yaml
card_id: KR-ABSTRACT-S2
axis: space
scene: "한정된 면적에서 물건을 임시로 보관하는 비식별 공간 기록"
constraint: "점유·접근·안전·촬영 권한과 관계 상태가 확인되지 않음"
decision: hold
decision_reason: "공간 사용 방식은 접근·안전·권리 확인 없이 일반화할 수 없음"
hold_reason: "근거와 locator가 없고 공개 접근·안전 경로·관계·권리·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 접근·안전·촬영 권리와 관계 고지 또는 관계 없음을 확인하며, 민감한 위치·동선은 기록하지 않음"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: unknown
public_access_status: unknown
safety_route_status: unknown
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## O1 — 좁은 작업면의 임시 수납을 다루는 물건 기록

```yaml
card_id: KR-ABSTRACT-O1
axis: object
scene: "좁은 작업면에서 임시 수납이 필요한 비식별 물건 기록"
constraint: "기능·소유·관계·권리·자산 상태가 확인되지 않음"
decision: hold
decision_reason: "용도와 제약을 확인하지 않은 물건 설명은 추천으로 오인될 수 있음"
hold_reason: "열린 근거와 locator가 없고 관계·권리·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 기능 근거와 locator, 관계 고지 또는 관계 없음, 권리와 자산 상태를 확인함"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: not_applicable
public_access_status: not_applicable
safety_route_status: not_applicable
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## O2 — 반복 사용의 마찰을 줄이려는 물건 기록

```yaml
card_id: KR-ABSTRACT-O2
axis: object
scene: "반복 사용에서 정리 마찰을 줄이려는 비식별 물건 기록"
constraint: "성능·가격·대안·관계·권리·자산 상태가 확인되지 않음"
decision: hold
decision_reason: "확인되지 않은 효용을 비교·구매 판단으로 확장하지 않음"
hold_reason: "근거와 locator가 없고 관계·권리·자산 상태가 unknown임"
reopen_condition: "내부 기록으로 검증 가능한 기능 근거와 locator, 관계 고지 또는 관계 없음, 권리와 자산 상태를 확인함"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: not_applicable
public_access_status: not_applicable
safety_route_status: not_applicable
asset_status: unknown
external_action: none
reuse_limit: internal-only
```

## 실험 결과

여섯 카드 모두 빈 근거와 `unknown` 관계·권리·자산 상태를 갖기 때문에 `hold` 외의 상태로 전환되지 않습니다. 이는 실제 소재의 적합성이나 국내 사례의 대표성을 증명하지 않으며, 외부 행동을 허용하지 않습니다.
