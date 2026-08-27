# Red 검증 — research-36

후속 검증 결과, YouTube 공식 Data API 수집 파일은 요구한 행 단위 필드를 충족합니다.

- 대상 파일: `artifacts/research-36/youtube-title-evidence-20260827.csv`
- 검증 행 수: 120
- 필수 필드 누락: 0
- 2021-08-27 이전 게시일: 0
- 미래 게시일: 0
- 잘못된 canonical URL: 0
- 조회수 숫자 결손: 0
- 고유 URL 수: 120
- 고유 채널 수: 109

YouTube 표본은 `search.list -> videos.list(part=snippet,statistics)` 공식 API 응답으로 제목·채널·게시일·공개 조회수를 동시에 확보했으므로, research-36의 YouTube 범위는 PASS로 본다.

다만 Instagram Reels는 여전히 0건이며, 로그인 세션·브라우저 세션·유료 API·자격증명 변경 없이 대량 수집을 성공했다고 말하면 안 됩니다.

따라서 전체 research-36 상태는 **YouTube PASS / Instagram WAITING**입니다. 다음 액션은 YouTube 120행 표본으로 제목 패턴 분석을 진행하고, Instagram은 별도 승인 전까지 보조 트랙으로 유지하는 것입니다.
