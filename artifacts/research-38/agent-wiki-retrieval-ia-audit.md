# Agent Wiki 검색·목차 IA 감사

> 대상: `agent-wiki/content/docs/`의 컴파일 문서 124개(감사 시점 `.mdx` 실측).
> 범위: 읽기 전용 감사와 권고안. Agent Wiki 파일·사이드바·배포는 변경하지 않았다.

## 결론

8×8은 원본의 사고 위치와 매핑 경계를 보존하는 **원본 지도**로 유지한다. 다만 에이전트 검색의 주 진입점으로는 부족하다. 중앙 목차에 과업 언어의 진입층을 더하고, 원본 지도에는 실제 문서 링크를 연결하며, 링크·메타데이터·대표 질의를 회귀 검증하는 **2층 IA**로 보완해야 한다.

## 현재 근거

| 항목 | 관찰 | 의미 |
|---|---|---|
| 문서 | 124개 `.mdx` | intake의 133과 집계 기준이 달라 기준 고정이 필요하다. |
| 최상위 노출 | Insights, Diary, Logs, Mapped, Maintenance | 8×8은 실제 최상위 navigation이 아니라 원본 매핑 모델이다. |
| 직접 검색 | `/llms.txt`, `/llms-full.txt`, 개별 Markdown endpoint, 한글 bigram 검색 | 직접 URL·검색 retrieval은 가능하다. |
| 지도 | `mapped/source-category-map.mdx` 링크 0개 | 축 설명에서 세부 지식으로 내려가는 목차 경로가 끊긴다. |
| 메타 | title 124/124, tags 25/124, type 45/124 | facet·동의어 기반 retrieval 품질이 불균일하다. |
| 링크 | 현재 구현은 존재하지 않는 wikilink도 URL로 fallback한다. 여행 현재성 문서의 related link 2개는 실제 대상 파일 부재가 재현됐다. | build 통과가 링크 유효성을 뜻하지 않는다. 전체 미해결 수는 route-aware lint와 제외 규칙이 도입된 뒤에만 기준값으로 기록한다. |

근거 파일: `content/docs/meta.json`, `index.mdx`, `mapped/source-category-map.mdx`, `source.config.ts`, `app/api/search/route.ts`, `lib/search-tokenizer.ts`, `app/llms*.ts` routes.

## 대표 retrieval 시나리오

| 질의 | 현재 경로 | 판정 |
|---|---|---|
| 반복 실행 판단 | `/docs` → `insights/known-play-execution` | 1 hop, 통과 |
| 여행 현재성·위치 노출 | `/docs` → Insights/search → `insights/currentness-safe-travel-context` | 대상 도달은 가능하나 related 링크 2개가 실패해 확장 불가 |
| 첫 세션 온보딩 | `/docs` → `mapped/source-category-map`(링크 0) → Mapped/Integration/Marketing → search → `insights/first-session-onboarding-gates` | 2단계 초과·우회 |
| 원본 8×8의 Idea/Travel | `/docs` → source category map(축 설명만) | 세부 노드 링크 부재로 실패 |

따라서 현 상태는 `change`: 대표 질의 대부분을 목차·메타데이터·링크만으로 2단계 안에 재현한다고 말할 수 없다.

## 최소 개편안 (별도 승인 후)

1. **목적형 진입층**: 중앙 목차 첫 레이어에 5~8개 과업 언어 entry를 둔다. 예: 반복 판단, 기록의 흐름, 원본 위치, 글·콘텐츠 재료, 최근 변화/운영 상태.
2. **원본 지도층**: 8×8은 보조 설명으로 유지하고, `source-category-map`을 축 → mapped README/대표 노드 링크형 허브로 바꾼다. `blog`, `deep-knowledge`, 루트 노드는 8×8과 분리 표기한다.
3. **메타 계약**: 새 Insight·IA 허브에는 `title`, `description`, `tags` 또는 `aliases`, `type`, `status`, `updated`를 요구한다. 기존 mapped는 점진 보강한다.
4. **링크 계약**: route-aware link lint로 `[[...]]`, `/docs/...`, 상대 Markdown 링크의 존재·canonical route를 검증한다. 문서 이동은 하지 않고 additive release(목차·alias·메타)부터 한다.

## 검증·롤백 계약

- 구조 스냅샷: 문서 수, 경로, 최상위·2단계 분포 JSON과 diff.
- retrieval fixture: 8×8 각 축에서 최소 1개, 총 8개 질의에 `query → first entry → expected page → <=2 hops`를 선언한다.
- 게이트: link lint, retrieval fixture, `verify:log`, `types:check`, `lint`, production build. 배포 전후 URL smoke는 별도 승인 후 실행한다.
- 롤백: 첫 변경은 URL 이동 없이 additive로 제한한다. 경로 이동은 redirect map·route 스냅샷·즉시 revert commit을 갖춘 별도 작업으로 한다.

## 수치 재현 경계

이번 감사는 전체 wikilink 수를 정식 운영 지표로 채택하지 않는다. 과거의 단순 상대경로 정적 점검은 `logs/`·alias·root-relative route를 같은 방식으로 처리하지 않아 결과를 재현 가능한 기준값으로 쓸 수 없다. 후속 lint는 (1) 문서 유형별 포함/제외, (2) alias/root-relative/relative 규칙, (3) 존재 판정과 canonical route 판정을 명시하고 그 스크립트와 결과를 함께 보관해야 한다.

## 역할 종합

- **Planner**: 8×8과 보조 컬렉션의 경계를 보이고, 3개 이상 대표 질의를 2단계 기준으로 고정해야 한다.
- **Developer**: 검색 endpoint는 존재하나 지도 링크·link resolution·메타 통일이 빠져 있다.
- **Marketer**: 사용자는 분류명이 아니라 “무엇을 다시 찾거나 결정하는가”로 진입하므로 내부 레이어명보다 목적 언어를 먼저 보여야 한다.
- **Operator**: 문서 수·링크·검색·경로를 자동 검증하지 않으면 다음 변경에서 같은 주장을 재현할 수 없다.

## 지표 판정

- `metric_result`: 4개 대표 경로 중 1개만 명확히 2단계 이내. 3개는 링크 단절·검색 우회·확장 실패가 있다.
- `metric_next_decision`: `change` — Agent Wiki 변경 권한이 생기면 additive 2층 IA와 검증 게이트를 별도 Intent로 구현한다.
- `follow_up_intent_ids`: `[]` — 변경은 별도 승인 경계이며, 충분히 구체화된 구현 범위는 위 최소 개편안에 보존했다.
