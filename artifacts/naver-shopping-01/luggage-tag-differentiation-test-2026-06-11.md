# 러기지택/캐리어네임택 분화 테스트 준비

- intent: `naver-shopping-01`
- created: 2026-06-11T10:00Z
- mode: prepare (cloud) — 로컬 OpenAPI/SearchAd 검증 대기
- scope: docs-only, no live Naver store/listing/price/shipping/ads action

## 0. 배경

이전 패스(2026-06-10T19:07Z)에서 arrival-day failure-prevention sourcing/friction screen을 수행했다. 결론:
- `캐리어네임택` 7,310/mo (SearchAd), `러기지택` 3,780/mo (SearchAd) — demand 확인
- 두 키워드 모두 "이름만 표시하는 것 이상의 분화"가 필요
- 다음 안전 액션: **커스터마이징/분화 각도 테스트**

이 문서는 클라우드에서 준비(prepare)한 분화 테스트 계획이다. Naver OpenAPI/SearchAd 검증은 로컬 cron 또는 다음 Heartbeat 로컬 패스에서 실행한다.

## 1. 구매 상황 가설 (Purchase Situation Before Object Shape)

`러기지택`/`캐리어네임택` 자체는 broad object-shape keyword다. 분화를 위해 먼저 구매 상황을 정의한다.

| # | 구매 상황 | 핵심 욕구 | 기존 제품과의 차이 | 검증 필요 지점 |
|---|---|---|---|---|
| S1 | 해외여행 출발 전 짐 준비 마지막 단계 | 내 짐인지 바로 알아볼 수 있게 + 분실 시 연락 가능하게 | generic 이름표 — 이름만 표시 | `여행 준비` + `네임택` 결합 키워드 수요 |
| S2 | 커스텀/나만의 것 만들기 | 이름/연락처 외에 디자인·재질을 직접 고르고 싶다 | 대량 생산 commodity | `커스텀 캐리어택`, `주문제작 러기지택` 수요 |
| S3 | 여행 선물 세트 | 실용적이고 받는 사람 이름이 들어간 선물 | 개인화 없는 generic gift | `여행 선물 네임택`, `캐리어 선물 세트` 수요 |
| S4 | 여행 준비 시스템 구성 | 출국 체크리스트, 짐 태그, 준비물을 한 세트로 | 단품 구매 | travel-prep system 번들 컨셉 키워드 |

현재 데이터 기반 가장 유력한 구매 상황: **S2 (커스텀)** — 기존 keyword-weak 단점을 보완하는 differentiation story가 가능하고, 소량 생산/개인화 경로가 있음.

## 2. 키워드 분화 후보

다음 로컬 OpenAPI + SearchAd 검증 대상 키워드:

### 핵심 후보 (커스텀/개인화 각도)
| 키워드 | 분화 각도 | 검증 필요 항목 |
|---|---|---|
| `캐리어네임택 커스텀` | 개인화/custom object | OpenAPI total, SearchAd volume, top-10 경쟁 상품 수 |
| `러기지택 주문제작` | 커스텀 소량 제작 | OpenAPI total, SearchAd volume |
| `캐리어 이름표 가죽` | 소재 차별화 | 가죽 제품 경쟁 상품 수 |
| `러기지택 가죽` | 소재 차별화 | OpenAPI total, CTR |
| `여행 네임태그 개인화` | 여행 준비 + 개인화 | 수요 신호 여부 |

### 보조 후보 (기능/기술 각도)
| 키워드 | 분화 각도 | 검증 필요 항목 |
|---|---|---|
| `RFID 러기지택` | 보안 기능 추가 | demand 규모, 경쟁 |
| `QR 네임태그` | QR코드 연락처 | 여행 컨텍스트 연결 여부 |
| `캐리어택 선물` | 선물 세트 맥락 | gift 구매 상황 연결 |

