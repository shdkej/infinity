# Virtue Launch-Ready PLG Signal Gate

Intent: `marketing-59`  
Scope: L1 docs-only local strategy translation for Virtue prelaunch.  
Source note: `source/external-links/marketing/2026-06-14-plg-signal-hierarchy.md` exists.  
Predecessor gate: marketing-55, marketing-56, and marketing-58 are archived as completed.

## Operating Rule

Virtue is still prelaunch, so the first 10 real users should not be read like a mature PLG funnel. The job of this gate is to separate three layers:

1. **Look now**: signals that can be observed manually during the first 10 user sessions without adding tracking.
2. **Hold as unknown**: signals that are plausible but too early to diagnose from first-contact behavior.
3. **Look after launch**: signals that need live traffic, repeat sessions, pricing exposure, or enough volume to compare cohorts.

This keeps acquisition, activation, and measurement-too-early from being collapsed into one vague failure label.

## Signal Gate Table

| Signal area | Look now in first 10 | Hold for now | Look after launch | First-10 manual review gate |
| --- | --- | --- | --- | --- |
| First win | Did the user reach the job-specific first successful output? J1/J2/J4 require `deed_saved`; J3 can complete at `deed_judged`. | Do not call a confused or slow first session a channel problem. | Compare first-win arrival by source, job, and repeat visit window. | For each observed user, write: job, expected result, first successful output reached, evidence shown on screen, next action chosen. |
| Activation quality | Did the user understand what Virtue did and what to do next after the output? | Do not infer long-term retention from one satisfied first result. | Test whether first-win users return for a second related deed or judgment. | Capture the user's own words: "what did Virtue help you decide or save?" and "what would you do next?" |
| PQL or upgrade readiness | Only note explicit pull signals such as asking for limits, more saves, team use, export, or recurring use. | Do not treat `deed_save_capped` or one heavy session as paid intent. | Evaluate PQL as a bundle: repeated value, limit pressure, job clarity, and willingness signal. | Mark as `pql_candidate_note`, not as score: exact phrase, context, and whether availability friction was present. |
| Acquisition problem | Track whether the user was the intended job/person and whether they arrived with a real deed to judge. | Do not diagnose channel quality from fewer than 10 conversations. | Compare qualified traffic and job mix by source once public acquisition starts. | Record source if known, job fit, and whether the session began with a real-life decision/deed. |
| Measurement problem | Check whether existing events and manual notes can reconstruct the first-win path. | Do not add new events, dashboards, or session replay before the first-10 review is understood. | Add or revise instrumentation only after manual ambiguity repeats. | After each session, ask: could we explain the path using existing event names plus notes? If not, note the missing observation. |
| Messaging problem | Listen for mismatch between the user's expected value and the actual output. | Do not rewrite public copy from one mismatch unless it repeats across jobs. | Update positioning after repeated mismatch patterns by job. | Capture the expectation sentence before use and the post-output value sentence after use. |

## First-10 Review Gate

Use one row per real user. This is a manual review gate, not a metric dashboard.

| Field | Required note |
| --- | --- |
| user/session label | Non-identifying local label only. |
| source/job fit | How the user arrived and which Virtue job they brought. |
| expected first win | User's pre-use description of the result they wanted. |
| first successful output | `deed_saved` for J1/J2/J4, `deed_judged` for J3, or `not reached`. |
| evidence quality | What the user saw that made the output useful, unclear, or unusable. |
| next action | Saved, judged and stopped, rerolled, abandoned, asked for more, or asked for help. |
| activation read | `reached`, `not_reached`, `ambiguous`, or `availability_blocked`. |
| acquisition read | `qualified`, `wrong_job`, `unclear_source`, or `too_early`. |
| measurement read | `observable_with_existing_events`, `manual_note_needed`, or `missing_observation`. |
| launch-after flag | Any PQL, retention, pricing, or channel question that must wait for post-launch comparison. |

## Decision Rules

- If the first win is not reached but the user was wrong-fit or arrived without a real deed, do not call it an activation failure.
- If the first win is reached but the user cannot explain what changed for them, treat it as activation quality ambiguity.
- If the user asks for more capacity, recurring use, or limits, preserve the phrase as a launch-after PQL candidate, not as purchase intent.
- If the path cannot be reconstructed with existing event vocabulary and manual notes, record the missing observation before proposing tracking.
- If first-10 observations disagree, keep the disagreement by job instead of averaging it away.

## No-Change Boundary

This artifact changes no production code, tracking, privacy behavior, public copy, pricing, dashboards, deployments, external messaging, or cost-bearing resources. It is a local docs-only interpretation layer for first-10 review.

## Source Snapshot

The source note was used as a PLG signal hierarchy lens. Bounded excerpt:

