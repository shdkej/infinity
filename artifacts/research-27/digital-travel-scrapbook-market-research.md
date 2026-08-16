# 디지털 여행 스크랩북 시장 조사

- intent: `research-27`
- 조사일: 2026-08-16 (current retry evidence access date)
- execution_mode: `multi_subagent_roles`
- target_agent: `genie`
- 범위: internal-research-only; 공개 발행·외부 사진 업로드·결제·배포 제외

## 결론

**검증할 가치가 있는 가설 — 단, 일반 여행 다이어리/스크랩북이 아니라 ‘다시 열고 싶은 도시 기억 카드’로 좁혀 2주 검증한다.**

공식 제품 페이지는 여행 추적·저널·사진 회고에 대한 기존 수요를 보여주지만, 이 좁은 기억 카드의 시장 수요나 지불 의향을 검증하지는 않는다. 따라서 지도·소셜·전체 사진 보관으로 경쟁하지 않는다. 기회 가설은 여행 중 흩어진 사진·한 줄 메모·장소를 사용자의 관찰과 다음번 교훈이 살아 있는 짧은 이야기로 압축하고, 나중에 다시 꺼내게 하는 것이다.

## 역할별 판단

### Planner — `dcdf4493-0041-4a6c-98cc-ba5f649a5c0c` — completed

핵심 사용자는 장기 여행 중 사진·짧은 메모·음성을 남기지만 나중에 해석·재사용하지 못하는 solo/couple 여행자다. 핵심 시나리오는 저마찰 캡처 → 주간 압축 → 장소·감정·교훈 검색 → 콘텐츠/회고 재사용이다. 지도·소셜·협업은 첫 범위에서 제외하고 ‘작은 입력 하나가 의미 있는 기억으로 바뀌는가’를 검증한다.

근거: `agent-wiki/content/docs/mapped/Idea/Travel.mdx`, `Idea/Journal.mdx`, `deep-knowledge/product.mdx`, `Integration/Creator.mdx`, `source/openclaw-system/docs/WORLD_TRAVEL_PROJECT.md`.

### Developer — `f0487c72-d08f-4227-a5ae-f9e379f40158` — completed

2주 구현은 가능하다. Trip/Entry/Media/AIArtifact/Reflection을 분리하고, IndexedDB 기반 responsive PWA에서 수동 사진 import, 한 줄 메모, 편집 가능한 memory card, chronological stream, JSON export/import, delete를 제공한다. AI는 opt-in adapter와 mock fallback만 두고, 영상 처리·OAuth·지도 SDK·소셜 공유는 미룬다. 원본/사용자 메모/AI 산출물을 분리해 재처리·삭제·provider 교체를 보장한다.

### Marketer — `f5a5be0e-28a6-4d32-9b70-f3c5126dd9c8` — completed; prior `01a007b5-01da-71f2-8c00-37ff0e35317b` timeout retained as historical lineage

경쟁/대안은 아래와 같다.

| 서비스/대안 | 강점 | 확인된 빈틈 |
|---|---|---|
| Polarsteps | 공식 페이지상 계획·추적·공유·Travel Books; Plus €8.99/월 또는 €29.99/년(지역별 변동) | 개인적 의미·재방문이 약하다는 것은 가설 |
| FindPenguins | 공식 페이지상 경로·공유·travel books; 공식 지원상 구독/프리미엄 없음 | ‘무엇이 중요했나’ 층이 약하다는 것은 가설 |
| Day One | 멀티미디어 저널; Silver $49.99/년·Gold $74.99/년 | 여행 서사/지도 출력이 별도 구성이라는 평가는 가설 |
| Journey | 공식 페이지상 크로스플랫폼 저널·공유·타임라인·지도/사진 보기 | 범용 설정이 많고 여행 집중도가 낮다는 것은 가설 |
| Apple Journal | 공식 발표상 사진·장소·활동·오디오·검색/필터·iCloud 암호화 | Apple 중심이며 다국가 여행책/편집 흐름이 아니라는 평가는 가설 |
| Google Photos | 공식 지원상 여행·순간 하이라이트 생성 및 원본과 별도 편집/삭제 | 사진 재노출은 강하나 사용자 해석·서사화가 약하다는 것은 가설 |
| Notion | 공식 가격 페이지상 Free/Plus/Business/Enterprise와 Plus $10/member/월 | 빈 캔버스와 유지보수 부담이라는 평가는 가설 |
| Obsidian | 공식 페이지상 로컬 노트와 선택적 암호화 Sync; Sync $4/월(연간 청구) | 여행 캡처·미디어 큐레이션이 기본 제공되지 않는다는 평가는 가설 |
| Instagram/Threads | 공개 게시와 사회적 반응을 제공하는 대안 | 소유·연대기·사후 회고보다 공개 관심을 최적화한다는 평가는 가설 |
| 카메라 롤/종이 앨범 | 사용자가 이미 보유한 비용 없는 저장/기록 대안 | ‘나중에 정리’가 비행동 대안이라는 평가는 가설 |

