# marketing-123 product evidence — actual travel purchases

- intent: `marketing-123`
- checked_at: 2026-08-17T11:45Z
- scope: travel dashboard / Notion-synced expense evidence only
- public_action: none
- account_action: none

## Selection rule

첫 주제는 `여행 짐 줄이는 생활템 7일 실험`으로 유지하되, 후보는 일반 검색 상품이 아니라 마스터가 실제로 산/준비한 물건에서 출발한다. 직접 구매 근거를 찾지 못한 `여행용 압축파우치`와 `접지형 65W GaN 충전기`는 제외한다.

## Sources checked

- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/travel/dist/travel-data.json`
- `/home/ubuntu/workspace/space/infra-aws-static-sites/sites/travel/scripts/build-travel-data.py`
- Notion-synced expense rows embedded in the travel dashboard data
- Telegram-backed manual travel prep rows embedded in the travel dashboard data

## C01 — 여행용 파우치와 칫솔

- actual record: 2026-05-30 `여행용 파우치, 칫솔 등 (무인양품)` 28,400원
- sources:
  - `notion:3a107aba-cae7-818a-a0c1-fc490fa88cf5`
  - `telegram:433493318/message/10729`
- content angle:
  - "짐을 압축한다"가 아니라 "매일 꺼낼 물건을 덜 흐트러뜨린다"로 말한다.
  - 압축파우치 대신 실제 구매한 파우치/세면도구 정리 경험을 쓴다.
- risks:
  - 정확한 개별 상품명과 현재 판매 링크는 회원 화면 또는 구매 내역에서 다시 확인해야 한다.
  - 무인양품 동일 상품이 Toss Sharelink 발급 대상인지 알 수 없다.

## C02 — 여행용 멀티플러그와 종이세제

- actual record: 2026-05-19 `여행용 멀티플러그, 종이세제 (쿠팡)` 39,200원
- sources:
  - `notion:3a107aba-cae7-815f-bb59-dac644a867e2`
  - `telegram:433493318/message/10729`
- content angle:
  - `65W GaN 충전기`가 아니라 실제 산 `멀티플러그`를 기준으로 충전/숙소 생활을 말한다.
  - 종이세제는 빨래 루틴과 연결해 "숙소가 바뀌어도 생활이 이어지는가"로 설명한다.
- risks:
  - 국가별 플러그 호환, 정격 전압/전류, USB 포트 여부는 최종 상품 페이지에서 확인해야 한다.
  - 종이세제는 항공/숙소/세탁 조건과 맞지 않을 수 있다.

## C03 — 손톱깎이, 수건, 빨랫줄

- actual record: 2026-05-10 `Travel prep · 손톱깎이/수건/빨랫줄` 70,200원
- sources:
  - `notion:3a107aba-cae7-8128-be24-d86b5f2fa9ff`
  - `telegram:433493318/message/10729`
- content angle:
  - 빨랫줄은 기존 후보와 겹치지만, 이번에는 실제 구매 근거가 있다.
  - "빨래를 많이 하자"가 아니라 "젖은 물건 둘 곳 만들기"로 말한다.
- risks:
  - 묶음 구매라 개별 단가와 정확한 브랜드는 확인되지 않았다.
  - Sharelink 발급은 동일/유사 상품을 최종 선택해야 가능하다.

## Actual purchase evidence not found

- `여행용 압축파우치`: 여행 대시보드와 Notion-synced expense에서 직접 구매 기록을 찾지 못했다. `여행용 파우치, 칫솔 등 (무인양품)` 기록으로 대체한다.
- `접지형 65W GaN 3포트 충전기`: 직접 구매 기록을 찾지 못했다. `여행용 멀티플러그, 종이세제 (쿠팡)` 기록으로 대체한다.

## Publication unit decision

- first action: publish 3 candidate posts, one per actual purchase group, only after account self-check and user approval.
- 7-day unit: 21 posts total = 3 posts per day.
- daily shape:
  - one actual purchase post
  - one "why I bought/not bought it" criteria post
  - one replacement or similar Sharelink candidate post
- primary metrics:
  - saves
  - replies
  - link clicks
  - confirmed revenue
- secondary metric:
  - likes

## Remaining gates

- logged-in Toss Sharelink member-screen eligibility check for exact or similar products
- official Sharelink URL generation for each final product
- final price/option/stock/shipping/refund check immediately before publication
- explicit user approval before any public post
