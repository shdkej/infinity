# [Cloud Prepare] marketing-43: Virtue 첫 주 재초대 경계표 초안

> Cloud prepare 단계 — Local Claude Code 실행 전 구조 초안.
> 이 파일을 참조하여 `apps/web/docs/first-week-reactivation-boundary-table.md`를 작성할 것.

## 목적

Amplitude win-back/첫 주 retention 렌즈를 Virtue prelaunch에 수치 목표로 이식하지 않고,
D1/D3/D7 미방문을 실패 판정 전에 잡별 first value 이후의 value recall 후보로 분류하는 내부 경계표.

## 계승 기반 (재정의 0)

| 항목 | 값 | 출처 |
|------|----|---------|
| J1/J2/J4 first value | `deed_saved`:183 | marketing-42, m06 |
| J3 first value | `deed_judged`:106 (저장 없는 종료 = 정상) | marketing-42, m21 |
| `deed_save_capped`:167 | availability/friction (재초대/업그레이드 수요 해석 금지) | marketing-41, m28 |
| synthetic/mock/self-test | 분류 제외 | marketing-42, m25 |
| 이벤트 앵커 | add_flow_started:72, deed_judged:106, deed_rerolled:149, deed_save_capped:167, deed_saved:183, level_up_viewed:199 | m36 skill sheet |

## VR 분류 체계 (미방문 4분류)

| 분류 | 기준 | 처리 방향 |
|------|------|----------|
| **VR-A** | First value 도달 이후 D1/D3/D7 미방문 | Value recall 후보 — 잡별 분류 후 관찰 |
| **VR-B** | First value 미도달 미방문 | 재초대 전 별도 진단 필요 (first session 완성이 선행) |
| **VR-C** | `deed_save_capped`:167 기록 있음, first value 미도달 | Availability/friction 먼저 확인 (업그레이드 수요 해석 금지) |
| **VR-X** | Synthetic/mock/self-test/메이커 self-test | 분류 대상 아님, 집계 제외 |

## 심장 표: 잡별 재초대 경계

### 구조 (Local Claude Code가 채울 표)

| 잡 | First Value 이벤트 | D-일 관찰 기준 | VR 분류 적용 | 돌아올 이유 후보 (proposal-only) | 보내면 안 되는 조건 | Availability/Synthetic 제외 | 승인 필요선 |
|----|--------------------|----------------|--------------|----------------------------------|--------------------|-----------------------------|-------------|
| J1 기록형 | `deed_saved`:183 | D1, D3 | VR-A: deed_saved 이후 D1 미방문 → 기록은 했으나 재확인 없음 | "저장한 덕행 다시 보기" 리마인더 후보 | VR-B (deed_saved 없음), VR-C, VR-X; D1/D3 rate/% 결론 | `deed_save_capped` early-return 세션 제외; mock/641 seed 제외 | 실제 메시지 발송, in-app 알림, 푸시 설정 |
| J2 누적형 | `deed_saved`:183 | D3, D7 | VR-A: D3 미방문 → 누적 payoff (`level_up_viewed`:199) 미도달 가능성 | "연속 기록 확인" / level_up 가능성 안내 후보 | VR-B, VR-C, VR-X; level_up 1회로 retention 확보 단정 금지 | `deed_save_capped` 제외; synthetic 제외 | 실제 push/email 발송, retargeting 설정 |
| J3 AI 호기심형 | `deed_judged`:106 | D3, D7 | VR-A: deed_judged 이후 D7 미방문 → AI 결과 확인 후 호기심 충족, 재방문 없음 (정상 가능성) | "다른 행동 AI 채점해보기" 재판정 invite 후보 | judged−saved 갭을 이탈 단정 금지; VR-B (deed_judged 없는 미방문); VR-X | mock 임시판정 세션 제외; 641 demo seed 제외 | in-app 재판정 invite 배포, retargeting |
| J4 회고형 | `deed_saved`:183 | D7 | VR-A: D7 미방문 → 회고 리듬 미형성 가능성 | "저번 덕행 되돌아보기" 회고 리마인더 후보 | VR-B, VR-C, VR-X; 1주 미형성을 이탈 단정 금지 | `deed_save_capped` 제외; synthetic 제외 | 실제 메시지 발송, 알림 설정 |

## 공통 승인 필요선 (Waiting/approval-needed)

