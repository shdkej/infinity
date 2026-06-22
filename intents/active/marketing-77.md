# marketing-77 Virtue 승인된 마케팅 UI/카피 구현 패킷

- id: marketing-77
- status: in_progress
- created_at: 2026-06-22T11:25Z
- updated_at: 2026-06-22T12:00Z
- projects: [virtue]
- task_type: implementation
- topics: [marketing, activation, product, ui-copy]
- trigger: user said `마케팅 작업 승인`
- approval: user-approved

## 현재 상태

Cloud prepare 완료. 로컬 구현 패킷 생성됨.

다음 액션: 로컬 Claude Code에서 아래 패킷 기반으로 virtue-rebirth-app 구현 실행.

```
Infinity Intent: marketing-77 Virtue UI/카피 구현 패킷
Mode: execute_local
Goal: /add 첫 표면에 sample 결과 1줄, 결과 카드에 J4 경계 문구 footer 추가
Context:
  - 앱: /home/ubuntu/dev/virtue-rebirth-app
  - 구현 가이드: artifacts/marketing-77/implementation-packet.html
  - 근거: marketing-74 (Option B), marketing-76 (Yes 판정), marketing-71 (sample 표식 원칙)
Allowed: L0/L1 only — copy/UI 변경, 빌드, 테스트, commit, push
Forbidden: tracking/privacy/credential/external-message/cost 변경; force push; L2/L3
Verification: npm run build 통과, sample 표식 확인, 경계 문구 위치 확인
Report back: reports/marketing-77/{timestamp}.html (HTML 결론 2축 양식)
```

## 구현 패킷

- artifacts/marketing-77/implementation-packet.html

## 승인 범위

- product UI/copy implementation (scoped, reversible)
- L1/L2 non-force commit/push after verification

## 승인 제외

- external announcements / paid actions / tracking / privacy / credentials / force push

## Source Recommendations

- marketing-70: home empty-state proof gap and implementation ordering
- marketing-71: seeded proof must use explicit sample/preview labeling
- marketing-73: home empty-state recommended Option C (ghost AI result card)
- marketing-74: /add first surface recommended Option B (sample 결과 1줄); J4 boundary → result card footer
- marketing-75: /add first surface and result card = Tier 3; home empty state = Tier 2
- marketing-76: /add and result card guidance = Yes; home empty state guidance = No

## 성공 기준

- diff는 Virtue product UI/copy 및 관련 docs/report로만 제한됨
- sample/preview UI는 비실제 데이터임을 명시
- tracking/privacy/announcement/cost/credential 변경 없음
- 빌드/테스트/lint 통과 또는 blocker 기록

## 완료 기준

구현 및 검증 완료 후에만 archive. 앱 worktree에 dirty changes나 배포 모호성이 있으면 Waiting으로 기록.
