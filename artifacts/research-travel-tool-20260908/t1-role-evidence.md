# T1 역할별 독립 조사 — 증거 수렴

> 2026-09-08T08:51Z에 timebox 재평가로 채택한 대안: 새 시장 조사를 반복하지 않고, 이미 회수된 네 역할의 독립 결과를 session evidence와 출처 링크로 수렴한다.

## Planner

- session: `01a0801c-da88-7ed1-a330-1e0336ec0c72`
- 권장: 여행 중/직후의 상황·선택·다음번 판단을 한 장의 카드로 복원하는 도구.
- 대안/제외: Polarsteps의 회고·시각화 premium 및 TripIt의 실시간 운영 알림과 직접 경쟁하지 않는다.
- 유료 행동 근거: [TripIt Pro](https://www.tripit.com/web/pro/pricing), [Polarsteps Plus](https://www.polarsteps.com/fr/plus), [TravelJournal](https://www.traveljournal.me/en/pricing). 각 가격은 인접 서비스의 반복 결제 신호이며 이 후보의 직접 WTP 증거는 아니다.

## Developer

- session: `01a0801c-f184-74e2-b6ce-46575f00df73`
- 권장: `장면 → 판단 → 다음 선택 기준`을 복원하는 저입력 여행 회수 카드.
- 구현 경계: 계정·지도·추천·AI·위치·사진 업로드·외부 API 없이 로컬 우선 카드와 수동 내보내기만 검토한다.
- 반증/대체재: [Day One plans](https://dayoneapp.com/plans/)의 일반 저널 기능과 [Wanderlog 비교](https://wanderlog.com/blog/2024/11/26/wanderlog-vs-tripit/)의 지도·일정 기능을 반복하지 않는다.

## Marketer

- session: `01a0801d-0bb5-7783-944f-950b8260d478`
- 가치 문장 초안: “여행이 끝난 날, 사진과 메모를 쌓는 대신 다음 여행에서 다시 쓸 선택 기준 하나만 남깁니다.”
- 반증: 기존 Day One·사진·노트로 충분하거나, 3분 내 입력과 다음 계획 재열람이 반복되지 않으면 폐기한다.
- 가격 신호: [Day One 가격](https://dayoneapp.com/guides/premium-subscription/day-one-pricing-features-guide/), [TripIt Pro](https://www.tripit.com/web/pro/pricing), [Flighty](https://flighty.com/pricing). 인접 신호로만 쓰며 직접 결제 수요로 해석하지 않는다.

## Operator

- session: `01a0801d-c55e-71d2-b9ea-4d681c47675b`
- 운영 후보: 수동·로컬 우선 여행 후 취향 회수 로그.
- 금지: 지도/일정 자동화, GPS 기반 기록, Places API 추천, 결제·권한·배포·외부 발송.
- 최소 수집: 정확 위치, EXIF, 예약/여권/계정 정보, 원본 사진을 수집하지 않는다. 7일 검증은 동의·삭제·pause/stop/continue 규칙을 사전 고정해야 한다.

## 수렴과 다음 leaf

네 역할은 “기록량·자동화”가 아니라 **다음 선택에 재사용될 한 개의 판단**을 보존하는 후보로 수렴했다. 다만 인접 제품 가격은 직접 지불 의사 증거가 아니므로, T2.1에서 후보 비교·반증·7일 기준을 하나의 결론으로 고정하고 T2.2 Red에서 판정 충돌을 재검증한다.

공개 조사·참여자 모집·결제·사전결제·배포·외부 전송은 수행하지 않았다.
