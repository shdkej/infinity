# Virtue `/add` first-input prompt design audit

- intent: `marketing-52`
- source note: `/home/ubuntu/workspace/knowledge-lab/source/external-links/marketing/2026-06-10-ai-onboarding-click-tax-output.md`
- scope: docs-only / proposal-only / no public copy change
- status: internal audit
- permission: L1 docs-only

## 0. Purpose

The source note says AI onboarding should reduce click tax by moving attention from "teach the UI" to "teach the AI what result the user wants." For Virtue, that does not mean the AI should complete the reflective work for the user. The safe prelaunch task is to audit the current `/add` first input surface and separate three things:

1. UI instructions: words that explain controls or required input.
2. Judgment delegation: words that invite the user to hand the decision to AI.
3. Desired-result teaching: words that help the user tell AI what kind of reflection, record, or curiosity result they want.

This document creates proposal-only candidates and approval boundaries. It changes no code, public copy, event, tracking, privacy setting, dashboard, session replay, deployment, pricing, messaging, or account state.

## 1. Inherited criteria

| Criterion | Inherited rule | Use in this audit |
|---|---|---|
| First Value Mapping | J1/J2/J4 = `deed_saved`; J3 = `deed_judged`. | Prompt design must not optimize every job toward save. |
| Guided First-Value Is A Four-Stage Handoff | First input -> AI wait -> result interpretation -> save/exit. | This audit focuses only on stage 1, while preserving the later handoff. |
| First-Input Defaults Steer The Job | Placeholder/examples decide which job the user thinks the product is for. | Current prompts are read as steering devices, not decoration. |
| Decision-Delegation Risk Rides The Verb | `채점`/`판정` can read as judgment; `본`/`읽은` can read as perspective. | Candidate text should lean toward "show/read/reflect" rather than "decide." |
| Prelaunch Boundary | Tiny samples and self-tests are not decision-grade. | All candidates are internal and require observation before implementation. |

## 2. Current `/add` first-input inventory

| Surface | Current text | Classification | Job effect | Risk |
|---|---|---|---|---|
| Header | `덕 쌓기` | Job-performing frame | Strong for J1/J2/J4 because it says the task is to add a deed. | J3 curiosity is not called before the input. |
| Photo slot | `오늘의 한 컷, 골라주세요` / `카메라 또는 갤러리에서` | UI instruction + low-friction input cue | Helps J1/J4 select concrete material. | Can over-weight photo even though memo-only is allowed. |
| Memo label | `한 줄 메모 (선택)` | UI instruction + friction reduction | Good for J1/J4 because it lowers effort. | Does not say what kind of result the user can ask AI to return. |
| Memo placeholder | `뭐 했어요? 한 줄이면 충분해요.` | Desired-result teaching, but job-neutral | Good default: asks for the user's actual action, not a feature question. | It asks for input content, not desired output; J2/J3 remain weakly steered. |
| Disabled judge button | `사진 또는 메모 필요` | UI instruction | Clear prerequisite. | Purely mechanical; no value cue. |
| Judge button | `AI 채점` / `메모로 AI 채점` / `임시 판정` | Judgment delegation risk | Calls J3 after input, and gives a clear next action. | `채점` can frame AI as evaluator rather than mirror; mock mode lowers J3 signal. |
| Empty hint | `갤러리 사진이나 카메라 촬영본을 고를 수 있어요. 사진 없이 메모만 있어도 AI가 보수적으로 채점합니다.` | UI instruction + trust/function explanation | Reduces uncertainty about memo-only input. | "보수적으로 채점" reinforces judgment frame and does not ask what result the user wants. |

Current state: Virtue already avoids support-bot style prompts. There are no suggested prompt chips, examples, categories, or feature-tour steps. The main gap is not too much UI explanation; it is that the first input asks "what did you do?" but not "what do you want the AI to help you see in it?"

## 3. UI instruction vs judgment delegation vs desired-result teaching

| Pattern | Current examples | Keep / reduce / add | Reason |
|---|---|---|---|
| UI instruction | `사진 또는 메모 필요`, `한 줄 메모 (선택)`, `카메라 또는 갤러리에서` | Keep minimal | These reduce click tax only when they remove uncertainty at the input point. They should not become a tutorial. |
| Judgment delegation | `AI 채점`, `임시 판정`, `보수적으로 채점` | Reduce or reframe, proposal-only | They can make the first action feel like submitting oneself for evaluation. This conflicts with m45's verb-frame rule. |
| Desired-result teaching | `뭐 했어요? 한 줄이면 충분해요.` | Add job-aware variants only after observation | The existing placeholder is a good neutral base, but it does not help the user specify whether they want a record, a cumulative step, an AI reading, or a reflection. |

## 4. Job-by-job prompt design audit

