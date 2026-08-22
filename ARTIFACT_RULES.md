# Infinity Artifact / Path Rules

> 의도(Intent), 산출물(Artifact), 실행 로그(Report)의 위치와 책임을 명확히 분리한다.
> 모든 Heartbeat 및 Local 실행은 이 규칙을 따르며, 완료 시 archive intent를 canonical index로 만든다.

## 디렉터리 책임

| 경로 | 역할 | 수명 |
|------|------|------|
| `intents/active/{id}.md` | 활성 Intent의 **현재 상태와 다음 액션만** | 진행 중 |
| `../archive/infinity/{id}.md` (Knowledge Lab) | 완료된 Intent의 **canonical final index** (결과 요약 + 산출물·리포트·커밋·URL 링크) | 영구 |
| `artifacts/{id}/...` | **결과로서 가치 있는 산출물** (research 결과, 설계 초안, 구현 산출물, 데이터) | 영구 |
| `reports/{id}/{timestamp}.html` | 단일 실행 로그 (heartbeat run 결과, 진행 보고) | 누적 |
| `reports/heartbeat/` | **전역** heartbeat 요약만 (intent 결과 보고서가 아님) | 누적 |

## Archive Tag Standard

Archive intent는 대시보드에서 프로젝트별/성격별로 묶어 볼 수 있도록 아래 3축 태그를 포함한다.

| 필드 | 필수 | 값 규칙 | 책임 |
|------|------|---------|------|
| `projects` | 필수 | 1~3개, controlled vocabulary | 어떤 프로젝트/제품/시스템에 걸린 일인가 |
| `task_type` | 필수 | 정확히 1개, MECE | 이 태스크의 주된 성격은 무엇인가 |
| `topics` | 선택 | 0~3개, controlled vocabulary | 보조 주제/렌즈는 무엇인가 |

### Project Tags

프로젝트 태그는 여러 개를 허용한다. 다만 한 태스크에 3개를 넘기지 않는다.

- `virtue` — Virtue / 덕 쌓기 앱, 관련 마케팅·제품·계측 문서
- `infinity` — Infinity 운영 시스템, 큐, 대시보드, 태스크 원장
- `knowledge-lab` — Knowledge Lab 원본/source/wiki 체계
- `agent-wiki` — 공개 agent-wiki 사이트, diary/publish/build 흐름
- `openclaw` — OpenClaw 런타임, 스킬, 에이전트 운영
- `infrastructure` — 서버, 배포, DNS, Kubernetes, GitHub Actions, 보안
- `personal-ops` — 회고, 생활 기록, 캘린더, 자동화된 개인 운영
- `research-bank` — 특정 실행 프로젝트에 묶이지 않는 외부 리서치/학습 자산
- `naver-shopping` — 네이버쇼핑몰/스마트스토어 수익화 에이전트, 전략, 지표, 승인 대기, 운영 라우팅

새 프로젝트 태그는 반복될 가능성이 높고 위 목록으로 표현이 어려울 때만 추가한다. 일회성 이름은 `topics` 또는 원장 본문에 남긴다.

### Task Type Tags

`task_type`은 정확히 하나만 고른다.

- `research` — 외부/내부 자료 조사, 시장·기술·사례 리서치
- `strategy` — 방향성, 포지셔닝, 기준표, 운영 원칙 수립
- `design` — UX/IA/문서 구조/시스템 설계
- `implementation` — 코드/문서/설정의 실제 생성·수정
- `verification` — 빌드, 배포, 원격 raw/page/API, 지표 확인
- `maintenance` — 정리, 마이그레이션, 깨진 상태 복구, 워크플로우 보강
- `monitoring` — 주기 점검, 알림, 상태 감시
- `coordination` — 로컬/클라우드/서브에이전트 위임과 작업 라우팅

여러 성격이 섞이면 최종 산출물의 주된 책임을 기준으로 하나만 선택한다. 예를 들어 "리서치 후 내부 브리프 작성"은 `research`, "리서치를 바탕으로 제품 기준표 확정"은 `strategy`, "깨진 자동화 수정"은 `maintenance`다.

### Topic Tags

`topics`는 보조 필터다. 최대 3개만 쓴다.

- `growth`, `marketing`, `product`, `activation`, `retention`, `analytics`
- `ai-agents`, `llm`, `wiki`, `automation`, `workflow`, `dashboard`
- `infra`, `security`, `calendar`, `review`, `finance`, `health`, `content`

