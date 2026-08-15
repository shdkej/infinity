# research-26 — 디지털 오거나이저 시장성 조사

작성: 2026-08-14T22:15Z | 범위: 내부 조사만 | target_agent: genie

## Planner

목표는 “모든 앱을 통합한다”가 아니라, 연동이 없어도 사용자가 자기 디지털 생활을 한눈에 보고 다시 찾는 문제에 돈을 낼지 판정하는 것이다. 완료 기준은 경쟁 8개 이상, 시장성 결론, 최소 MVP, 차별화 3개, 함정 5개, 2주 실험 3개다. Knowledge Lab 근거는 `agent-wiki/content/docs/syntheses/sufficient-boundary-for-next-action.mdx`의 검증 가능한 다음 행동/충분함, `observable-feedback-systems.mdx`의 관측 신호가 다음 행동으로 압축되어야 한다는 원칙, `concepts/human-agent-fit.mdx`의 권고·판정·저장·외부 실행 경계다.

## Developer

권장 구현은 계정 연동 허브가 아니라 로컬 우선 “서랍 카탈로그”다. 1차 데이터 모델은 `item {name, url, category, icon, note, last_verified, integration_status}`와 `drawer {name, color, order}` 정도로 제한한다. 수동 입력/CSV·브라우저 북마크 import를 우선하고, 실제 콘텐츠 embed는 2~3개 공개·안정 API만 후순위로 둔다. 핵심 화면은 서랍 홈, 항목 상세/열기, 검색·필터, 가져오기/내보내기다. 연동 토큰을 저장하지 않는 구조가 롤백·보안·운영 비용을 낮춘다.

## Marketer

구매 동기는 “모든 앱을 안에서 본다”보다 “내가 쓰는 디지털 생활의 입구를 잃지 않는다”가 더 강하고 설명 가능하다. 통합 뷰는 기대치를 과대생성하고 연동 실패 때 신뢰를 깎는다. 포지셔닝 후보는 `앱을 모으는 곳`이 아니라 `내 디지털 생활을 서랍처럼 다시 찾는 홈`이다. 첫 사용자군은 앱·서비스가 20개 이상이고, 프로젝트/취향/생활용으로 오가는 솔로프리너·크리에이터·개발자다. 무료 카탈로그 + 유료 백업/자동 정리/다중 디바이스 동기화(월 $4~8 가설)가 가장 자연스럽고, 팀 플랜은 초기 범위 밖이다.

## Operator

초기 운영의 핵심 리스크는 OAuth 토큰, API 변경, embed 장애, 링크 부패, 데이터 잠금이다. 따라서 v0는 링크와 메타데이터 중심, export JSON/CSV와 삭제 기능 필수, integration_status와 last_verified를 사용자에게 보인다. 측정은 가입 수가 아니라 1) 15분 안에 20개 항목 등록, 2) 7일 뒤 재방문해 항목 열기, 3) “이걸 계속 쓰겠다” 유료 의향이다. 외부 발송·결제·공개 배포는 실행하지 않는다.

## 경쟁 스크린

| 대체재 | 현재 신호/가격 | 강점 | 이탈 이유와 빈틈 |
|---|---|---|---|
| Notion | Free; Plus $10/member/mo | 데이터베이스·문서·연결 | 직접 설계해야 하며 앱 런처/시각적 서랍이 핵심이 아님 |
| Raindrop.io | 무기한 Free; Pro 유료 | 북마크·컬렉션·검색·2,600+ integrations | 저장한 웹 콘텐츠 중심, 생활 전체의 앱 카탈로그는 아님 |
| Anytype | 개인 Free/유료 membership; Business $20/editor/mo | local-first, object/space, privacy | 학습 비용과 구조 설계가 크고 “내 앱 입구”가 전면 가치가 아님 |
| Capacities | 핵심 Free; Pro는 AI·calendar·API 등 | 객체 기반 지식관리·검색 | 지식 축적에 강하고 시각적 서비스 서랍에는 과함 |
| Readwise Reader | 연간 결제 $9.99/mo, 월 $12.99 | 읽기·하이라이트·오프라인·검색 | 읽기 흐름에 특화, 모든 서비스의 홈이 아님 |
| Fabric | 무료 체험/플랜 안내; capture·deep search·AI | 파일·링크·메모 통합 검색 | 범용 second brain 경쟁, 시각적 분류보다 검색/AI 중심 |
| mymind | 저장량 기반 Free guest + 유료 구독 | 자동 분류·비주얼 저장·프라이버시 | 콘텐츠 저장이 중심, 앱/서비스 운영 입구와 다름 |
| Arc | 무료 브라우저; Spaces/Favorites/Archive | 생활 영역별 공간과 앱 탭 정리 | 브라우저 안에 갇히며 브라우저 밖 서비스·메타데이터 관리가 약함 |
| Apple Shortcuts/기본 폴더 | OS 기본 제공 | 앱/자동화 접근성과 폴더 | 플랫폼 종속, 설명·검색·크로스플랫폼 카탈로그 부족 |

