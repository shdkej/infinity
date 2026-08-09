# Knowledge Gaps

## build-17 — 2026-08-09

- `Spatial Type / 공간형 타이포그래피 인터페이스`의 직접 정본 문서가 Knowledge Lab과 `/home/ubuntu/workspace/space`에서 확인되지 않았다.
- Status 프로젝트의 `BRAND.md`도 확인되지 않았다. 이번 구현은 요청 문맥의 `텍스트 우선`, `필요할 때 객체 호출`, `카드/패널 중심 탈피`와 기존 `DESIGN.md`·`DESIGN_SYSTEM.md`·현재 데이터 계약을 근거로 제한했다.
- 후속 보강 조건: 사용자가 Spatial Type/BRAND 정본을 제공하면 토큰·타입 스케일·컴포넌트 명명 규칙을 재대조한다.
# ops-23 · 2026-08-09

- 현재 로컬 cron snapshot(`jobs.json.migrated`)에는 dispatcher id `a409109a-b1ff-4242-9f17-1eb68e5880a0`가 없어 실제 활성 payload의 canonical path 여부를 파일만으로 확정할 수 없다. 다음 운영 점검에서 runtime cron `get` 결과를 저장해야 한다.
- source 이동 후 legacy 경로 10개는 symlink 호환 경로인지 정리 대상인지 payload별 판정이 필요하다. historical Infinity artifact의 legacy 경로는 과거 근거로 보존하되 active payload와 분리해야 한다.
- 의미 있는 daily-tracking 날짜의 얇은 diary/log pointer backfill과 ignored asset provenance gate가 후속 수정 후보로 남았다.
