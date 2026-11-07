# 미국 IT 시장 창업 기회 탐색 지도 — 1차 근거판

- 조사 기준일: 2026-11-06 (UTC)
- 범위: 미국 IT 카테고리와 인접 업무의 구조화. 단일 기회 추천, 투자·출시 결정은 하지 않는다.
- 판정: 이 문서는 초기 증거 지도다. 고용 전망·기술 채택·벤더 제품 존재는 고객의 구매 의사나 스타트업 수익성을 직접 증명하지 않는다.
- 사용자 맥락: Knowledge Lab의 AI 위임/사업 판단 노트는 AI를 사람을 대체하는 유행이 아니라 반복 업무·고객의 선택·실제 구매 신호와 연결해 살펴보도록 한다. 참고: `agent-wiki/content/docs/outputs/deep-knowledge/ai.mdx` §AI에게 위임할 수 있는 것; `outputs/Integration/Business.mdx` §핵심 판단 모델·운영 판단판.

## 읽는 기준

각 카테고리는 제품군 이름보다 `구매자 → 반복 업무/손실 → 현행 대안 → 변화 신호`로 읽는다. 근거 레이블은 `공식 통계/규칙`, `벤더 자기기술`, `가설`로 분리한다. 회사 제품은 해당 카테고리의 존재를 보여주는 예시이지 시장점유율·만족도 순위가 아니다. 사례별로 미국 진출과 한국 적용은 별도 질문으로 둔다.

## 카테고리 지도 (비랭킹)

| 영역 | 구매자·반복되는 일 | 대표 사례(예시)와 사업모델 패턴 | 대체 접근 | 초기 변화 신호·근거 상태 |
|---|---|---|---|---|
| 클라우드·데이터 기반 | 개발·IT·데이터 조직이 서버/저장소/DB/분석환경을 만들고 운영·비용·복구를 관리 | AWS: 컴퓨트·저장·DB·분석·네트워크 등 클라우드 서비스; 사용량 기반 인프라 과금(벤더 설명) | 자체 데이터센터, 다른 클라우드, 매니지드 서비스, 오픈소스/온프레미스 | Census ABS는 클라우드 기반 기술과 특수 소프트웨어를 업무상 중요하다고 답한 기업 비중이 높았음(아래 표본/기간 한정). 구매 예산·클라우드 이탈·비용 최적화 수요는 별도 확인 필요. |
| 업무용·수직 SaaS | 운영/재무/영업/인사/고객지원/산업별 팀이 기록·승인·정산·일정·재고 등 프로세스를 처리 | Stripe 제품군(결제/청구/세금/사기 방지 등), Epic EHR(의료 기록); 구독/거래 수수료/사용량/계약형은 카테고리의 일반적 모델 패턴(개별 가격은 별도 확인) | 스프레드시트·이메일, 기존 ERP/CRM/EHR, 아웃소싱/BPO, 수작업 | Census는 클라우드·특수 소프트웨어 채택의 주요 동기로 프로세스 품질·신뢰성 개선을 보고. 업종·구매자별 워크플로우와 실제 지출 근거는 부족. |
| 개발자 도구·소프트웨어 공급망 | 엔지니어링 팀이 코드 작성·리뷰·테스트·배포·취약점 대응을 반복 | GitHub: 저장소, 코드 리뷰, Actions CI/CD, 보안 기능, 개발 에이전트; 좌석/조직/사용량 기반 요금 패턴 | 자체 툴체인, 오픈소스 forge/CI, 클라우드 제공 도구, 수동 릴리스 | GitHub 제품 페이지는 기능 범위만 증명한다. BLS 보안 인력 전망은 기술 노동 수요 신호이지 개발 보안 제품 구매 신호는 아님. 통합·권한·오탐·리뷰 병목을 고객 인터뷰로 검증해야 함. |
| AI·자동화·데이터 앱 | 기능 조직/IT가 문서·문의·분류·예측·검색 등 정보 처리와 예외 핸들링을 개선하려 함 | AI/분석/워크플로 제품은 API·사용량·좌석·성과연동 모델을 취할 수 있음(범주 패턴, 가설) | 규칙 기반 자동화, 인력 증원/BPO, 기존 SaaS 기능, 검색/템플릿, 작업을 하지 않음 | Census BTOS 기반 CES 논문(2023-09~2024-02)은 기업 AI 사용률이 3.7%→5.4%로 올랐다고 추정하고, 적용 불가를 비도입의 흔한 이유로 보고. AI 도입 자체를 보편적 수요 또는 지불의사로 해석하면 안 됨. |
| 보안·컴플라이언스 | CISO/IT/법무/재무가 취약점·사고·접근권한·감사 증거·복구·공시를 관리 | BLS 정보보안 분석가 전망은 직업 수요의 방향 지표. SEC 규칙은 상장사에 중대한 사이버 사고 및 거버넌스 공개 요구를 둠. 벤더 예: GitHub code security | 내부 보안팀, MSSP/컨설팅, 클라우드·개발 플랫폼 번들, 보험/감사 체크리스트 | BLS의 2025–35 고용 전망 +21% 및 SEC 공시는 문제의 제도·인력 맥락을 보여줄 뿐, 신생 보안 제품 시장 크기나 구매 의사 증거는 아님. 신뢰·책임·조달·인증 장벽이 큼(검증 가설). |
| 헬스 IT·상호운용성 | 의료기관·보험자·환자 앱이 기록·예약·청구·사전승인·교환·환자 제출 데이터를 연결 | CMS가 소개하는 Epic 등 EHR/네트워크 참여자, CMS의 자발적 상호운용성 프레임워크 | 기존 EHR 모듈, HIE/네트워크, 팩스·전화·수작업, 통합 전문업체 | CMS는 2026년 프레임워크의 참여자 유형과 FHIR/USCDI 등 데이터 교환 기준을 공개. 이는 제도적 방향 신호이며, 채택·구매·성과는 해당 업체별로 추가 확인 필요. |
| 핀테크·커머스 기반 | 판매자/플랫폼/재무팀이 결제 수납, 정산, 사기·분쟁, 구독·세금·국경 간 지급을 처리 | Stripe: 결제, Connect, Billing, Tax, Radar 등(제품 자기기술); 거래 수수료/소프트웨어·금융 수익 조합은 범주 패턴 | 은행·카드사 직접 연동, PSP/마켓플레이스 기본 기능, 수기 정산 | Stripe 제품 페이지는 상품 범위와 판매자 주장을 보여줄 뿐, 특정 고객군의 미충족 요구나 경쟁 우위를 입증하지 않는다. 승인율·분쟁률·정산 지연의 실제 업무비용을 확인할 필요. |

## 근거 강도·최신성·수요 단계 비교

| 영역 | 근거 강도(이 주장에 한해) | 최신성/관측 시점 | 현재 입증된 수요 단계 | 구매·유지 증거 |
|---|---|---|---|---|
| 클라우드·데이터 | 중간 — 공식 Census employer-business 조사 요약의 기술 중요도/채택 동기 | 게시 2025-09; 기준 자료 2020–2022 | 채택·업무 중요성 | 지출/계약·유지율 미측정 |
| 업무·수직 SaaS | 낮음 — Census의 넓은 특수 소프트웨어 신호이며 업종별 제품 수요는 아님 | 위와 동일, 오래된 관측 | 범주 수준 채택 신호 | 세그먼트별 구매/유지 미측정 |
| 개발자 도구 | 낮음 — GitHub 제품 자기기술 | 조사일 2026-11-06 스냅샷 | 제품 존재/기능 주장 | 독립 고객 결과·지출 증거 없음 |
| AI·자동화 | 중간 — Census working paper의 관측기간 사용률 추정 | 2024-03 게시; 관측 2023-09~2024-02 | 채택/사용 | 예산·지불·유지 미측정 |
| 보안·컴플라이언스 | 중간 — BLS 고용 전망과 SEC 규칙은 각자 인력/규제 주장에는 강함 | SEC 2023; BLS 전망 2025–2035 | 규칙·관련 직무 수요 | 스타트업 상품 구매/유지 미측정 |
| 헬스 IT | 중간 — CMS 공개 프레임워크/참여자 정보 | 2026 framework 및 2026-07 GA 목록 | 정책 방향/공개 참여 | 참여 사실은 지출·성과·유지 증거 아님 |
| 핀테크·커머스 | 낮음 — Stripe 제품 자기기술 | 조사일 2026-11-06 스냅샷 | 제품 존재/기능 주장 | 특정 구매자군의 지불·유지 미측정 |

강도는 자료의 수가 아니라 해당 출처가 그 문장 자체를 얼마나 직접 뒷받침하는지 표시한다. `제품 존재 → 채택/업무 사용 → 예산/지출 → 반복 구매/유지` 사다리에서 현재 자료는 대체로 제품 존재 또는 채택/제도 단계에 머물며, 예산·유지 단계는 미측정이다.

