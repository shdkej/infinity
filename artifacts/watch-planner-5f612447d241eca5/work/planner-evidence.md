# MM-001·PC-001 채널·지표 원천 확인

확인 시각: 2026-10-25T23:35Z–23:40Z

## 확인한 근거

- `/home/ubuntu/workspace/projects/minimalmoeum/CHANNELS.md`
- `/home/ubuntu/workspace/projects/policycock/CHANNELS.md`
- 두 프로젝트의 `PROJECT.md`, `docs/INTEGRATIONS.md`, `TASKS.md`, `AGENTS.md`
- `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/agent-inbox/marketing.jsonl`
- Infinity Context Pack: `intents/context/watch-planner-5f612447d241eca5.json`
- Knowledge Lab: `agent-wiki/content/docs/outputs/Integration/Marketing.mdx`, `agent-wiki/content/docs/outputs/Communication/Document.mdx`

## 판정

| 프로젝트 | 고객 문의 채널 | 마케팅 원천 | 대시보드 경로 | 확인 결과 |
| --- | --- | --- | --- | --- |
| minimalmoeum | 미확정 | 공통 inbox `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/agent-inbox/marketing.jsonl` | 프로젝트 전용 경로 미확정 | 공통 파일은 존재하나 프로젝트 태그 신호 0건, 전용 대시보드·기간 정의 없음 |
| policycock | 미확정 | 공통 inbox `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/agent-inbox/marketing.jsonl` | 프로젝트 전용 경로 미확정 | 공통 파일은 존재하나 프로젝트 태그 신호 0건, 전용 대시보드·기간 정의 없음 |

두 프로젝트 문서의 PostHog·GA4·R2는 연결 준비 계약과 예정 이벤트 이름만 담고 있으며 실제 host, property/project ID, URL, 테스트 이벤트, 접근 가능한 dashboard는 없습니다. 따라서 이를 실제 전용 원천으로 승격하지 않았습니다.

## 역할별 판단

### Planner

범위를 고객 문의 채널, 전용 마케팅 지표 원천, 대시보드 경로, 담당, 검증 방법으로 고정했습니다. 확인되지 않은 계정·채널·대시보드는 추정하지 않습니다. 완료 기준을 충족하지 못했으므로 외부/프로젝트 원천 확보 전까지 Waiting이 맞습니다.

### Developer

로컬 문서와 공통 inbox read-only 확인만 수행했습니다. 계정 연결, 권한 부여, 시크릿 등록, 외부 API 호출은 하지 않았습니다. 현재 구현 가능한 변경은 없으며, 다음 증거는 실제 project-specific source와 dashboard URL/ID입니다.

### Marketer

프로젝트별 전용 지표가 없으면 채널별 기대와 반응을 합산해 해석할 위험이 있습니다. 최소 계약은 프로젝트 태그, 기간, 유입 채널, 대표 이벤트, 담당, 확인 주기를 분리 기록하는 것입니다.

### Operator

실제 접근 가능한 고객 문의 관리 화면과 프로젝트별 analytics workspace/property가 필요합니다. 승인 경계(계정·권한·시크릿·외부 발송)는 건드리지 않았습니다. 재개 조건은 두 프로젝트의 정확한 source path/URL/ID와 read-only 확인 권한입니다.

## 정확한 blocker

`waiting_on: external`

두 프로젝트의 고객 문의 관리 채널과 전용 마케팅 analytics 원천/대시보드가 로컬 문서·공통 inbox에 존재하지 않습니다. 프로젝트 담당자가 실제 채널·dashboard URL 또는 property/project ID·기간 정의를 제공하거나 read-only 접근 가능한 원천을 연결해야 `CHANNELS.md`에 정확히 기록하고 접근 검증을 완료할 수 있습니다. 공개 게시·계정 연결·권한 변경·시크릿 등록은 이번 작업 범위가 아닙니다.
