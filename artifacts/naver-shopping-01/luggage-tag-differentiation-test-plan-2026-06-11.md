# 캐리어네임택/러기지택 차별화 테스트 플랜

- intent: naver-shopping-01
- created_at: 2026-06-11T01:07Z
- mode: cloud-prepare
- next_step: local-execute (SearchAd / OpenAPI / DataLab 검증)

## 배경

- 19:07Z screen: `캐리어네임택` 7,310/mo, `러기지택` 3,780/mo — 가장 낮은 friction의 WATCH 표면
- 20:07Z test: paper/card insert HOLD — Naver keyword noise 심함 (trading card, photo card 오염)
- 목표: 캐리어네임택이 단순 generic object를 넘어 **arrival-day failure-prevention 스토리**를 담을 수 있는지 키워드로 검증

## 웹 조사 요약 (Cloud pass)

### 시장 신호
- 한국 내 DIY 러기지택 체험 수요 확인: 인사동 쌈지길 ₩10,400/개 (커스텀 이름+이모지)
- 2026년 해외여행 수요 급증, 프리미엄 여행 액세서리 트렌드 강세
- Etsy, Zazzle, MochiThings 등 해외에서 Korean/Seoul 테마 러기지택 판매 활성
- personalized/customized luggage tag: "no minimum quantity" 소량 맞춤 수요 있음
- 개인화 각도가 가장 경쟁력 있는 차별화 방향으로 보임

### 경쟁 환경 관찰
- 시장은 크게 3 tier: ① 대량 generic PVC/실리콘 ② 디자인 인쇄 ③ 커스텀/각인/자수
- Tier ③이 가격 프리미엄을 실현할 수 있는 공간
- 사용자 취향(미니멀, 시스템, 여행 스토리)과 fit

## 키워드 가설 세트

### 각도 A: 개인화/커스텀
| 키워드 | 예상 성격 | 검증 포인트 |
|--------|-----------|-------------|
| `커스텀 캐리어 네임택` | 명확한 intent | volume + top-10 object type |
| `이름 캐리어 네임택` | 개인화 명시 | noise vs. 개인화 상품 비율 |
| `이니셜 러기지택` | 모노그램 수요 | SearchAd volume |
| `이니셜 캐리어 택` | 동의어 체크 | - |
| `영어이름 캐리어 택` | 해외여행 수요 | - |

### 각도 B: 소재/품질
| 키워드 | 예상 성격 | 검증 포인트 |
|--------|-----------|-------------|
| `가죽 캐리어 네임택` | 프리미엄 신호 | volume + margin 가능성 |
| `가죽 러기지택` | 동의어 | - |
| `메탈 캐리어 택` | 내구성/고급 | 상위 상품 가격대 |
| `알루미늄 러기지택` | 차별화 소재 | - |

### 각도 C: 여행 선물/감성
| 키워드 | 예상 성격 | 검증 포인트 |
|--------|-----------|-------------|
| `여행 선물 네임택` | 선물 수요 | volume + 가격 프리미엄 |
| `여행 기념품 네임택` | 소비자 구매 맥락 | - |
| `감성 러기지택` | 취향 소비 | 상위 상품 스타일 |
| `여행 선물 러기지택` | 선물 각도 | - |

### 각도 D: 도착일/스토리 (원래 arrival-day 가설 연장)
| 키워드 | 예상 성격 | 검증 포인트 |
|--------|-----------|-------------|
| `캐리어 구별 택` | 분실방지/식별 | noise level |
| `캐리어 분실 방지` | 실용 narrative | SearchAd + 오브젝트 타입 |
| `내 캐리어 구분` | 동의어 | - |
| `수하물 이름표` | 공항 context | cpc 수준 |

## 판독 기준 (Promote / Pivot / Hold)

| 판정 | 조건 |
|------|------|
| **PROMOTE** | SearchAd ≥ 1,000/mo + mobile CTR ≥ 2% + top-10에서 customized/quality object ≥ 50% |
| **PIVOT** | volume 있지만 commodity/noise 지배적 → 다른 각도 탐색 |
| **HOLD** | volume < 300/mo 또는 non-product noise 지배적 |

## 로컬 실행 요청

다음 순서로 Local SearchAd/OpenAPI/DataLab 검증 수행:

1. **SearchAd API**: 각도 A~D 전체 키워드 exact-match volume + 예상 CPC
2. **OpenAPI top-10**: 각 각도별 대표 키워드 top-10 상품 유형 분류 (generic/custom/quality/noise)
3. **DataLab**: 캐리어용품 또는 여행용품 카테고리 top-20 키워드 rank 확인
4. 결과 정리 후 report 작성 (`reports/naver-shopping-01/2026-06-11T{time}Z-local.html`)
5. PROMOTE 후보가 나오면 소싱/friction screen → 승인 라우팅 준비
