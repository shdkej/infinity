# marketing-128 — 토스 Sharelink 일일 실험 운영 백서

- id: marketing-128
- status: archived
- archived_at: 2026-08-21T23:32Z
- target_agent: genie
- priority: high
- permission: L0-research-and-strategy; approval-required-before-public-action
- execution_mode: multi_subagent_roles
- projects: personal-brand,threads,affiliate,commerce,infinity
- task_type: operating-playbook-and-experiment
- topics: toss-sharelink,threads,affiliate-marketing,whitepaper,hook,item-selection,daily-learning
- artifact: artifacts/marketing-128/whitepaper.md; artifacts/marketing-128/first-experiment-set.md
- report: reports/marketing-128/20260821T2218Z.html
- verification: reports/marketing-128/verification.md
- red_status: follow_up_required (2026-08-22 feedback supersedes prior pass for candidate set)
- red_report: reports/marketing-128/verification.md
- role_sessions: planner=01a0269f-e529-7dd2-89fd-d25bee5322af; developer=01a026a0-0e4b-74c2-ba8c-adf23830a758; marketer=01a026a0-3638-7543-920a-fcae35b499b2; operator=01a026a0-5e45-7381-8f42-e47e9d9b9a88; red=01a026b6-f123-7541-ba2f-ff39f52bc5a3; prior_red=PASS (2026-08-21T23:47Z, superseded); follow_up_red=FAIL (2026-08-22, candidate identity still pending)
- result: 구매·준비 사실과 사용 경험을 분리하는 원칙은 유지하되, 구매 묶음명을 한 게시물로 복사하지 않고 개별 상품 후보로 나눠 계속 진행한다. 개별 상품·옵션·Sharelink 동일성이 덜 확인된 부분은 `purchase_only` 주장 상한으로 제한한다. 공개 게시·공개 링크·로그인·비용 집행은 실행하지 않았다.
- learning_update_2026-08-22: 한 번에 구매한 기록의 묶음명을 한 게시물로 복사한 것이 오류였다. 앞으로는 기록을 개별 상품 후보로 분해해 계속 진행하고, 서로 다른 상품은 관련 구매 기록에 함께 있어도 별도 게시물로 운영한다. 상품 동일성이 덜 확인된 부분은 `purchase_only` 주장 상한으로 제한한다. 결과는 `metrics.jsonl`에 쌓고 매일 23:10 KST 학습 루프가 백서에 반영한다.
- next_action: 개별 후보별 훅·본문을 만들고, 결과를 `metrics.jsonl`에 기록한다. 매일 학습 루프가 백서를 업데이트하며, 공개 Threads 게시·공개 Sharelink 공유는 별도 사용자 승인이 필요하다.
- knowledge_status: promoted
- knowledge_decision: promote
- knowledge_targets: [agent-wiki/content/docs/concepts/evidence-bounded-content-experiment.mdx]
- knowledge_reflection: 구매 묶음명과 검색 결과를 게시물·사용 후기로 과장하지 않고, 개별 상품 후보·근거·주장 상한을 분리하는 실패 교훈을 재사용 규칙으로 정제했다. 새 상품 식별과 Red 재검증 전에는 내부 준비로만 제한한다.
- knowledge_commit: ee69f6e

## Boundary

- 현재 후보는 개별 상품 단위의 `record_label`/`purchase_only`이며, 미확인·불일치 제휴 링크는 삽입하지 않는다.
- 이 Archive는 수정된 운영 규칙과 공개 승인 경계를 기록하며, 공개 실행 승인을 뜻하지 않는다.
