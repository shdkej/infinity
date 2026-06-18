# research-16: Parsed 3D Character Stage Implementation Options

- id: research-16
- status: archived
- completed_at: 2026-06-18T08:00Z
- result_summary: SAM YouTube parse(Figma→AI asset→Spline→Unicorn Studio 파이프라인) 기반 CharacterStage 구현 옵션 재비교 완료. Status-first = Option D(pre-rendered+CSS parallax) 즉시; Spline prototype = Phase 2; R3F 프로덕션 = Phase 3.
- artifacts:
  - artifacts/research-16/youtube-reference-parse.md
  - artifacts/research-16/3d-character-stage-options.md
- reports:
  - reports/research-16/2026-06-18T0800Z.html
- commits: heartbeat 2026-06-18T08:00Z
- next: build-12 (Option D 기준 Status 3D Character Background 구현)

## 원래 Intent 요약

- source: SAM Gemini YouTube parse (https://www.youtube.com/watch?v=dROkEnvxch4)
- goal: CharacterStage/FloatingHUD 구현 경로 비교 + Status 적용안 + reusable skill outline 산출
- research questions answered:
  1. CharacterStage best route: 단계적(D→B→A). 즉시는 Option D(pre-rendered)
  2. Spline+Unicorn Studio: prototype 환경만 권장. 프로덕션 전환 필요
  3. Status-first simplest: Option D (pre-rendered+CSS parallax), 반일
  4. Reusable skill: code scaffold + CSS tokens + verification gates (inputs: asset, mode, page, budget)
  5. Mobile: ≤640px poster still + ±4° parallax max; desktop: 70-80vh + ±8° parallax

## 결론 (2축 요약)

- 축1 (무엇을 조사했나): SAM Gemini YouTube parse 기반 CharacterStage 구현 옵션 4개(R3F/Spline/Unicorn/pre-rendered) 재비교
- 축2 (핵심 결과): Status 즉시 = Option D(pre-rendered+CSS parallax); prototype = Option B(Spline); 프로덕션 = Option A(R3F)