```text
---
title: "PLG 지표는 가입 수보다 첫 가치와 다음 행동을 먼저 본다"
source_type: external-link
platform: mixed
url: "https://mixpanel.com/blog/product-led-growth/"
captured_at: "2026-06-14T10:00:00Z"
status: summarized
category: marketing/growth
tags:
  - product-led-growth
  - activation
  - metrics
  - onboarding
  - prelaunch
notes: "Virtue prelaunch 단계에서 정식 출시 전후에 어떤 신호를 먼저 볼지 정리하기 위해 수집했다."
---

# PLG 지표는 가입 수보다 첫 가치와 다음 행동을 먼저 본다

- 수집일: 2026-06-14
- 처리 상태: summarized
- 수집 맥락: Virtue는 아직 정식 출시 전이고 실사용 지표가 decision-grade가 아니다. 이번 노트는 지금 성패를 판단하기보다, 출시 전 준비해야 할 지표 우선순위와 first-user 관찰 게이트를 정리하기 위한 학습 자료다.

## Source Boundary

- 이 문서는 `source/external-links/marketing/`에 보관한다.
- 원본 노트 트리인 `source/shdkej-content/`와 섞지 않는다.
- 후속 정리나 매핑이 필요할 때만 `agent-wiki/` 레이어에 연결한다.

## 출처 URL

- Mixpanel, "Product-led growth in 2026: A complete guide (and the metrics that actually matter)" (2026): https://mixpanel.com/blog/product-led-growth/
- Userflow, "Product-Led Growth: The Ultimate Guide for SaaS Success" (2026-06-05): https://www.userflow.com/blog/product-led-growth-the-ultimate-guide-for-saas-success
- ProductLed, "PLG Predictions For 2026: The Playbook is Being Rewritten. Fast." (2026): https://productled.com/blog/plg-predictions-for-2026

## 수집일

2026-06-14

## 핵심 요약

- Mixpanel은 2026년 PLG에서 page view나 signup보다 activation, product-qualified lead, expansion revenue 같은 행동 기반 지표가 더 높은 레버리지를 가진다고 본다.
- 같은 글은 PLG가 단독 self-serve로 끝나기보다, 제품 안의 행동 신호를 기반으로 sales나 CS가 적절한 시점에 붙는 product-led sales로 확장된다고 설명한다.
- Userflow는 PLG의 핵심 병목을 "새 사용자가 이탈하기 전 첫 승리에 닿는가"로 둔다. 온보딩은 설명 순서가 아니라 첫 win까지의 경로를 줄이는 장치다.
- ProductLed는 AI-native 제품에서 time-to-value 기대치가 초 단위로 압축되고, 사용자는 튜토리얼보다 즉시 결과를 기대한다고 본다.
- 세 자료의 공통점은 PLG가 더 많은 트래픽을 먼저 요구하지 않는다는 점이다. 제품이 스스로 팔리려면 사용자가 처음으로 가치를 느끼고, 그 다음 행동을 선택하는 순간이 관찰 가능해야 한다.
- prelaunch 제품에서는 지표 수집보다 지표 해석 경계가 먼저다. synthetic/test traffic, 초기 호기심 방문, 내부 검증 이벤트를 실사용 activation과 섞으면 잘못된 결론이 나온다.
- AI 제품에서는 첫 가치가 단순 클릭 완료가 아니라 "AI 결과를 믿고, 저장하거나 다시 시도하거나 다음 행동으로 옮기는가"로 읽혀야 한다.

## 왜 중요한가

Virtue는 이미 J1/J2/J4=`deed_saved`, J3=`deed_judged`라는 first-value 매핑을 갖고 있다. 하지만 정식 출시 전에는 방문자 수, 가입 수, 단일 이벤트 수를 성장 판단으로 쓰기 어렵다. 지금 필요한 것은 launch 이후를 위한 신호 위계다. 첫 사용자가 어떤 경로로 들어왔고, 몇 초 안에 어떤 결과를 봤으며, 그 결과 다음에 저장·재판단·종료 중 무엇을 했는지를 한 줄로 묶어야 한다. 그래야 낮은 표본에서도 "마케팅 메시지가 틀렸는가", "온보딩 경로가 막혔는가", "측정이 아직 이른가"를 구분할 수 있다.

## Virtue/Infinity에 적용 가능성

- Virtue에는 이미 first-10 관찰표와 first successful output contract가 있다. 이번 렌즈는 그것을 전환율 표로 바꾸지 않고, 출시 전후 신호 해석 순서를 고정하는 docs-only 작업에 적합하다.
- 첫 사용자 기준선은 `source/referrer`, `job guess`, `first-value event`, `time-to-first-value`, `next action`, `manual confidence`를 함께 봐야 한다. 하나만 보면 acquisition 문제와 activation 문제를 혼동한다.
- PostHog API 접근이 가능해져도 prelaunch/low-signal 단계에서는 숫자를 판정문으로 쓰지 않는다. 먼저 synthetic/test 제외 기준, first-10 수기 관찰, launch-after 최소 표본 gate를 둔다.
- Infinity 라우팅은 L1 docs-only가 적합하다. 신규 이벤트, tracking/privacy, dashboard, public copy, deploy, external outreach, cost-bearing action은 이번 후보에서 제외한다.

## 후속 실험 후보

1. Virtue launch-ready PLG signal gate를 만든
```
