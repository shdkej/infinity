# ops-09 로컬 실행 프롬프트

**Infinity Intent**: ops-09 — 데일리 리뷰 Calendar Result 렌더 게이트 보강  
**Mode**: execute_local  
**Approval**: agent-approved L2 (2026-07-10T00:13Z)

---

## Goal

`LOCAL_REVIEW_AUTOMATION.md`의 렌더 게이트에 `## Calendar Result` 영어 헤더 차단 규칙과 `both`/`all_day` 등 raw status placeholder → 한국어 변환 규칙을 추가한다.

## Context

- **대상 파일**: `/home/ubuntu/.openclaw/workspace/system/docs/LOCAL_REVIEW_AUTOMATION.md`
- **문제**: 2026-07-08·09 데일리 리뷰에서 `## Calendar Result` 영어 헤더와 `both` raw placeholder 재현
- **기존 게이트 (ops-03)**: `중복 게이트`, `확인 소스`, `소스 한계`, `## 중복`, `## 소스` 패턴만 차단 — Calendar Result 계열 미포함
- **참조 리포트**: `infinity/reports/ops-09/20260709T0700Z-prepare.html`

## Implementation

### Candidate A — LOCAL_REVIEW_AUTOMATION.md 렌더 게이트 규칙 추가

`/home/ubuntu/.openclaw/workspace/system/docs/LOCAL_REVIEW_AUTOMATION.md`의 저장/발송 직전 렌더 게이트 항목(section 7 또는 "렌더 게이트" 블록)을 찾아 아래 규칙을 추가:

```
렌더 게이트 추가 규칙:
- `## Calendar Result` 헤더가 존재하면 해당 블록 제거 또는 `## 캘린더 반영 결과` 로 변환
- 캘린더 status raw 값(both, all_day, confirmed, tentative 등)이 사용자 문장에 그대로 노출되면 저장·발송 보류
```

### Candidate B — 캘린더 연동 스크립트 status 한국어 매핑 추가

캘린더 연동 관련 스크립트(`.openclaw/workspace` 하위 calendar 관련 스크립트)를 찾아 status 값 한국어 매핑 추가:

| raw 값       | 한국어 변환       |
|-------------|-----------------|
| `both`      | `오늘·내일 모두`  |
| `all_day`   | `종일`           |
| `confirmed` | `확정`           |
| `tentative` | `미확정`         |

## Verification

구현 후 데일리 리뷰 dry-run 실행:
```bash
# openclaw workspace에서 dry-run 스크립트 실행 (경로는 실제 환경 확인 필요)
# 결과에 다음 패턴이 없으면 통과:
# - "## Calendar Result"
# - "both" (단독 사용)
# - "all_day"
```

## Allowed / Forbidden

- Allowed: L0/L1 범위 파일 수정, 커밋, 테스트
- Forbidden: L2/L3 액션(force push, 프로덕션 변경, 타인 알림 등)

## Report Back

완료 후 결과를 `infinity/reports/ops-09/{timestamp}.html`로 작성.  
HTML report 게이트: `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 존재 확인 필수.
