# 국내 미니멀 큐레이션·리뷰 가이드 — 최종 내부 브리프

## 결론

이 가이드는 ‘국내 성공 공식’이나 추천 목록이 아니라, **조건부 선택 기록을 위한 내부 템플릿**이다. T2.3은 실제 후보·촬영·게시 없이 상태 규칙이 안전하게 작동하는지만 확인했다.

## 빈 카드 `hold` 상태 실험

> 이 카드는 실제 대상·브랜드·공간·인물을 지칭하지 않는 내부 검증용 빈 카드입니다. 구매·방문·구독·상담·촬영·게시를 제안하지 않습니다.

```yaml
card_id: KR-TEST-HOLD-01
axis: object # 스키마 열거값일 뿐 식별된 물건이 아님
scene: null
constraint: null
decision: hold
decision_reason: "필수 검증 메타데이터가 없음"
hold_reason: "열린 원문과 locator가 없고, 관계·권리·프라이버시·자산 상태가 unknown이다"
reopen_condition: "열린 원문과 locator, 관계 고지 또는 관계 없음 확인, 권리·프라이버시·자산 상태를 내부적으로 검증해 기록한다"
viewer_condition: null
evidence: []
relationship_status: unknown
relationship_disclosure: "확인 불가"
rights_status: unknown
privacy_status: unknown
public_access_status: not_applicable
safety_route_status: not_applicable
asset_status: unknown
reuse_limit: "internal-only; no asset, contact, filming, or posting"
external_action: none
reviewed_at: "2026-09-12T01:42:05Z"
```

## 검증 결과

| 점검 | 결과 |
|---|---|
| 빈 카드가 실제 대상·URL·이미지·사실 주장·가격·위치·CTA를 포함하지 않는가 | 통과 |
| 빈 `evidence`, `relationship_status=unknown`, `asset_status=unknown`이 `hold`로 귀결되는가 | 통과 |
| `hold_reason`과 관찰 가능한 `reopen_condition`이 모두 비공란인가 | 통과 |
| `draftable` 전환·30/45/60초 대본 생성·외부 행동을 수행하지 않았는가 | 통과 |
| 외부 실행(후보 확정·촬영·공개·연락·구매·제3자 자산 사용)이 0건인가 | 통과 |

## 역할 수렴과 비적용 경계

- **Planner:** 빈 카드·상태 게이트·재개 조건만으로 완료를 판정한다.
- **Developer:** 스키마 필드와 판정기 결과를 재현 가능한 형태로 남긴다.
- **Marketer:** 상업·추천·브랜드 모방으로 읽힐 문구를 제거한다.
- **Operator:** 실제 후보·촬영·공개·외부 연락·자산 사용은 별도 승인 전 금지한다.

이 실험은 카드 상태 전이만 검증한다. 실제 후보 적합성, 콘텐츠 성과, 공개 가능성, 구매·방문 판단을 주장하지 않는다.

