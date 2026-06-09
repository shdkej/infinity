# marketing-48: 트래블러스노트 여행준비 속지 제목/카피 포지셔닝

- id: marketing-48
- status: inbox
- projects: [naver-shopping, infinity, personal-ops]
- task_type: marketing-positioning
- topics: [naver-shopping, listing-copy, positioning, keyword-strategy]
- owner: Marketer
- source_agent: naver-shopping-agent
- source_intent: naver-shopping-01
- target_agent: Marketer
- request_type: title-copy-positioning
- created_at: 2026-06-09T10:00Z
- user_visible: false

## Question

트래블러스노트 standard-size travel-prep structured insert 피벗 SKU의 내부용 listing title/copy 포지셔닝을 정리한다. 공개 등록, 광고 집행, 가격/재고 확정, 고객 커뮤니케이션은 하지 않는다.

## Context

- `naver-shopping-01`은 첫 SKU를 standalone `여행 체크리스트`가 아니라 `트래블러스노트` 리필/속지 생태계 안의 여행준비 구조화 속지로 피벗했다.
- DataLab/OpenAPI/SearchAd 증거는 방향성 PIVOT이다. PROMOTE급 확정은 아니다.
- `여행 체크리스트`는 검색량은 있으나 광고 CTR이 낮아 정보형 수요로 읽힌다.
- `트래블러스노트리필`/`트래블러스노트속지`는 얇지만 거래형 신호가 있고, anchor `트래블러스노트`가 트래픽 엔진이다.
- 상위 상품은 저가 범용 속지/체크리스트가 많아, 프리미엄 정당화는 종이 자체가 아니라 여행준비 구조와 사용 장면에서 나와야 한다.

## Evidence

- `/home/ubuntu/workspace/knowledge-lab/infinity/intents/active/naver-shopping-01.md`
- `/home/ubuntu/workspace/knowledge-lab/infinity/reports/naver-shopping-01/2026-06-09T0707Z-local.html`
- `/home/ubuntu/workspace/knowledge-lab/infinity/reports/naver-shopping-01/2026-06-09T0807Z-local.html`
- `/home/ubuntu/workspace/knowledge-lab/infinity/reports/naver-shopping-01/2026-06-09T0907Z-local.html`
- `/home/ubuntu/.openclaw/workspace/agents/naver-shopping-agent/listing-preflight-travelers-notebook-insert.md`

## Desired Output

내부 산출물 1개를 작성한다.

- 권장 파일: `artifacts/marketing-48/travelers-notebook-insert-listing-copy-positioning.md`
- 포함 항목: 제목 후보 5-8개, 금지/주의 제목 패턴, 1문장 가치 제안 후보, 상세페이지 첫 문단 후보, 검색 키워드 묶음, 이미지/썸네일 문구 후보, 승격 전 검증 게이트
- 모든 문구는 draft/proposal-only로 표시한다.

## Output Contract

- source evidence를 문서 상단에 링크한다.
- `여행 체크리스트`를 제목 맨 앞에 두지 않는 이유를 명시한다.
- `트래블러스노트` 상표/호환 표현은 법적/플랫폼 리스크가 있을 수 있으므로 "호환/규격/브랜드명 사용" 문구를 approval-needed로 표시한다.
- 가격, 배송, 재고, 옵션, 광고 문구 확정은 하지 않는다.
- 공개 발행 가능한 최종 카피가 아니라 내부 후보군이어야 한다.

## Approval Boundary

허용: 내부 문서 작성, 후보 문구 작성, 기존 증거 재해석, Infinity report/archive 업데이트.

금지: 상품 등록, 공개 상세페이지 반영, 광고/비용 집행, 외부 메시지, 고객/주문/계정 조작, 가격/재고/배송 확정, 상표/호환 표현의 공개 사용 확정.

## First Verification Gate

- `rg '여행 체크리스트.*트래블러스노트|트래블러스노트.*여행 체크리스트' artifacts/marketing-48`로 제목 후보가 standalone checklist 리드로 흐르지 않는지 확인한다.
- 산출물 안에 `draft`, `proposal-only`, `approval-needed` 경계가 모두 포함되어야 한다.
