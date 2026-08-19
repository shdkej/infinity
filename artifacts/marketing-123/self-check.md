# marketing-123 self-check

확인 시각: 2026-08-17T11:45Z. 공개 게시, 로그인, 공식 링크 발급, 댓글, DM, 광고 집행 없음.

## 2026-08-19 Sharelink Open API self-check

- Official guide used: `https://sharelink-docs.toss.im/guide/open-api`
- Credential storage: local `.env`, gitignored, file mode `600`.
- Token issuance: PASS.
- Health check: PASS.
- Product/category lookup: PASS.
- Link issuance: PASS for 3 unpublished test candidates.
- Private link cache: `.sharelink-cache/marketing-123-links-20260819T1201Z.json`.
- Public artifact: `artifacts/marketing-123/sharelink-api-execution-20260819T1215Z.md`.
- Safety boundary: official links were issued for preparation, but not posted, shared, sent by DM, advertised, or inserted into a public channel.
- Current stop point: explicit user approval is required before public Threads posting or public affiliate link sharing.

## 2026-08-19 dashboard retry

- Dashboard action: `resolve_waiting`
- Request id: `59c08d5b-a7a6-42e8-9e86-b8d9dc58bc26`
- Queue result: S3 `action_requests/processed/2026/08/19/20260819T071410Z-marketing-123-resolve_waiting-59c08d5b-a7a6-42e8-9e86-b8d9dc58bc26.json`
- SAM action: Sharelink/Toss Shopping member-screen check attempted.
- Current stop point: Toss Business/토스쇼핑 파트너스 로그인 화면. QR login or email/password login is required before member-screen product/link checks.
- Safety boundary: no public post, official link share, account setting change, purchase, payment, comment, DM, or ad action was performed.
- Next executable step: after the user completes Toss login in the browser session, check whether the 3 actual-purchase candidates or close substitutes can issue official Sharelink URLs, then request explicit public-post approval.

| 항목 | C01 파우치/칫솔 | C02 멀티플러그/종이세제 | C03 손톱깎이/수건/빨랫줄 |
|---|---|---|---|
| 실제 구매/준비 근거 | PASS | PASS | PASS |
| 여행 대시보드/Notion source 기록 | PASS | PASS | PASS |
| 실제 사용 후기 단정 없음 | PASS | PASS | PASS |
| 기존 미근거 후보 제거 | PASS | PASS | PASS |
| 가격·재고·옵션·배송·환불 확인 시각 | PRE-PUBLISH RECHECK REQUIRED | PRE-PUBLISH RECHECK REQUIRED | PRE-PUBLISH RECHECK REQUIRED |
| 고지가 링크보다 앞섬 | PASS | PASS | PASS |
| 금지 표현 없음 | PASS | PASS | PASS |
| 상황·선택 선언형 첫 줄 | PASS | PASS | PASS |
| 후보별 각도 차이 | PASS | PASS | PASS |
| Sharelink 회원 화면/API self-check | PASS_OPEN_API | PASS_OPEN_API | PASS_OPEN_API |
| 공식 Sharelink URL | ISSUED_PRIVATE_CACHE | ISSUED_PRIVATE_CACHE | ISSUED_PRIVATE_CACHE |
| 사용자 발행 승인 | PENDING_EXPLICIT_APPROVAL | PENDING_EXPLICIT_APPROVAL | PENDING_EXPLICIT_APPROVAL |
| Red pass | PASS_PREPUBLICATION_PACKAGE | PASS_PREPUBLICATION_PACKAGE | PASS_PREPUBLICATION_PACKAGE |

판정: SAM이 해소 가능한 `실제 구매 근거 기반 후보·게시 초안·7일 운영 단위`와 Sharelink Open API 기반 `상품 조회·공식 링크 발급 가능 여부` 확인은 완료했다. 기존 일반 후보 중 실제 구매 근거가 없던 항목은 제외했고, 초안은 실제 사용 후기처럼 단정하지 않고 구매/준비 기준으로 낮췄다. 남은 대기는 공개 발행 승인이다.

회원 화면 self-check에서 볼 것:

- 후보 3개 또는 유사 상품이 토스쇼핑 Sharelink로 발급 가능한가
- 발급 링크가 각 상품 단위인지 검색/카테고리 단위인지
- 상품명, 가격, 옵션, 배송, 재고가 공개 초안과 충돌하지 않는가
- 수수료/정산/고지 조건 화면에 추가 제약이 있는가
- 게시 전 고지 문구가 링크보다 위에 배치되는가
