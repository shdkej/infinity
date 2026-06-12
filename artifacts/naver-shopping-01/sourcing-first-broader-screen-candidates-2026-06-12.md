# naver-shopping-01: Sourcing-First Broader Screen Candidates

- id: naver-shopping-01-sourcing-broader-screen
- prepared_at: 2026-06-12T06:00Z
- mode: Cloud prepare (for local Naver Shopping Agent execution)
- artifact_type: research
- context: 사용자 선호 업데이트(2026-06-11): 나래는 소싱 중심. 러기지택 선호 낮음. 더 넓은 소싱-우선 스크린 필요.

## 이전 스크린 요약 (제외된 경로)

| 카테고리 | 결론 | 사유 |
|---------|------|------|
| 캐리어네임택/러기지택 | DOWNGRADED | 사용자 선호 낮음 (2026-06-11) |
| 워크샵/질문카드 | WITHDRAWN | 사용자 직접 철회 (너무 미시적, 네이버 수익 부적합) |
| 반도난/문서 케리 | WATCH | 수요 있지만 commodity-heavy, 소싱 복잡 |
| 종이/카드 삽입물 | HOLD | generic shelf, buyer intent 약함 |

## 다음 스크린 대상: 6개 소싱-우선 후보 카테고리

우선순위: 사용자 선호 적합도 + 소싱 마찰 낮음 + 옵션 복잡도 낮음 + QA/반품 리스크 관리 가능

---

### Category 1: 폴라로이드/즉석사진 액세서리

- **User fit**: travel + memory-making (매우 높음)
- **예시 상품**: 폴라로이드 포토 코너 스티커, 미니 앨범, 즉석사진 홀더/슬리브
- **소싱 경로**: Alibaba/중국 도매 sourceable, MOQ 낮음 (50개 이하 예상)
- **옵션 복잡도**: 낮음 (사이즈별 1-2가지)
- **QA/반품 리스크**: 낮음
- **Naver 키워드 테스트**: `폴라로이드 포토코너`, `즉석사진 홀더`, `폴라로이드 앨범`, `미니 포토앨범`, `사진 슬리브`
- **Content angle**: 여행 메모리 만들기 — 사용자의 travel+memory 리듬과 직접 연결

---

### Category 2: 디지털 액세서리 정리 파우치

- **User fit**: AI/creator workflow + travel (높음)
- **예시 상품**: 케이블 정리 파우치, SD카드 케이스, 이어폰+충전기 정리 파우치
- **소싱 경로**: highly sourceable
- **옵션 복잡도**: 낮음-중간
- **QA/반품 리스크**: 낮음-중간
- **Naver 키워드 테스트**: `케이블 정리 파우치`, `여행 전자기기 정리`, `멀티 파우치`, `SD카드 케이스`, `충전기 파우치`
- **Content angle**: 디지털 크리에이터/AI 워크플로우 정리

---

### Category 3: 여행/플래너 스티커 세트

- **User fit**: documentation rhythm + travel + memory-making (높음)
- **예시 상품**: 여행 테마 스티커, 다이어리 꾸미기 스티커, 플래너 스티커 시트
- **소싱 경로**: sourceable / printable-on-demand 가능
- **옵션 복잡도**: 낮음-중간
- **QA/반품 리스크**: 낮음
- **Naver 키워드 테스트**: `여행 스티커`, `다이어리 꾸미기 스티커`, `플래너 스티커`, `여행 다이어리 꾸미기`, `버킷리스트 스티커`
- **Content angle**: 여행 기록/다이어리 꾸미기

---

### Category 4: 마그네틱 북마크 세트

- **User fit**: documentation rhythm + daily system (높음)
- **예시 상품**: 마그네틱 책갈피, 페이지 마커 클립, 노트북/다이어리용 북마크
- **소싱 경로**: sourceable, very low MOQ
- **옵션 복잡도**: 매우 낮음
- **QA/반품 리스크**: 매우 낮음
- **Naver 키워드 테스트**: `마그네틱 책갈피`, `마그네틱 북마크`, `페이지마커`, `책 북마크`, `자석 책갈피`
- **Content angle**: 독서/문서 정리 시스템

---

### Category 5: 투명 지퍼 파우치 세트

- **User fit**: travel + packing organization (중간)
- **예시 상품**: 투명 여행 파우치, 분리 수납 지퍼백 세트
- **소싱 경로**: highly sourceable, commodity
- **Naver 키워드 테스트**: `투명 파우치`, `여행 파우치 세트`, `지퍼백 파우치`, `수납 파우치 세트`
- **주의**: commodity shelf, 경쟁 강함. 우선순위 낮음.

---

### Category 6: 미니 폰 스탠드 / 링홀더

- **User fit**: AI/creator workflow + daily system (중간-높음)
- **예시 상품**: 폰 링홀더 + 스탠드 콤보, 데스크탑 폰 스탠드
- **소싱 경로**: highly sourceable
- **Naver 키워드 테스트**: `폰 링홀더`, `스마트폰 스탠드`, `폰그립 스탠드`, `링홀더 콤보`
- **주의**: 경쟁 강한 시장. story/angle 필요.

---

## 스크린 실행 템플릿 (로컬 에이전트용)

### Demand Check (OpenAPI Shopping Search)
- 키워드별 SearchCount (목표: 5,000+/mo mobile preferred)
- Top-10 listing 가격 범위 (median)
- 카테고리 적합성

### Competition Check (OpenAPI)
- 전체 상품 수
- 브랜드 지배도 (1-2개 브랜드 독점 = 진입 어려움)
- Top-10 평균 리뷰 수

### Keyword Quality (SearchAd)
- PC + mobile 월간 검색량
- Mobile CTR (목표: 2%+)
- CPC 추정

### Sourcing Friction Gate
- Alibaba/타오바오 유사 상품 존재 여부
- MOQ 추정 (목표: 50개 이하)
- Unit cost × 3 margin check

### 판정 기준

| 판정 | 조건 |
|------|------|
| **PASS** | 수요 5,000+, CTR 2%+, 소싱 가능, margin OK |
| **WATCH** | 수요 있지만 경쟁 강하거나 소싱 마찰 있음 |
| **DRAFT** | copy/story-led 가능하지만 keyword 약함 |
| **HOLD** | 수요 약하거나 사용자 선호 낮음 |

## 우선 스크린 순서

1. Category 1 (폴라로이드 액세서리) — User fit 가장 높음
2. Category 3 (여행/플래너 스티커) — Documentation rhythm 직접 연결
3. Category 2 (디지털 정리 파우치) — AI/creator workflow fit
4. Category 4 (마그네틱 북마크) — 진입 마찰 최소
5. Category 6 (폰 스탠드/링홀더) — creator workflow fit
6. Category 5 (투명 파우치) — commodity, 우선순위 낮음

## Routing

이 문서는 Cloud prepare artifact다.
로컬 Naver Shopping Agent가 다음 실행에서 위 스크린 템플릿으로 OpenAPI + SearchAd 데이터를 수집하고
결과를 `product-curation.md`에 반영한다.
