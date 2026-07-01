# [design-01] 카드뉴스 미감 업그레이드

- id: design-01
- status: in_progress
- priority: medium
- target_agent: workflow-master
- projects: content, card-news, design-system
- task_type: design-audit
- topics: card-news, visual-system, library

## 목표
카드뉴스 산출물의 미감을 한 단계 올리기 위해 최근 카드뉴스 결과물과 제작 파이프라인을 감사하고, 앞으로 반복 적용할 시각 기준과 샘플 개선안을 만든다.

## 현재 상태
- Cloud prepare 단계 완료 (2026-07-01): 5개 시각 실패 패턴 가설 + 7개 실행 규칙 초안
- 로컬 실행 필요: `skills/insight-card-maker` 출력물과 실제 카드뉴스 3-5세트로 가설 검증

## 다음 액션 (로컬 실행)

로컬 Claude에 아래 프롬프트로 위임한다.

```
Infinity Intent: design-01 카드뉴스 미감 업그레이드
Mode: execute_local
Goal: 최근 카드뉴스 3-5세트의 시각 실패 패턴을 실제로 확인하고, 실행 규칙 7개를 확정한 뒤 샘플 preview 1개를 작성한다.
Context:
  - skills/insight-card-maker (로컬 스킬)
  - 최근 카드뉴스 출력물 3-5세트
  - reports/design-01/2026-07-01T0100Z.html (Cloud prepare 리포트)
Prepared findings:
  - 5개 실패 패턴 가설: 텍스트 패널 과다 / keyword-title 미적용 / 크롭 처리 부재 / CTA 불일치 / 모바일 안전영역 미준수
  - 7개 실행 규칙 초안: 리포트 참조
Allowed: L0/L1 actions only
Forbidden: 공개 라이브러리 대량 재렌더, 기존 산출물 일괄 교체, 외부 비용, 공개 배포, 이미지 임의 생성 대체
Verification: 샘플 preview를 390px 모바일 기준으로 확인
Report back to: reports/design-01/{timestamp}.html
```

## 준비된 자료
- Cloud prepare 리포트: `reports/design-01/2026-07-01T0100Z.html`
- 참조: `prompt-archive/DESIGN.md`
- 참조: `prompt-archive/skills/keyword-title/SKILL.md`

## 제약
공개 라이브러리 대량 재렌더, 기존 산출물 일괄 교체, 외부 비용, 공개 배포, 사용자 이미지 라이브러리의 임의 생성 이미지 대체는 별도 승인 전에는 하지 않는다.

## 완료 기준 (success_criteria)
- 최근 카드뉴스 3-5세트의 시각 실패 패턴 확인 완료
- 실행 규칙 5-7개 확정 문서 (`artifacts/design-01/visual-rules.md`)
- 샘플 카드 또는 preview 1개 (모바일 기준 검증)
- HTML 리포트 (`reports/design-01/{timestamp}.html`)
