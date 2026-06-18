# research-15: 3D Interactive Character Background Feasibility

- id: research-15
- status: archived
- completed_at: 2026-06-18T07:01
- projects: [personal-ops, infinity]
- task_type: research
- topics: [dashboard, workflow, content]
- result_summary: Sam Samuel 웹의 3D character background + floating HUD 문법은 다음 Status 적용에서는 pre-rendered scene + pointer parallax가 안전하고, 재사용 skill 단계에서는 Three.js/R3F scene + HUD 시스템으로 확장하는 것이 적합하다.
- artifacts:
  - path: artifacts/research-15/3d-interactive-character-background-feasibility.md
    role: research
    note: 구현 옵션 3단계, 모바일 fallback, Status 적용안, 문서/skill 반영 계획
- reports:
  - path: reports/research-15/2026-06-18T0701Z-local.html
    role: final
- commits:
  - repo: infinity
    sha: e741270
    note: archived research-15 artifact, report, and intent registry update
- urls:
  - url: https://www.youtube.com/watch?v=dROkEnvxch4
    note: reference video; server extraction blocked by YouTube bot confirmation, so used only as directional brief
- next_actions:
  - If implementation is requested, create a separate build/design intent for Status or Sam Samuel web. Do not modify Status code under research-15.

## Axis Summary

- axis1: YouTube reference and Sam Samuel visual direction were translated into practical web implementation routes for an interactive character background with floating controls.
- axis2: Start with pre-rendered scene + pointer parallax; graduate to Three.js/R3F only when reusable scene/HUD skill and asset pipeline are ready.

## Boundaries Kept

- No production implementation.
- No deploy.
- No paid service signup.
- No public posting.
- No Status code modification.

## Source Notes

- React Three Fiber performance pitfalls: https://r3f.docs.pmnd.rs/advanced/pitfalls
- React Three Fiber scaling performance: https://r3f.docs.pmnd.rs/advanced/scaling-performance
- Spline Viewer export: https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer
- Three.js pixel ratio docs: https://threejs.org/docs/pages/CanvasTarget.html
- Lottie web runtime: https://github.com/airbnb/lottie-web
