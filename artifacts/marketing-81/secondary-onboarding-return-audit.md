# marketing-81 Virtue 첫 저장 후 홈 복귀 secondary onboarding 감사표

## Goal

첫 저장 또는 첫 판단 뒤 홈으로 돌아온 사용자가 다시 처음 사용자처럼 읽히지 않도록, 기존 홈 표면만 기준으로 `현재 문장 / 사용자 상태 / 다음 행동 브리지 / 잡별 오독 위험 / 추천안`을 한 표로 정리한다.

## Inherited Learning

- `marketing-80`: 저장 성공 뒤에도 `최근 덕행` empty-state가 남아 있으면 first feedback consistency가 깨질 수 있다.
- `marketing-79`: J1/J2/J4의 first value는 `deed_saved`, J3의 first value는 `deed_judged`다.
- `marketing-43`: 반환 사용자는 generic welcome보다 직전 가치와 연결된 재초대 이유가 필요하다.
- `marketing-70`: 홈 empty-state 문제는 CTA 부족보다 proof/next-step preview 부족으로 읽는 편이 안전하다.

## Audit Table

| Surface | Current copy / state | Implied user state | Recommended next-action bridge | Job-specific misread risk | Recommendation |
| --- | --- | --- | --- | --- | --- |
| Hero headline | `오늘 1덕만 쌓아볼까요?` | 아직 시작하지 않은 사용자 | 첫 가치 이후에는 유지하지 말고, 반환 사용자에게는 "방금 남긴 흐름을 한 번 더 이어보기" 계열 문장으로 분기 필요 | J1/J2/J4는 이미 저장했는데도 첫 입력 전 사용자처럼 느낄 수 있음. J3는 이미 AI 판단을 봤는데 출발선으로 되감긴 느낌이 날 수 있음 | 홈 진입 시 first value 직후 상태가 확인되면 hero 보조문구만이라도 반환형 브리지로 바꾼다. 신규 UI 추가 없이 문장 분기만 proposal-only |
| Primary CTA | `오늘 덕 쌓기` | 새로운 기록을 바로 시작할 준비 | 반환 사용자에게는 CTA 자체보다 "왜 한 번 더 눌러야 하는지" 한 줄 이유가 필요 | J1/J2/J4는 누적/연속성 맥락이 없으면 반복 이유가 약해짐. J3는 새 사례를 다시 AI로 보고 싶은지 여부가 갈림 | CTA 라벨은 유지 가능. 대신 인접 보조문구로 J1/J2/J4는 "하나 더 남겨 누적 보기", J3는 "다른 사례도 AI로 다시 보기"처럼 목적을 분리 |
| Summary / count card | 누적 덕 수치가 보일 수 있음 | 제품이 방금 무언가를 기억했다는 신호 | 숫자만으로는 "다음에 무엇을 할지"가 안 보이므로, 반환형 안내가 없으면 성과와 행동이 분리됨 | J2는 누적형이라 다음 행동 브리지가 특히 필요. J1/J4는 저장은 했지만 반복 가치가 약해 보일 수 있음 | 누적 카드 하단 보조문구 후보를 second-step bridge 우선 검토 표면으로 둔다 |
| `최근 덕행` empty state | `아직 기록이 없어요.` | 아직 저장/기록이 없는 상태 | first value 직후 사용자에게는 부정확한 상태 설명이므로 반환형 문장이나 gating 정렬 필요 | 저장 성공 뒤에도 empty-state가 보이면 J1/J2/J4 신뢰를 가장 크게 깎음. J3는 저장 전 종료가 정상일 수 있어 전면 제거보다 상태 분기 필요 | 가장 우선순위 높은 수정 포인트. `deed_saved` 이후에는 empty-state 문구를 숨기거나 sample/proof/recency형 문장으로 대체하는 proposal-only 후속 intent 권고 |

## Safe Bridge Candidates

- J1: "방금 남긴 한 가지처럼, 오늘 하나만 더 기록해도 흐름이 쌓여요."
- J2: "조금씩 쌓인 기록이 패턴이 되니, 이어서 하나 더 남겨보세요."
- J3: "다른 사례도 AI 관점으로 다시 보면 내 기준이 더 선명해져요."
- J4: "이번 기록을 남긴 김에, 다음에도 같은 기준으로 한 줄 더 붙여보세요."

## What This Cycle Learned

- secondary onboarding의 핵심은 새로운 교육이 아니라 first value 직후의 다음 한 걸음 명료화다.
- Virtue 홈에서는 새로운 CTA보다 `반환 사용자를 첫 사용자처럼 다시 설명하는 표면`을 줄이는 편이 더 안전하다.
- 가장 위험한 충돌은 `누적/요약 신호가 보이는데 empty-state는 여전히 미기록 사용자처럼 말하는 상태`다.

## Handoff Rule

- 다음 implementation/proposal intent는 홈 전체 리디자인이 아니라 `hero 보조문구`, `summary card 보조문구`, `최근 덕행 empty-state gating` 세 표면만 범위로 제한한다.
- 신규 이벤트, tracking/privacy, 공개 발송, 배포 없이 문장/상태 분기 proposal-only로 다룬다.
