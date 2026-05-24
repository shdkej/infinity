# marketing-15 Intent Archive

- id: marketing-15
- title: Virtue 웹/iOS 활성화 이벤트 패리티 브리프 작성
- status: archived
- priority: medium
- permission: L1
- created_at: 2026-05-24T22:07Z
- completed_at: 2026-05-24T22:07Z
- source_note: `/home/ubuntu/dev/knowledge-lab/source/external-links/marketing/2026-05-24-activation-metric-event-bundles.md`

## Result Summary

Virtue 웹/iOS 활성화 이벤트 패리티 브리프를 내부 문서로 작성했다. 문서는 첫 10-20명 관찰과 출시 후 PostHog 리뷰에서 "활성화 문제"와 "플랫폼 계측 불일치"를 분리하기 위한 기준을 제공한다.

## Artifact

- repo: `virtue-rebirth-app`
- commit: `10e3fa2`
- path: `apps/web/docs/ios-activation-event-parity-brief.md`

## Scope

- 신규 이벤트: 0
- 신규 속성/PostHog 설정/대시보드: 0
- 코드/카피/런타임 변경: 0
- 배포/외부 발송/비용/시크릿/권한 변경: 0

## Findings

- iOS에는 `add_flow_started`, `add_flow_abandoned`, `level_up_viewed`, `deed_rerolled`, `deed_save_capped`가 없다.
- `deed_saved` 속성은 웹 12개, iOS 3개로 다르다.
- `deed_judged` 속성은 웹 9개, iOS 7개로 다르다.
- iOS만 `platform=ios` super-property를 등록한다.
- `model` 기본값과 `memo_length` 계산 방식이 플랫폼별로 다르다.

## Verification

- `rg 'posthog.capture|Analytics.capture' apps/web/src apps/ios/Sources -S` 결과와 문서 표 일치
- `apps/web/src`, `apps/ios/Sources` 변경 0건
- 충돌 마커 0건
- PostHog 설정/대시보드 변경 0건
- `virtue-rebirth-app` push 후 local HEAD `10e3fa2` == `origin/master` `10e3fa2`

## Reports

- `reports/marketing-15/2026-05-24T2207Z-local.md`
