# Keyword API integration — 2026-11-13

Goal: keyword-title 스킬의 Naver SearchAd API를 Reel Room 서버에서 직접 호출하고 AI 없이 실제 연관어·월간 검색량을 선택·저장한다.
Architecture: web/studio_keywords.py (credential/signing/provider/measurement normalization); studio.py adds an independent capability and persisted project endpoint; KeywordResearch.tsx renders editable seeds and selectable measured results. OpenAI requests remain optional and separate.
Source: prompt-archive/skills/keyword-title/{SKILL.md,references/inflow.md,scripts/searchad_keyword.py}; actual existing credential call returned 58 rows for 세계여행. Existing product Context Pack is reused and extended, not a new Intent.
Constraints: preserve human script/hooks/assets; no paid AI validation; server-only existing skill credentials; scoped commit/push master; existing approved production Deployment only; preserve unrelated work.

- [x] TDD: assert endpoint works with no OpenAI key; normalizes multiple seeds, preserves <10 and unknown counts, source/time, and saved research after later edits/reopen. Reject missing/invalid queries; safe missing credential, upstream timeout/429/malformed responses. Mock only external HTTP.
- [x] Implement Naver signature and bounded direct request, independent capability/limiter, preserve server-owned research. No LLM fallback.
- [x] UI seed entry (comma-separated up to 5), measured results before optional AI section, selectable keywords, responsive metrics/source/time/empty/error states. Query state belongs to project view.
- [x] Full pytest, UI build/lint, browser 375/768/1440, real public keyword lookup with OpenAI absent; review. Commit/push intended files.
- [x] Build image; add only 3 Naver credential keys to existing server Secret in memory (never logs/git), secret refs + pinned image in Space manifest. Dry-run/publish/apply/rollout/live test, old data persistence.
- [x] Record exact evidence and AI deferral in Infinity and KL; verify scoped remote HEADs.

Review focus: unbounded counts must not become fake exact totals; old client PUT must not erase measurements; empty results retain honest source; invalid/expired API keys never expose raw provider messages; no OpenAI dependency for lookup or button availability.

## User followup (same authorized integration)
- Add easy image/video reference discovery: selected keyword/topic query chips, image/video + provider filters, in-app image/video preview, original page and import/save actions, external search shortcuts. Reuse existing YouTube API from keyword-title skill through server Secret; no OpenAI needed.
- Add user-entered OpenAI key in UI: current tab memory only, explicit clear, no localStorage/sessionStorage/project/env mutation. Only AI POST requests send an X-OpenAI-API-Key header over same origin; provider receives per-call key. Configuration presence is not authentication validation. No paid validation calls.
- Reviewer found first keyword search draft remount loses query. Hoist draft query to Studio, reset only on explicit project switch; verify first save and failed query retain text.

Completion: source f8d5ede, production revision 74, 212 tests, live Naver/YouTube/Commons and browser checks, 14 files unchanged. Review fix verified. Paid AI validation remains deferred.
