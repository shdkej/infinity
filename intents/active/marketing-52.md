# marketing-52: Virtue /add 초기 프롬프트 디자인 감사

- id: marketing-52
- status: active
- priority: medium
- permission: L0/L1
- projects: [virtue, infinity]
- task_type: marketing
- topics: [activation, onboarding, ai-product, prompt-design]
- target_agent: marketer
- created_at: 2026-06-10T22:01Z
- updated_at: 2026-06-10T22:30Z

## Goal

Virtue `/add` flow에서 사용자가 최초로 마주치는 프롬프트/UI 텍스트를 감사하여:
1. UI 안내형(범퍼)과 진짜 사용자 의도 확인형(조향)을 분류
2. 동사 프레임(판결 vs 관점)을 점검
3. 결과 지향 AI 지시로의 개선 방향을 proposal-only로 제시
4. first value 도달까지의 마찰 지점 파악

## Success Criteria

- [ ] `/add` flow의 모든 사용자-표면 텍스트를 3개 카테고리(UI안내형/의도확인형/결과지향형)로 분류 완료
- [ ] 동사 프레임 분석 완료 (판결/관점 프레임 비율)
- [ ] 잡별 조향 효과 평가 (J1/J2/J3/J4 기준)
- [ ] 개선 후보 목록 proposal-only로 작성
- [ ] 원문서 근거 확인, zero new instrumentation
- [ ] 승인 경계 명확화

## Context

- Virtue 앱 `/add` route 및 관련 AI 프롬프트 파일
- 관련 artifacts: `artifacts/marketing-52/`
- 선행 report: `reports/marketing-51/2026-06-10T1007Z-local.html` (Guided First-Value 4구간)

## Inherited Learning

- **m51** `Guided First-Value Is A Four-Stage Handoff`: `/add` flow 어느 구간이 friction인가 (첫 입력 전 / AI 대기 / 결과 해석 / 저장-종료)
- **m45** `Decision-Delegation Risk Rides The Verb`: 동사 프레임 분류 → 판결(채점/판정) vs 관점(본/읽은/보여주기)
- **m32** `First-Input Defaults Steer The Job`: 첫 입력 기본값이 잡 조향 → 단일 중립 placeholder는 J3/J2를 가장 약하게 부름
- **m40** `Nudges Are Event-Triggered`: UI 안내형 넛지는 B-LOST에서만 후보 → 기본값 = 띄우지 않음

## Mode

- **prepare (Cloud, 완료)**: 분류 프레임워크 초안, 동사 프레임 체크리스트 → `artifacts/marketing-52/add-prompt-audit-framework.md`
- **execute_local (다음 단계)**: 실제 Virtue 코드에서 `/add` 관련 프롬프트 텍스트 수집 + 분류 수행

## Next Action

```
Infinity Intent: marketing-52 Virtue /add 초기 프롬프트 디자인 감사
Mode: execute_local
Goal: Virtue 앱의 /add route에서 사용자가 보는 모든 텍스트(placeholder, 힌트, 헤더, 버튼 레이블, AI system prompt 관련 텍스트)를 수집하고, artifacts/marketing-52/add-prompt-audit-framework.md의 분류 체크리스트로 분류 수행
Context: Virtue 앱 소스 코드 (apps/web 또는 관련 경로), /add route 관련 컴포넌트
Prepared findings: artifacts/marketing-52/add-prompt-audit-framework.md (분류 프레임워크 초안)
Allowed: L0/L1 읽기 전용 코드 분석, proposal-only 개선 초안 작성
Forbidden: 실제 카피 배포, 코드 수정, 프로덕션 반영 (모두 approval-needed)
Report back to: reports/marketing-52/{timestamp}.html
```
