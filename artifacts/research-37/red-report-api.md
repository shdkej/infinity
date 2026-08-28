# Red 검증 — research-37 YouTube API 재수집

1. 방향은 맞다. 사용자가 지적한 RSS 최신 15개 한계를 공식 YouTube Data API `search.list(order=viewCount, channelId) -> videos.list(part=snippet,statistics)` 경로로 다시 확인했다.
2. 다음 액션이 있다. 하루다씀은 API 기준 상위 50개에서도 10만+ 영상이 없으므로, `10만+ 없음`으로 두고 3채널 비교로 전환할지 대체 채널을 받을지 결정해야 한다.
3. 선택은 맞다. 비공식 스크래핑·로그인·쿠키·봇 제한 우회를 쓰지 않고, 제목·게시일·공개 조회수·canonical URL이 같은 API 응답에서 확인되는 행만 승격했다.
4. 요청과는 부분 일치다. 플팽부부 4개, 시칠리안 85개, 신디와쏭 18개는 충족했지만 하루다씀은 0개라 `4개 채널 모두 10만+` 완결 기준은 아직 미충족이다.

**Red verdict: CHANGE / WAITING**

- validator: SAM direct evidence gate
- checked_at: 2026-08-28T21:08Z
- red_status: waiting
