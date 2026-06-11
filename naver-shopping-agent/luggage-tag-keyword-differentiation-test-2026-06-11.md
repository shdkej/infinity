# Luggage-Tag / Carrier Name-Tag Keyword Differentiation Test

> 작성: 2026-06-11 (Infinity Heartbeat naver-shopping-01)
> 모드: prepare (Cloud research — Naver OpenAPI/SearchAd IP 제한으로 수치 미확정)
> 목적: luggage-tag/carrier-name-tag 키워드가 Travel-Prep System 첫 SKU 후보로 유효한지 differentiation 각도 분석

---

## 배경

- 이전 HOLD: `해외여행 체크리스트` (mobile CTR 0.05%, generic), paper/card insert (arrival-day)
- 승인된 첫 씨드: Travel-Prep System / Travel Scenario Card / Checklist Insert Set
- 이번 패스 목표: 러기지 태그 / 캐리어 이름표가 Travel-Prep System 맥락에서 cleaner differentiation 각도를 제공하는지 테스트

---

## 키워드 후보 분류

### Tier 1 — 핵심 테스트 대상

| 키워드 | 예상 검색 의도 | 리스크 |
|---|---|---|
| `러기지 태그` | 여행가방 식별/장식 | 패션·장식·브랜드 noise 높음 |
| `캐리어 이름표` | 캐리어 소유자 식별 | 기능형에 가까움, 볼륨 미확인 |
| `여행 네임태그` | 여행 전용 이름표 | 네임태그 일반(책가방·사무용) noise 가능 |
| `분실방지 러기지태그` | 분실 예방 기능 | intent clear, 볼륨 미확인 |

### Tier 2 — 보조 탐색

| 키워드 | 예상 검색 의도 | 비고 |
|---|---|---|
| `수하물 태그` | 공항·항공 맥락 | formal/institutional tone, generic |
| `캐리어 식별 태그` | 캐리어 구분 | 볼륨 낮을 가능성 |
| `여행가방 이름표` | 기능형 | 조합어, 검색 패턴 불확실 |

---

## Differentiation 분석 프레임워크

### 분화 각도 1: 기능형 vs 장식형

- **기능형** (`분실방지`, `식별`, `이름표`): 실용 구매 의도. 하지만 네이버에서 이 카테고리는 보통 저가 commodity.
- **장식형** (브랜드 러기지태그, 가죽/디자인): 패션/여행 액세서리 shelf. 경쟁이 높고 브랜드 의존도 큼.

→ Travel-Prep System 포지셔닝에서는 **기능형 + 여행준비 맥락**이 유일한 차별화 경로.

### 분화 각도 2: 독립 SKU vs 세트 구성품

- 러기지 태그를 단독 SKU로 판매 → 카테고리 경쟁에 직접 노출
- 러기지 태그를 Travel-Prep 시스템 세트 구성품 중 하나로 → 패키지 포지셔닝, 더 높은 AOV 가능성

→ 현재 단계에서는 독립 SKU 테스트 먼저. 세트 구성은 수요 확인 후.

### 분화 각도 3: 재사용/내구성 vs 일회성

- 재사용 가능한 가죽/금속 태그 → 프리미엄 포지셔닝, 진입 단가 높음
- 일회용/교체 가능 종이 태그 → 저가, 차별화 어려움

→ **재사용 가능, 내구성 있는 재료**로 포지셔닝하면 "travel investment" 언어 사용 가능.

---

## PROMOTE / PIVOT / HOLD 루브릭

다음 조건을 Naver OpenAPI/SearchAd 수치 확인 후 적용:

| 조건 | 판정 |
|---|---|
| 주요 키워드 월간 검색량 > 5,000 AND top 10이 기능형 item 위주 | **PROMOTE** — 해당 키워드로 listing 방향 승인 요청 |
| 주요 키워드 볼륨 충분 BUT top 10이 장식형/패션 noise | **PIVOT** — `분실방지` modifier 또는 `여행준비 세트` 묶음으로 전환 |
| 주요 키워드 월간 검색량 < 500 | **HOLD** — 수요 부족, 다음 SKU 후보 탐색 |
| `캐리어 이름표`가 `러기지 태그`보다 cleaner | **PIVOT to `캐리어 이름표`** 리드 키워드 |

---

## 검증 필요 항목 (Naver 접근 시)

- [ ] `러기지 태그` OpenAPI 월간 PC/Mobile 검색량
- [ ] `캐리어 이름표` OpenAPI 월간 검색량
- [ ] Top 10 상품: 기능형 vs 장식형 비율
- [ ] 평균 판매가격 범위 (저가 commodity vs 프리미엄 여부)
- [ ] `분실방지` modifier SearchAd 볼륨
- [ ] 기존 SKU 리뷰 키워드에서 "여행준비" 언어 등장 여부

---

## 다음 안전 액션

1. Naver SearchAd 접근 확보 후 위 수치 검증
2. `캐리어 이름표` 볼륨이 충분하면 PROMOTE 방향 사용자에게 보고
3. 모든 키워드가 HOLD면 다음 SKU 후보 탐색 (예: 여행 파우치, 패킹 큐브 정리대)

---

## 금지선

- 라이브 상품등록 0
- 가격·배송·재고·옵션 설정 0
- 광고·고객·주문·계정 액션 0
- 공개 상세페이지 수정 0