# Threads 조회 가능성 확인 — research-36

- checked_at_utc: 2026-08-27T11:15Z
- scope: Threads 공개 게시물/프로필 조회 가능성
- decision: official-possible-token-required

## 결론

Threads도 조회는 가능하다. 다만 YouTube처럼 이 머신에서 바로 대량 수집을 돌릴 수 있는 상태는 아니다.

공식 경로는 Meta Threads API의 검색/조회 엔드포인트다. 공개 게시물은 `keyword_search` 계열로 키워드·토픽 태그 검색이 가능하고, 공개 프로필 게시물은 `profile_posts?username=...` 계열로 조회할 수 있다. 2026-04-14 Meta 개발자 블로그 기준으로는 공개 게시물을 media type 또는 author username으로 검색하는 기능도 추가됐다.

현재 로컬 환경에는 `THREADS`, `META`, `FACEBOOK` 계열 토큰이 없어서 실제 API 호출 smoke test는 하지 않았다.

## 공식 경로

1. Threads Keyword and Topic Tag Search
    - URL: https://developers.facebook.com/documentation/threads/keyword-search
    - 기능: 공개 Threads 게시물을 키워드/토픽 태그로 검색.
    - 확인 포인트: `GET /keyword_search`, `media_type` 필터.

2. Threads Retrieve User Posts
    - URL: https://developers.facebook.com/documentation/threads/retrieve-and-discover-posts/retrieve-posts
    - 기능: 공개 프로필의 게시물을 `username` 기준으로 조회.
    - 확인 포인트: `GET /profile_posts?username=...`.

3. Threads API 2026 업데이트
    - URL: https://developers.facebook.com/blog/post/2026/04/14/whats-new-in-the-threads-api/
    - 기능: 공개 게시물 검색에서 media type, author username 필터가 추가됐고, profile discovery follower threshold가 100으로 낮아졌다고 공지.

## 로컬 준비 상태

- `env | rg -i 'THREADS|META|FACEBOOK'`: no match
- 즉시 가능한 것: 공식 문서 기반 설계, 요청 파라미터 정의, 결과 CSV 스키마 설계
- 즉시 불가능한 것: 공식 Threads API 실제 조회, 대량 수집, 토큰 기반 smoke test

## 비공식 경로

1. browser-act Threads user posts / keyword search skill
    - URL: https://github.com/browser-act/skills/blob/main/solutions/social-listening/threads-user-posts/SKILL.md
    - 방식: Threads 웹 페이지의 SSR embedded JSON에서 공개 글과 engagement metric 추출.
    - 장점: 공식 API 토큰 없이 일부 공개 페이지를 읽을 수 있다.
    - 리스크: 지역/IP/로그인 wall에 따라 흔들리고, 안정적인 대량 수집에는 로그인 브라우저 세션이 필요할 수 있다.

2. 비공식 threads-api 클라이언트
    - URL: https://github.com/Danie1/threads-api
    - 방식: Instagram/Threads 비공식 흐름을 클라이언트화.
    - 리스크: 로그인 세션, 계정 제한, 정책 변경, 유지보수 리스크가 커서 기본 경로로 쓰지 않는다.

## research-36 적용 판단

Threads는 Instagram Reels보다 공식 조회 경로가 낫다. 그러나 현재 목표가 `제목·계정·게시일·공개 반응 수·URL`을 행 단위 근거로 저장하는 일이므로, 공식 API 토큰 없이 대량 수집을 성공으로 보고하면 안 된다.

권장 순서:

1. Meta Developer 앱과 Threads API 권한/토큰을 준비한다.
2. 키워드 5개로 공식 API smoke test를 한다.
3. 필드 완비율을 본다.
    - text/title-like first line
    - author username
    - created time
    - permalink
    - like/reply/repost/quote 또는 노출 가능한 engagement metric
4. 30행 이상 안정적으로 나오면 research-36의 `Threads` 표본으로 승격한다.

## 승인 경계

다음은 별도 승인 전까지 하지 않는다.

- Meta/Threads 앱 생성 또는 권한 변경
- 액세스 토큰 발급/저장/회전
- 로그인 브라우저 세션 사용
- 쿠키 추출
- 유료 스크래핑 API 결제
- 공개 게시/댓글/DM/팔로우

## 다음 액션

사용자가 승인하면 `Threads 공식 API smoke test`를 새 하위 작업으로 열고, 5개 키워드에서 10~30행만 먼저 확인한다. 비공식 브라우저/스크래핑 경로는 공식 API가 막힌 뒤의 보조 옵션으로 둔다.