## 미국 진출과 한국 적용은 별도 축

- **미국 직접 진출:** 구매자와 예산 소유자가 누구인지, 주·연방별 규제/조달/보안 요구, 유통 채널과 기존 플랫폼의 번들 기능, 고객 지원·책임 구조를 별도 조사해야 한다. 이번 1차 지도만으로 시장 진입 가능성을 판정하지 않는다.
- **한국 적용:** 같은 문제 빈도와 지불 의사가 한국에도 있는지 확인해야 한다. 언어·결제/세금·개인정보/의료 규정·공공 및 대기업 조달·국내 레거시/유통 파트너가 달라질 수 있다. 미국 제품의 단순 현지화로 성립한다고 가정하지 않는다.
- **교차 영역:** AI는 별도 시장 칸이면서 클라우드, 보안, 개발도구, 수직 SaaS의 기능층이다. 한 회사가 여러 카테고리에 걸치는 경우 중복 집계하지 않는다.

## 공개 구매·예산 신호 (사례 증거, 국가 비교 아님)

앞선 지도에는 실제 구매·예산 근거가 거의 없었다. 아래는 공개 기록으로 확인되는 **두 국가의 서로 다른 공공조달 사례**다. 시장 전체, 민간 소프트웨어 수요, 일반적 구매 의사로 외삽하지 않는다.

| 국가/구매자 | 공개 기록과 범위 | 금액·단계 | 수요 증거의 의미 | 경계 |
|---|---|---|---|---|
| 미국 / Department of Veterans Affairs (VA) | USAspending 계약 PIID `36C10B23F0346`; prime recipient Maveris LLC; “VA Cybersecurity Operations Center Next Generation II (CSOC NG II) Support”; performance period 2023-09-29–2027-09-28; PSC R499(기타 전문 지원), NAICS 541511(custom programming). | API 응답 조회일 2026-11-06: `total_obligation` $219,083,824.48; 별도 필드 `total_account_outlay` $147,432,546.43; `base_and_all_options` $331,158,125.88. 경쟁 제안 3건으로 기록. | 한 대형 연방 구매자가 장기간 사이버 운영/지원 서비스를 조달한 관측 사례. obligations는 정부의 지출 약정, outlays는 실제 지급을 나타내므로 다른 단계·집계 필드다. | 다년간 서비스·인력·운영이 결합된 계약이다. `total_obligation`을 제품 예산, 연간 매출, 민간 WTP로 볼 수 없다. 계정 outlay를 계약 총 지급액으로 단정하지 않는다. line-item 증거 없이 소프트웨어 몫을 분리할 수 없다. |
| 미국 / Department of Energy (DOE), SC Oak Ridge Office | USAspending PIID `89243126FSC400871`; `CROWDSTRIKE, INC. ENTERPRISE LICENSE AGREEMENT (ELA) - SC LABS`; NASA multiple-award GWAC `NNG15SC33B` delivery order, performance 2026-06-01–2027-05-30; recipient EMERGENT LLC(리셀러). USAspending의 solicitation ID는 비어 있음. | 2026-11-06 API 스냅샷: `total_obligation` $1,811,671.50; `total_outlay` $1,751,043.22; fixed-price, full-and-open competition, 3 offers; PSC DJ10 (Security and Compliance as a Service). | 연방 연구기관 단위에서 CrowdStrike enterprise license를 조달한 구체 사례. obligation과 outlay를 별도 필드로 확인. | 단일 delivery order이며 공개 API상 공급자는 리셀러다. 연간 시장규모·민간 WTP·독립 소프트웨어 가격/매출로 일반화하지 않는다. |
| 미국 / National Aeronautics and Space Administration (NASA) | USAspending PIID `80TECH26FA015`; NASA IT Procurement Office delivery order via NASA multiple-award GWAC `NNG15SC92B`; prime recipient THUNDERCAT TECHNOLOGY, LLC(리셀러); description: SentinelOne licensing subscription and data retention; PSC DA10 (SaaS), NAICS 541519; NASA solicitation `80TECH26QA010`, multiple-award fair opportunity (MAFO), total small-business set-aside, 1 offer; performance 2025-12-11–2026-10-31. | 2025-12-11 base action obligation/outlay $3,366,493.98; award current/potential amounts same in snapshot. History has 3 rows: base $3,366,493.98, `P00001` and `P00002` each $0. | 별도 연방 구매자의 보안 SaaS category 구매 기록 한 건. | 0달러 수정은 증액 증거가 아니며, quote/상품 설명은 SKU·seat 수·단가·결과나 독립적 vendor revenue를 확인하지 않는다. 민간 WTP/TAM/ARR로 일반화 금지. |
| 미국 / U.S. Immigration and Customs Enforcement (ICE), DHS | USAspending PIID `70CMSD25FR0000087`; 설명상 FinalMobile mobile-forensics software 갱신, NASA multiple-award GWAC `NNG15SD74B` delivery order; prime recipient Software Information Resource Corp.; 2025-09-27–2026-09-26, 옵션 포함 잠재기간 2028-09-26까지. | API 스냅샷 2026-11-06: `total_obligation`/`total_outlay` $29,022; `base_and_all_options` $87,066; 고정가격, 경쟁제한 후 경쟁, 2 offers; PSC 7A21 perpetual-license software. | 조사 업무용 모바일 분석 소프트웨어의 계약상 갱신/연속성 사례 1건. | 설명의 “renews”를 구독 SaaS나 연간 반복매출로 해석하지 않는다. 현재 의무액과 옵션 전체 잠재액을 분리하며 시장 크기로 외삽하지 않는다. |
| 한국 / 한국인터넷진흥원(KISA) | 2025-145 입찰공고 「전국 정보보호최고책임자(CISO) 대상 현황 조사 및 긴급 교육」, 게시 2025-08-04; 계약기간은 계약 후 2025-12-12까지. 공고에서 학술연구용역으로 명시. | 공고의 `소요예산` 99,700,000원(VAT 포함), 입찰 예정예산/공고 단계. 낙찰·계약액·실지급액은 이 기록만으로 확인하지 않음. | 한국 공공 구매자가 CISO 현황 조사 및 교육 용역에 예산을 배정해 경쟁입찰을 낸 관측 사례. | 보안 SaaS 구매가 아닌 조사·교육 서비스이며, 예정예산은 체결 또는 지급 증거가 아니다. 미국 계약과 기간·범위·회계단계·통화를 맞추지 않았으므로 수치 비교 금지. |
| 한국 / KISA (별도 이전 건) | 2024-081 「정보보호 최고책임자 지정 신고 실태조사」 사전규격공개, 2024-04-05; 용역 기간/공고 범위가 2025-145와 다름. | 78,000,000원(VAT 포함) 예정예산. | 별도 시점의 제한된 공공 연구용역 예산 신호. | 2025-145의 99.7M과 동일 입찰의 수정액이 아니다. 개별 공고이며 수주/지급액 아님. 반복 구매나 시장 추세로 간주하지 않는다. |

### Transaction history로 확인한 수정 범위

2026-11-06 조회한 공식 USAspending `POST /api/v2/transactions/` 결과를 별도 보존했다. DOE CrowdStrike ELA에는 2026-06-04 수정번호 `0`의 초기 의무액 $1,751,043.22와 2026-08-28 `P00001`의 “SUPPLEMENTAL AGREEMENT FOR WORK WITHIN SCOPE” / “ADD ADDITIONAL LICENSES” 추가 의무액 $60,628.28가 있어 현재 award obligation $1,811,671.50과 합치한다. 이는 같은 order 내 license 추가 수정의 직접 기록이지만 SKU·수량·단가 또는 전체 CLIN schedule은 보여주지 않으며, 옵션 행사라고 부를 근거도 없다.