| Job | First value | What first input should teach AI | Current support | Proposal-only candidate direction | Approval boundary |
|---|---|---|---|---|---|
| J1 record | `deed_saved` | "Turn this small action into a record I can keep." | Strong: `뭐 했어요?` and memo/photo support concrete action. | A tiny internal example could emphasize ordinary action, not moral greatness. | Public placeholder/example copy requires approval and copy-spec review. |
| J2 accumulation | `deed_saved` | "Make this count toward an ongoing pile." | Weak: accumulation appears mostly after saving. | If repeated J2 confusion appears, a proposal could hint that today's one line becomes part of the total. | Do not add progress promises or retention copy without approval. |
| J3 AI curiosity | `deed_judged` | "Show me how AI reads this, without requiring save." | Medium after input, weak before input. `AI 채점` calls curiosity but also judgment. | Reframe from scoring to perspective in internal copy candidates; keep save optional. | Public AI promise/button changes require approval; do not treat judged-save gap as failure. |
| J4 reflection | `deed_saved` | "Help me preserve what this meant in my own words." | Medium: memo is easy, but desired reflection outcome is not named. | Result-after self-appropriation question should stay observational first, not in-app copy. | Public reflection prompt, tracking, or new form fields require approval. |

## 5. Proposal-only candidate set

These are not implementation instructions. They are internal wording directions to test manually in first-user observation or future approval-gated copy work.

| Candidate | Where it would belong | Why it exists | Guardrail |
|---|---|---|---|
| "오늘 한 일을 한 줄로 알려주세요. AI가 어떻게 보이는지 보여줄게요." | Memo helper / placeholder direction | Teaches the AI desired result: show a reading, not decide identity. | Needs public copy approval; avoid overpromising AI truth. |
| "대단한 일 아니어도 괜찮아요. 나중에 기억할 한 장면이면 충분해요." | J1/J4 example direction | Reduces input hesitation without adding tutorial clicks. | Must pass copy-spec; avoid moral praise language. |
| "저장하지 않고 AI가 본 것만 확인해도 괜찮아요." | J3 result interpretation / save-exit direction | Preserves J3's first value at `deed_judged`. | Do not push this before observing actual J3 confusion; public copy approval needed. |
| "오늘의 한 줄이 쌓이면 나중에 흐름을 볼 수 있어요." | J2 accumulation direction | Names the second value without forcing first-session metrics. | Avoid retention claims, streak pressure, or progress guarantees. |

## 6. Click-tax reading

| Click-tax type | Current status | Reading |
|---|---|---|
| Menu/tutorial click tax | Low | `/add` has no tutorial or extra setup. |
| Input uncertainty tax | Medium | The user knows they can add photo/memo, but may not know what kind of action is "enough." |
| Judgment anxiety tax | Medium | `AI 채점` and `보수적으로 채점` can make the user feel evaluated. |
| Desired-output ambiguity tax | Medium | The input asks what happened, but not whether the user wants record, accumulation, AI perspective, or reflection. |
| Save-pressure tax | Low-to-medium | Result actions preserve cancel/reroll/save, but candidate copy must not make J3 save mandatory. |

## 7. Changed assumptions and conflicts

### Inherited assumptions

- J1/J2/J4 first value remains `deed_saved`.
- J3 first value remains `deed_judged`; save is optional.
- `deed_save_capped`, 503, delay, and mock mode are availability/friction or traffic-quality issues, not upgrade demand.
- First-user learning should capture user language and decision-delegation reading, not force automatic personalization.

### Changed assumptions

- None. This audit narrows marketing-51 from the full four-stage handoff to the stage-1 prompt-design surface.

### Conflicts

- No conflict with marketing-32: the earlier finding that current defaults are "question placeholder + empty slots" still holds.
- No conflict with marketing-45: the risk remains verb-frame alignment, especially `채점`/`판정`.
- No conflict with marketing-51: this document gives the first-input stage a more detailed prompt-design lens, while keeping the same four-stage handoff.

## 8. Next Marketer rules

- For `/add` prompt design, ask first: "Does this text teach UI mechanics, delegate judgment, or help the user tell AI the result they want?"
- Reduce click tax only when the removed step is unrelated to the desired result. Do not remove reflective input time merely because it takes time.
- Treat prompt examples as job steering. Do not add one global example until first-user language shows which job needs steering.
- Keep J3 save-optional. Any copy that makes save the normal second action for J3 conflicts with the first-value mapping.
- Public copy, code changes, new tracking, dashboards, personalization, privacy changes, deployment, or external messages are approval-needed.

## 9. MARKETING_LEARNINGS.md promotion candidate

First-input prompt design should teach the AI the user's desired result, not the user the UI and not the AI the authority to decide. In Virtue, the useful split is UI instruction vs judgment delegation vs desired-result teaching: keep UI instructions minimal, reframe judgment verbs cautiously, and add job-aware desired-result prompts only after observation. Click-tax reduction must not remove the reflective input that creates the value.

## 10. Verification gate

- Source note path included: yes.
- J1-J4 first value mapping included: yes, J1/J2/J4 = `deed_saved`, J3 = `deed_judged`.
- New instrumentation/tracking/privacy changes: 0.
- Public copy/code/deployment changes: 0; all wording candidates are proposal-only and approval-needed.
- Conflict markers: 0.
