# 캐리어네임택/러기지택 차별화 테스트 플랜
- prepared_at: 2026-06-11T02:07Z
- prepared_by: SAM cloud heartbeat (prepare mode)
- executor: local naver-shopping-agent cron

## Context

2026-06-10T20:07Z arrival-day insert keyword test 완료 → HOLD 판정.
Paper/card insert는 lead SKU 후보에서 내림. 남은 저마찰 경로는 캐리어네임택/러기지택 분기.

### 이전 데이터 요약
| 키워드 | 월간검색(SearchAd) | 메모 |
|--------|-------------------|------|
| 캐리어네임택 | 7,310/mo | mobile-dominant |
| 러기지택 | 3,780/mo | |
| 판단 | "이름 표시 이상의 차별화 필요" | 소싱/샘플 없는 research 단계 |

## 차별화 가설 3축

### 축 A: 개인화 / 커스터마이징 (1순위)
**가설**: 커스텀 텍스트/각인/이니셜 네임택은 범용 실리콘/PVC 태그 대비 프리미엄을 지불할 buyer가 Naver에 존재하며, 키워드 언어도 더 구체적이다.

테스트 쿼리:
- `캐리어네임택 커스텀`
- `캐리어네임택 각인`
- `캐리어 이름표 각인`
- `러기지택 이니셜`
- `네임택 각인`

PROMOTE 기준: 전용 셀러 ≥5, CTR >2%, ₩12,000–25,000 가격대 공백 존재, 상위 리뷰 수 moderate(범람 아님)

### 축 B: 소재 / 품질 티어 (2순위)
**가설**: 진짜 가죽 또는 프리미엄 소재가 ₩2,000–5,000 commodity tier와 명확히 다른 층을 만든다.

테스트 쿼리:
- `가죽 러기지택`
- `캐리어네임택 가죽`
- `소가죽 네임택`

PROMOTE 기준: 가죽 네임택 shelf 존재, 상위 셀러가 established 브랜드에 잠기지 않음

### 축 C: 여행서사 / 기능 프레임 (전략적)
**가설**: 분실방지 QR 코드 또는 '여행 컴패니언' 카피가 copy differentiation을 만든다. keyword-led가 아닌 copy-led이므로 shelf 유무 확인이 목적.

테스트 쿼리:
- `여행 네임택`
- `캐리어 여행용품 세트`
- `QR 캐리어태그`

Note: QR 코드 태그가 기존 niche인지 blue ocean인지 판별.

## 로컬 에이전트 실행 쿼리 플랜

### SearchAd (`/keywordstool`) — 수집 필드
- `monthlyPcQcCnt` / `monthlyMobileQcCnt` (월간검색량)
- `monthlyAvePcClkCnt` / `monthlyAveMobileClkCnt` (광고 클릭량)
- `monthlyAvePcCtr` / `monthlyAveMobileCtr` (CTR)

우선순위 순서:
1. `캐리어네임택 커스텀`
2. `캐리어네임택 각인`
3. `러기지택 이니셜`
4. `가죽 러기지택`
5. `여행 네임택`
6. `캐리어 이름표`
7. `QR 캐리어태그`

rate limit 정책: 첫 rate-limit 신호에서 중단, 같은 실행 내 재시도 없음.

### OpenAPI Shopping Search (`/v1/search.json`) — 수집 필드
top-10, sort=sim / 우선순위 쿼리:
1. `캐리어네임택 커스텀`
2. `캐리어네임택 각인`
3. `가죽 러기지택`

수집:
- 상품명 키워드 패턴 (개인화 언어 밀도)
- 가격 분포 (min, median, max, mode-cluster)
- 브랜드/셀러 분포 (집중도)
- 리뷰 수 범위 (시장 성숙도)

## PROMOTE / PIVOT / HOLD 루브릭

| 판정 | 기준 |
|------|------|
| PROMOTE | 개인화 shelf 명확, CTR >2%, 셀러 ≥5, ₩12,000–25,000 가격 공백 |
| PIVOT | 관련 번들 기회(여행파우치+네임택 세트), 또는 소재 프리미엄 앵글 확인 |
| WATCH | 키워드 존재하나 established 브랜드 장악 또는 commodity 가격 경쟁 |
| HOLD | 명확한 shelf 언어 없음, noise 비율 높음, 마진 불가 |

## 완료 기준

다음 중 하나라도 판정되면 이 테스트는 완료:
1. 개인화 축 판정(PROMOTE/PIVOT/WATCH/HOLD) + 키워드·가격·셀러 근거
2. 소재 축 가격 분포 확인
3. 여행서사 축: `여행 네임택` / `QR 캐리어태그` shelf 언어 확인
