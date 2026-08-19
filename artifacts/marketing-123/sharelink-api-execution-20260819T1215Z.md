# marketing-123 Sharelink Open API execution

- checked_at: 2026-08-19T12:15Z
- scope: Open API credential, health, product candidate, and link issuance self-check
- docs:
  - https://sharelink-docs.toss.im/guide/open-api
  - https://sharelink-docs.toss.im/guide/open-api/auth.md
  - https://sharelink-docs.toss.im/guide/open-api/readme.md
  - https://sharelink-docs.toss.im/guide/open-api/convention.md
  - https://sharelink-docs.toss.im/guide/open-api/api/link.md

## Result

Open API token issuance and health check passed. Product/category lookup passed. Official Sharelink URL issuance passed for all 3 selected unpublished test candidates.

Actual issued `shortUrl` and `originUrl` values are stored only in local private cache:

`/home/ubuntu/workspace/knowledge-lab/infinity/.sharelink-cache/marketing-123-links-20260819T1201Z.json`

The link URLs are intentionally not committed to the public Infinity artifact set.

## Selected API candidates

### C01

- product: 휴비딕 휴비케어 휴대용칫솔살균기 무선칫솔살균기 HTS-20
- tacaItemId: 72279505
- observed_price: 29,800 KRW
- Sharelink API result: SUCCESS
- angle: 실제 구매 기록의 `파우치와 칫솔` 맥락을 여행 세면도구 관리 기준으로 좁힌다.

### C02

- product: USB 3.0 멀티허브 4포트 듀얼 커넥트 C타입+USB-A
- tacaItemId: 8415151
- observed_price: 8,800 KRW
- Sharelink API result: SUCCESS
- angle: 실제 구매 기록의 `멀티플러그` 맥락을 숙소 이동 중 충전/연결 변수 줄이기로 좁힌다.

### C03

- product: 퓨어버블 미니 세탁기 속옷세탁기
- tacaItemId: 1181394807
- observed_price: 24,900 KRW
- Sharelink API result: SUCCESS
- angle: 실제 구매 기록의 `빨랫줄/세탁 준비` 맥락을 장기여행 중 빨래 처리 기준으로 좁힌다.

## Safety boundary

No public post, DM, comment, ad, purchase, payment, account setting change, or external share was performed. The next required human step is explicit approval before posting or sharing any affiliate link publicly.