`topics`는 프로젝트 태그와 중복 의미로 쓰지 않는다. 예를 들어 Virtue 마케팅 작업은 `projects: [virtue]`, `topics: [marketing]`처럼 둔다.

## 핵심 원칙

1. **Reports는 실행 로그이고 결과물이 아니다.** 동일한 결론을 두 번 찾기 위해 사람이 reports 디렉터리를 뒤져야 하면 운영 실패다. 결과는 archive intent에 요약하고, 산출물은 `artifacts/{id}/`로 옮긴다.
2. **Active intent는 짧게 유지한다.** 분석/결과를 본문에 누적하지 말고, 산출물은 `artifacts/{id}/`에 만들고 active intent에서는 참조만 한다.
3. **완료 시 archive intent가 canonical index가 된다.** 사용자가 "그래서 뭐 했더라"를 찾을 때 한 파일만 봐도 산출물 / 리포트 / 커밋 / URL 까지 한 번에 도달해야 한다.
4. **`drafts/`는 폐기.** 과거 drafts 산출물은 모두 `artifacts/{id}/`로 이동했다. 모든 신규 detail 링크는 `artifacts/{id}/` 또는 `intents/archive/{id}.md`만 가리킨다.
5. **Archive는 프로젝트 종료와 다를 수 있다.** 프로젝트성 작업은 한 intent가 설계·조사·MVP 같은 한 단계를 끝내고 Archive로 가더라도, 원래 사용자 목표가 남아 있으면 반드시 다음 intent를 `Inbox`/`Active`/`Waiting` 중 하나로 연결한다. Archive 요약에는 `next` 또는 후속 intent id를 남긴다.

## 문서 역할 표준

Infinity 문서는 아래 3개 역할로 통일한다. 새 문서를 만들 때 이 역할을 벗어나는 `detail`, `draft`, `summary copy` 문서를 따로 만들지 않는다.

| 역할 | 경로 | 책임 | 대시보드 표시 |
|------|------|------|---------------|
| Intent 원장 | `knowledge-lab/archive/infinity/{id}.md` | Intent의 최종 상태, 결과 요약, 성공 기준 충족 여부, 링크 인덱스 | `Intent 원장` |
| Artifact | `artifacts/{id}/...` | 재사용 가능한 산출물 원문. 조사 결과, 설계안, 실행 프롬프트, 데이터, 화면/HTML 등 | `Artifact` |
| Report | `reports/{id}/{timestamp}.html` | 특정 실행 1회의 HTML 로그. 무엇을 했고 무엇을 검증했는지 기록 | `Report` |

### 중복 금지

- `Intent 원장`과 `Detail`이 같은 파일을 가리키게 만들지 않는다.
- 완료된 Intent의 `detail` 링크가 필요하면 `intents/archive/{id}.md` 하나만 canonical detail로 쓴다.
- active 상태에서 임시 상세가 필요하면 `intents/active/{id}.md` 또는 `artifacts/{id}/...` 중 하나를 선택한다. 같은 내용을 둘 다 만들지 않는다.
- 대시보드/자동화는 같은 path가 `archive`와 `detail` 양쪽에서 발견되면 하나의 `Intent 원장`으로 합쳐야 한다.
- 사람이 읽는 최종 요약은 Report에만 남기지 말고 반드시 Intent 원장의 `result_summary`, `artifacts`, `reports`, `commits`, `urls`, `next_actions`에 반영한다.
- 신규 Report는 Markdown으로 만들지 않는다. 과거 `.md` report는 legacy로만 읽고, 새 실행 로그는 반드시 HTML이다.
- 프로젝트성 작업에서 `next_actions`가 "구현", "배포", "검증", "승인 후 실행"처럼 실제 후속 단계를 가리키면, 같은 turn 또는 같은 heartbeat에서 후속 intent를 만든다. 사용자가 다시 요청해야만 이어지는 상태로 두지 않는다.

## Archive Intent 표준 포맷

완료된 Intent를 archive로 옮길 때 최소 아래 필드를 포함한다.

```md
# [intent-id] 제목

- id: {intent-id}
- status: archived
- completed_at: YYYY-MM-DDTHH:MM
- projects: [virtue]
- task_type: strategy
- topics: [activation, analytics]
- result_summary: 한 줄 결과
- artifacts:
  - path: artifacts/{id}/foo.md
    role: design | research | implementation | data
    note: 짧은 설명
- reports:
  - path: reports/{id}/{timestamp}.html
    role: final | run | heartbeat
- commits:
  - repo: prompt-archive | space | ...
    sha: 894c3f8
    note: 짧은 설명
- urls:
  - url: https://...
    note: 라이브/배포 위치
- next_actions:
  - 후속 작업 / 권장 다음 Intent
```

