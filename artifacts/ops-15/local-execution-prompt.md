# Infinity Intent: ops-15 — layer-check 당일 라인 작성 경로 분리
Mode: execute_local
Invocation: Prefer the existing pt/purplemux Claude pane via `tmux -L purple`; capture first, clear stale input, send this bounded prompt once, then capture the result.

## Goal
KST 당일 23:00 이전에 아침/오후 크론 경로가 `layer-check.jsonl`에 `date == today` 라인을 추가하지 않도록 경계 코드 또는 설정을 추가한다.

## Context
- 파일: `system/data/quality-gates/layer-check.jsonl`
- Source signal: `system/docs/EVALUATION_NOTES.md#layer-check.jsonl-당일-보류-라인-최신-재현` — 문제 재현 방식과 보류 라인 판별 기준 확인
- 문제: 2026-07-13, 07-14 연속으로 아침(07:00 리캡)/오후 크론이 `date == today` 라인을 먼저 추가함
- 정책: `date == today` 라인은 KST 23:00 밤 데일리 리뷰 경로만 추가해야 함
- 예외: 어제(`date == yesterday`) 백필은 아침/오후 경로에서 허용

## Steps

### Step 1: 쓰기 경로 식별
layer-check.jsonl에 쓰는 모든 경로를 찾는다:
```bash
grep -rn "layer-check.jsonl" ~/.openclaw/workspace/ \
  --include="*.sh" --include="*.py" --include="*.md" \
  --include="*.json" --include="*.yaml" -l
```
각 경로가 언제 실행되는지(크론 시간, 호출 맥락) 확인한다.
EVALUATION_NOTES.md의 해당 섹션도 읽어 실제 보류 라인 재현 맥락을 파악한다.

### Step 2: 호출자 기반 가드 추가 (방법 B 우선)
아침/오후 경로와 밤 리뷰 경로를 구분하는 방식:

**방법 B — 환경변수/플래그 기반 (권장)**
- 밤 데일리 리뷰 크론에만 `LAYER_CHECK_NIGHTLY=1` 환경변수 추가
- layer-check.jsonl 쓰기 직전: `if date == today and not os.environ.get('LAYER_CHECK_NIGHTLY'): skip`
- 또는 헬퍼 함수에 `allow_today` 파라미터 추가

**방법 A — 시간 기반 (대안)**
- KST 시간이 22:30 이전이면 `date == today` 라인 skip
- `from datetime import datetime, timezone, timedelta; kst = datetime.now(timezone(timedelta(hours=9)))`

방법 B가 더 명확한 역할 분리를 제공하므로 우선 시도한다. 코드 구조상 어려우면 방법 A로 전환.

### Step 3: 어제 백필 경로 보존
`date == yesterday` 라인을 쓰는 백필 경로는 수정하지 않는다.

### Step 4: Dry-run 검증
```bash
# 아침 경로 mock 실행 — layer-check.jsonl 변경 없어야 함
DRY_RUN=1 <morning-script-path> 2>&1 | grep -i layer-check

# 밤 리뷰 경로 mock 실행 — today 라인 추가되어야 함  
LAYER_CHECK_NIGHTLY=1 DRY_RUN=1 <nightly-review-path> 2>&1 | grep -i layer-check

# 현재 layer-check.jsonl에서 오늘 날짜 라인 수 확인
today=$(date +%Y-%m-%d)
grep "\"date\":\"$today\"" ~/.openclaw/workspace/system/data/quality-gates/layer-check.jsonl | wc -l
```

## Allowed
L0/L1 actions: 파일 읽기, 코드 수정, dry-run 테스트, 커밋

## Forbidden
프로덕션 직접 변경 없이 dry-run만. 어제 백필 경로 수정 금지.

## Report back to
`reports/ops-15/{timestamp}.html` (HTML report 필수)

## Verification Gate
성공 기준:
1. 아침 경로 실행 후 layer-check.jsonl에 `date == today` 라인이 새로 추가되지 않음
2. 밤 리뷰 경로 실행 후 `date == today` 라인 정상 추가
3. 어제 백필 경로 변경 없이 정상 동작