### 대조 후보 (이미 노이즈 많음, 테스트 대상이지만 lead 아님)
| 키워드 | 이유 |
|---|---|
| `러기지택` (plain) | Broad object shape, 분화 없음 |
| `캐리어네임택` (plain) | demand 있으나 commodity 경쟁 |
| `이름표 캐리어` | 학교/기관 용도 noise 가능 |

## 3. 캡처 스키마 (로컬 실행용)

로컬 패스에서 아래 데이터를 수집한다:

```
keyword: <검색어>
openapi_total: <OpenAPI 검색결과 건수>
searchad_pc: <SearchAd PC 월 조회수>
searchad_mobile: <SearchAd 모바일 월 조회수>
top3_products: <상위 3개 상품명 (간략)>
differentiation_signal: STRONG/MEDIUM/WEAK/NOISE
buyer_intent_note: <구매 의도 신호 메모>
verdict: PROMOTE/WATCH/HOLD
```

## 4. 분화 PROMOTE/WATCH/HOLD 루브릭

기존 `keyword-competitor-validation-plan.md`의 루브릭 확장:

| 판정 | 조건 | 후속 액션 |
|---|---|---|
| PROMOTE | SearchAd ≥ 500/mo + top-10에 커스텀/개인화 전문 상품 < 5개 + buyer intent clear | sourcing friction screen 진행 |
| WATCH | SearchAd 200~500/mo OR top-10 경쟁 있지만 differentiation gap 확인됨 | 추가 각도 테스트 or 소규모 sourcing inquiry |
| HOLD | SearchAd < 200/mo AND noise 많음 OR top-10 포화 | 해당 키워드 각도 종료 |

## 5. 제품 커레이션 맥락

나래(Narae) 큐레이션 기준 대조:
- **user-fit thesis**: 사용자 travel/memory-making 취향에 맞음 — 커스텀 여행 준비 아이템
- **Knowledge Lab / source-note signal**: Idea/Travel.md의 여행 준비 시스템 컨셉과 일치
- **demand signal**: SearchAd 7,310/mo (캐리어네임택) — medium demand, plain keyword는 commodity
- **margin/registration-friction**: 개인화 아이템은 MOQ 부담 가능 → sourcing screen 필요
- **content angle**: 여행 준비 체크리스트 + 네임택 세트 → 커스텀 과정 콘텐츠 생산 가능
- **measurement path**: OpenAPI top-10 분화 비율 + SearchAd 커스텀 키워드 수요
- **approval boundary**: 상품등록/가격/배송/재고/광고/고객 모두 approval-needed

현재 판정: **WATCH** — 수요는 확인됐으나 분화 키워드 검증 전 listing-ready 아님.

## 6. 다음 로컬 실행 프롬프트

로컬 Naver Shopping 에이전트에 전달할 액션:

```
naver-shopping-01 luggage-tag differentiation test
Mode: execute_local (OpenAPI + SearchAd read-only)
Keywords to test: [캐리어네임택 커스텀, 러기지택 주문제작, 캐리어 이름표 가죽, 러기지택 가죽, 여행 네임태그 개인화]
Schema: artifacts/naver-shopping-01/luggage-tag-differentiation-test-2026-06-11.md §3 캡처 스키마
PROMOTE/WATCH/HOLD rubric: §4
Rate limit note: SearchAd rate limits after first exact checks — stop on rate limit, log partial results
Allowed: read-only Naver API calls only
Forbidden: listing, price, stock, shipping, ads, customer, order, account, public action
Report to: reports/naver-shopping-01/{timestamp}-local.html
```

## 7. 라이브 액션 경계

이 문서 범위 내 실행 완료 항목:
- 분화 후보 키워드 정리 ✓
- 구매 상황 가설 4개 ✓
- 캡처 스키마 ✓
- PROMOTE/WATCH/HOLD 루브릭 ✓

라이브 Naver 액션 0건: 상품등록/가격/배송/재고/광고/고객/주문/계정/공개발행 변경 없음.
