# T2.1 조건부 사용자 적합성 별점 — Red 수정본

## 산식과 판정

각 축은 0~2점이며 합계 `S`를 `floor(S / 2)`로 환산한다. 근거가 없는 축은 0점이 아니라 `미평가`로 둔다. 핵심 필드가 비어 있는 후보는 숫자 별점을 확정하지 않고 `보류`로 표시한다. 가격·필요 자본은 `capital_risk`로 분리한다.

| 축 | 2점 기준 | 이번 자료의 판정 원칙 |
|---|---|---|
| 반복 현금흐름 | 기간·정의가 있는 이익/현금흐름과 지속성 | 매출·이익 숫자만 있고 기간/정의가 없으면 미평가 |
| 1인 운영 가능성 | owner hours와 업무·자동화/외주 범위 확인 | owner hours 미확인이면 미평가 |
| 사용자 강점 활용 | 제품·콘텐츠·자동화의 구체적 개선 경로 | 후보별 근거가 없으면 미평가 |
| 인수 후 개선 여지 | 저활용 채널·가격·전환 기회 확인 | 판매자 주장만 있으면 미평가 |
| 검증 가능성 | 가격·핵심 재무·이전 범위를 직접 원문 확인 | 핵심 필드 누락 또는 목록 페이지만이면 미평가 |

## 후보별 재현 입력

`미평가`는 숫자 0점이 아니므로 합계를 산출하지 않았다. 현재 자료로 4점 이상을 확정할 후보는 0개다.

| 후보 | 현금흐름 | 1인 운영 | 강점 활용 | 개선 여지 | 검증 가능성 | 별점/상태 | capital_risk |
|---|---|---|---|---|---|---|---|
| Online gift-card SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $2.395M 표시가격 |
| Education SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $2.325M 표시가격 |
| WordPress plugins | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $2.25M 표시가격 |
| Short-term rental SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류/under offer | $1.03M 표시가격 |
| 16-year SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $1.000025M 표시가격 |
| Performance management SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 우선 확인, 별점 미확정 | $149K 표시가격 |
| Recurring health app | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $320K 표시가격 |
| AI fundraising SaaS | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | offers, 가격 미확인 |
| Municipalities accounting software | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | $575K 표시가격 |
| Low-workload subscription business | 미평가 | 미평가 | 미평가 | 미평가 | 미평가 | 보류 | 가격 미표시 |

## 근거 연결

- 후보 수치·출처: `candidate-ledger.md` 및 `marketplace-inventory.md`; 확인 시각은 2026-10-10T21:50Z이며 판매자·중개자 표시다. Pack의 `evaluation_rubric.candidate_fields.source_url`·`checked_at`·`fit_stars`·`risks` 필드에 대응한다.
- 사용자 근거: `intents/context/acquisition-cashcow-research-20261010.json#/request`는 1인 운영·현금흐름 목표를 요구하고, `#/evaluation_rubric/fit_stars`는 5축을 선언한다. `#/evaluation_rubric/candidate_fields`의 `owner_hours`, `transfer_scope`, `source_url`, `checked_at`, `fit_stars`, `risks`가 후보 표의 필드 계약이다. `#/rules/0`~`#/rules/4`는 공개 원문·주장/검증 분리·승인 경계를 요구한다. 가용 자본 숫자와 후보별 역량 매핑은 Pack에 없으므로 강점 축과 가격 적합성은 확정하지 않았다.
- 재평가 조건: 후보별 직접 상세 URL, 통화·기간·지표 정의, 최근 결제/환불 또는 독립 검증, owner hours, transfer scope가 공개 근거로 연결될 때 축별 점수를 다시 계산한다.
