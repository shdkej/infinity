# Instagram 모바일 canvas 공개 조회 smoke test — research-36

- checked_at_utc: 2026-08-27T12:55Z
- device: OpenClaw iPhone canvas
- scope: read-only public Instagram popular/tag pages
- login_handling: user logged in manually on device; no password, 2FA code, cookie, token, or session file was read or stored
- decision: partial-access-works

## 결론

Instagram 공개 조회는 모바일 canvas 경로에서 동작한다. `#여행`, `#신혼여행` popular page에서 Reels URL, 계정명, 공개 수치, 캡션 일부를 DOM 텍스트로 추출했다.

다만 아직 research-36의 완전 행 계약에는 미달한다. 게시일이 추출되지 않았고, 일부 태그는 로그인 페이지로 튕겼다. 따라서 이번 결과는 “접근 제한으로 0건” 상태를 벗어난 smoke test로만 기록한다.

## 테스트 결과

- `#여행`
    - URL: `https://www.instagram.com/popular/%EC%97%AC%ED%96%89/?utm_source=explore_tag`
    - extracted_reels: 6
    - fields: reel URL, account, public metric, caption snippet
- `#신혼여행`
    - URL: `https://www.instagram.com/popular/%EC%8B%A0%ED%98%BC%EC%97%AC%ED%96%89/?utm_source=explore_tag`
    - extracted_reels: 6
    - fields: reel URL, account, public metric, caption snippet
- `#여행준비`
    - result: redirected to login page
    - extracted_reels: 0

## 표본

```csv
tag,account,public_metric,url,caption_snippet
여행,sujin.trip,216.3만,https://www.instagram.com/reel/DbvQgcMTprC/?utm_source=popular_topic_grid,우정 릴스와 이탈리아 여행 추억
여행,seosum,422.5만,https://www.instagram.com/reel/DZhoYeTsv_8/?utm_source=popular_topic_grid,튀르키예 여행과 다음 도시 질문
여행,sin_droms,205.5만,https://www.instagram.com/reel/Db5XlWpzH4C/?utm_source=popular_topic_grid,여름 휴가 브이로그
여행,koreago3_life,488.4만,https://www.instagram.com/reel/DbVBV9kSTz1/?utm_source=popular_topic_grid,여름방학 여행과 부산 해운대
여행,bubble__j__,928.3만,https://www.instagram.com/reel/DbShuZEvcbu/?utm_source=popular_topic_grid,나트랑 여행 릴스
여행,oneview_economy,178.1만,https://www.instagram.com/reel/DcHkL1fzF0T/?utm_source=popular_topic_grid,해외여행 시기와 도시 기준
신혼여행,yoonoh_log,161.5만,https://www.instagram.com/reel/DZ9f_UZRMIx/?utm_source=popular_topic_grid,세부 신혼여행 에피소드
신혼여행,um._.24,772.5만,https://www.instagram.com/reel/Daz2egTpUAA/?utm_source=popular_topic_grid,오키나와 커플 릴스
신혼여행,siri_sir1,109.6만,https://www.instagram.com/reel/DbQSNViI8s3/?utm_source=popular_topic_grid,라스베가스 신혼여행 에피소드
신혼여행,yepji_,43.9만,https://www.instagram.com/reel/DZm5dACNzmv/?utm_source=popular_topic_grid,오체헝 신혼여행 기록 방식
신혼여행,summer_jiin,8.4만,https://www.instagram.com/reel/DaVPrjNz-CZ/?utm_source=popular_topic_grid,탄자니아 숙소와 여행지 경험
신혼여행,eunheeis,9.4만,https://www.instagram.com/reel/DZ1og_HzEGP/?utm_source=popular_topic_grid,스위스 신혼여행 일정과 팁
```

## 품질 판정

성공:

- 모바일 canvas에서 Instagram popular/tag page 접근.
- 릴스 URL, 계정명, 공개 수치, 캡션 일부 추출.
- 로그인 정보, 쿠키, 토큰 파일 접근 없이 읽기 전용으로 확인.

미달:

- 게시일은 DOM 텍스트에서 바로 확인되지 않았다.
- 페이지별 접근성이 다르다. `#여행준비`는 로그인 페이지로 튕겼다.
- snapshot 캡처는 모바일 연결 상태에 따라 `node disconnected`가 발생해 아직 안정적이지 않다.
- 화면에는 `가입하기`, `앱 열기`가 함께 보여 로그인 세션이 완전히 적용됐는지 확정하지 않는다.

## research-36 반영

Instagram은 `WAITING`에서 `PARTIAL SMOKE PASS`로 낮은 단계 승격이 가능하다. 다만 완전 표본으로 쓰려면 게시일 또는 재현 가능한 확인 시각/URL 계약을 새로 정의해야 한다.

추천 다음 액션:

1. 인기 페이지 기준이면 게시일 요구를 제외하고 `확인시각 + 공개 metric` 표본으로 별도 분석한다.
2. 게시일이 필요하면 각 reel permalink를 개별로 열어 JSON-LD/meta/script에서 `datePublished` 계열이 잡히는지 확인한다.
3. 태그별 튕김 여부를 기록해 안정 태그 목록과 차단 태그 목록을 분리한다.
