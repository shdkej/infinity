# T2.2R Red — 상태 스키마와 `hold` 경계 재검증

**판정: PASS**

## 확인한 규칙

1. 카드 스키마와 판정기·사전 점검표는 `hold`에 `hold_reason`과 `reopen_condition`을 모두 요구한다.
2. `relationship_status`는 `none_confirmed | disclosed | unknown`으로 제한된다. `disclosed`는 `relationship_disclosure`에 고지 위치가 있어야 하며, `unknown`은 강제 `hold`다.
3. `asset_status=unknown`은 강제 `hold`다. 권리·프라이버시의 `unknown` 또는 `fail`, 접근 제한 원문도 `hold`다.
4. 30·45·60초 템플릿에는 모두 시청자 적용 조건 및 사실·출처·관계 고지 슬롯이 있다.
5. `draftable`은 내부 대본 초안 가능 상태일 뿐이다. 실제 후보 확정, 촬영, 외부 연락, 자산 사용, 공개 게시에는 별도 승인이 필요하다.

## 결론

T2.2의 결함은 T2.1R에서 해소됐다. 최소 추가 보완은 필요 없으며, 다음 C2는 실제 후보가 아닌 빈 카드의 `hold` 상태가 재현되는지만 내부적으로 확인한다.

