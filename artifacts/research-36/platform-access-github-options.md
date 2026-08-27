# research-36 플랫폼 접근 제한 대응 조사

기준 시각: 2026-08-27T10:30Z

## 결론

YouTube는 익명 웹 스크래핑을 더 밀어붙이는 대신 공식 YouTube Data API를 1순위 수집 경로로 바꾸면 막힌 부분을 상당히 풀 수 있다. 방금 `search.list -> videos.list` 조합으로 제목, 채널, 게시일, 조회수를 한 행에서 확인했다.

Instagram Reels는 공식 공개 API만으로 임의 계정/해시태그의 원문 제목, 게시일, 공개 재생 수를 안정적으로 수집하는 경로가 아직 약하다. GitHub 도구들은 대부분 로그인 세션, 비공식 API, 유료 스크래핑 공급자, 브라우저 자동화 중 하나에 기대고 있어 승인 없이 기본 경로로 넣기 어렵다.

## GitHub에서 확인한 경로

### 1. YouTube: 공식 API 우선

- 확인 경로: YouTube Data API `search.list`로 후보 videoId를 얻고, `videos.list(part=snippet,statistics)`로 제목, 채널, 게시일, 조회수를 가져온다.
- 방금 테스트 결과: 한국어 쿼리 `여행 짐 기내수하물`에서 3건 조회 성공.
- 장점: 로그인 쿠키, 프록시, 브라우저 우회 없이 행 단위 근거를 만들 수 있다.
- 한계: API quota가 필요하고, 검색 결과 품질은 쿼리 설계에 좌우된다.

샘플 필드:

```text
videoId | title | channelTitle | publishedAt | viewCount
rqg27ydxJNc | 해외여행 전 기내수하물 위탁수하물 쉽게 구분하기 | 빠니보틀 Pani Bottle | 2023-11-01T22:13:10Z | 1488173
MFrm4U8_QOQ | 해외여행 준비물 이것만 챙기면 끝! 위탁수하물 없이 캐리어 짐싸기 실전 팁 대방출✈️(+체크리스트 파일 공유) | 타이거투어 - 나만 알기 아까운 여행정보 | 2025-11-16T05:06:17Z | 61076
98NVnut9av4 | 해외 여행 가기 전 반드시 봐야 할 비행기 반입 물품 총정리✈️ 이 영상 하나면 여행 준비 끝! 캐리어 짐싸기 꿀팁🧳 [기내반입금지물품,보조배터리,화장품,액체,음식,캐리어] | 타이거투어 - 나만 알기 아까운 여행정보 | 2025-04-15T09:00:12Z | 499872
```

### 2. YouTube: 최신 yt-dlp는 보조 경로

- GitHub: https://github.com/yt-dlp/yt-dlp
- 확인 상태: 최신 릴리스는 `2026.08.19`, 로컬 설치본은 `2026.03.17`.
- 관련 기능: `--cookies-from-browser`, `--extractor-args`, YouTube `player_client`, `po_token`, `fetch_pot`, `player_skip`.
- 판단: `yt-dlp`는 개별 URL 보조 검증에는 좋지만, 지금 문제의 100건 근거 수집 1순위로 두면 봇 확인에 다시 막힐 수 있다.
- 주의: yt-dlp 이슈에서 쿠키 사용은 YouTube 계정 리스크가 있다고 논의되어 있다. 계정 쿠키를 기본 자동화에 넣지 않는다.

근거:

- https://github.com/yt-dlp/yt-dlp
- https://github.com/yt-dlp/yt-dlp/issues/15796
- https://github.com/yt-dlp/yt-dlp/issues/15106
- https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/youtube/pot/README.md

### 3. YouTube: PO Token은 기본 경로로 두지 않음

- yt-dlp에는 PO Token provider framework가 있다.
- 다만 PO Token은 YouTube 내부 보호 흐름 대응에 가깝고, 구현 안정성도 플랫폼 변화에 영향을 받는다.
- research-36의 목표는 제목/게시일/조회수 근거 수집이므로, 다운로드/플레이어 제한을 뚫는 쪽보다 공식 메타데이터 API가 맞다.

### 4. Instagram: Instaloader는 가능하지만 경계가 큼

- GitHub: https://github.com/instaloader/instaloader
- 기능: 공개/비공개 프로필, 해시태그, reels, 댓글, 위치, 캡션 수집을 지원한다.
- 이슈 확인: `i.instagram.com` API가 403 `login_required`를 반환하는 사례가 있고, `--no-iphone`으로 반복 재시도 비용을 줄이는 논의가 있다.
- 판단: 공개 프로필 일부 수집에는 쓸 수 있지만, Reels의 게시일·재생 수·원문 제목을 100건 안정적으로 맞추려면 로그인 세션 또는 브라우저/유료 공급자 의존이 생긴다.

근거:

- https://github.com/instaloader/instaloader
- https://github.com/instaloader/instaloader/issues/2661
- https://github.com/instaloader/instaloader/issues/2480

### 5. Instagram: 유료/외부 API 공급자는 승인 후 옵션

GitHub 검색 결과에는 Apify, Thordata, SocialAPIs 계열 Instagram scraper 래퍼들이 보였다. 이들은 대체로 외부 유료 API나 스크래핑 인프라에 의존한다.

판단:

- 승인 없이 자동화에 넣지 않는다.
- 구매, 계정 연결, API 키 발급은 별도 승인 필요.
- 사용한다면 원시 응답은 로컬 캐시에 두고, Git에는 요약/행 근거만 올린다.

## research-36 재개안

1. YouTube는 공식 Data API 기반으로 즉시 재개한다.
    - 쿼리 묶음: 여행 짐, 기내수하물, 미니멀 여행, 여행 기록, 신혼여행, 부부 여행, 한달살기 등.
    - `search.list`로 후보를 넓게 모은다.
    - `videos.list`로 `title/channelTitle/publishedAt/viewCount`를 채운다.
    - 2021-08-27 이후, 한국어 제목, 공개 조회수 있는 영상만 행으로 승격한다.

2. Instagram은 별도 트랙으로 분리한다.
    - 무로그인 공개 permalink 화면에서 보이는 것만 소량 검증한다.
    - 대량 수집이 필요하면 사용자 승인 후 Apify/Instaloader 로그인/브라우저 세션 중 하나를 고른다.
    - Instagram이 막혀도 YouTube 100건 표본은 독립적으로 완료한다.

3. 기존 Waiting 사유를 바꾼다.
    - 이전 blocker: YouTube와 Instagram이 모두 접근 제한으로 0건.
    - 새 판단: YouTube는 공식 API로 재개 가능, Instagram은 별도 승인 전까지 hold.

## 운영 경계

- 비밀키, 쿠키, 세션 파일, 계정 토큰은 Git에 올리지 않는다.
- 계정 쿠키나 로그인 세션을 쓰는 방식은 승인 전 자동화하지 않는다.
- 봇 제한을 피하려고 IP 회전, CAPTCHA 우회, 약관 위반 가능성이 큰 프록시를 기본 경로로 넣지 않는다.
- 공개 근거 행에는 확인시각과 canonical URL을 붙이고, 화면 수치와 API 수치가 다르면 차이를 기록한다.
