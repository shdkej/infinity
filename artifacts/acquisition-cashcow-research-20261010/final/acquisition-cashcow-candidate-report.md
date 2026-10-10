# 소규모 서비스 인수 후보와 사용자 적합성 조사

## 결론

공개 목록에서 10개 후보를 확인했지만, 사용자의 1인 운영·자본 제약에 맞는 **조건부 4점 이상 후보는 현재 0개**입니다. 가장 먼저 추가 확인할 후보는 `Performance management SaaS`(별점 미확정, 표시 가격 $149,000)입니다. 다만 owner hours, 지원 부담, 코드·도메인·결제계정 이전, 이탈률·고객 집중도, 재무 증빙이 확인되기 전에는 추천하지 않습니다.

이번 결과는 구매 추천이 아니라 공개 근거를 바탕으로 한 보류·검증 우선순위입니다. 매출과 이익은 판매자/중개자 주장으로만 취급했으며 독립 회계 검증값이 아닙니다.

## 후보 목록

| 우선순위 | 후보 | 표시 가격 | 표시 매출 / 이익 | 조건부 별점 | 판정 |
|---:|---|---:|---:|---:|---|
| 1 | Performance management SaaS | $149,000 | $193,855 / $49,089 | 별점 미확정 | 공개 추가 확인 우선 |
| 2 | WordPress plugins | $2,250,000 | $1,085,344 / $583,373 | 보류 | 가격·운영·이전 보류 |
| 3 | Online gift-card SaaS | $2,395,000 | $763,977 / $686,077 | 보류 | 자본·owner hours 미확인 |
| 4 | Education SaaS | $2,325,000 | $497,232 / $463,083 | 보류 | 운영·이전 미확인 |
| 5 | 16-year SaaS | $1,000,025 | $577,671 / $256,533 | 보류 | 운영·이전 미확인 |
| 6 | Municipalities accounting software | $575,000 | $270,545 / $229,179 | 보류 | Microsoft Access 기술부채 |
| 7 | Short-term rental SaaS | $1,030,000 | $412,371 / $325,281 | 보류/under offer | 이전 미확인 |
| 8 | Recurring health app | $320,000 | $106,077 / $99,608 | 보류 | passive 주장·규제/스토어 의존 |
| 9 | AI fundraising SaaS | offers | $98,809 / $18,608 | 보류 | 가격·운영·이전 미공개 |
| 10 | Low-workload subscription business | 미표시 | $144,000 / 약 $46,000 SDE | 보류 | 가격·이전 미공개 |

원문 목록 출처: [Quiet Light listings](https://quietlight.com/listings/), [online gift-card 상세](https://quietlight.com/listings/3393139-2/), [low-workload 상세](https://quietlight.com/listings/10607099-2/). 개별 URL이 목록 페이지로만 확인된 후보는 해당 목록 페이지를 원문으로 기록했습니다.

## 후보별 다음 검증 질문

1. **Performance management SaaS:** $49,089 이익에서 소유자 노동과 지원 비용을 공제한 월 잉여현금은 얼마인가?
2. **WordPress plugins:** 10,000 paid subscribers의 최근 12개월 유지율·환불률과 WordPress 의존도는 얼마인가?
3. **Online gift-card SaaS:** 88% net margin 주장에 결제수수료·지원·개발·세금이 포함되어 있는가?
4. **Education SaaS:** low churn의 기간·분모와 고객 집중도, 인수 후 기술 이전 범위는 무엇인가?
5. **16-year SaaS:** recurring revenue의 계약/결제 근거와 9% 성장률의 기준 기간은 무엇인가?
6. **Municipalities accounting software:** Microsoft Access 런타임·고객별 커스터마이징을 포함한 이전/유지보수 부담은 얼마인가?
7. **Short-term rental SaaS:** under offer 상태에서 실제 이전 가능한 자산과 $43K MRR의 검증 범위는 무엇인가?
8. **Recurring health app:** passive·zero marketing 주장이 앱스토어 정책, 건강 규제, 유지보수 시간을 포함해 재현되는가?
9. **AI fundraising SaaS:** offers 구조에서 최소 가격·고객 유지·핵심 모델/데이터 이전이 공개되는가?
10. **Low-workload subscription business:** 약 $46K SDE가 owner labor와 모든 운영비를 반영하며 가격이 얼마인가?

## 공통 인수 후 현금흐름 기준

`월 잉여현금 = 검증된 현금 매출 - 결제/호스팅/도구/지원 비용 - 환불·세금·유지보수 충당금`

다음 네 항목이 모두 확인되기 전에는 회수기간이나 수익률을 계산하지 않습니다.

- 최근 6~12개월 결제·환불 원장
- 소유자 주간 운영시간과 대체 노동비
- 고객·트래픽·플랫폼 의존도 및 계정 이전 가능성
- 매수가 외 운영자본·세금·마이그레이션 비용

구매·판매자 연락·계약·결제·비공개 자료 요청은 이번 실행에서 하지 않았습니다.

## 근거와 한계

- 근거 원장: `work/marketplace-inventory.md`, `work/candidate-ledger.md`, `work/fit-scoring.md`, `work/alternatives-and-risks.md`
- 사용자 기준 근거: `intents/context/acquisition-cashcow-research-20261010.json`의 `request`, `evaluation_rubric.fit_stars`, `rules[0..4]`
- 확인 시각: 2026-10-10 UTC 실행 기록
- Flippa, Acquire, Fello, Listing.co, Sellernet, Empire Flippers는 이 실행에서 후보별 핵심 수치·이전 범위를 안정적으로 공개하지 않아 주 비교표에서 보조 출처로만 다뤘습니다.
- 사용자의 정확한 가용 자본 숫자가 Context Pack에 없어 가격 적합성은 확정하지 않았습니다.

## 다음 행동

공개 원문에서 추가 확인 가능한 `Performance management SaaS`부터 위 질문의 답을 확인하고, owner hours·이전 범위·검증 재무 중 하나라도 비어 있으면 후보를 보류합니다. 공개 정보만으로 답을 얻을 수 없을 때는 승인 없이 판매자에게 연락하지 않고, 조사 결론을 `검증 불충분`으로 유지합니다.
