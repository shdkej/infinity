# ops-16 카드뉴스 published 재현성 게이트 고정

- id: ops-16
- status: archived
- completed_at: 2026-07-18T00:07
- projects: [openclaw, infinity]
- task_type: maintenance
- topics: [content, workflow, automation]
- approval: agent-approved L2
- result_summary: 카드뉴스 library의 published 항목이 untracked `local_config` 또는 같은 slug의 `source-assets`를 참조하면 빌드가 실패하도록 재현성 게이트를 추가했다.
- artifacts:
  - path: /home/ubuntu/.openclaw/workspace/system/scripts/build_card_news_library.py
    role: implementation
    note: published local input boundary gate
- reports:
  - path: reports/ops-16/20260718T0007Z.html
    role: final
- commits:
  - repo: openclaw-workspace
    sha: c71ac09
    note: 카드뉴스 library 빌더 경계 검사
  - repo: infinity
    sha: be90d1f
    note: ops-16 archive/report
- urls: []
- next_actions:
  - No continuation. 다음 publish 실행에서 gate가 실패하면 해당 템플릿/source-assets를 tracked 정본으로 승격하거나 ignored runtime/external store 경계로 명시한 뒤 다시 빌드한다.

## Summary

`system/docs/EVALUATION_NOTES.md`의 golden-eagle 및 prague 반복 사례를 기준으로 `build_card_news_library.py`에 publish boundary validation을 추가했다. 검사는 published item의 `local_config`와, 존재하는 경우 `system/data/card-news/source-assets/{config-stem}`를 대상으로 한다. 각 입력은 git tracked 또는 ignored 상태여야 하며, untracked이면 빌드를 중단한다.

## Verification

- `python3 -m py_compile system/scripts/build_card_news_library.py` 통과
- `python3 system/scripts/build_card_news_library.py --data system/data/card-news/library/items.json --out /tmp/card-news-library-test.html` 실패 확인
- 실패 항목: `czech-walk-prague-2026-07-16`, `ai-news-golden-eagle-2026-07-16`, `ai-feedback-loop-2026-07-15`, `cologne-insight-2026-07-14`의 untracked local input
