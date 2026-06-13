# 소싱 우선 광범위 스크린 — 준비 자료

- 준비일시: 2026-06-13T03:00Z
- Intent: naver-shopping-01 (나래/Narae)
- Mode: cloud prepare → local execute
- 준비자: Heartbeat Agent (cloud)

## 컨텍스트

### 이전 스크린 결과 요약

| 후보 | 판정 | 이유 |
|------|------|------|
| 러기지택/캐리어네임택 | 내림 (사용자) | 사용자 선호 낮음 |
| 여행준비 paper-card insert | HOLD | buyer intent 약함(0.05% CTR), generic checklist commodity |
| AI/creator workshop card | DRAFT/copy-led | native keyword 없음, 수요 미검증 |
| 트래블러스노트 리필/속지 | PIVOT ✓ | transactional CTR 2.44%, brand-anchored, 6,420/mo |

### 사용자 선호 프로필

- 소싱 우선 (제조·커스터마이징 지양)
- 실용/미니멀/정리형 성향
- 여행 연관 제품
- 샘플 마찰 낮은 것, 옵션 복잡도 낮은 것

## 외부 시장 신호 (2026-06-13 기준)

### 1. Inventario 2026 (문구 페어)
- 일시: 2026-06-10~14, COEX 더플라츠홀
- 규모: 103개 브랜드 참여 (전년 대비 2배 이상 확대), 2만 5천명+ 방문 예상
- Naver 타이틀 스폰서로 참가, Naver Pay FaceSign 결제 시범 운용
- **의미**: 한국 문구/여행노트 카테고리 실구매 수요가 지금 이 시점에 집중됨
- **기회**: 트래블러스노트·여행 스테이셔너리 관련 제품의 검색·구매 욕구 최고조

### 2. 패킹큐브/여행수납 시장
- 연간 12~15% 성장률 (compression packing cube 주도)
- 2025년 8월 피크: 검색량 정규화 100, 21,180개 판매 기록
- 6~8월 성수기 현재 진행 중
- **기회**: 지금이 검증 타이밍 (성수기 수요 실확인 가능)

### 3. 여행파우치/세면파우치
- 여름 해외여행 시즌 수요 급증기
- 한국 내 중국 소싱 상품이 많아 경쟁 포화 가능성 존재

## 소싱 후보 카테고리 (우선순위순)

### A. 패킹큐브/여행수납세트 ★★★ (최우선)

**소싱 조건 체크**
- 소싱 마찰: 낮음 (알리바바/1688 저MOQ, 3~6개 세트 구성 표준화)
- 옵션 복잡도: 낮음 (색상 2~3가지, 사이즈 세트 구성)
- QA 리스크: 낮음 (패브릭 내구성, 지퍼 품질 체크만)
- 반품 리스크: 낮음 (사이즈 이슈 없음, 개인 취향 낮음)

**수요 신호**
- 6~8월 성수기 NOW
- 연 12~15% 시장 성장
- 비즈니스/친환경 소비자 수요 확대

**사용자 적합도**: 높음 (실용/정리형 + 여행)

**Naver 검증 키워드**
- Core: `패킹큐브`, `여행수납파우치`, `압축파우치`
- Sub: `여행짐정리`, `캐리어수납파우치`, `여행짐싸기`

**로컬 액션**
1. OpenAPI top-20 (`패킹큐브`, `여행수납파우치`, sort=sim)
2. SearchAd CTR/depth/월간검색량
3. DataLab 계절성 (최근 12개월)
4. 알리바바 1688에서 MOQ/단가 확인
5. PROMOTE/PIVOT/HOLD 판정

---

### B. 트래블러스노트 호환 속지 (structured travel-prep insert) ★★★

**소싱 조건 체크**
- 소싱 마찰: 중간~낮음 (소량 인쇄 가능, printable insert 방식이면 낮음)
- 옵션 복잡도: 낮음 (사이즈 2가지: 패스포트·미디움만)
- QA 리스크: 낮음 (종이 규격, 인쇄 품질)
- 반품 리스크: 낮음

**수요 신호**
- 트래블러스노트 월 6,420 검색, 리필 ad CTR 2.44% (transactional)
- Inventario 2026 NOW — 문구/노트 구매 열기
- 속지/리필 시즌: 12월~1월(연말/신년) + 현재 여행시즌 중간

**사용자 적합도**: 최고 (기존 PIVOT 방향, 가장 fit)

**Naver 검증 키워드**
- Core: `트래블러스노트속지`, `트래블러스노트리필`
- Sub: `트래블러스노트호환`, `속지리필`, `트래블러스노트패스포트속지`

**로컬 액션**
1. OpenAPI 트래블러스노트속지 top-20 (경쟁 속지 스펙/가격)
2. SearchAd 리필 관련 키워드 CTR/depth
3. 인쇄 소싱 경로 확인 (국내 소량 인쇄 / 중국 직인쇄)
4. PROMOTE/PIVOT/HOLD 판정

**주의**: 브랜드명 직접 사용 시 "호환" 표기 필수

---

### C. 여행용 세면/화장 파우치 ★★

**소싱 조건 체크**
- 소싱 마찰: 매우 낮음 (중국 저MOQ 다양, 표준화된 제품)
- 옵션 복잡도: 낮음 (색상 2~3가지, 방수/비방수)
- QA 리스크: 낮음 (방수 처리 확인)
- 반품 리스크: 중간 (색상 불일치 가능)

