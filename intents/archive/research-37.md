# research-37 여행 YouTube 4개 채널 제목 비교 조사

- id: research-37
- status: archived
- archived_at: 2026-08-30T09:12Z
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy
- requested: 2026-08-28T17:50:58Z
- scope_corrected_at: 2026-08-28T19:20:00Z
- execution_mode: multi_subagent_roles
- projects: research-bank,infinity,knowledge-lab,world-travel
- task_type: youtube-title-evidence-comparison
- topics: youtube,travel-couple,title-analysis,content-strategy
- goal: 플팽부부·시칠리안·하루다씀·신디와쏭 4개 YouTube 채널의 공개 영상 중 조회수 10만 이상 영상을 채널별로 수집하고, 제목을 비교 분석 가능한 근거 목록으로 정리한다.
- user_request: "플팽부부·시칠리안·하루다씀·신디와쏭의 10만 조회 이상 인기 영상 제목을 채널별로 수집하고, 비교 분석 가능한 목록으로 정리"
- user_closure_note: 2026-08-30 사용자가 하루다씀도 조회수 기준으로 확인했으므로 Waiting에 둘 이유가 없다고 판단했다.
- api_recheck_at: 2026-08-28T21:06:41Z
- api_source: YouTube Data API `search.list(order=viewCount, channelId) -> videos.list(part=snippet,statistics)`
- result_summary: 공식 YouTube API 기준으로 플팽부부 4개, 시칠리안 85개, 신디와쏭 18개의 10만+ 완전 행을 확보했다. 하루다씀 HARUDASSEUM은 API `order=viewCount` 기준 상위 50개 최고 조회수가 38,739회라 10만+ 행이 없음을 결론으로 채택했다.
- metric_result: 하루다씀은 `10만+ 없음`으로 포함하고, 4개 채널 모두에 대해 조회수 기준 확인 결과와 결손 사유를 명시했다. 후속 요청으로 채널별 상위 10개·하위 10개 제목 학습까지 완료했다.
- artifacts:
  - path: artifacts/research-37/four-channel-api-evidence.csv
    role: evidence
    note: 공식 YouTube API 기준 10만+ 포함 행
  - path: artifacts/research-37/four-channel-api-exclusions.csv
    role: exclusions
    note: 하루다씀 포함 10만 미만 또는 제외 행
  - path: artifacts/research-37/four-channel-api-comparison.md
    role: synthesis
    note: 4채널 API 재수집 비교와 하루다씀 10만+ 없음 결론
  - path: artifacts/research-37/channel-top-bottom-lessons-20260828.md
    role: content-strategy
    note: 각 채널 상위 10개·하위 10개 조회수 기준 제목 학습
  - path: artifacts/research-37/four-channel-api-collection-summary.json
    role: collection-summary
    note: 채널별 수집 수·중단 사유 요약
  - path: artifacts/research-37/red-report-api.md
    role: verification
    note: API 재수집 검증. 사용자 승인 후 하루다씀 결손을 완료 결론으로 전환
- reports:
  - path: reports/research-37/20260828T2108Z-youtube-api-waiting.html
    role: api-recheck
  - path: reports/research-37/20260830T0912Z-closed.md
    role: final-closure
- red_status: pass-with-user-closure
- previous_invalid_run:
  - superseded_at: 2026-08-28T19:20:00Z
  - superseded_reason: 원 요청은 4개 채널 비교였으나 첫 실행은 플팽부부 단일 채널만 다뤘다.
  - report: reports/research-37/20260828T1908Z.html
- knowledge_status: used
- knowledge_decision: retain-as-operating-principle
- knowledge_reflection: 공개 조회수 기준의 결손은 무조건 blocker가 아니라, 충분한 공식 API 확인 후에는 `조건 미충족 확인 완료`라는 결론으로 닫을 수 있다.
- next_action: 실제 여행 장면과 검증 가능한 선택 기준이 생기면 `장소명 + 선택 압력 1개 + 기대와 다른 결론` 구조로 제목 2안을 만들고 72시간 신호를 비교한다.
