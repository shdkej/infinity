# Subtype Sourcing-Friction Screen

- date: 2026-06-15T11:00Z
- intent: naver-shopping-01
- prior artifact: `artifacts/naver-shopping-01/ready-made-sourcing-openapi-searchad-screen-2026-06-15.md`
- boundary: cloud research only; no Naver API calls; live commerce/account/public actions 0

## Screened Subtypes

### Phone Anti-Theft Strap / Tether (3 subtypes)

Based on prior OpenAPI/SearchAd evidence:
- `핸드폰 도난방지 스트랩` 33,062 total, median 9,900 KRW
- SearchAd `핸드폰도난방지스트랩` 280 PC + 1,500 mobile/mo, CTR 4.26%

| subtype | option complexity | return risk | sourcing friction | verdict |
|---------|-------------------|-------------|-------------------|---------|
| **목걸이/크로스넥 스트랩** (neck/crossbody strap) | MEDIUM (material × color) | LOW (strap not phone-model-specific) | LOW (1688: 手机防丢绳 abundant) | **LEAD** |
| 손목 스트랩 (wrist strap) | LOW (color only) | LOW | LOW | WATCH |
| 태그홀더 패치 + 스트랩 세트 (tag-holder patch + strap set) | MEDIUM-HIGH (patch + adapter + strap) | MEDIUM (adhesive claims) | MEDIUM (multi-component) | HOLD |

**목걸이/크로스넥 스트랩 detail:**
- Strap style: adjustable length nylon or fabric cord
- Attachment: universal adhesive patch (phone-back) or loop ring (phone case slot)
- Color options: 2-5 per run → LOW SKU count at launch
- Claim framing: "여행 중 소매치기·낙하 리스크 감소 보조 스트랩" (not "도난방지 보장")
- Europe travel / pickpocket content angle: natural user content story
- Estimated landing price range: 5,000–15,000 KRW
- Estimated sourcing cost: 300–1,000 KRW/pc from 1688/Alibaba
- Margin floor: ~60-70% before platform fees
- MOQ: 50–100 pcs

### Compression Pouch (2 subtypes)

Based on prior OpenAPI/SearchAd evidence:
- `압축파우치` 175,568 total listings — heavily crowded
- SearchAd `압축파우치` 1,230 PC + 7,020 mobile/mo, mobile CTR 3.21%

| subtype | option complexity | return risk | sourcing friction | verdict |
|---------|-------------------|-------------|-------------------|---------|
| 단순 2-3종 압축파우치 세트 (simple set) | MEDIUM (set size × color) | MEDIUM (size expectations) | LOW (commodity) | HOLD/conditional |
| 세탁물/습식 파우치 (laundry/wet-clothes pouch) | MEDIUM-LOW (size × color) | LOW | LOW | HOLD standalone |

**Why compression pouch subtypes are HOLD for first SKU:**
- `압축파우치` simple set: 175,568 competing listings → commodity positioning risk. Strong demand but differentiation is hard without brand story.
- 세탁물 파우치: SearchAd signal 20 mobile/mo — demand too thin for standalone.
- Both are better as bundle/upsell components after the strap establishes base traffic.

## Comparative Matrix

| Subtype | Option | Return | Sourcing | Demand | User fit | Verdict |
|---------|--------|--------|----------|--------|----------|---------|
| 목걸이/크로스넥 스트랩 | MEDIUM | LOW | LOW | HIGH (CTR 4.26%) | HIGH | **LEAD** |
| 손목 스트랩 | LOW | LOW | LOW | MEDIUM | MEDIUM-HIGH | WATCH |
| 태그홀더 패치+세트 | MEDIUM-HIGH | MEDIUM | MEDIUM | MEDIUM | MEDIUM-HIGH | HOLD |
| 단순 압축파우치 세트 | MEDIUM | MEDIUM | LOW | HIGH (7,020/mo) | MEDIUM | HOLD/conditional |
| 세탁물 파우치 | MEDIUM-LOW | LOW | LOW | LOW (20/mo) | MEDIUM | HOLD standalone |

## Next Step

1. **목걸이/크로스넥 스트랩 확정 → DataLab 키워드 스크린** (local execution needed)
   - Target SearchAd keywords: `핸드폰목걸이줄`, `폰목걸이스트랩`, `핸드폰도난방지스트랩`, `넥폰스트랩`, `여행폰스트랩`
   - DataLab category: `휴대폰 액세서리` 월간 클릭 트렌드 12개월
2. **1688 소싱 후보 3개 정리** (cloud research possible next heartbeat)
   - 검색어: `手机防丢绳`, `手机挂绳防盗`, `手机颈挂绳`
   - MOQ, 최소 품질 기준, 배송 일수 추정
3. **경쟁사 TOP 10 분석** (local execution, Naver Shopping 접근 필요)
   - TOP 10 셀러 가격대, 옵션 구조, 리뷰 패턴, 사진 스타일
   - Blocked by HTTP 418 — needs user browser session
