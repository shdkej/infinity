# 러기지 태그/캐리어 명찰 분화 키워드 검증 준비

- intent: `naver-shopping-01`
- date: 2026-06-11
- mode: prepare (cloud) — Naver Shopping IP 차단 상태. Electron 세션 복귀 시 실행
- scope: 키워드 후보 분류 + 검증 프로토콜 준비. 소싱/상품등록/공개 카피/광고/재고/가격/배송/고객/주문/계정 액션 0

## 0. 배경

2026-06-10 arrival-day-insert keyword test 결과:
- `해외여행 체크리스트`: mobile CTR 0.05%, generic commodity — HOLD
- `여행 준비 카드` / `여행 체크리스트 카드`: trading card/photo holder noise — HOLD

다음 검증 후보: luggage-tag / 캐리어 명찰 (arrival-day failure-prevention 프레임 유지)

적용 기준: m50 (Purchase Situation Before Object Shape)

## 1. 구매 상황 기반 키워드 후보

| 구매 상황 | 리드 키워드 후보 | 차별화 포인트 |
|---|---|---|
| 수하물 찾기 식별 | `캐리어 명찰`, `러기지 태그 가죽`, `캐리어 명찰 커스텀` | 패션/캐릭터 태그와 분리 가능 |
| 분실 방지 — 연락처 보안 | `여행 네임태그`, `네임택 여행`, `러기지 태그 이름` | 감성 캐릭터 태그와 차별화 |
| 개인 아이덴티티 표현 | `캐리어 꾸미기 태그`, `러기지 태그 커스텀` | 기능+감성 이중 소구 |

## 2. 소음 키워드 (title 단독 사용 금지)

| 키워드 | 예상 노이즈 유형 |
|---|---|
| `여행 태그` | 광범위 여행 소품 / 스티커·배지 포함 |
| `러기지 태그` (단독) | 패션·캐릭터·로고 태그 포화 예상 |
| `캐리어 태그` (단독) | 캐릭터 스티커 노이즈 |
| `수하물 태그` | 항공사 비닐 태그 연상, buyer intent 약함 |

## 3. 검증 프로토콜 (Naver 접근 복귀 시)

읽기 전용 검색: 각 키워드 상위 20개 상품 분류

Shelf 판정:
- CLEAN: 기능형/식별용 70%+ — buyer intent 있음
- MIXED: 관련 상품 절반, 노이즈 혼재
- NOISY: 타겟 외 상품 60%+

수치 기준: mobile SearchAd 500+/mo, CTR 0.1%+

PROMOTE/PIVOT/HOLD 기준 (keyword-competitor-validation-plan.md 계승):
- PROMOTE: Shelf CLEAN + mobile 500+/mo + CTR 0.1%+
- WATCH: Shelf MIXED, 기능형 경쟁자 존재
- PIVOT: Shelf NOISY, 패션·캐릭터 포화
- HOLD: 검색량 200/mo 미만

## 4. 우선 검증 순서

1. `캐리어 명찰` — 기능형 명찰 시장 여부 확인 (shelf 오염도 낮을 것으로 예측)
2. `여행 네임태그` — 이름·연락처 중심 shelf, 캐릭터 노이즈 수준 확인
3. `러기지 태그 가죽` / `러기지 태그 커스텀` — 수식어로 shelf 좁힘
4. `캐리어 명찰 커스텀` — 개인화 각도 최적 좁힘

## 5. 사용자 fit

- 여행·기록·시스템·소품 관심 → 실제 문제 해결형 실용 아이템: fit HIGH
- 커스텀/가죽 소재: 기록·소장 가치와 연결, fit MEDIUM-HIGH

## 6. 다음 액션

- Electron 브라우저 세션 복귀 시: `캐리어 명찰` 검색부터 시작
- 접근 지속 차단 시: OpenAPI total count 공개 API 재탐색
- 검증 결과에 따라 listing-direction approval 요청 여부 결정 (write/listing/price는 approval-needed)
