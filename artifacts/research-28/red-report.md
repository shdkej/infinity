# Red report — research-28

- reviewer: `01a02110-df6f-7613-8432-45078ca16e69`
- status: `fail`
- content gate: PASS (원리 대응표, 비적용 범위, MVP, 필드, 성공·중단·롤백, 1~2주 실험안, 한국어 전략, 네 역할 종합)
- failed gates: HTML에 `axis ax1` 누락, 연구형 필수 `근거 · 소스`/`다음 판단` 영역 누락, Red 상태 미반영, 템플릿 구조 축약
- disposition: HTML을 수정하고 다음 유효 사이클에서 Red 재검증. `red_status: pass` 전에는 완료·Archive 금지.

## Rerun — 2026-08-20T22:19Z

- reviewer: `independent rerun`
- status: `pass`
- content gate: PASS (artifact와 HTML의 전략 범위·MVP·필드·성공·중단·롤백·1~2주 검증안 및 네 역할 판단 일치)
- HTML/body gate: PASS (유효한 HTML 문서와 body 확인)
- axis gate: PASS (literal `axis ax1`/`axis ax2` 클래스와 `axis-ax1`/`axis-ax2` 식별자 확인)
- details gate: PASS (핵심 결과, 네 역할, 역할 종합, 근거·소스, 다음 판단·검증 메타 details 확인)
- evidence/path gate: PASS (근거·소스, literal artifact/report/red-report 경로 확인)
- consistency gate: PASS (rerun 후 HTML·Red report·Intent 모두 `red_status: pass`; 공개·코드·cron·credential·외부 변경 없음)
- failed gates: 없음
- disposition: 검증 완료. research-28을 Archive로 이동.
