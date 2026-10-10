# T1.3 후보별 수치·운영·이전 정규화

확인 시각 기준: 2026-10-10T21:50Z. 모든 수치는 Quiet Light 공개 목록/상세의 판매자·중개자 표시이며 독립 확인 아님.

| 후보 | 가격 | 수익 | 1인 운영 | 이전 범위/의존성 | 정규화 판정 |
|---|---|---|---|---|---|
| Online gift-card SaaS | $2.395M | 매출 $763,977 / 이익 $686,077 | 미확인 | SaaS, 12년 운영; 고객·코드·결제 이전 미확인 | 보류: 핵심 수치는 있으나 owner hours/transfer 미확인 |
| Education SaaS | $2.325M | $497,232 / $463,083 | low churn만 확인 | SaaS; 기술·고객 이전 미확인 | 보류 |
| WordPress plugins | $2.25M | $1,085,344 / $583,373 | 미확인 | 10,000 paid subscribers; WordPress 의존·이전 미확인 | 보류 |
| Short-term rental SaaS | $1.03M | $412,371 / $325,281; $43K MRR | 미확인 | under offer; 플랫폼·고객 이전 미확인 | 보류/under offer |
| 16-year SaaS | $1,000,025 | $577,671 / $256,533 | 미확인 | recurring revenue, 9% YoY claim; 이전 미확인 | 보류 |
| Performance management SaaS | $149K | $193,855 / $49,089 | 미확인 | 28 customers, 15 countries, 4.5-year tenure; 이전 미확인 | 보류: 가격은 상대적으로 낮지만 운영 정보 부족 |
| Recurring health app | $320K | $106,077 / $99,608 | passive 주장, 검증 안 됨 | 앱/규제·스토어 의존 및 이전 미확인 | 보류: passive는 판매자 주장 |
| AI fundraising SaaS | offers | $98,809 / $18,608 | 미확인 | 가격·기술·고객 이전 미확인 | 판정 보류 |
| Municipalities accounting software | $575K | $270,545 / $229,179 | 미확인 | Microsoft Access, 장기 고객; 레거시 기술 이전 위험 | 보류 |
| Low-workload subscription business | 미표시 | $144K / 약 $46K SDE | low workload 주장 | starter business; 상세 이전 미확인 | 보류: 가격 미확인 |

## 독립 확인과 공백

이번 단계에서 독립 회계자료, 소유자 시간, 고객지원량, 코드/도메인/결제계정 이전 범위를 공개 원문으로 확인하지 못했다. 따라서 매출·이익을 사실로 확정하지 않고 `판매자/중개자 주장`으로만 사용한다. 사용자의 자본 규모도 Context Pack에 숫자로 주어지지 않아 가격 적합성은 별도 미확정이다.

**T1.3 결론:** 공개 숫자만으로는 1인 운영·이전 조건까지 충족하는 4점 이상 후보를 확정할 수 없다. 다음 T2.1은 수치가 있는 후보의 조건부 별점과 보류 사유를 계산한다.

## Red 보강 메타데이터

- `checked_at_utc`: 모든 후보 행은 `2026-10-10T21:50Z`에 확인했다.
- `currency`: `$` 표기는 원문 표기를 보존했으며 통화가 명시되지 않은 값은 확정 환산값으로 사용하지 않는다.
- `period_and_definition`: 원문 목록에 기간·정의가 함께 노출되지 않은 값이 많다. `MRR`, `SDE`, `net margin`, `revenue`, `profit`은 서로 대체하지 않는다.
- `source_character`: 모든 수치는 판매자/중개자 주장이고 독립 검증 없음이다.
- `direct_detail_url`: 직접 상세 URL이 확인된 후보는 `https://quietlight.com/listings/3393139-2/`와 `https://quietlight.com/listings/10607099-2/`뿐이다. 나머지는 목록 URL만 확인되어 직접 상세 원문 미확인이다.
- `unknowns`: 모든 후보에서 `owner_hours`와 `transfer_scope`가 미확인이다.

목록 루트만 확인된 8개 후보의 표시 수치는 후보 발굴용 메모일 뿐 최종 재무 근거가 아니다. 직접 상세 URL을 확인할 수 없었으므로 최종 리포트의 조건부 별점·추천 산정에는 사용하지 않고 보류한다.

## 후보별 source metadata 고정표

| 후보 | source_url | checked_at_utc | 통화 | 기간/지표 정의 | 출처/신뢰도 | 짧은 원문 표시 |
|---|---|---|---|---|---|---|
| Online gift-card SaaS | https://quietlight.com/listings/3393139-2/ | 2026-10-10T21:50Z | USD 표기 추정 | 기간·revenue/profit 정의 미확인 | 판매자/중개자, 낮음 | `$2.395M`, `$763,977`, `$686,077` |
| Education SaaS | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; 기간·revenue/profit 정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; 목록 표시 주장만 보존 |
| WordPress plugins | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; 기간·revenue/profit 정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; `10,000 paid subscribers` 주장 |
| Short-term rental SaaS | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; `$43K MRR` 외 재무기간 미확인 | 목록 루트, 재현 불가 | 수치 보류; `under offer` 주장 |
| 16-year SaaS | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; `9% YoY` 기준기간 미확인 | 목록 루트, 재현 불가 | 수치 보류; recurring revenue 주장 |
| Performance management SaaS | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; revenue/profit 기간·정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; `28 customers`, `15 countries` 주장 |
| Recurring health app | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; revenue/profit 기간·정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; `passive`, `zero marketing` 주장 |
| AI fundraising SaaS | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; revenue/profit 기간·정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; `accepting offers` 주장 |
| Municipalities accounting software | https://quietlight.com/listings/ | 2026-10-10T21:50Z | 미확인 | 직접 상세 미확인; revenue/profit 기간·정의 미확인 | 목록 루트, 재현 불가 | 수치 보류; Microsoft Access·20년 고객 주장 |
| Low-workload subscription business | https://quietlight.com/listings/10607099-2/ | 2026-10-10T21:50Z | USD 표기 추정 | `$46K SDE`의 기간·정의 미확인 | 판매자/중개자, 낮음 | `low workload`, `~$46K SDE` |