### Archive Card 표준 템플릿

사람이 대시보드 Archive 카드만 보고도 "무엇이 끝났고, 어떤 상태이며, 어떤 기준으로 다음에 이어지는지" 알 수 있도록 신규 archive intent는 아래 블록을 포함한다. 이 블록은 `result_summary`보다 더 사용자-facing인 요약 카드이며, 대시보드와 후속 intent 자동 승격이 우선 참조한다.

```md
## Archive Card

[프로젝트]
토스 쉐어링크 Threads 테스트

[상태]
실행 준비 완료

[결과 기준]
7일간 게시물 21개 테스트

[다음 행동]
내일 첫 상품 3개 게시
```

자동화 호환을 위해 같은 내용을 아래 key 필드로도 남길 수 있다. 둘 다 있으면 `[프로젝트]` 형식의 사람이 읽는 블록을 우선한다.

```md
- archive_project: 토스 쉐어링크 Threads 테스트
- archive_state: 실행 준비 완료
- result_criteria: 7일간 게시물 21개 테스트
- next_action: 내일 첫 상품 3개 게시
- next_action_intent: marketing-123
```

`next_action`이 비어 있지 않고 `없음`, `완료`, `no continuation`이 아니면 Heartbeat는 같은 목적의 열린 intent가 있는지 확인한 뒤 후속 intent를 만든다. 공개 게시, 광고, DM/댓글, 계정 연결, 비용, 권한, 자격증명, 파괴적 변경이 포함된 다음 행동은 `Inbox` 또는 `Waiting`에 등록하되 실제 외부 실행은 사용자 승인 전까지 하지 않는다.

기존 archive 문서(`build-01.md`, `research-06.md` 등)는 형식이 일관되지 않지만 이 패스에서는 마이그레이션하지 않는다. **신규 archive부터** 이 포맷을 따른다.

### Execution Mode 기록

신규 Archive intent는 실행 방식이 검증 가능해야 한다.

- `execution_mode: single_genie_roles` — 지니가 네 역할 관점을 직접 기록한 경량 실행.
- `execution_mode: multi_subagent_roles` — Planner, Developer, Marketer, Operator가 실제 별도 서브에이전트로 실행된 중요 작업.
- `execution_mode: multi_subagent_roles_blocked` — 중요 작업이지만 역할 서브에이전트 실행이 불가능해 Waiting에 남긴 상태.
- `execution_mode: single_genie_roles_fallback_user_approved` — 중요 작업이지만 사용자가 단일 처리 fallback을 명시 승인한 상태.

`multi_subagent_roles` 완료 원장에는 `role_subagents`에 planner/developer/marketer/operator session id를 남긴다. 해당 값이 없으면 Archive 완료로 보지 않는다.

### 프로젝트 연속성 게이트

아래 중 하나라도 참이면 archive 전환 전에 후속 상태를 명시해야 한다.

- 원래 사용자 요청이 배포/사용 가능한 기능인데 현재 intent가 설계·조사·인벤토리만 완료했다.
- `next_actions`가 실제 구현/배포/검증 단계를 요구한다.
- 사용자가 "계속", "프로젝트", "CMS", "앱", "대시보드", "사이트"처럼 장기 산출물을 기대했다.
- 완료 요약에 "미구현", "approval-needed", "별도 intent" 같은 문구가 들어간다.

후속 상태는 다음 중 하나로 남긴다.

- `Active`: 다음 단계가 명확하고 안전하며 바로 진행 가능하다.
- `Inbox`: 다음 단계는 필요하지만 슬롯/우선순위 정리가 필요하다.
- `Waiting`: 사용자 결정, 외부 계정, 비용, 권한, 시크릿, 공개 발송, destructive action이 필요하다.
- `No continuation`: 원래 목표가 실제로 끝났거나 사용자가 명시적으로 중단했다.

## Heartbeat가 지켜야 할 흐름

