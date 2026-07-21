# ops-19 insight-card-maker Card 1 이미지 규칙 충돌 해소

- status: completed
- completed_at: 2026-07-21T06:12Z
- approved_by: user
- projects: openclaw,infinity
- type: maintenance
- topics: card-news,workflow,skill

## 결과

Card 1 원본사진 규칙과 샘 캐릭터 피드백 규칙의 우선순위를 한 가지 해석으로 정리했다.

## 변경

- Card 1은 기본적으로 `USER_ORIGINAL_PHOTO`를 사용한다.
- 샘 캐릭터 피드백은 기본적으로 Cards 2-5에 적용한다.
- Card 1까지 샘 캐릭터나 내부 제작 표지를 쓰려면 사용자의 명시 승인과 `image_policy` 기록이 필요하다고 고정했다.
- 기록 문구는 `Card 1 USER_ORIGINAL_PHOTO exception approved by user`로 통일했다.

## 검증

- `skills/insight-card-maker/SKILL.md`에서 Card 1 기본 규칙, Cards 2-5 샘 적용 범위, Card 1 예외 승인 조건을 모두 확인했다.
- 기존 `News Mode Image Classes`의 기본 이미지 맵과 충돌하지 않는다.

## 다음

기존 published config를 재수정할 때 Card 1이 원본사진이 아니면 `image_policy`에서 사용자 승인 근거를 먼저 확인한다.
