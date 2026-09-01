# wiki-ia-01 — Agent Wiki 만다라트 탐색 허브 구현

## 구현

- `mapped/source-category-map.mdx`를 생성형 8축 navigation hub로 변경했다.
- 새 축 허브 8개를 추가했다: `axes/{fundamental,deep-knowledge,integration,communication,health,human,idea,meta}.mdx`.
- 각 축 허브는 현재 core mapped 노드만 링크한다. blog·README·기타 컬렉션은 inventory와 지도 본문에서 제외했다.
- `scripts/mandalart_navigation.mjs`는 source 및 mapped 디렉터리에서 inventory를 생성하고 map·hub를 갱신한다.
- 추적 manifest `content/docs/data/mandalart-core-inventory.json`을 추가했다. CI는 raw source가 없어도 mapped↔manifest parity를 항상 실패 조건으로 검사하며, 로컬에서는 source↔manifest도 검사한다.
- `deploy.yml`은 build 전 `npm run verify:mandalart-nav`을 실행한다.

## 검증 결과

| 항목 | 결과 |
|---|---|
| 생성 검증 | 8축, source 62, mapped 62 통과 |
| CI-모드 검증 | source 미존재 환경에서 mapped↔manifest 62 통과 |
| lint | 통과 (ESLint 9.39.5로 Next 16 config 호환 정렬) |
| types | 통과 |
| Pages build | GitHub Actions run 33558827703에서 통과 |
| live route | map, Fundamental hub, 기존 Architecture URL 모두 200 |
| Red | cache-busted 렌더 screenshot으로 map/hub의 중복 H1 없음·축/노드 링크 확인, pass |

## inventory

Fundamental 8, Deep Knowledge/deep-knowledge 8, Integration 8, Communication 8, Health 7, Human 8, Idea 7, Meta 8 = **62**. 64는 하드코딩하지 않으며 새 source/mapped 쌍이 추가되면 generator와 manifest가 갱신되어야 한다.

## 롤백

기존 mapped node URL은 이동하지 않았다. 문제 시 Agent Wiki IA 관련 두 커밋만 revert하면 된다: `fa536e7`, `a357a1d`.