1. 실행 결과를 `reports/{id}/{timestamp}.html`로 남긴다 — 이것은 **로그**다. (양식은 아래 "Report 양식" 참고)
2. 의미 있는 산출물이 생기면 `artifacts/{id}/...`로 만든다. active intent 본문에 두지 않는다.
3. Intent가 완료되면:
   - 원래 프로젝트 목표가 끝났는지 먼저 판정하고, 끝나지 않았으면 후속 intent id 또는 Waiting blocker를 만든다.
   - `intents/active/{id}.md` → `intents/archive/{id}.md`로 이동
   - 위 표준 포맷으로 재작성하면서 artifacts / reports / commits / urls 링크
   - `INTENTS.md`의 Active 블록 제거, 완료 코멘트 추가 (`<!-- {id} completed YYYY-MM-DDTHH:MM → intents/archive/{id}.md [projects: virtue; type: strategy; topics: activation,analytics] (한 줄 결과) -->`)
   - Archive 전환 변경을 Infinity 저장소에 commit/push하고, 대시보드가 읽는 원격 `main`에서 해당 Archive 코멘트가 보이는지 확인한다. Knowledge Lab submodule을 통해 노출되는 경우 parent pointer도 commit/push한다.
4. 대시보드 등 외부 도구가 detail 링크를 기대하면 archive 경로가 유효한지 확인한다.
5. 완료 직후 같은 내용을 `detail` 파일로 다시 만들지 않는다. 추가 원문이 필요하면 `artifacts/{id}/...`에 별도 역할을 부여한다.

## Report 양식 (HTML, 결론 2축)

최종 보고(Report)는 **HTML로 작성**하고, **"결론 2축"을 맨 위에 큼직하게** 둔다. 그 아래에는 사용자가 HTML만 열어도 핵심 내용을 바로 읽을 수 있는 본문을 둔다. 상세·메타·로그는 접는다.
이 2축은 사후에 파싱하는 것이 아니라, **작업이 끝나는 순간 에이전트가 직접 도출해 채우는 산출물**이다.

Report는 여전히 실행 로그지만, 특히 조사형(`research`, `wiki`, `doc`)은 얇은 링크 카드가 되면 실패다. 핵심 발견, 근거, 비교, 다음 판단이 HTML 안에 포함되어야 한다. Artifact는 원문/재사용 산출물이고, Report는 그 실행의 읽을 수 있는 요약 표면이다.

보고서를 쓰기 전에는 먼저 **MECE 구조**를 잡는다. 핵심 발견, 옵션, 리스크, 다음 액션은 서로 중복되지 않게 나누고, 사용자가 판단해야 할 주요 축이 빠지지 않았는지 확인한 뒤 HTML을 채운다. 예를 들어 리서치 보고서는 `문제/맥락`, `선택지`, `근거`, `제약`, `추천`, `다음 결정`이 서로 섞이지 않게 배치한다.

### 결론 2축 (필수)

모든 Report/원장은 아래 2축을 한 줄(또는 짧게)로 반드시 채운다. 작업하면서 이 두 질문의 답을 먼저 정하고 보고를 쓴다.

- **축1 = 맥락/대상/문제** — 왜 이 작업을 했나, 무엇에 대한 것인가
- **축2 = 결과/해법/발견** — 그래서 어떻게 됐나

축 라벨은 Intent id의 prefix로 작업 성격을 판별해 자동 선택한다.

| 성격 | id prefix | 축1 라벨 | 축2 라벨 |
|------|-----------|----------|----------|
| **조사형** | `research`, `wiki`, `doc` | 🔍 무엇을 조사/정리했나 | 📊 핵심 결과 |
| **개선형** | `marketing`, `product`, `dev`, `build`, `pages` | 🔴 무엇이 문제였나 | ✅ 어떻게 해결하나 |
| **감시형** | `monitor`, `maintenance`, `router` | 🟡 무엇을 점검했나 | ✅ 이상 여부·조치 |
| **범용(폴백)** | 그 외 / 분류 불가 | 무엇을 했나 | 결과 |

새 카테고리가 생기면 가장 가까운 성격에 매핑하고, 애매하면 범용 라벨을 쓴다.

### 작성 규칙

