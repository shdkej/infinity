# ops-05 카드뉴스 중간 산출물 경계 고정

- id: ops-05
- status: active
- priority: medium
- permission: L2 (agent-approvable after local state verification)
- goal: 카드뉴스 생성 흐름에서 정본 config/library/최종 asset과 ignored run/cache 산출물을 분리하는 .gitignore 규칙 또는 검증 스크립트를 보강한다
- success_criteria: 새 카드뉴스 실행 후 git status에 추적 대상 정본 파일만 남고, 실험 preview/sample/중간 config는 ignored 또는 명시적 tracked asset 경로에만 존재한다
- context: system/docs/EVALUATION_NOTES.md#카드뉴스-산출물-경계 (OpenClaw workspace)
- source: Inbox (sam-proposer)
- added_to_active: 2026-07-05T0600Z
- projects: [openclaw, knowledge-lab, infinity]
- task_type: maintenance
- topics: [automation, content, workflow]

## 현재 상태

Cloud prepare 완료 (2026-07-05T0600Z). 로컬 실행 대기.

## 문제 구조

카드뉴스 생성 시 아래 2종류 파일이 생성된다:

| 종류 | 예시 | 처리 방향 |
|------|------|----------|
| 정본 | config library, 최종 JPG/WebP asset | git track |
| 실험/run/cache | preview 이미지, sample 렌더, 중간 config 초안 | ignored 또는 별도 경로 |

이 둘이 같은 경로에 쌓여 `git status`가 불필요한 파일을 노출하고 검토 경계가 흐려진다.

## 해결 후보

**방향 A — .gitignore 패턴 보강 (권장 1차 시도)**
- 카드뉴스 디렉토리에 preview/sample/cache 패턴 추가
- 예: `**/preview-*.jpg`, `**/sample-*.webp`, `**/.card-cache/`
- 장점: 간단, reversible (git rm --cached 로 되돌림 가능)
- 단점: 정본과 preview 이름 패턴이 겹치면 정본도 무시될 수 있음 → 검증 필수

**방향 B — 생성 스크립트 수정으로 run/cache 디렉토리 격리**
- 생성 스크립트가 preview/sample을 `.card-cache/` 또는 `tmp/` 하위에 쓰도록 변경
- 장점: 경계가 명확함, .gitignore 패턴 충돌 없음
- 단점: 스크립트 수정 필요, 기존 파일 이동 작업 동반

## 다음 액션 (로컬 실행)

1. `system/docs/EVALUATION_NOTES.md#카드뉴스-산출물-경계` 원문 읽기
2. 카드뉴스 생성 디렉토리 구조 확인 (`ls -la` 또는 `find . -name '*.jpg' -o -name '*.webp'`)
3. 현재 `.gitignore` 내용 확인
4. 방향 A/B 선택 → 구현
5. 테스트 카드뉴스 실행 후 `git status --short`로 검증
6. 성공 기준: preview/sample/중간 config가 git status에 나타나지 않아야 함

## 로컬 실행 프롬프트

```
Infinity Intent: ops-05 카드뉴스 중간 산출물 경계 고정
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; fall back to bounded `claude --dangerously-skip-permissions -p` if no usable pane.
Workflow: Direct execution acceptable (single-scope boundary fix). Use workflow-master only if multiple files need coordinated changes.
Goal: 카드뉴스 생성 흐름에서 정본과 run/cache 산출물을 분리하는 .gitignore 규칙 또는 생성 스크립트 보강
Context:
  - system/docs/EVALUATION_NOTES.md#카드뉴스-산출물-경계 (문제 정의 원천, 먼저 읽기)
  - 카드뉴스 생성 스크립트/디렉토리 (현재 구조 확인 필요)
Prepared findings:
  - 문제: 카드뉴스 실행 시 preview/sample 이미지, 중간 config가 정본 library 경로에 쌓여 git status 검토 경계를 흐림
  - 방향 A (권장 1차): .gitignore에 preview/sample/* 패턴 추가
  - 방향 B (대안): 생성 스크립트가 run/cache를 별도 디렉토리(예: .card-cache/)에 쓰도록 변경
  - 검증 명령: 카드뉴스 실행 후 `git status --short`에 정본 파일만 표시되는지 확인
Allowed: L0/L1 actions, L2 agent-approvable (.gitignore 보강은 reversible)
Forbidden: 정본 library 파일 삭제, production 환경 변경
Verification: `git status --short` 실행 후 preview/sample/중간 config 파일이 untracked로 나타나지 않아야 함
Report back to: reports/ops-05/{timestamp}.html (HTML format, 결론 2축 필수)
```
