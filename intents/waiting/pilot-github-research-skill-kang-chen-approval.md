# [pilot-github-research-skill-kang-chen-approval] Kang-chen 문헌검토 부분 기능 격리 파일럿 승인 대기

- status: waiting
- target_agent: genie
- task_type: approval-gated-research
- depends_on: research-github-skills-20260912
- blocker: 사용자 명시 승인, repo/subfile 라이선스 확인, 실제 의존성·egress·데이터 전송 경로 확인, no-secret·deny-egress 격리 환경 확인이 모두 필요하다.
- allowed_after_approval: 단일 공개 학술 질문의 읽기 전용 fixture에서 DOI dedupe·screening·citation traversal 부분 기능만 비교한다.
- forbidden_before_approval: clone, install, sync, script execution, account connection, secret entry, paid API, workspace/skill-registry modification.
