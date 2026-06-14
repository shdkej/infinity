# INTENTS.md Archive 복원 필요

생성: 2026-06-14T13:30Z  
사유: cloud heartbeat에서 INTENTS.md push 시 Archive 섹션이 절삭됨

## 현재 상태

- INTENTS.md의 `## Inbox`, `## Active`, `## Waiting` 섹션: 정상
- INTENTS.md의 `## Archive` 섹션: 5개 항목만 남음 (marketing-59, 58, 57, 56, build-09)
- 누락된 항목 수: 약 77개 (build-08, marketing-55 이하 전부)
- 개별 archive 파일 (`intents/archive/*.md`): 정상 (모두 그대로 존재)

## 수정 방법

로컬에서 다음 중 하나를 실행:

### 방법 A: git으로 이전 버전 복원 후 재편집
```bash
# 이전 정상 커밋에서 INTENTS.md 체크아웃
git show 32590cc0448b4a681aa2c5e3a1887a1ee1b19f45:INTENTS.md > /tmp/intents_original.md

# 수정할 내용:
# 1. ## Inbox 에서 marketing-59 inbox 주석 제거 (이미 Archive로 이동됨)
# 2. ## Archive 상단에 marketing-59 completed 항목 추가:
#    <!-- marketing-59 completed 2026-06-14T13:00Z → intents/archive/marketing-59.md 
#    [display: Virtue Launch-Ready PLG Signal Gate; projects: virtue; type: strategy;
#    topics: plg,activation,measurement,prelaunch]
#    (PLG 신호 위계를 Virtue prelaunch 3열 게이트로 번역. 지금 볼 신호/보류할 신호/launch
#    이후 볼 신호 표와 first-10 수기 review checklist 완성. J1/J2/J4=`deed_saved`,
#    J3=`deed_judged` 유지. 선행 marketing-55/56/58 충돌 없음.
#    신규 이벤트·tracking/privacy·dashboard·public copy·deploy·external message·cost 변경 0.) -->
```

### 방법 B: intents/archive/ 디렉토리에서 재구성

`intents/archive/*.md` 파일들은 모두 정상이므로, 각 파일의 id/status/completed_at/result_summary를 읽어서 Archive 섹션을 재구성할 수 있습니다.

## 확인 후 이 파일 삭제

INTENTS.md Archive 복원 완료 후 이 파일(`INTENTS_REPAIR_NOTE.md`)을 삭제하세요.
