# ops-17 카드뉴스 published 원본 자산 재현성 게이트 고정

- id: ops-17
- status: archived
- completed_at: 2026-07-18T22:03
- projects: [openclaw, infinity]
- task_type: verification
- topics: [content, workflow, automation]
- result_summary: 카드뉴스 라이브러리 빌드가 published 항목의 untracked local_config와 source_assets를 모두 차단하는 것을 프라하/쾰른 사례로 확인했다.
- artifacts: []
- reports:
  - path: reports/ops-17/20260718T2203Z.html
    role: final
- commits: []
- urls: []
- next_actions:
  - No continuation.

## Result

`python3 system/scripts/build_card_news_library.py --out /tmp/card-library-test.html` dry-run은 렌더/다운로드 전에 재현성 게이트에서 실패했다. 실패 목록에는 `czech-walk-prague-2026-07-16`과 `cologne-insight-2026-07-14`의 `local_config`뿐 아니라 `source_assets` 경로도 포함됐다.

따라서 최근 평가 노트가 요구한 "untracked source-assets를 참조한 채 published로 닫히는 경로 차단"은 현재 빌드 게이트에서 확인됐다.
