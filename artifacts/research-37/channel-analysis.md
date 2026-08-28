# research-37 — 플팽부부 공개 YouTube 원문 조사

## 결론

공식 YouTube Atom feed에서 최신 15개 영상의 원문 제목·게시 시각·canonical URL·공개 조회 수를 모두 확인했다. 이 표본에는 여행·장기체류·주거를 직접 다룬 최신 15건 중 **여행/세계살이 10건, Shorts 5건, 장기체류를 제목에서 명시한 1건**이 있다. 따라서 intent의 `5개 이상 원문 근거 + 실행 가능한 실험 1개` 기준은 충족한다. 다만 feed가 최신 15건만 제공하므로 채널 전체의 장기 대표성, 시청자 반응, 실제 영상 장면은 판단하지 않는다.

## 방법과 근거 경계

- 채널: [플팽부부](https://youtube.com/@flyingpenguin992), channel id `UCsEfn-G__mrwWwhw2cZKu6Q`.
- 1차 근거: [공식 YouTube RSS/Atom feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCsEfn-G__mrwWwhw2cZKu6Q), 2026-08-28T19:08:04Z 수집. 원본 스냅샷은 실행 환경의 `/tmp/research37-rss.xml`에만 두고 재현은 feed URL로 한다.
- 행 단위 원문: `evidence-table.csv`의 15개 행. 각 행은 video id, 제목, 게시 시각, public view count, retrieval timestamp, canonical URL을 가진다. 링크의 `v=`/short id와 video id를 대조했다.
- 하지 않은 것: 로그인·쿠키·API key·유료 도구·봇 제한 우회·댓글/자막 수집·외부 발송. `yt-dlp` 개별 조회는 봇 확인에 막혀 근거로 쓰지 않았다.

## 확인된 반복 구조

| 관찰 범주 | 근거 행 | 확인된 사실 | 해석 상한 |
|---|---|---|---|
| 장소 + 판단/긴장 | rMooU1XKoEA, jpwTuDu7yeM, l6euJMh-XZM, pgeFXBIiaC8, WL3exfTITns, eYVwfTV4w9o, YlHhoy3zaPw, Z8w2IkXMYfA | 제목이 장소·여행 맥락에 ‘개인계좌 송금 요구’, ‘폭염’, ‘온도차’, ‘기대 이상’, ‘한국이 더 좋은 이유’처럼 판정 또는 구체적 조건을 붙인다. | 제목 구조의 반복일 뿐, 클릭 원인이나 영상 만족도를 뜻하지 않는다. |
| 생활 조건으로 보는 여행 | jpwTuDu7yeM, eYVwfTV4w9o, Z8w2IkXMYfA | 설명/제목에 귀농 삶 체험, 장기 체류, 여행비 정산이 명시된다. | 채널 전체가 주거 전문이라는 뜻은 아니다. |
| 장소의 실용 근거 | l6euJMh-XZM, WL3exfTITns | 설명에 촬영월과 실제 방문 장소 목록이 있다. | 장소·가격·날씨는 촬영 시점 정보라 오늘의 여행 조언으로 재사용하면 안 된다. |
| 롱폼과 Short의 분리 | long 10, short 5 | Shorts 5개는 RSS description이 비어 있고, 3개가 ‘여행하면서 그림그리기’를 제목에 반복한다. | Short의 실제 편집/장면/성과는 확인하지 않았다. |

## 바꿀 첫 실험 — 복사하지 않는 구조 적용

**채택할 메커니즘:** 목적지명만 내세우지 말고, 직접 확인한 한 가지 생활 조건 또는 선택을 함께 둔다. 예: `카이로에서 3일째, 숙소보다 먼저 확인한 한 가지`.

이 문장은 플팽부부의 제목을 베끼는 것이 아니라, ‘장소 + 검증 가능한 조건/판단’이라는 관찰 구조를 세계여행의 직접 장면으로 다시 쓴 것이다. 장소·가격·안전·날씨는 촬영 당시 직접 확인된 것만 넣고, 현재 여행 정보처럼 단정하지 않는다. 첫 실험은 (1) 실제 장면 1개, (2) 선택 기준 1개, (3) 결론을 과장하지 않는 제목 2안으로 만든다. **판정:** 72시간 동안 클릭률과 구체 댓글을 직전 유사 영상과 비교하되, 표본 1건으로 성과 일반화는 하지 않는다.

## 적용하지 않는 것

- ‘폭염’, ‘가성비’, ‘최신 뉴스’, ‘버킷리스트’ 같은 표현은 실제 확인 없이 채택하지 않는다.
- 공개 조회 수는 수집 시점의 스냅샷이며 제목 품질·수익·추천 원인을 증명하지 않는다.
- 제목과 빈 description만으로 영상 서사, 부부 관계, 한달살이 경험, 시청자 동기를 추정하지 않는다.
- 현행 장소 정보/가격/환율/날씨를 여행 권고로 전환하지 않는다.

## 지식 반영 판정

- `knowledge_status`: used
- `knowledge_decision`: retain-as-operating-principle
- `knowledge_targets`: `agent-wiki/README.md`, `concepts/evidence-bounded-content-experiment.mdx`, `concepts/currentness-safe-travel-context.mdx`, `syntheses/original-proof-distribution-loop.mdx`
- `knowledge_reflection`: 조회 수를 제목의 성공 증거로 읽지 않고, 1차 원문에서 확인된 제목 구조만 실험 가설로 낮춘다.
- `knowledge_commit`: no-promotion-needed — 기존 증거 경계·여행 현재성 원칙을 적용했으며 새 wiki 규칙으로 승격할 일반화는 만들지 않았다.
