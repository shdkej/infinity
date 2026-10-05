# Planner
- 목표: 기존 Knowledge Lab dirty 변경을 보존하면서 checkpoint 대상만 targeted commit/push하는 실행 경로를 고정한다.
- 완료 기준: exact-path staging, non-force push, local/origin SHA 일치, scheduled 2회 검증.
- 범위: proposer job/payload 경로 식별과 read-only 검증까지. job이 노출되지 않으면 정확한 외부 artifact blocker로 Waiting.
- 근거: `source/openclaw-system/docs/INFINITY_OPERATING_RULES.md`, `source/openclaw-system/docs/OPENCLAW_RUNTIME_MAINTENANCE.md`, `source/openclaw-system/docs/SIGNAL_TO_INTENT_PROPOSER.md`.
