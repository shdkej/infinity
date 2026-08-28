# corrected research-37 — 공개 RSS 표본 결손

수집 시각: `2026-08-28T19:29:52Z`.

| 채널 | 공식 channel ID | RSS 최신 행 | 10만+ 완전 행 | 판정 |
|---|---:|---:|---:|---|
| 플팽부부 | UCsEfn-G__mrwWwhw2cZKu6Q | 15 | 0 | 이 최신-15 RSS 창에서는 10만+ 행을 재현하지 못함 |
| 시칠리안 SICILIAN | UCchu6XLsbV9PISj5b7XArQA | 15 | 15 | 포함 |
| 하루다씀 HARUDASSEUM | UC7wGJnpnPk50yMm6Kv6lMsQ | 15 | 0 | 이 최신-15 RSS 창에서는 10만+ 행을 재현하지 못함 |
| 한달살러 신디와쏭 Shindywassong | UC1E2DOD7f4E-bfKGUr1r2jQ | 15 | 1 | 포함 |

- 출처: 각 채널의 `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>`.
- 제외 규칙: `views < 100000` 또는 필수 필드 누락인 행은 제목 비교 분모에 넣지 않았다.
- 한계: RSS는 최신 15개만 제공한다. 따라서 플팽부부·하루다씀에 10만+ 영상이 채널 전체에 없다고 결론내리지 않는다. 전체 업로드 재생목록은 공개적으로 열리지만 개별 영상 날짜·조회 수 조회는 인증 없는 접근에서 bot confirmation으로 막혀, 쿠키·로그인·우회 없이 과거 행을 검증할 수 없었다.
