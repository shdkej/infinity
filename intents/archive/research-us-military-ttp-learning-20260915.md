# 미군 TTP: 현장 학습이 조직 자산으로 변환되는 실제 메커니즘

- id: research-us-military-ttp-learning-20260915
- status: archived
- research_mode: exploratory_research
- execution_mode: single_genie_roles
- permission: L0-research-and-draft-only
- projects: infinity,research-bank
- task_type: research
- topics: workflow,automation
- context_pack: intents/context/research-us-military-ttp-learning-20260915.json
- trace: traces/research-us-military-ttp-learning-20260915.json
- final_artifact: artifacts/research-us-military-ttp-learning-20260915/final/us-army-ttp-learning-loop-report.md
- supporting_work: artifacts/research-us-military-ttp-learning-20260915/work/remote-proof.md
- report: not_required (exploratory_research; final Markdown is the user-facing surface)
- red_status: not_required
- red_report: not_required (exploratory_research)
- result_summary: AAR의 즉시 교정과 ALLP의 검증·해결·전파·효과평가를 분리해, Infinity에는 observation→검증→변경→재사용 확인의 최소 폐루프만 전용했다.
- metric_question: 다음 실제 intent에서 학습 기록이 재사용 가능한 결정 또는 검증을 바꾸는가?
- metric_signal: 후속 intent의 관찰 레코드와 재사용 증거.
- metric_decision_rule: 재사용이 다음 행동 또는 검증 기준을 바꾸지 못하면 Observation 템플릿을 축소하거나 폐기한다.
- metric_result: 공개 1차 기관 자료의 AAR·ALLP·JLLP 단계를 하나의 폐루프로 대조했다.
- metric_next_decision: 다음 안전한 내부 intent 하나에서 5필드 Observation 템플릿을 실제 적용한다.
- knowledge_status: raw
- knowledge_decision: retain_in_infinity
- knowledge_targets: artifacts/research-us-military-ttp-learning-20260915/final/us-army-ttp-learning-loop-report.md
- knowledge_reflection: 군사 조직의 전담 인력·지휘·보안 체계를 복제하지 않고, 증거가 있는 관찰을 실제 변경과 다음 실행의 재검증으로 닫는 원칙만 Infinity에 남긴다.
- knowledge_commit: no-promotion-needed
- knowledge_log: agent-wiki/content/docs/log.mdx#research-us-military-ttp-learning-20260915
- notification_channel: slack
- notification_target: channel:C0BR41W31MM
- notification_reply_to: 1789445926.950759
- notification_origin: channel:C0BR41W31MM;reply_to:1789445926.950759
- remote_verified: pending
- archived_at: 2026-09-15T04:35:06Z

## Archive Card

- [프로젝트] Infinity / Research Bank
- [상태] 공개 기관 원문 기반 탐색형 리서치 완료
- [결과 기준] AAR·ALLP·JLLP의 포착→검증→변경→전파→평가 흐름과 Infinity 적용/비적용 경계를 분리했다.
- [다음 행동] 안전한 내부 intent 한 건에서 5필드 Observation 템플릿의 재사용 효과를 검증한다.