가격·기능은 2026-08-16 공식 페이지에서 확인했다. 직접 근거는 아래에 고정하며, 지역·플랜에 따라 달라질 수 있다. 기능 차이가 개인적 의미·재방문 가치의 부족을 증명하지는 않는다.

- Polarsteps: https://www.polarsteps.com/plus 및 https://support.polarsteps.com/hc/en-us/articles/37272667752850-Is-Polarsteps-Plus-worth-it
- FindPenguins: https://findpenguins.com/ 및 https://support.findpenguins.com/hc/en-us/articles/360013914533-Is-FindPenguins-free
- Day One: https://dayoneapp.com/guides/premium-subscription/day-one-pricing-features-guide/
- Journey: https://help.journey.cloud/en/article/what-is-journey-1cmxhui/ 및 https://support.journey.cloud/en/categories/purchase-payment/articles/journey-license-comparison
- Apple Journal: https://www.apple.com/newsroom/2023/12/apple-launches-journal-app-for-reflecting-on-life/
- Google Photos: https://support.google.com/photos/answer/10688442
- Notion: https://www.notion.com/pricing
- Obsidian: https://obsidian.md/sync

Notion Plus $10/member/월과 Obsidian Sync $4/월(연간 청구)도 각 공식 가격 페이지에 표시되지만, 조사 시점·지역에 따른 변동 가능성이 있다. Instagram/Threads, 카메라 롤, 종이 앨범은 정량 비교하지 않은 대안 가설이다.

추천 메시지는 검증 전 제안 가설로 “여행 하루를, 다시 열고 싶은 이야기로 바꿔보세요.”를 사용한다. “AI 여행 다이어리”, “올인원 여행 플랫폼”, “사진을 모두 정리”는 포지셔닝 가설과 범위에 맞지 않아 피한다.

### Operator — `57e75cc0-7b1c-4909-9590-8fa2ea20c5a4` — completed

2주 동안은 로컬 파일과 수동 입력만 사용하며 원본 사진을 외부에 올리지 않는다. 얼굴·동행인·EXIF GPS·문서 노출을 위험으로 본다. 성공은 입력량이 아니라 3·7·14일 재방문, 기억 회수, 삭제/수정 신뢰, 다음 입력이다. 미래 비용은 storage/egress, AI vision, geocoding, auth, backup, deletion/export다. 외부 AI, cloud sync, OAuth, 공개 모집·설문·결제는 승인 전 금지한다.

## 첫 MVP: City Memory Card

선택한 사진을 로컬 import하고 도시/날짜를 붙인 뒤 다음 세 질문에 답한다.

1. 무엇을 보았나?
2. 무엇이 의외로 좋거나 어려웠나?
3. 다음에 무엇을 기억해야 하나?

결과는 편집 가능한 1장의 카드이며 도시·날짜로 탐색하고 Markdown/PDF/image로 export한다. live tracking, public feed, 자동 전체 라이브러리 ingest, 결제, 영상 편집은 제외한다.

## 2주 검증 실험

1. **개인 캡처 trial**: 로컬 사진/한 줄 메모 10–15개. median capture time, 완료율, skip 수, privacy concern을 측정한다.
2. **Resurfacing 비교**: 동일 자료를 timeline·map-plus-scenes·theme scrapbook으로 보여주고 retrieval time, 회수한 기억 수, 선호 형식, 수정/삭제를 기록한다.
3. **반복 사용 gate**: 3·7·14일에 무프롬프트 재방문을 관찰한다. unprompted return, 신규 입력, 재열람/저장, 계속 사용할 의향을 기록한다.

후속 외부 검증은 승인 후 concierge 5–10명에게 1일 사진+3문장을 받아 24시간 내 1쪽 story를 돌려주고, 2일차 제출률·‘다시 열겠다’ 응답·€5–10 지불 의향을 측정한다. 현재 intent 범위에서는 실행하지 않는다. 수요·가격·재방문 결과는 모두 미검증 가설이다.

## Genie synthesis / 기각안

네 역할은 모두 ‘저마찰 입력–의미 있는 압축–재방문’에 수렴했다. 공식 제품의 존재는 카테고리 활동을 보여주는 근거일 뿐 시장 수요·지불 의향·경쟁 약점을 증명하지 않는다. “broad scrapbook은 crowded”와 차별화 가능성은 가설로 둔다. 최종 순서는 (1) 로컬 City Memory Card, (2) 3·7·14일 재방문 측정, (3) 반복 신호가 있을 때만 opt-in AI와 외부 concierge를 검토한다.

기각안은 지도·실시간 GPS·소셜 피드·전체 사진 자동 업로드·영상 생성·범용 여행 플래너다. 이들은 핵심 습관 증명 전 비용·권한·프라이버시·운영 복잡도를 키운다.

## Red handoff

최종 산출물은 Red가 요청 일치성, 8개 이상 비교, 직접 URL과 조사일, 근거와 가설의 분리, internal-only 경계, MVP 범위, role session 기록을 검증한 뒤 Archive한다.