- 위치: `reports/{id}/{timestamp}.html`
- 템플릿: `reports/_TEMPLATE.html` 을 복사해 `{{...}}` 자리표시자를 치환한다. (`_`로 시작하는 파일은 대시보드가 무시한다)
- 완료 게이트: `reports/{id}/{timestamp}.html` 파일이 실제로 존재하고 비어 있지 않으며, `<html`, `<body`, `axis ax1`, `axis ax2`, `<details`를 포함해야 한다. 이 검증 없이 완료 처리하지 않는다.
- 연구형 Report는 `핵심 내용 · 리서치 본문` 영역을 반드시 채운다. 최소 3개, 가능하면 5~7개의 핵심 발견을 쓰고, 각 발견은 사용자가 다음 결정을 할 수 있을 만큼 구체적이어야 한다.
- 핵심 발견과 옵션 비교는 MECE하게 쓴다. 같은 발견을 표현만 바꿔 반복하지 말고, 비용/속도/품질/리스크/실행 난이도처럼 서로 다른 판단 축으로 나눈다.
- 연구형 Report에는 반드시 `근거 · 소스`, `다음 판단`, 필요 시 `옵션 비교` 또는 `추천안`이 들어간다. "자세한 내용은 artifact 참고"만으로 끝내지 않는다.
- 긴 표는 모바일에서 좌우 스크롤을 요구하지 않게 2열 이하로 줄이거나, 항목형 카드/목록으로 바꾼다. URL, 코드, 파일 경로, 긴 단어는 줄바꿈되게 작성한다.
- Claude/workflow-master 위임 작업도 같은 규칙을 따른다. 위임받은 에이전트가 코드·문서 변경은 끝냈지만 HTML report를 남기지 않았다면, Heartbeat는 직접 `reports/_TEMPLATE.html`로 관측 결과를 보강해 HTML report를 만든 뒤 완료한다.
- Markdown report만 존재하는 경우 신규 완료로 인정하지 않는다. 같은 실행에서 `.md`가 함께 생겼다면 `.html`을 final report로 archive에 연결하고 `.md`는 보조 로그로만 둔다.
- **제약**: 대시보드는 이 파일을 `iframe sandbox="allow-same-origin"` 으로 렌더하므로 **JS·외부 리소스는 동작하지 않는다.** 스타일은 인라인 `<style>` 로만, 접기는 `<details>`(JS 불필요)로 한다.
- 모바일 기준은 390px 폭이다. 브라우저 검증이 가능하면 `document.documentElement.scrollWidth <= window.innerWidth`를 확인하고, 어렵다면 템플릿 CSS의 `overflow-x:hidden`, 긴 텍스트 wrapping, 모바일 테이블 stacking 규칙을 깨지 않았는지 눈으로 확인한다.
- 디자인은 **"Quiet Note"** 시스템을 따른다 — 따뜻한 본(bone) 배경(`--bg #f4f2ea`) + 저채도 단일 악센트. `_TEMPLATE.html`의 CSS는 그대로 두고 `:root`의 **`--a1`/`--a1-deep` 두 줄만 카테고리색으로 교체**한다 (축2는 항상 sage 고정):
  - 조사형(research/wiki/doc): `--a1:#5a6f8a; --a1-deep:#3f536e;` (slate-blue) — 라벨 "무엇을 조사했나 / 핵심 결과"
  - 개선형(marketing/product/dev/build/pages): `--a1:#a9745a; --a1-deep:#8a5c45;` (clay) — 라벨 "무엇이 문제였나 / 어떻게 해결하나"
  - 감시형(monitor/maintenance/router): `--a1:#b08545; --a1-deep:#8a6633;` (muted gold) — 라벨 "무엇을 점검했나 / 이상 여부·조치"
- 구조: **eyebrow(id·상태) → 제목 + dek 한 줄 → 결론 2축(좌측 컬러 라인) → `<details open>` 핵심 내용 → `<details open>` 상세 → `<details>` 메타**. JS 없이 CSS `animation-delay`로 스태거 로드.
- 같은 시점의 보고를 `.md` 와 `.html` 로 함께 두면 대시보드는 **`.html` 을 우선** 노출한다. 신규 보고는 `.html` 하나만 만든다.

> Report 는 여전히 "실행 로그"다. 2축은 그 로그의 결론을 사람이 한눈에 보게 하는 장치이며, canonical index 는 `intents/archive/{id}.md` 에 둔다는 원칙은 그대로다. 원장에도 동일한 2축(`result_summary`가 축2에 해당)을 남긴다.

## Migration Note (현 상태)

- `drafts/` → `artifacts/{id}/`로 전부 이관 완료. archive intent 참조 경로도 함께 갱신했다.
- `reports/` 하위 디렉터리는 그대로 둔다. 신규 final 결과는 reports가 아니라 archive intent + artifacts 조합으로 표현한다.
- 대시보드는 archive intent 본문과 `artifacts/{id}/` 디렉토리를 우선 로드하고, 마지막 fallback으로 reports 최신 1건을 표시한다.