공식 근거: [Notion pricing](https://www.notion.com/pricing), [Raindrop pricing](https://raindrop.io/pro/buy), [Anytype memberships](https://doc.anytype.io/anytype-docs/advanced/monetization), [Anytype Business](https://business.anytype.io/), [Capacities pricing](https://capacities.io/pricing), [Readwise pricing](https://async.readwise.io/upgrade), [Fabric](https://fabric.so/download/mobile), [mymind pricing rationale](https://mymind.com/mymind-pricing-why-pay-for-an-app-when-others-are-free), [Arc](https://arc.net/), [Apple Shortcuts folders](https://support.apple.com/en-ca/guide/shortcuts/apd113493874/ios).

## 종합 판단

시장성은 **중간**이다. 개인 생산성 전체를 대체하는 제품으로는 무료·강력한 대체재가 많아 낮다. 그러나 “내가 실제로 쓰는 앱/서비스를 역할별로 배치하고 다시 여는 개인 홈”으로 좁히면, 연동 없이도 반복되는 탐색 비용을 줄이는 명확한 문제와 지불 가능성이 있다. 구매 동기는 통합 열람보다 `정리된 입구 + 재방문`에 있다. 따라서 먼저 20~50개 항목을 15분 안에 정리하는 경험을 검증하고, 돈을 받는 지점은 저장량보다 자동 분류·백업·동기화로 둔다.

## 가장 작은 MVP

- 대상: 앱/서비스가 많은 솔로프리너·크리에이터·개발자
- 입력: 이름/URL/아이콘/짧은 설명 수동 입력, 브라우저 북마크·CSV import
- 화면: 서랍 홈(카테고리/색/정렬), 검색, 항목 상세, 링크 열기, export/import
- 연동: embed 없음. `연결됨/링크만/확인 필요` 상태만 표시
- 검증 가격: 14일 무료 후 월 $5 또는 연 $49 가설; 결제 구현 없이 선호도와 예약 의향만 측정

## 차별화 문장

1. “내가 쓰는 모든 서비스를, 다시 찾을 수 있는 디지털 서랍으로 만든다.”
2. “연동되지 않아도 괜찮다. 중요한 건 콘텐츠 통합보다 내 생활의 입구를 잃지 않는 것.”
3. “Notion처럼 직접 설계하지 않고, 브라우저처럼 탭을 쌓지 않고, 내 앱 생활을 한 장으로 본다.”

## 피해야 할 함정

1. 처음부터 ‘모든 서비스 통합’ 약속을 해 OAuth·API 유지보수에 빠지는 것.
2. Notion/second brain 기능을 복제해 제품 정체성을 잃는 것.
3. 예쁜 카드/서랍만 만들고 검색·export·재방문을 측정하지 않는 것.
4. 개인용 문제를 팀 협업·AI 비서·마켓플레이스로 동시에 확장하는 것.
5. 링크 부패·아이콘 저작권·개인정보·데이터 이동성을 뒤늦게 처리하는 것.

## 2주 실험

1. 랜딩/프로토타입에 “20개 앱을 15분에 서랍으로 정리”를 제시하고 10명에게 실제 목록을 import하게 한다. 성공: 7명 이상이 15분 안에 20개 등록, 5명 이상이 7일 내 재방문.
2. 동일한 데모로 `통합해서 보기`와 `정리해서 다시 열기` 두 메시지를 무작위 비교한다. 성공: 유료 의향·첫 행동 완료율이 어느 메시지에서 더 높은지 결정.
3. 수동 입력 MVP를 5명에게 7일 제공하고, 마지막에 “월 $5/연 $49를 내고 유지” 예약 의향을 묻는다. 성공: 2명 이상 유료 의향 + 3명 이상 주 2회 재방문. 실패하면 소비자 전체가 아닌 특정 직군으로 재세분화한다.

## Master synthesis / rejected

합의: 서랍형 시각 정리, 링크 우선, 좁은 초기 사용자군, 재방문 측정. 충돌: Developer는 연동을 후순위로, Marketer는 통합 열람의 매력을 인정했으나 초기 약속에서 제외했다. 기각: 범용 second brain, 팀 워크스페이스, 다수 OAuth, AI 자동 분류를 MVP에 포함하는 안. 이유는 Knowledge Lab의 “충분함은 검증 가능한 다음 행동이 생겼는가”와 운영 복잡도 상한에 어긋난다.

## Sources / evidence date

공식 페이지를 2026-08-14 UTC에 확인했다. 가격은 지역·청구주기·변경에 따라 달라질 수 있으므로 후속 실험에서는 실제 checkout 표시를 재확인한다. 시장 규모의 정량 TAM은 이번 범위에서 과장하지 않고, 실제 지불 의향 실험으로 남긴다.
