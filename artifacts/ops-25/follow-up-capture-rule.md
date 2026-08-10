# ops-25 후속 intent 자동 등록 계약

- intent: `ops-25`
- status: archived after implementation and Red validation
- source evidence: `agent-wiki/content/docs/mapped/Meta/AGENTS.mdx`, `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md`, `infinity/workflows/heartbeat.md`, `infinity/ARTIFACT_RULES.md`, `infinity/EVALUATION_INDEX.md`

## Planner

목표는 완료·감사 report에서 이미 드러난 실행 가능한 다음 일을 사용자 재지시 없이 보존하는 것이다. 범위는 Infinity 운영 규칙과 heartbeat pickup 계약이며, 새 서비스·새 알림 경로·외부 발송은 제외한다. 완료 기준은 자동 등록/승인 대기/등록 보류의 경계, 근거 게이트, 중복 방지, 필수 intent 필드, report 필드, lane 재검증이 정본 문서에 남는 것이다.

## Developer

호출면은 `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md`와 `infinity/workflows/heartbeat.md`다. `INTENTS.md`에는 ops-25를 `target_agent: genie`, `status: active`로 구조화하고 `projects`, `task_type`, `topics`, `priority`, `permission`, `goal`, `success_criteria`, `next_action`을 기록했다. 실제 변경은 두 canonical 문서와 원장에 한정했다. 검증은 `python3 scripts/check_intents_consistency.py` 및 파일 재검색으로 수행한다.

## Marketer

해당 없음(사용자-facing 카피·외부 발행 작업이 아님). 다만 사용자에게 보이는 상태를 오염시키지 않도록 후속 intent 등록 자체는 Telegram 알림 대상에서 제외하고, 승인 필요·실패·실제 완료만 기존 알림 경계를 따르도록 규칙에 명시했다.

## Operator

실행은 로컬 문서/원장 변경으로 제한했다. 구현·배포·외부 발송·파괴적 작업·자격증명·권한 변경·비용이 필요한 후속은 Inbox에 등록하되 `permission: user-approval` 또는 gate를 적고 실행하지 않는다. 의미 있는 변경은 Infinity 저장소와 상위 Knowledge Lab의 원격 가시성 게이트를 통과해야 한다. 기존 dirty worktree의 무관한 변경은 건드리지 않는다.

## 지니 종합 판단

역할 합의는 “후속을 별도 intent로 보존하되 실행 권한은 원래대로 분리한다”이다. Planner의 범위와 Developer의 두 canonical 문서 변경을 채택했고, Operator의 승인 경계를 추가했다. Marketer의 직접 산출물 없음 판단은 채택하되 사용자-facing 침묵 규칙으로 반영했다. 기각안은 (1) 새 proposer/daemon을 만드는 것, (2) 완료한 intent를 재활성화하는 것, (3) 후속을 report 링크만으로 남기는 것이다. 최종 순서는 원장 구조화 → 운영 규칙 반영 → heartbeat pickup 계약 반영 → 정합성/HTML/Red 검증 → 원격 push다.

## 계약 요약

1. 근거 신호·기대 산출물·판정 가능한 완료 기준을 모두 채울 때만 자동 등록한다.
2. 동일 목적의 Inbox/Active/Waiting이 있으면 새 id를 만들지 않고 기존 id를 연결한다.
3. 모든 새 intent는 `target_agent: genie`로 정규화한다.
4. report에 `follow_up_intent_ids`와 `follow_up_not_created_reasons`를 항상 남긴다.
5. 등록 뒤 `INTENTS.md`를 다시 읽어 원래 Inbox 제거와 새 lane을 검증한다.

## Red

- `red_status: pass`
- report: `reports/ops-25/20260810T0453Z-red.html`
- finding: ops-25 success criteria explicitly names evidence signal, expected output, judgeable completion criteria, both follow-up report fields, and post-registration lane re-read verification.