NASA의 SentinelOne order `80TECH26FA015`는 별도 보안 소프트웨어 구매 사례다. 2026-11-06 23:34 UTC USAspending `SentinelOne` 키워드 검색은 14행(`hasNext=false`)을 반환했다. NASA detail/history는 모두 HTTP 200이며, 기록된 구매기관은 NASA IT Procurement Office, prime recipient는 reseller THUNDERCAT, parent는 NASA GWAC `NNG15SC92B`다. 세 거래행은 기본 $3,366,493.98(2025-12-11), `P00001` $0(2025-12-17), `P00002` $0(2026-05-20)이며, 수행기간은 2025-12-11–2026-10-31이다. 현재 award obligation/outlay/base-and-all-options는 각각 $3,366,493.98이다. 14행 검색 결과는 14개 award를 뜻하지 않는다. NASA order는 MAFO/총액 small-business set-aside 경로에서 1 offer로 기록되어 있다. 이 정보만으로 독점조달 또는 경쟁부재로 추론할 수 없으며 경쟁가격 발견으로 간주할 수도 없다. 이 응답은 공개 조달 의무와 설명된 scope를 확인하지만 seat 수, SKU, 단가, 구독과 data-retention 비용 분리, 사용자 결과, 추가 유료 갱신, 민간 WTP/TAM 또는 vendor-recognized revenue를 확인하지 않는다. 기간이 1년 미만인 이 주문액을 ARR로 표현하지 않는다. 완전한 query/detail/history raw payload는 `public-spend-observations.json`의 `distinct_buyer_security_purchase_20261106T2334Z`에 저장했다. [USAspending award detail](https://www.usaspending.gov/award/CONT_AWD_80TECH26FA015_8000_NNG15SC92B_8000/).

**FinalMobile 명칭의 ICE 조달 연속성 (서로 다른 award 기록):** USAspending 공식 API에서 `FinalMobile` 키워드 검색(계약 유형 C, 1페이지, 100행 한도, 거래액 내림차순, 2026-11-06 22:54:54Z, HTTP 200, 10행, `hasNext=false`)을 수행하고, 관련 두 award의 detail 및 전체 history를 보존했다. [2020 PIID `70CMSD20FR0000130`](https://www.usaspending.gov/award/CONT_AWD_70CMSD20FR0000130_7012_NNG15SD27B_8000/)는 prime recipient V3GATE LLC의 8개 거래행을 보이며 2020 기본 $25,857.30, 2021–2024의 네 건 각각 $25,908.15, 2025-12-02의 $0 closeout 설명이 있다(최신 obligation $129,489.90). [2025 PIID `70CMSD25FR0000087`](https://www.usaspending.gov/award/CONT_AWD_70CMSD25FR0000087_7012_NNG15SD74B_8000/)는 다른 prime recipient인 Software Information Resource Corp.의 단일 기본 거래 $29,022이며, 설명이 HSI의 mobile-data forensics software “FINALMOBILE” 갱신을 명시한다. 기록된 수행기간은 전 order 2020-08-13–2025-09-26, 후 order 2025-09-27–2026-09-26으로 인접하지만, 이는 두 별도 계약이며 같은 reseller·SKU·scope, 무중단 서비스 또는 상업적 ARR을 증명하지 않는다. 옵션 잠재액 $87,066은 행사액이 아니다. 별도 ICE PIID `70CMSD26FR0000041`은 “forensics examinations” agent-license 설명으로 2026-07-08 기본 $25,693.20과 2026-07-31 $0 funding-only 수정이 확인되지만 제품명을 언급하지 않아 FinalMobile과 연결하지 않는다. 조회 전문은 `public-spend-observations.json`의 `ice_finalmobile_search_20261106T2254Z`에 보존했다.

**DOE P00001 첨부 접근 경계:** USAspending은 P00001의 추가 라이선스 transaction을 보여주지만 첨부·CLIN 정보를 제공하지 않았다. 2026-11-06 SAM.gov 검색 페이지는 HTTP 200의 JavaScript shell로 응답했고, 정확 PIID로 시도한 SAM API 두 경로는 이 런타임에서 HTTP 404였다. GSA 문서는 Contract Awards API에 등록 계정/API key가 필요하고 SAM 계약-award 결과 열람도 로그인이 필요하다고 안내한다. 이는 접근 조건과 이번 경로의 결과일 뿐 첨부가 없거나 비공개라는 증거가 아니다. 첨부, CLIN, SKU, 수량, 단가는 계속 미확인이다. 정확 URL·UTC·HTTP status·응답 hash 및 공식 문서 링크는 `public-spend-observations.json`의 `doe_sc_p00001_official_access_check_20261106T2256Z`에 기록했다.

### 추가 연방 보안조달 스크리닝 (정확 ID 재검증)

2026-11-07 00:03–00:04 UTC에 USAspending 공식 API에서 세 PIID의 거래 검색, award detail, transaction history를 재조회했다. 검색·detail·history 응답은 HTTP 200이며, Treasury 이력은 10행 첫 페이지와 3행 두 번째 페이지를 모두 받아 총 13행으로 확인했다. 원문 요청/응답은 `public-spend-observations.json`의 `exact_id_revalidation_20261107T0004Z`에 보존했다.

| PIID / 구매기관 | 재검증된 이력 | 해석 경계 |
|---|---|---|
| DOE/NNSA `89233126FNA400754`, Thundercat Technology | NASA GWAC `NNG15SC92B` delivery order. 3행: 기본 $1,750,637(2026-01-06), `P00001` $9,924,171(2026-05-12), `P00002` $0(2026-09-04). 최신 award obligation $11,674,808; 수행기간 2026-01-01–2027-05-31(잠재 종료 2029-05-31). | 거래 설명은 Falcon/Falcon Complete licenses. 수정 행은 존재·날짜·금액·설명을 확인하지만 SKU 수량, CLIN, 단가를 보여주지 않는다. |
| DOJ `15JPSS23F00000692`, Thundercat Technology | NASA GWAC `NNG15SD26B` delivery order. 전체 8행: 기본 $1,417,931.50(2023-09-11); `P00014` $11,100(2025-09-23), `P00015` $325,101.85(2025-09-29), `P00016` $4,649,687.97(2025-12-02), `P00017` $6,972.50(2026-05-07), `P00018` $14,043.10 및 `P00019` $273,188.02(2026-09-11), `P00020` $273,188.02(2026-09-29). 최신 obligation $6,971,212.96; 수행기간 2023-09-13–2027-09-12(잠재 종료 2028-09-12). | 설명은 JMD/OCIO/CSS용 CrowdStrike license/support의 annual renewal. 개별 변동액을 연간 가격·ARR로 보거나 반복 거래를 민간 지불의사로 외삽하지 않는다. |
| Treasury/Fiscal Service `2033H624F00068`, FCN Inc. | NASA GWAC `NNG15SC71B` delivery order. 전체 13행(페이지 1=10, 페이지 2=3). 주요 행: `P00008` $1,701,003.89(2026-01-21, option period two 및 in-scope services), `P00010` $70,981.77(2026-08-13, additional within-scope items), `P00011` $507,069.03(2026-09-18, in-scope upgrade); `A00001` $0(2026-10-28). 최신 obligation $5,330,666.69; 수행기간 2024-02-01–2027-01-31(잠재 종료 2029-01-31). | award 수준 CrowdStrike products/services를 확인한다. 수정별 금액·설명은 있으나 제품별 귀속, 라이선스 수량·단가를 분리하지 못한다. |

모든 금액은 USAspending transaction의 federal action obligation이며 vendor 매출/순액이 아니다. 이 세 공공 구매 기록은 연방 조달 관찰치이지 민간 WTP·TAM·ARR를 입증하지 않는다. 옵션·수정·in-scope 표현도 제품 단위의 갱신률이나 사용량 증거로 해석하지 않는다.
**비교 제한:** 이 사례들은 공개된 특정 조달의 범위와 단계만 보여준다. 국가 IT 지출 또는 민간시장 추정치가 아니며, 금액 차이는 조달 범위·대상·회계·시점·통화 차이와 실제 수요가 함께 반영될 수 있다. 미국 award의 obligation/outlay와 한국 RFP의 예정예산은 직접 비교하지 않는다.

### 미국·한국 기업 기술통계의 비교 가능성

**판정: headline 비율 직접 비교는 불가하며, 좁은 정의 일치 비교만 별도 검토한다.** Census 2023 ABS는 reference year 2022의 기술 모듈에서 “2020–2022년 동안” 클라우드 등을 사업의 프로세스·방법에 사용했는지 묻는다. 답은 미적용, 적용 가능하나 미사용, 시험했으나 프로세스에 미사용, 프로세스에 사용, 모름으로 나뉜다. 이는 기준일 현재의 모든 클라우드 서비스 이용 여부와 같지 않다.

| 조사 | 모집단·단위 | 기준/측정 창과 질문 | 추정·분모 단서 | 비교 판정 |
|---|---|---|---|---|
| 미국 Census 2023 ABS | 일부 산업 제외 미국 employer businesses, 기업(firm) 단위; 비고용 기업 제외 | 2023은 수집연도이며 reference year는 2022. 기술 모듈은 2020–2022년의 사업 프로세스/방법 내 기술 사용을 질문 | 특성 추정은 해당 항목 응답이 하나 이상 있는 기업을 포함하며 비응답 조정을 하지 않았다고 방법론이 설명. 기업 규모는 3월 12일 급여기간 고용으로 분류 | NIA의 2023년 말 상태 문항과 기간·질문·분모가 다름 |
| 미국 Census BTOS | 미국의 농업 제외 고용 사업체, 단일·다중 사업장 포함 | 격주 조사; 통상 직전 2주 또는 향후 6개월 전망. AI 문항은 시기별 문구 변경 | 패널·고빈도 추정 | ABS 및 NIA 연간 기준 조사와 다른 측정 창·문항 |
| 한국 NIA 기업정보화통계조사(2024 조사) | 전국 종사자 10인 이상 민간 기업체; 기업체 단위; 12,500 표본 중 12,203 응답완료 | 기준기간 2023년, 기준시점 2023-12-31; 현장조사 2024-07-29~10-06. 클라우드 이용/유형 문항과 목적·미이용 사유 문항 포함 | 표본설계와 지역·조직형태·산업·규모 모집단 주변합에 대한 가중/사후보정이 설명됨. 연도별 문항 예시와 서비스 분류도 변경 | ABS와 서비스 개념·응답범주·기간·응답분모/추정 절차가 같다는 근거가 부족 |

**10인 이상 크기 구간 재구성은 일부 가능하지만 충분조건이 아니다.** Census/NCSES의 ABS Table 77은 회사 규모 구간별 클라우드 기술 표를 제공하므로 크기 구간을 합치는 방식은 검토할 수 있다. 그러나 2020–2022년 “생산 기술” 사용과 2023-12-31 현재 클라우드 이용은 같은 관측치가 아니다. 고용 기준일, 산업 범위, 기업 단위, 문항 정의·응답범주, 항목 응답 분모 및 추정치를 각각 원표에서 확인하고 정렬하기 전에는 한 표의 국가별 headline 비교를 하지 않는다. 조사된 NIA 설문지 PDF에서 응답 선택지의 세부 코딩은 확인하지 못했으므로 이를 임의로 맞다고 가정하지 않는다.

이 채택률은 구매의도·지출·WTP·미충족 수요가 아니다. 다음 탐색은 통계 headline 추가 비교 대신 구체 구매자 세그먼트의 구매·갱신·예산 집행 흔적과 현재 대안을 찾는 것으로 전환한다.

### DOE P00001 공개 첨부 접근과 구매 문서 경계

2026-11-07에 DOE SC Oak Ridge `89243126FSC400871` 및 USAspending에 연결된 solicitation 식별자 `89243126QNA000448`로 SAM.gov 검색 페이지를 확인했다. 두 페이지 모두 HTTP 200이지만 서버 응답은 검색 결과를 포함하지 않는 JavaScript shell이었다. GSA의 [Contract Awards API 안내](https://open.gsa.gov/api/contract-awards/)는 공개(revealed) 계약 자료 조회에도 SAM.gov 계정과 API key가 필요하다고 설명한다. 인증을 사용하거나 우회하지 않았다.

[NASA SEWP V 주문 안내](https://www.sewp.nasa.gov/sewpv/ordering.shtml)는 발행기관이 delivery order를 발행하고, 수정도 SEWP PMO를 거치며, 주문 처리에 계약자 quote 및 line items/pricing가 필요하다고 명시한다. [SEWP V 계약 정보](https://www.sewp.nasa.gov/sewpv/contract_info.shtml)와 공개 계약자 페이지는 차량·prime 계약자 수준 자료다. 이 일반 절차는 해당 DOE 주문의 실제 quote, 첨부 또는 CLIN 내용을 입증하지 않는다. 이번 비인증 공개 경로에서 P00001 원문 첨부는 찾지 못했다. 이는 조사한 경로의 결과일 뿐 첨부가 없다는 뜻이 아니다. SKU·수량·단가는 계속 미확인이다. 요청·응답 상태, UTC, hash와 범위는 `public-spend-observations.json`의 `doe_p00001_public_access_recheck_20261107T0035Z`에 기록했다.

### 엔드포인트 운영 신호: 정성 리드와 공식 복원력 자료 분리

Reddit 검색 색인에서 관리 콘솔 복잡성·정보 탐색 문제와 Microsoft Defender 번들로의 전환 고려가 리드로 나타났고, 반대로 대규모 fleet 운영자에게 안정성과 지원이 좋았다는 반례도 나타났다. 그러나 대상 글 직접 요청은 HTTP 403이었고 본문을 확인하지 못했다. 그러므로 이는 검증된 고객 발언이나 빈도·이탈·구매 의향 자료가 아니라 후속 조사 질문을 만드는 discovery lead로만 보존한다. G2 결과는 직접 접근이 차단되어 사용하지 않았고 재시도·스크래핑을 하지 않았다. 검색 및 접근 정보는 같은 JSON snapshot의 `endpoint_security_operational_signal_discovery_20261107T0046Z`에 있다.

독립적인 공식 자료는 사건의 실제 규모와 통제 대안을 조금 더 좁혀 준다. [Microsoft는 2024년 7월 사고 당시 Windows 기기 850만 대 미만 1%가 영향을 받은 것으로 추정](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)하고 안전한 배포와 재해복구를 강조했다. [CrowdStrike의 사후 원인분석](https://www.crowdstrike.com/en-us/blog/channel-file-291-rca-available/)은 Windows 센서에 배포한 Rapid Response Content 설정 오류와 개선을 설명한다. 한편 [Intune update rings](https://learn.microsoft.com/intune/intune-service/protect/windows-10-update-rings)는 테스트·파일럿·프로덕션 단계 배포를 문서화한다. 이는 Windows/관리형 update rollout 대안의 존재를 보여주지만, 해당 ring이 Falcon의 vendor-managed Rapid Response Content를 통제한다는 뜻은 아니다. 사건 하나와 공급자 자체 RCA는 반복 빈도·신규 도구 수요·WTP/TAM을 입증하지 않는다.

## 다음 탐색에서 검증할 것

1. **다음 evidence leaf:** 보안 에이전트의 vendor-managed content와 OS/app 배포 도구(Intune/Autopatch/기존 endpoint suites)가 제공하는 pause, staged rollout, rollback/recovery 경계를 공식 문서로 대조한다. 결과는 “기능 있음/없음”이 아니라 정확한 payload와 통제 주체 단위로 비교하고, 중복 제품 제안 전에 기존 해결책을 확인한다.
2. 다음으로 독립적인 buyer evidence(실제 구매·갱신·교체 또는 접근 가능한 직접 사용자 인터뷰/후기)를 찾아 alert tuning·복구 부담이 어느 규모와 예산권자에게 중요한지 검증한다. 검색 색인 스니펫은 확인 질문으로만 쓰고, WTP나 이탈 증거로 집계하지 않는다.
3. DOE P00001 문서 확인은 SAM 계정/API key 또는 해당 order/quote 원문이 합법적으로 접근 가능해질 때 재개한다. 인증을 추정·우회하거나 외부에 연락하지 않으며, 첨부 부재를 추론하지 않는다.
4. ICE FinalMobile 후속 award/옵션과 `70CMSD26FR0000041` SOW/CLIN은 제품명으로 이어지지 않는 한 별도 lineage로 유지한다.
5. 현재 자료는 미국/한국 구매 의사, 유지율, WTP 또는 서비스 가능 시장 비교를 제공하지 않는다. 따라서 단일 승자나 TAM을 제시하지 않는다.

## 근거 레지스터

접근일은 모두 2026-11-06 UTC. 1차/공식 자료는 그 자료가 직접 측정·기술하는 범위 안에서만 사용했다.

| ID | 출처·발행/관측 시점 | 유형·지리 | 여기서 뒷받침하는 주장 | 한계 |
|---|---|---|---|---|
| S1 | [U.S. Census Bureau, 2023 Annual Business Survey 기술 채택 요약](https://www.census.gov/library/stories/2025/09/technology-impact.html), 게시 2025-09-17; 주 관측 2020–2022 | 공식 조사 요약, 미국 employer businesses | 클라우드·특수 소프트웨어·AI 채택 동기 중 업무 프로세스 품질/신뢰성 개선; 해당 기술 중요도 응답 | 조사명 2023은 데이터 기준연도와 다름(요약은 2022 데이터 언급). 구매액·SaaS 수요·비고용 사업자에 일반화 불가. |
| S2 | [Census CES-24-16, BTOS AI 추적](https://www.census.gov/library/working-papers/2024/adrm/CES-WP-24-16.html), 2024-03; 관측 2023-09~2024-02 | Census working paper, 미국 사업체 | 해당 기간 AI 사용 추정치 3.7%에서 5.4%; 사용은 규모/업종에 따라 다르고 비도입에 적용 불가가 흔함 | 2026 현재의 사용률 아님. 채택/기대 측정이지 구매예산·ROI·지불의사 아님. |
| S3 | [BLS, Information Security Analysts](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm), 페이지 기준 2025년 임금·2025–2035 전망 (2026-11-06 확인) | 공식 고용 전망, 미국 | 직업 고용 +21%, 연평균 약 14,100개 오프닝 전망; 보안 업무 설명 | 직업 전망은 보안 소프트웨어/서비스 시장 규모나 미충족 구매 수요가 아님. |
| S4 | [SEC, Cybersecurity Disclosure Rule](https://www.sec.gov/newsroom/press-releases/2023-139), 2023-07-26; 효력 2023-09-05 | 공식 규칙, 미국 상장 발행인 | 중대 사고 공개 및 연례 리스크 관리·거버넌스 공개 요구 | 대상 기업/공시 규칙에 한정; 보안 벤더 구매 증가량을 직접 측정하지 않음. |
| S5 | [CMS Interoperability Framework](https://www.cms.gov/initiatives/health-technology-ecosystem/overview/interoperability-framework), 2026년 현황 확인; [July 2026 GA 참여자](https://www.cms.gov/initiatives/health-technology-ecosystem/overview/general-availability-july-2026) | 공식·자발적 프레임워크, 미국 의료 생태계 | 참여 유형 및 상호운용성 정책·기술 방향, 공개된 참여자 예시 | 자발적 프레임워크/참여 목록은 전체 시장 채택·품질·ROI 증거가 아님. |
| S6 | [AWS 공식 개요](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/), 페이지 이력 2026-06-02 | 벤더 자기기술 | 클라우드 서비스 범주와 사용량 기반 인프라 패턴 예시 | AWS의 제품·가격 포지셔닝 자료; 독립 시장 검증 아님. |
| S7 | [GitHub Platform](https://github.com/platform), 조사일 페이지 스냅샷 2026-11-06 | 벤더 자기기술 | 저장소·리뷰·CI/CD·코드 보안·에이전트 기능 예시 | 제품 기능 페이지; 효과/시장점유율/고객만족도 증거 아님. |
| S8 | [Stripe Products](https://stripe.com/products), 조사일 페이지 스냅샷 2026-11-06 | 벤더 자기기술 | 결제·플랫폼 금융·Billing/Tax/Radar 등의 제품군 예시 | 기능/성장 문구와 숫자는 공급자 주장; 독립 성과 검증 아님. |
| S9 | [Epic About](https://www.epic.com/about/), 조사일 페이지 스냅샷 2026-11-06; [CMS EHR pledgees](https://www.cms.gov/initiatives/health-technology-ecosystem/overview/early-adopters-all-pledgees/electronic-health-records-ehrs), 페이지 수정 2026-10-21 | 벤더 자기기술 + CMS 참여자 목록 | Epic의 EHR 제품 범위 자기설명; CMS 프레임워크 pledge 참여 EHR 사례 | 공급자 자기기술/자발 참여 사실일 뿐 채택 점유율·품질·환자성과의 독립 증거 아님. |

| S10 | [USAspending API - VA award detail `CONT_AWD_36C10B23F0346_3600_47QSWA18D008Q_4732`](https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C10B23F0346_3600_47QSWA18D008Q_4732/) 및 보존된 응답 `artifacts/research-us-it-opportunity-20261106/work/public-spend-observations.json`, 조회 2026-11-06 19:04 UTC | 공식 연방 award API, 미국 VA | 수령자·PIID·서비스 설명·공연 기간·API의 total_obligation/total_account_outlay/base_and_all_options 필드 | 고유한 한 건의 공공 계약이며 서비스 묶음; 필드명과 금액단계를 바꾸어 해석하지 않음. |
| S11 | [USAspending Federal Spending Guide](https://www.usaspending.gov/federal-spending-guide), 접근 2026-11-06 | 공식 데이터 정의 | obligation은 정부의 지출 약정, outlay는 실제 지출(pay-out) 개념 | 상위 정의가 특정 계약의 line-item 배분이나 수익 인식을 의미하지 않음. |
| S12 | [KISA 2025-145 CISO 현황 조사·긴급 교육 입찰](https://www.kisa.or.kr/403/form?postSeq=10270), 게시 2025-08-04 | 공식 공공 조달공고, 한국 | 99.7M KRW VAT-inclusive 소요예산; 계약 후 2025-12-12까지; 학술연구용역 표기 | 입찰 예정예산이지 낙찰가/지출이 아님; 조사·교육 용역이지 SaaS 구매가 아님. |
| S13 | [KISA 2024-081 CISO 지정 신고 실태조사 사전규격공개](https://www.kisa.or.kr/403/form?lang_type=KO&page=1&postSeq=9615), 게시 2024-04-05 | 공식 사전규격공개, 한국 | 다른 건의 78M KRW VAT-inclusive 예정예산과 2024년 공고 일정 | 2025-145 수정 공고가 아닌 별도 사업; 미낙찰·미지급 근거로 취급. |
| S14 | [NIA 2024 기업정보화통계집](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=27621&cbIdx=62156&parentSeq=27621), 게시 2025-01-02; [조사 설계 안내](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=27028&cbIdx=99835) 게시 2024-07-23 | 공식 한국 기업체 통계·조사 설계 | 클라우드, 데이터/AI, 정보화투자·인력·효과 등을 다루고 10인 이상 전국 기업체 12,500 표본이라고 안내 | 원표 및 문항 비교 전에는 Census와 채택률/투자액을 직접 비교하지 않음. |
| S15 | [Census 2023 ABS methodology](https://www.census.gov/programs-surveys/abs/technical-documentation/methodology.2023.html), [Census 2024 ABS methodology](https://www.census.gov/programs-surveys/abs/technical-documentation/methodology.2024.html), 접근 2026-11-06 | 공식 조사방법론, 미국 | 조사명 연도와 reference year 구분; employer-business 모집단·비고용 제외; 2023 ABS 기술 module과 2024 ABS의 다른 module 구성 | 서로 다른 ABS 조사연도의 module은 동일 문항 시계열로 취급 불가; Census도 다른 경제조사와 비교 시 주의 고지. |
| S16 | [Census BTOS data/methodology](https://www.census.gov/data/experimental-data-products/business-trends-and-outlook-survey.html), [BTOS methodology PDF](https://www.census.gov/hfp/btos/downloads/methodology/Business_Trends_and_Outlook_Survey_Methodology_V6.pdf), 접근 2026-11-06 | 공식·실험적 고빈도 사업체 조사, 미국 | 2023-09-11 이후 농업 제외 단일·다중 사업장 고용 사업체; 2주 reference/6개월 전망, 격주 패널; 표본·비응답 조정 | BTOS는 NIA 연간 기준기간 문항의 직접 대체물이 아님; AI 문항 변경 시계열도 별도 확인 필요. |
| S17 | [NIA 2024 survey announcement](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=27028&cbIdx=99835), [국가데이터처 2025 정기통계품질진단 보고서](https://sri.kostat.go.kr/boardDownload.es?bid=67&list_no=442669&seq=1), 접근 2026-11-06 | 공식 표본·조사방법 정보, 한국 | 10인 이상 모집단; 기준기간 2023년; 2024-07-29~10-06 조사; 12,500 표본, 12,203 응답완료; 기업통계등록부 표본틀 및 사후추정 주의 | 항목마다 기준시점이 다를 수 있어 해당 표/문항 정의 대조 필요. |
| S18 | [Census 2023 ABS Instructions, G.3](https://www2.census.gov/programs-surveys/abs/information/ABS-2023-Instructions.pdf), 접근 2026-11-06 | 공식 설문지, 미국 | 2020–2022 기간 및 클라우드 등 기술을 사업 프로세스/방법에 사용했는지와 응답범주 | 설문 문항 자체이지 국가 간 조화 추정치가 아님. |
| S19 | [NSF/NCSES, 2023 ABS Table 77](https://ncses.nsf.gov/pubs/nsf25303/assets/data-tables/tables/nsf25303-tab077.xlsx), 접근 2026-11-06 | 공식 통계표, 미국 | 생산기술로 사용한 클라우드 기반 시스템·앱을 회사 규모별로 제시; 10인 이상 구간 재집계 가능성 확인 | 크기 구간 정렬은 기간·질문·모집단·추정 차이를 해결하지 않음. |
| S20 | [국가데이터처, 2025 정기통계품질진단: 기업정보화통계조사](https://sri.kostat.go.kr/boardDownload.es?bid=67&list_no=442669&seq=1), 접근 2026-11-06 | 공식 품질진단, 한국 | NIA 문항(Q20 클라우드 이용/유형, Q21 목적, Q22 미이용 사유), 조사 기준기간·수집기간 및 설계/가중 정보 | 확인한 설문지 사본은 세부 응답 선택지 판독이 어려워 정확한 코드 일치 여부는 미확인. |

| S21 | [USAspending DOE award PIID 89243126FSC400871](https://www.usaspending.gov/award/CONT_AWD_89243126FSC400871_8900_NNG15SC33B_8000/), API 응답 2026-11-06 | 공식 연방조달 award, 미국 DOE SC Oak Ridge | CrowdStrike ELA description, EMERGENT LLC recipient, 2026-06~2027-05 delivery order; obligation $1.812M, outlay $1.751M, PSC DJ10, 3 offers | 단일 리셀러 경유 기업 라이선스 조달 사례; vendor revenue·반복 구매·민간 WTP 아님. |
| S22 | [USAspending DHS/ICE award PIID 70CMSD25FR0000087](https://www.usaspending.gov/award/CONT_AWD_70CMSD25FR0000087_7012_NNG15SD74B_8000), API 응답 2026-11-06 | 공식 연방조달 award, 미국 ICE | FinalMobile mobile-forensics software 갱신 설명; obligation/outlay $29,022, potential base+options $87,066; 2025-09~2026-09 기본기간 | 옵션은 실행 의무액이 아니며, 설명의 갱신은 SaaS·정기 ARR 증명이 아님. |
| S23 | [USAspending transaction history API](https://api.usaspending.gov/api/v2/transactions/) 및 [공식 API contract](https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/transactions.md), 조회 2026-11-06 | 공식 연방조달 거래내역 API, DOE·ICE | DOE 2 transactions: initial $1,751,043.22와 in-scope additional-license mod +$60,628.28; ICE FinalMobile 1 initial transaction; 별도 ICE forensic-agent order와 $0 accounting mod | 기록은 modification description/amount/date를 보일 뿐 SKU·수량·CLIN schedule을 제공하지 않음. 새 ICE order를 FinalMobile 갱신과 연결하지 않음. |
| S24 | [USAspending DHS/ICE award PIID 70CMSD26FR0000041](https://api.usaspending.gov/api/v2/awards/CONT_AWD_70CMSD26FR0000041_7012_NNG15SD74B_8000/), 조회 2026-11-06 | 공식 연방조달 award, 미국 ICE HSI | forensic evidence examination을 위한 agent licenses, $25,693.20 obligation; NASA multiple-award GWAC delivery order | description에 제품명이 없어 FinalMobile과 동일성/갱신 연결을 입증하지 않음. |
| S25 | [USAspending spending-by-transaction API contract](https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_transaction.md), 접근 2026-11-06 | 공식 API 문서 | keyword/type 필터, 필드, pagination, 정렬 방식 설명 | API 스펙은 개별 award 거래 증거가 아님. 이번 100행 검색의 원문 전체와 정확 조회시각은 보존되지 않아 세 행은 재검증 대기. |
| S26 | [Treasury Fiscal Service, ARC/FSA contract list](https://fr.fiscal.treasury.gov/files/doing-business-with-fiscal-service/ARC-FSA.pdf), 접근 2026-11-06, PDF p.1/텍스트 행 990–997 | 공식 기관 계약 목록, 미국 Treasury | FCN Inc.; parent `NNG15SC71B`; order `2033H624F00068`; “Crowdstrike products and services”; “Excepted or Exempt - Work Continues” | 거래내역·지출액·P00008 scope를 제공하지 않는다. 상태 문자열은 구매량 또는 갱신을 뜻하지 않는다. |
| S27 | [DOE/NNSA 89233126QNA000448 award notice mirror](https://www.governmentcontracts.us/government-contracts/opportunity-details/78853974975300159.htm?searchText=computer), 접근 2026-11-06 | SAM 공고의 2차 미러, 미국 DOE/NNSA | 원 award의 날짜, Thundercat, Falcon/Falcon Complete 라이선스 description; order `89233126FNA400754` | 사이트가 공식 공고가 아니라고 고지한다. 원 award 설명만 확인하며 P00001/후속 거래 리드 미검증. |

| S28 | [NASA SEWP V Ordering Information](https://www.sewp.nasa.gov/sewpv/ordering.shtml), 접근 2026-11-07 | 공식 주문 절차, 미국 federal GWAC | order modifications must route through PMO; order processing requirements include contractor quote and line items/pricing | 일반 절차만 설명; 특정 DOE order의 내용/첨부는 아님. |
| S29 | [GSA SAM.gov Contract Awards API](https://open.gsa.gov/api/contract-awards/), 접근 2026-11-07 | 공식 API 문서 | revealed award data requires registered SAM account and API key | API 접근요건이지 해당 PIID 첨부 존재/부재 판정이 아님. |
| S30 | [SAM.gov award search shell](https://sam.gov/search/?index=awards&keywords=89243126FSC400871) 및 [solicitation search shell](https://sam.gov/search/?index=opp&keywords=89243126QNA000448), 조회 2026-11-07 00:34 UTC | 공식 검색화면 접근 기록 | 두 페이지 HTTP 200, 동일 JavaScript shell 반환; 서버 HTML에 검색결과 없음 | UI 결과가 없다는 뜻이 아님. 무인증 직접 응답만으로 기록/첨부 존재 여부를 판단할 수 없음. |
| S31 | [Microsoft Official Blog: CrowdStrike outage response](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/), 게시 2024-07-20 | 직접 대응 OS 공급자의 사고 대응 기록 | 8.5 million Windows devices, less than 1% estimate; safe deployment and disaster recovery emphasis | 단일 공급망 사고 추정치; 빈도·시장 수요/WTP를 측정하지 않음. |
| S32 | [CrowdStrike Channel File 291 RCA](https://www.crowdstrike.com/en-us/blog/channel-file-291-rca-available/), 게시 2024-08-06 | 공급자 자체 사후 분석, 미국/글로벌 | Windows sensor content configuration update failure and mitigations/process learnings | 공급자 자체 보고; 고객 발생률이나 신규 시장 규모를 측정하지 않음. |
| S33 | [Microsoft Intune Windows update rings](https://learn.microsoft.com/intune/intune-service/protect/windows-10-update-rings) 및 [Windows update deployment channels](https://learn.microsoft.com/windows/deployment/update/get-started-updates-channels-tools), 접근 2026-11-07 | 공식 제품/관리 문서 | test/pilot/production-style phased OS/update deployments and policy controls exist | 이 기능들이 third-party Falcon Rapid Response Content를 제어한다고 문서가 말하지 않음. 기존 대안의 경계만 보강. |
| S34 | [r/sysadmin: Any reviews on CrowdStrike?](https://www.reddit.com/r/sysadmin/comments/1p2ufgk/any_reviews_on_crowdstrike/) 및 [CrowdStrike thoughts](https://www.reddit.com/r/sysadmin/comments/1ugqsyd/crowdstrike_thoughts/), 검색색인 조회 2026-11-07 | UGC discovery lead, 미국 Reddit | 검색색인이 console complexity 관련 불만과 대규모 fleet 운영의 안정성/지원 만족 반례를 표면화 | 직접 GET은 두 URL 모두 HTTP 403, 본문 미확인. 고객 증언 검증·표본 대표성·빈도 근거로 쓰지 않음. |
| S35 | [Reddit: Anyone move from CrowdStrike to Defender for Endpoint recently?](https://www.reddit.com/r/sysadmin/comments/1rsysav/anyone_move_from_crowdstrike_to_defender_for/), 검색색인 조회 2026-11-07 | UGC discovery lead, 미국 Reddit | subscription bundle을 이유로 Defender 전환을 고려하는 게시물 검색 신호 | 직접 GET HTTP 403; 전환 실행 여부·구매 결정·가격절감액 확인 안 됨. |

## Palo Alto Networks 연방 조달과 자산관리·감사 신호 — 서로 연결하지 말 것

USAspending 공식 API의 2026-11-07 조회에서 Palo Alto Networks 키워드로 정렬한 첫 100개 거래행(page 1, `hasNext=true`) 중 SSA와 Department of the Army award를 상세·전체 history까지 재검증했다. 둘은 각기 다른 federal award지만 검색은 비완전하며 prime은 Palo Alto Networks가 아니다.

| 구매·계약 역할 | award / 거래내역 | 금액 필드와 범위 | 해석 한계 |
|---|---|---|---|
| SSA 구매·수여 / Carahsoft prime | PIID `28321325FDX030100`, GSA FSS `47QSWA18D008F`; description은 Palo Alto 차세대 firewall 및 전문서비스, 단일 firewall platform 전환·mainframe/intranet 연동을 말한다. 수행기간 2025-05-01–2027-04-30. history 5행: 2025 기본 $3,883,521.50; 2026-01 P00001 $4,696,867.80; 2026-04 P00002 $0; 2026-06 P00003 $823,417.76(첫 option year에 빠졌던 professional-services CLIN 2건); 2026-09 P00004 $2,191,514.40(option year inventory spreadsheet에서 빠진 hardware CLIN 수정). | `total_obligation` $11,595,321.46; `total_account_outlay` $8,580,389.30; 별도 `base_and_all_options` $25,029,199.19. 5행 obligation 합계는 award detail과 일치. | 옵션 포함액을 지출·매출로 보지 않는다. P00004가 첨부 inventory spreadsheet를 언급하지만 그 파일 자체는 확보하지 못했다. CLIN/품목별 수량·가격 및 Palo Alto 직접 매출은 알 수 없다. |
| Army가 award / Navy office가 funding / Greenbrier prime | PIID `W519TC25F0425`, parent NASA multiple-award GWAC `NNG15SD49B`; description상 INDOPACOM의 탐지·방지를 위한 Palo Alto 네트워크 SW·HW·subscription 서비스 패키지. 수여기관 Department of the Army, funding office는 Department of the Navy / CDR US Pacific Command. 수행기간 2025-09-26–2026-09-25. history 6행: base 두 건 각 $2,952,434.49, 2025-12 P00001 두 건 $0, 2026-03 P00002 두 건 $0. | `total_obligation` 및 `base_and_all_options` 각각 $5,904,868.98; `total_account_outlay=0`, `total_outlay=null`(다른 필드임). history의 6행 합계는 obligation과 일치. | base/수정별 paired row는 서로 다른 transaction ID지만 날짜·mod·금액·설명이 같아 원인을 확인하지 못했다. 임의 dedupe하거나 별도 award 2건으로 세지 않는다. zero account outlay 필드와 null total_outlay를 지급 부재·벤더 수입으로 해석하지 않는다. 수량/단가·제품별 배분 미확인. 5 offers/full-and-open은 경쟁절차 필드이지 가격 발견 증거가 아니다. |

**해석:** 이는 서로 다른 federal procurement buyer가 네트워크 보안 패키지를 산 사례 두 건으로, federal/public segment의 조달 행동 및 구성요소·CLIN 복잡성 가설을 좁히는 신호다. 만족도, 사용성과, audit remediation, recurring private demand, 예산권자·pain 빈도, vendor revenue/ARR, WTP/TAM은 입증하지 않는다. routine inventory/contract reconciliation 또는 mission architecture라는 대안 설명도 가능하다.

별도 맥락으로 SSA OIG report 142315(2025-08-06; audit window 2024-01–2025-03)는 비통계 표본 firewall 40개와 관련 문서를 검토했고, inventory·patch/update·annual rule review·change management·privileged access/logs·backup·advanced-feature administration에서 deficiency를 보고했다. account/password 이슈는 검토 후 시정되어 권고가 없었고 physical firewall security에서는 deficiency가 없었다. 상세 민감 findings/recommendations는 별도 전달되어 공개 요약에 포함되지 않았다. Jan 29 2026 OIG compilation의 해당 보고서 항목은 2,5,6,8,9,10,11,13번 권고의 세부/상태를 민감정보로 withheld했고, Spring 2026 SAR(Appendix E; 보고기간 2025-10-01–2026-03-31)은 1*,2,3,7,8,10,11,13을 open으로 열거했다. 별표는 보고서 표기를 유지한다. 이는 각각 그 cutoff 날짜의 스냅샷이지 2026-11 현재 상태가 아니다. 해당 audit가 위 SSA award의 원인·scope·성과라는 직접 근거는 없다.

또 다른 별도 축인 GAO-26-108937(2026-09-30)은 civilian CFO Act 22개 기관의 networked IoT/OT inventory를 보았다. SSA는 초기 inventory의 필수 필드를 마련했으나 반복 유지하지 못한 상태로 표기됐다. 이는 firewall inventory 또는 위 Palo Alto contract와 다른 자산 범주·법적 기준이다. GAO-26-107668(2026)은 Section 889 대상 통신/영상장비를 다룬 선택 기관 6곳의 방법을 기록한다. DoD는 asset inventory 검색, network scan, 물리 검색을 사용했으며 procurement-record search는 표에 나타나지 않았다. Army Corps of Engineers Huntsville의 2026-07 공보는 Army Reserve·National Guard·DLA 시설 OT inventory 계약과 Army Reserve 약 10,000개 장치 기록, 후속 remediation/sustainment 계획을 소개한다. 이들은 현재 존재하는 공공 자산 가시성·서비스 대안의 예시이며, firewall 제품 주문과 동등하거나 새 제품 수요를 증명하지 않는다.

다음 탐색 leaf는 이 federal 사례에서 출발해 연방 asset visibility / inventory 서비스를 기존 시스템·서비스가 어떻게 충족하는지 비교하고, 공개 buyer 자료로 반복 업무·책임자·예산 증거가 독립적으로 드러나는지 확인한다. 연방·DoD·IoT/OT·firewall 범주를 섞지 않으며 공개 문서의 접근 제한은 부재로 추론하지 않는다.

| S36 | [USAspending SSA award PIID 28321325FDX030100](https://www.usaspending.gov/award/CONT_AWD_28321325FDX030100_2800_47QSWA18D008F_4732/) 및 공식 [USAspending transaction API](https://api.usaspending.gov/api/v2/transactions/) 응답, 2026-11-07 | SSA federal delivery order; Carahsoft prime; API search/detail/history 원문은 `public-spend-observations.json`에 response hash와 함께 보존 | 5 history rows와 detail amount의 합치, NGFW/professional-services description 및 hardware/pro services amendments | prime receipt·SKU별 금액·사용 결과가 아니며 100행 keyword search는 `hasNext=true`; P00004가 언급한 첨부 spreadsheet 미확보. |
| S37 | [USAspending Army award PIID W519TC25F0425](https://www.usaspending.gov/award/CONT_AWD_W519TC25F0425_9700_NNG15SD49B_8000/) 및 official transaction API, 2026-11-07 | Army awarding org; Navy funding office; INDOPACOM description; Greenbrier prime; NASA GWAC vehicle | 6 transaction rows/$5,904,868.98 obligation; Army/Palo Alto package description | paired IDs retained; `total_account_outlay=0` vs `total_outlay=null`; not two awards, price discovery, or vendor revenue. |
| S38 | [SSA OIG Firewall Administration report 142315](https://oig.ssa.gov/assets/uploads/142315.pdf), [official landing page](https://oig.ssa.gov/audit-reports/2025-08-07-firewall-administration/) | Official SSA OIG public audit summary, Aug 6 2025; audit Jan 2024–Mar 2025; non-statistical 40-firewall sample | Inventory, patching, rules/review, change, access/logging, backup and advanced-feature administration gaps | Sensitive details separately transmitted to SSA and withheld from public summary; no demonstrated link to Palo Alto order. |
| S39 | [SSA OIG unimplemented recommendations as of Jan 29 2026 (002612)](https://oig.ssa.gov/assets/uploads/002612.pdf) | Official SSA OIG dated status compilation | 142315 recs 2,5,6,8,9,10,11,13 listed; details/status marked sensitive | Only Jan 29 cutoff; not current status. |
| S40 | [SSA OIG Spring 2026 Semiannual Report](https://oig.ssa.gov/assets/uploads/2026-spring-sar.pdf), Appendix E | Official OIG report covering 2025-10-01–2026-03-31 | 142315 open recs 1*,2,3,7,8,10,11,13 | Snapshot cutoff Mar 31; preserves asterisk; does not resolve later status or link to award. |
| S41 | [GAO-26-108937, IoT and OT networked-device inventory](https://files.gao.gov/reports/GAO-26-108937/index.html), 2026-09-30 | Official GAO review of 22 civilian CFO Act agencies; SSA initial IoT/OT inventory fields vs recurring maintenance | 15 established, 11 maintained, 10 had all required fields, 7 fully addressed requirements | IoT/OT statutory scope differs from firewall inventory and Palo Alto order. |
| S42 | [GAO-26-107668, Selected Agencies Have Taken Steps to Address Risks of Equipment Linked to China](https://files.gao.gov/reports/GAO-26-107668/index.html), 2026 | Official GAO review of six selected agencies through Dec 2025; DoD methods include inventory search, network scan, physical search | Shows existing institutional search/control alternatives; DoD row does not list procurement-record search | Section 889 covered telecommunications/video hardware scope, not Palo Alto firewall software or buyer pain WTP. |
| S43 | [U.S. Army Corps of Engineers Huntsville, OT risk and inventory program](https://www.army.mil/article-amp/294305/huntsville_center_expertise_identifies_prioritizes_operational_technology_risks), 2026-07-31 | Official Army public affairs article | Army Reserve OT inventory completed; DLA final products and Army National Guard work; nearly 10,000 Army Reserve OT devices recorded; remediation/sustainment planning follows | Public-sector service/contract example for facility OT; separate from INDOPACOM enterprise security order and not standalone software demand. |

## 역할 교차검토 요약

- Planner: 비랭킹 커버리지 맵으로 만들고, 카테고리마다 구매자·업무·대안·신호·근거·미국/한국 오버레이를 분리한다. 모집단/시점 차이가 직접 비교를 왜곡하지 않도록 범주별 증거 단계 사다리를 추가했다. 카테고리 중첩, 세그먼트 차이, 대체재, 지불의사 공백은 남긴다.
- Planner: Census ABS, BTOS, NIA의 모집단·reference period·질문 단위를 분리했다. 공통 클라우드 항목을 찾더라도 분모/질문을 맞추기 전 수치 순위는 보류한다.
- Developer: 2024 ABS는 reference year 2023이며 그 해 module에는 기술이 없고, 2023 ABS technology module은 reference year 2022라는 조사연도 혼동을 방지했다. BTOS AI 문항 개정 및 고빈도 기간도 별도 표시한다.
- Marketer: 채택률은 수요/구매를 증명하지 않으며 세그먼트의 문제·예산권자·구매 행동·WTP 검증을 위한 가설 신호로만 사용한다.
- Operator: NIA 2025 품질진단 보고서의 기준기간·조사기간·표본틀·완료 수를 추가 보존했다. headline 비교는 보류하되 더 좁은 공통 질문·10인 이상 분모로 재구성 가능성은 후속 확인한다.
- Planner (transaction leaf): DOE는 초기 award 이후 날짜·금액이 있는 in-scope 추가 라이선스 수정까지 확인됐지만 옵션 행사나 line-item scope는 아니다. ICE FinalMobile의 `renews` 설명/잠재 옵션은 실제 후속 갱신 proof가 아니며, 70CMSD26FR0000041은 별도 lineage leaf로 유지한다.
- Developer: 공식 `POST /api/v2/transactions/`가 거래 ID·action date·modification·설명·의무액을 준다. DOE의 +$60,628.28은 additional-license modification; SKU·수량·가격을 추정하거나 옵션 행사로 부르지 않는다.
- Marketer: 세 건은 공공 구매 행동 사례일 뿐 민간 buyer pain, 구매 의향, WTP 또는 TAM으로 일반화하지 않는다. 별도 ICE forensic-license order를 FinalMobile 갱신으로 합치지 않는다.
- Operator: award detail과 transaction history는 서로 다른 API 응답이므로 HTTP 상태와 원문을 별도로 저장한다. transaction 응답 원문을 JSON에 보존했고, 공개 조달 첨부는 이번 검색에서 직접 확인되지 않아 “첨부 없음”으로 표현하지 않는다.
- Genie 통합: DOE P00001 첨부의 CLIN/scope 확인과 ICE 후속 award/70CMSD26FR0000041 제품 식별을 별도 leaf로 분할한다; attachment 공개 여부와 product lineage는 증거로 확인되기 전까지 unknown이다.

- Planner (dispatch-295764d0809e406b9c4286b886d48d64): order-doc 성공 기준은 해당 order에 귀속되는 공식 원문 첨부와 line-item evidence; 공개되지 않으면 검색 범위와 접근 경계만 기록한다.
- Developer (run3): 현재 파일 접근을 검증하지 못해 재현성 판정은 보류했다. 이전 Developer 리뷰는 exact query/permalink/status와 403를 보존하고 Reddit/G2 결과를 discovery lead로만 다루며 G2 재시도·스크래핑·접근통제 우회를 금지했다.
- Marketer (CMO 지원): 검색 스니펫은 질문 발굴, Microsoft/CrowdStrike 사건 자료는 구체적 resilience failure 사례에 유용하나, 어느 것도 빈도·WTP·TAM을 증명하지 않는다. 긍정 반례와 함께 표현한다.
- Operator: 인증 없는 공개 경로만 사용하고 외부 문의·로그인·시크릿 입력 없이 수행한다. 명시된 Infinity 파일만 stage/push하며 unrelated worktree를 보존한다.
- Genie 교차조정: 문서 접근 불가와 실제 문서 부재를 구분한다. 기존 Intune/Autopatch stage deployment는 대안 신호지만 Falcon content 업데이트를 제어한다고 확대하지 않는다. 다음 leaf는 payload·통제 주체별 기능 비교와 독립 buyer evidence다.
- Planner (dispatch-66249915ff5c4f77931be4b30764adee 재검토): SSA와 Army/DoD 기록은 두 개의 제한된 연방 구매사례다. SSA OIG 권고 상태는 Jan 29 및 Mar 31, 2026 cutoff로만 표현하고, current status·award 인과관계는 열어 두지 않는다. Army search는 `hasNext=true`; paired transaction rows는 별도 IDs로 보존한다. 다음 leaf는 audit finding과 공개 award scope의 직접 겹침 여부를 확인한다.
- Developer: SSA 5 history rows는 $11,595,321.46 obligation과 정확히 합산되지만 $25,029,199.19는 base+all-options다. Army detail은 $5,904,868.98; account outlay 0과 `total_outlay=null` 구분. Army는 awarding Army, funding Navy office, INDOPACOM scope, Greenbrier prime이다. 6 paired rows를 지우거나 중복 award로 세지 않으며 합산액은 detail과 맞는다.
- Marketer (CMO 지원): safe segment hypothesis는 복잡한 인프라·공식 조달/자산 책임을 가진 federal/regulated operators까지다. 통합방화벽·inventory/CLIN 수정은 문제 정의보다 구매 구성 및 bookkeeping일 수도 있다. private pain/WTP/TAM/ARR, 만족도, remedy, startup opportunity는 증거가 아니다. 필요한 다음 증거는 독립 agency의 반복 업무·비용·예산권자·현재 control 및 대안이다.
- Operator: 이번 최신 역할 세션은 모델 소유 검증 `403 Forbidden`(fresh request 권고)로 실패했다. 재개 조건은 새 역할 요청이 그 검증을 통과하는 것. 앞선 `/root/operator_run3b`의 공개경로만 사용·명시 파일 stage 운영판단은 유지하되, 이번 증거의 새 Operator cross-review 완료로 간주하지 않는다.
- 추가 공개 대안 검토: GAO-26-107668의 DoD inventory/scan/physical-search 절차와 Army Corps Huntsville OT inventory 계약은 기존 내부통제·서비스 대안을 보여주나 SSA firewall audit나 Palo Alto award와 다른 시스템 범주다. 신생 제품 수요로 읽지 않는다.

## 한계·확신도

카테고리의 존재와 일부 업무·규제 방향에는 공식 근거가 있으나, 어느 세그먼트가 실제 신규 스타트업 기회인지에 대한 확신도는 낮다. 공개 시장 숫자는 서로 다른 모집단·정의·시점을 사용하며, 이 자료만으로 시장 규모를 합산할 수 없다. 다음 라운드는 특정 분야 추천이 아니라 구매자/업무별 증거 공백을 줄이는 데 쓴다.


### 교차검토에서 반영한 조정

네 역할은 독립 판단 후 서로의 기준을 검토했다. 이번 방법론 검토 결과, 헤드라인 비율의 국가 간 직접 비교는 불가하되 인구·질문·시점·추정법을 좁혀 일치시키는 제한 비교는 향후 가능성만 열어두기로 했다. 채택 지표는 구매 수요가 아니며, 시장 순위나 WTP 근거로 사용하지 않는다. 앞선 구매사례 검토의 미국 obligation/outlay와 한국 예정예산 분리 원칙도 유지한다. 이번 교차검토에서 Developer는 Census에 가중치 적용이 있다는 점을 들어 “가중치 부재”를 비교 불가 이유로 쓰지 말라고 정정했고, Planner·Operator는 공통 분모 재구성은 원표/원자료로 입증되기 전까지 미확정이라고 반박·보완했다. Marketer는 구매자·예산권자 검증으로 방향을 좁히되 adoption/조달 기록만으로 구매 수요나 WTP를 단정하지 말라고 했다. Genie는 이를 반영해 국가 비율 순위는 보류하고 DOE·ICE 두 공개조달을 별도 사례 신호로만 추가했다. 두 건 모두 단일 연방기록이며 민간시장 결론을 뒷받침하지 않는다.

이번 추가 스크리닝에서는 Planner가 DOE 라이선스 description을 CLIN·수량 증거로 보지 말고 Treasury의 “in-scope services”를 추가 라이선스로 해석하지 말라고 제한했다. Developer는 100행 첫 페이지 결과의 전체 원문 미보존 및 targeted API replay 503 때문에 거래별 재검증 전 확신도를 올리지 않도록 했다. Marketer는 연방 구매·갱신 언어를 민간 구매 pain, WTP, TAM, vendor revenue 또는 ARR로 일반화하지 말라고 했고, Operator는 성공했던 query 요약·실패한 replay·공식 Treasury 목록·DOE 원 award의 2차 미러를 출처 유형별로 분리하도록 했다. Genie는 세 거래를 screening lead로만 남기고 full award/transaction 응답 재조회 leaf를 다음에 둔다.
