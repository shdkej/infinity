# Local Execution Prompt: marketing-25

## Infinity Intent: marketing-25 Virtue human/test/agent 트래픽 판독 경계표

**Mode**: execute_local  
**Required workflow**: Use workflow-master first. Read and follow `.agent/workflows/workflow-master.md` or `WORKFLOW-MASTER.md` when present before doing implementation work. If workflow-master is absent, record that fact and apply 4-role lens (Planner/Developer/Marketer/Operator) manually.  
**Allowed**: L0/L1 actions + L2 agent-approved push  
**Forbidden**: L3 actions, force-push, 신규 이벤트·속성·코드·카피·계측·대시보드·배포·외부발송·비용·시크릿·권한·개인정보 변경

## Goal

`shdkej/infinity` > `artifacts/marketing-25/human-agent-traffic-boundary-table.md`의 cloud draft를 `virtue-rebirth-app/apps/web/docs/human-agent-traffic-boundary-table.md`로 복사하고 커밋·push한다.

## Context

- **Cloud draft 경로**: `shdkej/infinity` > `artifacts/marketing-25/human-agent-traffic-boundary-table.md`
- **대상 경로**: `virtue-rebirth-app/apps/web/docs/human-agent-traffic-boundary-table.md`
- **source_note** (참고용): `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-28-human-agent-onboarding-metrics.md`
- **Infinity report**: `shdkej/infinity` > `reports/marketing-25/2026-05-28T2200Z.html`

## Prepared Findings (Cloud Draft 요약)

이번 Heartbeat에서 완료한 cloud draft 내용:

1. **5가지 트래픽 유형 정의** (H/M/S/P/A): human-real-use / maker-self-test / synthetic-mock / platform-difference / future-agent-api
2. **6이벤트 × 5유형 판독 경계표** (심장 표): 각 이벤트별 유형 분류와 해석 주의사항
3. **해석 금지선 6항목**: deed_judged 수치 단정 금지, 갭 이탈 단정 금지, iOS/웹 통합 비교 금지, S/M 제거 전 비율 산출 금지, A 트래픽 H 계산 금지, 단건 확정 금지
4. **Verification Gate V1/V2/V3**: 트래픽 분류 점검 / 이벤트 해석 전 체크 / 표본 크기 확인
5. **선행 문서 5개 연결** 충돌 0 확인

## Verification (로컬 실행 후 확인)

```bash
# 1. 새 파일만 추가됐는지 확인
git diff --stat HEAD

# 2. 기존 문서와 충돌 마커 없음 확인
git grep -n '<<<<<<\|>>>>>>\|=======' -- apps/web/docs/

# 3. 필수 문자열 존재 확인
grep -c 'human-real-use\|maker-self-test\|synthetic-mock\|platform-difference\|future-agent-api' apps/web/docs/human-agent-traffic-boundary-table.md
# 기대값: 각 5회 이상

grep -c 'deed_judged\|deed_saved\|add_flow_started\|level_up_viewed\|deed_rerolled\|deed_save_capped' apps/web/docs/human-agent-traffic-boundary-table.md
# 기대값: 각 1회 이상

# 4. HEAD == origin/master 확인
git status
```

## L2 Agent-Approved 조건 확인

- [x] 목표 Intent(marketing-25)와 직접 연결
- [x] 되돌림 가능 (git revert 가능)
- [x] 예상 비용 없음
- [x] 프로덕션 데이터·권한·시크릿 변경 없음
- [x] 타인에게 새 메시지·알림 없음
- [x] 실행 전 현재 상태 확인 (git status), 실행 후 검증 방법 있음

→ **L2 agent-approved** 조건 충족. 로컬에서 자체 승인 후 진행 가능.

## Report Back

실행 완료 후:
1. `shdkej/infinity` > `reports/marketing-25/{timestamp}Z-local.html` 작성 (결론 2축 HTML)
2. `shdkej/infinity` > `INTENTS.md`: marketing-25 status를 `waiting` → archived로 변경
3. Archive 코멘트 추가: `<!-- marketing-25 completed {timestamp} → intents/archive/marketing-25.md (...) -->`
4. `intents/archive/marketing-25.md` 생성 (canonical final index)
