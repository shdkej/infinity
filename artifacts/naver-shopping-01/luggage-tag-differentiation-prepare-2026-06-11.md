# 캐리어네임택/러기지택 차별화 검증 준비 (Cloud Prepare Pass)

- created: 2026-06-11T01:07Z
- mode: prepare (cloud)
- source: heartbeat agent web research pass
- next: 로컬 에이전트 OpenAPI/SearchAd 차별화 테스트용 입력 자료

## 배경

2026-06-10T20:07Z paper/card insert HOLD 처리 이후, 다음 안전 액션으로 지정된 `캐리어네임택`/`러기지택` 커스터마이제이션 차별화 테스트 전 클라우드 준비 패스.

## 시장 관찰 (웹 조사)

### 현재 플레이어 유형

| 유형 | 예시 판매처 | 가격대 | 포지션 |
|------|------------|--------|--------|
| 자수(embroidery) 커스텀 | 슬샵(zigzag), 힐링메이커스 | 9,900~11,400원 | 감성/개성/핸드메이드 |
| 양면인쇄 커스텀 | moodgoods, customshop.kr | 5,000~15,000원 | 저가~중가 범용 |
| 가죽(leather) 프리미엄 | LOMAD, spacelogic (이탈리아가죽) | 20,000원+ | 고급 선물 |
| 디자이너 브랜드 | Hozumi, Plepic | 10,000~20,000원 | 미감/디자인 |
| 스마트 기술 통합 | Samsung SmartTag2 러기지택 | 번들 제품 | 기술 |
| IP 캐릭터 | 해리포터, 푸바오 (Samsung) | 번들/고가 | 팬덤 |
| DIY 체험형 | 쌈지길 오프라인 | 10,400원/회 | 체험 (온라인 판매 불가) |

### 차별화 각도 분석

**자수(embroidery) 유형 - user-fit 가장 강함**
- 힐링메이커스: 양면, 9,900원 정가 12,900원, 자체 제작 루트
- 슬샵: 자수, 11,400원, 지그재그(패션 채널)에서 판매 → 패션/감성 구매자 타겟
- 차별화 포인트: 이름/이니셜 자수 + 사용자 여행 스타일(감성, 미니멀) 연결
- 콘텐츠 각도: "나만의 여행 장비 셋업" / "여행자 정체성 표현 소품"

**가죽(leather) 포지션**
- RIMOWA, Delsey, spacelogic → 프리미엄 브랜드 번들 또는 수입 아이템
- 소량 첫 상품으로 진입하기에는 소싱 난이도 높음
- 단가 압박으로 margin 확보 어려울 수 있음

**스마트태그 통합**
- Samsung 주도 → 제조사 번들이라 틈새 없음
- 단, SmartTag2 없는 여행자에게는 irrelevant

**IP/캐릭터**
- 라이선스 필요 → 소량 첫 상품 부적합

### 사용자 Fit 분석 (Knowledge Lab Idea/Travel.md 맥락)

- 사용자는 여행 기록, AI/크리에이터 워크플로우, 데일리 시스템에 강함
- "여행자 정체성" 표현 물건 → 커스텀 네임택은 여행 출발 전 준비 의식과 연결
- 콘텐츠 생산: "내 여행 짐 셋업" 숏폼/리뷰 자연스러운 소재
- 자수 커스텀: 핸드메이드 감성 + 1개 주문제작 → 소비자 체험 서사 생성
- 사용자 제품 판단 기준: 여행, 기억 만들기, AI/크리에이터 워크플로우, 일상 시스템, 기록 리듬과 맞아야 함

## 핵심 테스트 질문 (로컬 에이전트용)

**Q1 (SearchAd exact):** `캐리어네임택` vs `러기지택` vs `커스텀 캐리어네임택` vs `자수 네임택`
- 월간 검색량 비교
- 가설: `캐리어네임택`이 broad term으로 가장 크고, `커스텀`/`자수` 수식어가 구매의도 높음

**Q2 (OpenAPI top-20 + 가격 분포):** `캐리어네임택 커스텀` 검색
- 자수 vs 인쇄 vs 가죽 비율? → 자수 비율이 낮으면 차별화 공간 있음
- 가격 분포: 10,000원 이하 / 10,000~20,000원 / 20,000원+ 각각 몇 개?

**Q3 (SearchAd):** 대안 키워드 볼륨 확인
- `여행 이름표`, `가방 이름표`, `이름표 커스텀`, `여행 네임택`
- 가설: 네이버에서 `이름표`가 더 native 검색어일 수 있음

**Q4 (OpenAPI):** `러기지택 커스텀` top-10 가격대 분포
- `러기지택` 브랜드 스토어가 결과를 차지하는지? 아니면 개인 판매자 공간?

## 검증 루브릭 (로컬 테스트 통과 기준)

### PROMOTE 조건
- SearchAd `캐리어네임택` ≥ 5,000/월 (transactional demand 확인)
- `커스텀 캐리어네임택` or `자수 네임택` ≥ 500/월 (niche keyword viable)
- 10,000~20,000원 가격대에 top-10 자수 커스텀 경쟁자 ≤ 5개 (white space 존재)
- 사용자가 콘텐츠로 자연스럽게 다룰 수 있는 스토리 각도 확인

### WATCH 조건
- 키워드 볼륨 충분하나 자수 커스텀 경쟁자 이미 5개 초과
- 또는 볼륨은 낮지만 margin/콘텐츠 각도 추가 검증 필요
- 가격 분포에서 10,000~20,000원대 공간이 애매한 경우

### HOLD 조건
- 자수 커스텀 이미 다수 플레이어 밀집 + 낮은 margin (9,000원 이하 다수)
- 검색 볼륨 < 1,000/월 across all keywords
- 사용자 콘텐츠 각도와 fit 없는 경우

## 다음 로컬 에이전트 실행 명령

```
bounded_test: luggage-tag-customization-differentiation
tools: [Naver SearchAd API, Naver OpenAPI shopping search]
priority_keywords:
  1. 캐리어네임택  (broad, SearchAd + OpenAPI top-20)
  2. 러기지택       (broad, SearchAd + OpenAPI top-20)
  3. 커스텀 캐리어네임택  (niche, SearchAd exact)
  4. 자수 네임택    (niche, SearchAd exact)
  5. 여행 이름표    (alternative, SearchAd exact)
data_targets:
  - SearchAd exact monthly volume (PC + mobile)
  - OpenAPI top-20 price range distribution for 캐리어네임택 커스텀
  - Count of differentiation types (embroidery/print/leather) in top-20
  - Review count distribution if accessible
rate_limit_note: SearchAd limit hits fast — prioritize keywords 1 & 2 first
output_artifact: luggage-tag-differentiation-test-2026-06-11.md
verdict_format: PROMOTE | WATCH | HOLD + one-line reason
verdict_criteria: see 검증 루브릭 above
approval_boundary: SearchAd/OpenAPI read-only only. No store/listing/price/ad action.
```
