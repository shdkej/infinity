# Infinity Artifact / Path Rules

> 의도(Intent), 산출물(Artifact), 실행 로그(Report)의 위치와 책임을 명확히 분리한다.
> 모든 Heartbeat 및 Local 실행은 이 규칙을 따르며, 완료 시 archive intent를 canonical index로 만든다.

## 디렉터리 책임

| 경로 | 역할 | 수명 |
|------|------|------|
| `intents/active/{id}.md` | 활성 Intent의 **현재 상태와 다음 액션만** | 진행 중 |
| `intents/archive/{id}.md` | 완료된 Intent의 **canonical final index** (결과 요약 + 산출물·리포트·커밋·URL 링크) | 영구 |
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

## 문서 역할 표준

Infinity 문서는 아래 3개 역할로 통일한다. 새 문서를 만들 때 이 역할을 벗어나는 `detail`, `draft`, `summary copy` 문서를 따로 만들지 않는다.

| 역할 | 경로 | 책임 | 대시보드 표시 |
|------|------|------|---------------|
| Intent 원장 | `intents/archive/{id}.md` | Intent의 최종 상태, 결과 요약, 성공 기준 충족 여부, 링크 인덱스 | `Intent 원장` |
| Artifact | `artifacts/{id}/...` | 재사용 가능한 산출물 원문. 조사 결과, 설계안, 실행 프롬프트, 데이터, 화면/HTML 등 | `Artifact` |
| Report | `reports/{id}/{timestamp}.html` | 특정 실행 1회의 HTML 로그. 무엇을 했고 무엇을 검증했는지 기록 | `Report` |

### 중복 금지

- `Intent 원장`과 `Detail`이 같은 파일을 가리키게 만들지 않는다.
- 완료된 Intent의 `detail` 링크가 필요하면 `intents/archive/{id}.md` 하나만 canonical detail로 쓴다.
- active 상태에서 임시 상세가 필요하면 `intents/active/{id}.md` 또는 `artifacts/{id}/...` 중 하나를 선택한다. 같은 내용을 둘 다 만들지 않는다.
- 대시보드/자동화는 같은 path가 `archive`와 `detail` 양쪽에서 발견되면 하나의 `Intent 원장`으로 합쳐야 한다.
- 사람이 읽는 최종 요약은 Report에만 남기지 말고 반드시 Intent 원장의 `result_summary`, `artifacts`, `reports`, `commits`, `urls`, `next_actions`에 반영한다.
- 신규 Report는 Markdown으로 만들지 않는다. 과거 `.md` report는 legacy로만 읽고, 새 실행 로그는 반드시 HTML이다.

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

기존 archive 문서(`build-01.md`, `research-06.md` 등)는 형식이 일관되지 않지만 이 패스에서는 마이그레이션하지 않는다. **신규 archive부터** 이 포맷을 따른다.

## Heartbeat가 지켜야 할 흐름

1. 실행 결과를 `reports/{id}/{timestamp}.html`로 남긴다 — 이것은 **로그**다. (양식은 아래 "Report 양식" 참고)
2. 의미 있는 산출물이 생기면 `artifacts/{id}/...`로 만든다. active intent 본문에 두지 않는다.
3. Intent가 완료되면:
   - `intents/active/{id}.md` → `intents/archive/{id}.md`로 이동
   - 위 표준 포맷으로 재작성하면서 artifacts / reports / commits / urls 링크
   - `INTENTS.md`의 Active 블록 제거, 완료 코멘트 추가 (`<!-- {id} completed YYYY-MM-DDTHH:MM → intents/archive/{id}.md [projects: virtue; type: strategy; topics: activation,analytics] (한 줄 결과) -->`)
4. 대시보드 등 외부 도구가 detail 링크를 기대하면 archive 경로가 유효한지 확인한다.
5. 완료 직후 같은 내용을 `detail` 파일로 다시 만들지 않는다. 추가 원문이 필요하면 `artifacts/{id}/...`에 별도 역할을 부여한다.

## Report 양식 (HTML, 결론 2축)

최종 보고(Report)는 **HTML로 작성**하고, **"결론 2축"을 맨 위에 큼직하게** 둔다. 상세·메타·로그는 접는다.
이 2축은 사후에 파싱하는 것이 아니라, **작업이 끝나는 순간 에이전트가 직접 도출해 채우는 산출물**이다.

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
- Claude/workflow-master 위임 작업도 같은 규칙을 따른다. 위임받은 에이전트가 코드·문서 변경은 끝냈지만 HTML report를 남기지 않았다면, Heartbeat는 직접 `reports/_TEMPLATE.html`로 관측 결과를 보강해 HTML report를 만든 뒤 완료한다.
- Markdown report만 존재하는 경우 신규 완료로 인정하지 않는다. 같은 실행에서 `.md`가 함께 생겼다면 `.html`을 final report로 archive에 연결하고 `.md`는 보조 로그로만 둔다.
- **제약**: 대시보드는 이 파일을 `iframe sandbox="allow-same-origin"` 으로 렌더하므로 **JS·외부 리소스는 동작하지 않는다.** 스타일은 인라인 `<style>` 로만, 접기는 `<details>`(JS 불필요)로 한다.
- 디자인은 **"Quiet Note"** 시스템을 따른다 — 따뜻한 본(bone) 배경(`--bg #f4f2ea`) + 저채도 단일 악센트. `_TEMPLATE.html`의 CSS는 그대로 두고 `:root`의 **`--a1`/`--a1-deep` 두 줄만 카테고리색으로 교체**한다 (축2는 항상 sage 고정):
  - 조사형(research/wiki/doc): `--a1:#5a6f8a; --a1-deep:#3f536e;` (slate-blue) — 라벨 "무엇을 조사했나 / 핵심 결과"
  - 개선형(marketing/product/dev/build/pages): `--a1:#a9745a; --a1-deep:#8a5c45;` (clay) — 라벨 "무엇이 문제였나 / 어떻게 해결하나"
  - 감시형(monitor/maintenance/router): `--a1:#b08545; --a1-deep:#8a6633;` (muted gold) — 라벨 "무엇을 점검했나 / 이상 여부·조치"
- 구조: **eyebrow(id·상태) → 제목 + dek 한 줄 → 결론 2축(좌측 컬러 라인) → `<details>` 상세 → `<details>` 메타**. JS 없이 CSS `animation-delay`로 스태거 로드.
- 같은 시점의 보고를 `.md` 와 `.html` 로 함께 두면 대시보드는 **`.html` 을 우선** 노출한다. 신규 보고는 `.html` 하나만 만든다.

> Report 는 여전히 "실행 로그"다. 2축은 그 로그의 결론을 사람이 한눈에 보게 하는 장치이며, canonical index 는 `intents/archive/{id}.md` 에 둔다는 원칙은 그대로다. 원장에도 동일한 2축(`result_summary`가 축2에 해당)을 남긴다.

## Migration Note (현 상태)

- `drafts/` → `artifacts/{id}/`로 전부 이관 완료. archive intent 참조 경로도 함께 갱신했다.
- `reports/` 하위 디렉터리는 그대로 둔다. 신규 final 결과는 reports가 아니라 archive intent + artifacts 조합으로 표현한다.
- 대시보드는 archive intent 본문과 `artifacts/{id}/` 디렉토리를 우선 로드하고, 마지막 fallback으로 reports 최신 1건을 표시한다.