- 공개 발송 (이메일, 푸시, in-app 메시지, SMS)
- retargeting 설정 변경
- tracking/privacy 변경
- D1/D3/D7 rate/% 목표 수치 확정
- retention rate 벤치마크 적용
- 외부 서비스 (PostHog, Mixpanel 등) 재초대 트리거 설정
- 새 이벤트/속성 추가

## 공통 금지선 (prelaunch)

- first 10명 또는 first 7일에는 rate/% 결론 없이 분류 가능성만 확인
- D1/D3/D7 미방문을 onboarding 실패로 단정하지 않음
- `deed_save_capped`:167을 재초대 수요 또는 upgrade 수요로 해석 금지
- J3 `deed_judged` 이후 미방문을 가치 부재로 단정하지 않음 (정상 종료 가능)
- VR-B 상태에서 재초대 발송 금지 (first session 완성이 선행)
- 전환율/PMF/벤치마크 목표 수치 산출 금지
- 신규 이벤트·속성·카피배포·대시보드·코드·외부발송·비용·tracking/privacy 변경 금지

## source note 처리

source note 경로: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-06-first-week-reactivation.md`

로컬 부재 가능성 있음. 부재 시 → Intent rationale 요지만 근거로 인용:
- "Amplitude win-back/첫 주 retention 렌즈를 Virtue prelaunch에 그대로 수치 목표로 이식하지 말 것"
- "D1/D3/D7 미방문을 실패 판정 전에 잡별 first value 이후의 value recall 후보로 분류할 것"

## 로컬 실행 지시 (Claude Code용)

```
Infinity Intent: marketing-43 Virtue 첫 주 재초대 경계표
Mode: execute_local
Invocation: Prefer pt/purplemux Claude pane via tmux -L purple; fall back to bounded claude --dangerously-skip-permissions -p
Workflow: simple-doc 작업 — 직접 실행 가능

Goal: apps/web/docs/first-week-reactivation-boundary-table.md 작성
  - infinity/artifacts/marketing-43/first-week-reactivation-boundary-draft.md 참조
  - 심장 표 (J1~J4 × VR분류×돌아올이유후보×보내면안되는조건×availability제외×승인필요선) 포함
  - §1 목적, §2 VR 분류 기준, §3 심장 표, §4 공통 승인 필요선, §5 공통 금지선 구조
  - source note 로컬 부재 시 Intent rationale 요지만 근거로 §0에 명시

Context:
  - /home/ubuntu/dev/virtue-rebirth-app/apps/web/docs/ (기존 docs 참조)
  - marketing-42: apps/web/docs/value-per-session-reading-table.md 계승
  - 이벤트 앵커: add_flow_started:72, deed_judged:106, deed_rerolled:149, deed_save_capped:167, deed_saved:183, level_up_viewed:199

Allowed: L1 docs-only, 기존 이벤트만 인용
Forbidden: 신규 이벤트·속성·카피배포·대시보드·코드·외부발송·비용·tracking/privacy 변경; rate/% 결론; 재초대 실제 발송

Verification:
  - git diff --stat apps/web/src apps/ios → 빈 출력 (doc 1파일만)
  - rg -c "deed_judged\|deed_saved\|deed_save_capped" apps/web/docs/first-week-reactivation-boundary-table.md → 0이 아님
  - rg -c "^\+{1,3} |^={3,7}" apps/web/docs/first-week-reactivation-boundary-table.md → 0 (conflict marker 없음)
  - 이벤트 앵커 drift 확인: 72/106/149/167/183/199 현행 일치

Report back to: infinity/reports/marketing-43/{timestamp}-local.html (HTML 필수)
HTML report contract: reports/_TEMPLATE.html 기반, axis ax1/ax2 포함, details에 계승한 기준·이번에 새로 배운 것·다음 Marketer 규칙·승격 후보 포함
```

## 검증 게이트 (완료 전 확인 사항)

- [ ] 신규 이벤트·속성 0
- [ ] 코드 diff 0 (doc 1파일만)
- [ ] conflict marker 0
- [ ] first value 매핑 계승 확인 (J1/J2/J4=deed_saved, J3=deed_judged)
- [ ] rate/% 결론 없음
- [ ] 재초대 실제 발송 지시 없음
- [ ] source note 처리 명시
- [ ] HTML 보고서 `<html`, `<body`, `axis ax1`, `axis ax2`, `<details` 포함
- [ ] MARKETING_LEARNINGS.md durable learning 승격 후보 확인