**수요 신호**
- 여름 여행 시즌 수요 급증
- 범용적 카테고리

**우려**: 매우 포화된 카테고리 — 검증 시 경쟁밀도 필수 체크

**사용자 적합도**: 중간 (실용적이나 특별한 차별화 포인트 낮음)

**Naver 검증 키워드**
- Core: `세면파우치`, `여행파우치`, `여행화장파우치`
- Sub: `클리어파우치`, `방수파우치`, `여행용파우치세트`

**로컬 액션**
1. OpenAPI top-20 경쟁 밀도·가격대 분포
2. SearchAd CTR → informational vs transactional 분류
3. 포화 판정 시 HOLD 권고

---

### D. 케이블/전자기기 여행 정리 파우치 ★★

**소싱 조건 체크**
- 소싱 마찰: 낮음
- 옵션 복잡도: 낮음
- QA 리스크: 낮음
- 반품 리스크: 낮음

**수요 신호**
- 2026 여행 트렌드: 테크 오거나이저 수요 증가
- 비즈니스 여행자 타겟

**사용자 적합도**: 중간 (실용적이나 여행 소품 느낌 약함)

**Naver 검증 키워드**
- Core: `케이블파우치`, `여행케이블정리`, `전자기기파우치`
- Sub: `충전기파우치`, `여행IT파우치`

---

### E. 여권케이스/여권파우치 ★ (저우선순위)

- 바이어 인텐트 분명하나 매우 포화
- 사용자 적합도 낮음
- 우선순위 5번

## 소싱 우선순위 매트릭스

| 카테고리 | 수요 강도 | 소싱 난이도 | 경쟁 우려 | 사용자 적합도 | 우선순위 |
|---------|---------|-----------|---------|------------|--------|
| A. 패킹큐브/수납세트 | ★★★ 성수기NOW | 낮음 | 중간 | 높음 | **1** |
| B. 트래블러스노트속지 | ★★★ transactional | 중간 | 낮음 | 최고 | **2** |
| C. 세면/화장파우치 | ★★ 시즌 | 매우낮음 | 높음 | 중간 | **3** |
| D. 케이블정리파우치 | ★★ 트렌드 | 낮음 | 중간 | 중간 | **4** |
| E. 여권케이스 | ★ | 낮음 | 매우높음 | 낮음 | **5** |

## 로컬 실행 프롬프트

```
Infinity Intent: naver-shopping-01 나래/Narae 소싱 우선 광범위 스크린
Mode: execute_local
Invocation: Prefer existing pt/purplemux Claude pane via tmux -L purple; capture first, clear stale, send bounded prompt, capture result. Fall back to fresh bounded Claude Code only if no usable pt pane.
Workflow: Use workflow-master for multi-step Naver API sequence. Find under ~/.claude/skills/workflow-master/ or ~/.claude/agents/workflow-master.md first.

Goal: 아래 4개 카테고리(A~D)를 Naver OpenAPI + SearchAd + DataLab로 순서대로 검증하여
      PROMOTE/PIVOT/HOLD 판정 산출

Priority order: A(패킹큐브) → B(트래블러스노트속지) → C(세면파우치) → D(케이블파우치)

각 카테고리별 수행:
1. OpenAPI top-20 검색 (대표 키워드 2-3개, sort=sim)
   → 가격대 분포, 리뷰수, 상위 판매자 스펙 확인
2. SearchAd /keywordstool → CTR, ad depth, 월간 검색량
3. DataLab 계절성 (최근 12개월)
4. PROMOTE/PIVOT/HOLD 판정 (keyword-competitor-validation-plan.md 루브릭 적용)

Prepared findings:
- Inventario 2026 (6/10~14 COEX) NOW 진행 중 → 문구/노트 수요 피크
- 패킹큐브 성수기 NOW (6-8월), 연 12-15% 성장
- 트래블러스노트 리필 CTR 2.44% 이미 확인 (PIVOT 방향 유지)
- artifacts/naver-shopping-01/sourcing-first-broad-screen-2026-06-13.md 참조

Allowed: L0/L1 (read-only API, docs 작성, 결과 기록)
Forbidden: 상품등록/가격/배송/재고/광고/고객/주문/계정/공개발행 0
Verification: 각 카테고리 판정 근거 API 데이터로 명시

Report back:
- naver-shopping-agent/sourcing-broad-screen-{날짜}.md (산출물)
- reports/naver-shopping-01/{timestamp}-local.html (HTML 필수)
```

## 계승한 기준

1. **Purchase Situation Before Object Shape** (marketing-50): 오브젝트명보다 구매 상황 먼저
2. **PROMOTE/PIVOT/HOLD 루브릭** (naver-shopping-01): 기존 keyword-competitor-validation-plan.md 그대로 적용
3. **소싱 우선 기준**: 샘플마찰 낮음 + 옵션복잡도 낮음 + QA/반품 관리 가능 (사용자 2026-06-11 지시)

## 이번에 새로 배운 것

- Inventario 2026 (6/10~14 COEX, 103 브랜드, Naver 타이틀 스폰서) = 한국 문구 카테고리 수요 NOW 신호
- 패킹큐브 6-8월 성수기 = 지금 검증하면 실수요로 판정 가능
- 셀러해(1020bag.com) = 국내 가방/파우치 B2B 도매 경로
