# 캐리어네임택/러기지택 차별화 테스트 계획

- created: 2026-06-11T0107Z
- source: Cloud Heartbeat prepare pass
- context: naver-shopping-01 paper/card insert HOLD 이후 다음 WATCH 브랜치 검증

## 배경

2026-06-10T20:07Z paper/card-led arrival-day insert HOLD 판정 이후 남은 WATCH 브랜치는 `캐리어네임택`/`러기지택`이다. 기존 스캔(2026-06-10T19:07Z)에서 수요는 확인됐지만(캐리어네임택 7,310/mo, 러기지택 3,780/mo) 차별화 angle, 가격 화이트스페이스, ad intent는 미검증.

## 테스트 키워드 (우선순위 순)

| # | 키워드 | 기존 수요 | 역할 |
|---|--------|-----------|------|
| 1 | `캐리어네임택` | 7,310/mo | core |
| 2 | `러기지택` | 3,780/mo | core synonym |
| 3 | `커스텀 네임택` | 미확인 | 개인화 차별화 angle |
| 4 | `캐리어 이름표` | 미확인 | 어형 변형 |
| 5 | `러기지 태그` | 미확인 | 영어 영향 변형 |

## 실행 체크리스트

- [ ] OpenAPI top-20 (sort=sim) — 각 키워드: 가격대, 리뷰수, 상품명 언어 패턴
- [ ] SearchAd — 월검색량(PC+mobile), 클릭수, CTR, ad depth
- [ ] 상위 10개 상품: 도착일/분실방지 framing 차별화 상품 여부
- [ ] 가격 화이트스페이스 분석: 1,000–3,000원 commodity 대비 5,000원+ 진입 공간
- [ ] `product-curation.md` 업데이트
- [ ] HTML 리포트: `reports/naver-shopping-01/{timestamp}Z-local.html`

## PROMOTE / PIVOT / HOLD 루브릭

**PROMOTE**: 차별화 상품 가격 > 5,000원, 리뷰 10건+, thin competitor, user-fit 디자인 가능

**PIVOT**: 수요 있지만 commodity 상단 → 도착일 실패 방지 스토리 + 커스텀 디자인으로 이동

**HOLD**: 1,000원대 가격전쟁 + MOQ 위험 + 차별화 진입 불가 + buyer intent 약함

## 접근 제약

- Naver Shopping 웹: HTTP 418 (재시도 금지)
- Naver OpenAPI + SearchAd: 접근 가능 (rate limit 주의)
- SmartStore Commerce ID: 사용자 전환 대기
- 브라우저 리뷰 depth: HTTP 429 (세션 있으면 재시도 가능)

## 금지 액션

소싱, 상품등록, 가격, 광고, 고객, 계정, 공개 액션 금지.
DRAFT/WATCH/HOLD/PIVOT/PROMOTE 판정만.
