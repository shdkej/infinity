# ops-18 카드뉴스 재사용 배경 에셋 provenance 경계 정리

- status: completed
- completed_at: 2026-07-21T06:12Z
- approved_by: user
- projects: openclaw,infinity
- type: maintenance
- topics: card-news,assets,provenance

## 결과

`steel background` 재사용 에셋의 장기 provenance를 tracked 파일 기준으로 고정했다.

## 변경

- `system/data/card-news/generated-assets/steel-background-2026-07-19/asset.json`의 `source_reference`를 tracked PNG 자체로 변경했다.
- ignored one-off run 경로는 `generation_log_reference`로 낮추고, 재사용 검증 필수 입력이 아니라고 `provenance_note`에 명시했다.
- `skills/insight-card-maker/SKILL.md`의 Reusable Internal Backgrounds에 tracked `asset.json`과 tracked PNG가 재사용 근거라는 규칙을 추가했다.

## 검증

- `python3 -m json.tool`로 asset JSON 파싱 확인.
- `git ls-files` 기준 `asset.json`과 `steel-background-wallpaper.png`가 tracked 파일임을 확인.
- ignored run 경로는 `!! system/reports/card-news/runs/20260719-steel-cover/`로 남지만 필수 `source_reference`에서 제거했다.

## 다음

새 카드뉴스 config는 reusable background의 필수 provenance로 ignored run 파일을 참조하지 않는다.
