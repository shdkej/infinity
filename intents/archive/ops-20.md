# ops-20 media inbound staged 사진 경계 정리

- status: archived
- completed_at: 2026-07-23T07:40Z
- projects: openclaw,infinity
- type: maintenance
- topics: media,git,workflow
- source_signal: system/docs/EVALUATION_NOTES.md#media/inbound/openclaw-staged-* 원본 사진 누적 경계
- report: reports/ops-20/20260723T0740Z.html

## Outcome

`media/inbound/openclaw-staged-*`를 런타임 수신 캐시로 확정하고 `.gitignore`에 추가했다. 기존 untracked staged 폴더 3개가 `git status --short --ignored -- media/inbound`에서 `!!`로만 표시되는 것을 확인했다.

보존해야 하는 사진 원본은 기존 규칙대로 업로드 URL, daily-tracking, 카드뉴스 `source-assets` 같은 정본 경로로 승격하고, inbound staged 폴더 자체는 커밋 대상이 아니다.

## Verification

- `git status --short --ignored -- media/inbound` 결과: staged 폴더 3개가 `!!` ignored 상태
- 사용자 원본 파일 삭제 없음

