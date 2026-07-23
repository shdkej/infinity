# ops-22 카드뉴스 publish 최종 stage 게이트 보강

- status: archived
- completed_at: 2026-07-23T07:40Z
- projects: openclaw,infinity
- type: maintenance
- topics: card-news,workflow,git
- source_signal: system/docs/EVALUATION_NOTES.md#카드뉴스-library-데이터와-공개-HTML-staging-분리+부다페스트-night-red-team-반영분의-staged/unstaged-분리
- report: reports/ops-22/20260723T0740Z.html

## Outcome

`system/scripts/build_card_news_library.py`에 `--check-stage` 옵션을 추가했다. commit/push 직전 카드뉴스 publish 변경이 staged/unstaged로 갈라졌는지 검사한다.

차단 조건:

- `items.json`이 staged인데 공개 HTML이 unstaged
- 같은 카드뉴스 template slug가 staged/unstaged에 동시에 존재
- `items.json` 자체가 staged/unstaged에 동시에 존재

`insight-card-maker` 스킬의 라이브러리 발행 단계와 체크리스트에도 이 게이트를 추가했다.

## Verification

- 현재 Budapest 카드뉴스 split 상태에서 `python3 system/scripts/build_card_news_library.py --check-stage`가 실패
- 실패 메시지가 공개 HTML unstaged, `budapest-night-2026-07-21` mixed slug, `items.json` mixed 상태를 직접 지목

