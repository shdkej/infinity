# marketing-28: Virtue Prelaunch Monetization Boundary Brief — Cloud Draft

> 작성: 2026-05-30 Heartbeat cloud prepare 단계
> 출처 노트: `knowledge-lab/source/external-links/marketing/2026-05-30-plg-pricing-triggers.md`
> 최종 산출물 경로: `virtue-rebirth-app/apps/web/docs/prelaunch-monetization-boundary-brief.md`

## 핵심 렌즈

**Stripe PLG Pricing Guide + Growth Unhinged 2026 관찰:**
- 가격/제한이 첫 가치 이전에 나오면 → activation을 가린다 (마찰 신호와 가격 신호가 혼동됨)
- 첫 가치 이후의 자연스러운 확장 순간에 붙어야 한다
- Virtue는 출시 전 → 지금은 "무엇을 잠그지 말아야 하는가"를 정리하는 단계 (가격 결정 아님)

---

## §1 목적

Virtue prelaunch 단계에서 paywall·AI cap·저장 제한 논의를 activation 관찰과 분리한다.
첫 10-20명 학습에서 가격 신호와 마찰 신호를 혼동하지 않게 하는 경계 문서.

---

## §2 J1-J4별 첫 가치 이전 금지 제한 (심장 표)

| 잡 | 잡 유형 | 첫 가치 이벤트 | 이 이전에 잠그면 안 되는 것 | 이유 |
|---|---|---|---|---|
| J1 | 기록형 | `deed_saved` | deed_saved를 paywall로 막기 | 첫 기록 저장이 곧 가치 확인. 막으면 activation 자체 차단 |
| J2 | 누적형 | `deed_saved` | deed_saved 횟수 제한 (free tier save cap) | 누적이 가치인 잡에서 저장 한도 = 첫 가치 차단 |
| J3 | AI 호기심형 | `deed_judged` | AI 판정 횟수 제한 (AI usage cap) | deed_judged가 첫 가치. AI cap이 발화 전에 나오면 J3 activation 차단 |
| J4 | 회고형 | `deed_saved` | 회고 접근 전 로그인/결제 요구 | deed_saved 이전 장벽 = activation 차단 |

---

## §3 deed_save_capped 오독 금지

- `deed_save_capped` (code line 167): 저장이 **막혔을 때** 발화 (early return)
- **저장이 완료된 것이 아님** → `deed_saved`와 절대 혼동 금지
- paywall 도입 시 `deed_save_capped` ↑ + `deed_saved` ↓ = 예상된 패턴이지만,
  `deed_save_capped`를 activation 신호로 읽으면 안 됨
- prelaunch에서 `deed_save_capped`가 발화되면 → "왜 막혔는가" 근본 원인부터 확인
- `deed_save_capped` availability ≠ value (`deed_saved`만 가치 확인 이벤트)

---

## §4 첫 가치 이후 자연스러운 확장 트리거 후보

> 모두 현재 **proposal-only**. 실제 적용은 사용자 명시 승인 필요 (Waiting 이동).

| 트리거 | 이벤트 근거 | 적합 잡 | 설명 |
|---|---|---|---|
| 반복 저장 (습관 형성 신호) | `deed_saved` 3회+ (distinct session) | J1, J2, J4 | 첫 가치 이후 반복 = 습관 = 지불 의향 신호 |
| 누적 인식 순간 | `level_up_viewed` | J2 | 누적을 인식했을 때 → 확장 논의 시작 가능 |
| D7 복귀 | D7 내 deed_saved | J1, J2, J4 | 리텐션 확인 = 가치 검증 → 전환 논의 시작점 |
| AI 재시도 (호기심 능동화) | `deed_rerolled` | J3 | 1회가 아닌 능동적 탐색 = AI 가치 체감 확인 |

---

## §5 지금 잠그지 않는 것 (prelaunch 전면 금지 목록)

아래는 현재 도입하지 않는다:

- Paywall (deed_saved 이전 결제 요구)
- AI cap (deed_judged 횟수 제한)
- 저장 횟수 제한 (free tier save cap 강제)
- 공개 가격표
- 결제 연동 (Stripe 등)
- 프리미엄 tier / 기능 구분

---

## §6 승인 필요 경계 (나중에, 반드시 Waiting → approval)

아래는 사용자 명시 승인 없이 진행하지 않는다:

- 실제 paywall 구현 및 배포
- AI 사용량 cap 코드 도입
- 저장 한도 enforcement 코드 변경 (`deed_save_capped` 조건 수정)
- 공개 pricing 페이지 배포
- 결제 플랫폼 연동
- 외부 공개 가격 커뮤니케이션

---

## §7 검증 게이트 (Local Claude Code용)

최종 문서 작성 후 아래를 확인한다:

1. J1-J4 × (첫 가치 이전 금지 제한) 표가 존재하는가
2. 기존 first-value 매핑 재정의 없음 (J1/J2/J4=`deed_saved`, J3=`deed_judged`)
3. `deed_save_capped` 오독 금지 원칙이 포함되어 있는가
4. 첫 가치 이후 확장 트리거 후보가 proposal-only로 분리되어 있는가
5. 승인 필요 경계(paywall/AI cap/결제/배포)가 명시되어 있는가
6. 신규 이벤트·카피·결제·배포 변경이 없는가 (docs-only diff)
7. conflict marker 0, 기존 이벤트 앵커 drift 0

---

## §8 Local 실행 프롬프트

```
Infinity Intent: marketing-28 Virtue prelaunch monetization boundary brief
Mode: execute_local
Required workflow: Use workflow-master first. Find it under `~/.claude/skills/workflow-master/` and `~/.claude/agents/workflow-master.md`.

Goal: virtue-rebirth-app/apps/web/docs/prelaunch-monetization-boundary-brief.md 작성

Context:
- Source note: /home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-30-plg-pricing-triggers.md
- Cloud draft: infinity repo artifacts/marketing-28/prelaunch-monetization-boundary-brief-draft.md
- Prior docs: apps/web/docs/first-session-jtbd-matrix.md, onboarding-metrics-reading-table.md, traffic-source-reading-boundary-table.md
- First value mapping: J1/J2/J4=deed_saved, J3=deed_judged (재정의 금지)
- Event whitelist: add_flow_started, deed_judged, deed_saved, level_up_viewed, deed_rerolled, deed_save_capped (6개만)

Prepared findings: artifacts/marketing-28/prelaunch-monetization-boundary-brief-draft.md 참조

Allowed: L1 (docs-only 파일 작성, git commit & push)
Forbidden: 신규 이벤트, 코드 변경, 카피 반영, 결제/배포, 외부 발송

Verification gates:
1. J1-J4 × 첫 가치 이전 금지 제한 표 존재
2. first-value 매핑 재정의 없음
3. deed_save_capped 오독 금지 원칙 포함
4. 확장 트리거 후보 proposal-only로 분리
5. 승인 필요 경계 명시
6. conflict marker 0, 이벤트 앵커 drift 0
7. docs-only diff (코드 변경 0)

Report back to: infinity repo reports/marketing-28/{timestamp}.md
완료 후 INTENTS.md marketing-28 status를 archived로 업데이트
```
