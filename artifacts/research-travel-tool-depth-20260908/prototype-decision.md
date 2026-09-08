# T4.1 — 로컬 프로토타입 판단 기준

## 판정

**fixture-only decision contract ready; prototype remains `no-build/hold`.**

이 leaf는 로컬 합성 fixture를 미래에 검토할 수 있는 판단 기준만 고정한다. 프로토타입 구현, 실제 사용자·참여자 데이터 처리, 외부 연동·배포는 수행하거나 승인하지 않는다.

## 허용될 수 있는 fixture 범위

- 합성·비식별 토큰만 사용한 카드 2건 이상.
- 고정 카드 스키마: `장면 → 유지/피함 → 다음 기준` 3필드.
- 시간순 수동 목록 열람만 허용. 검색·태그·필터·위치·지도·추천·AI·알림·자동 재노출은 제외.
- 결정적 lifecycle 확인: `생성 → 시간순 목록 → 사전 지정 카드 수동 열람 → 비식별 집계 export → 단일 삭제·목록/열람/export 부재 확인 → 전체 삭제·fresh read 빈 상태`.
- 허용 필드: 합성 fixture ID, 비교쌍 ID, 3필드의 합성 토큰, 경과 시간, actual/hypothetical 라벨, 기준 인용 boolean, 채택/거절 코드.

## 통과 기록과 한계

fixture 결과에는 hash·레코드 수·각 lifecycle assertion의 pass/fail만 남긴다. fixture prose나 개인 경험처럼 보일 수 있는 원문은 보존하지 않는다.

fixture 통과는 **로컬 구현·측정 계약 준비성**만 뜻한다. 실제 사용자 이해, 다음 선택 기여, 재사용, 반복성, 타깃 적합성, WTP, 가격 수용성, 수요 또는 출시 가능성을 입증하지 않는다. fixture 결과를 Continue 수치·반복 사용·전환·WTP에 합산하지 않는다.

## `no-build/hold` 게이트

다음 중 하나라도 해당하면 prototype은 고려조차 보류한다.

1. 3필드 스키마, 3분 무보정 입력 기준, 시간순 수동 열람 또는 동일 과업 비교 순서가 사후 변경됨.
2. fixture가 합성·비식별임을 확인할 수 없거나, 금지 필드·식별 자유 텍스트·사진·위치·예약 정보가 들어감.
3. export/delete/re-query 불가 assertion을 결정적으로 증명하지 못함.
4. 실제 다음 선택·저장 기준 명시 인용·기존 자료 대비 추가 근거라는 사전등록 조건이 승인된 후속 범위에서도 충족되지 않음.
5. 기존 자료가 동등·우세하거나, 저널/사진 보관·장소 리스트·플래너·추천 수요로 환원되거나, 다른 Stop/Discard 신호가 하나라도 성립함.

모든 fixture assertion이 통과해도 다음 행동은 **승인 게이트가 있는 study-design review**뿐이다. 실제 참여자 모집·연락·데이터 수집·결제·계정·API·네트워크 동기화·텔레메트리·배포·외부 발송은 별도 승인 없이는 금지한다.

## 역할 수렴

- **Planner:** 합성 fixture, 3필드, 수동 열람, lifecycle 증거를 사전 조건으로 고정하고 경계 실패 시 hold.
- **Developer:** 합성 데이터만으로 lifecycle assertion·비식별 export·delete 재조회 불가를 검증할 수 있어야 하며, 실제 데이터와 외부 연동은 제외.
- **Marketer:** fixture는 표현과 판정 규칙의 명료성만 확인한다. 사용자의 행동 효용·반복성·WTP를 검증하거나 주장하지 않는다.
- **Operator:** 저장은 runtime/local fixture 한정이며 backup·sync·analytics·로그 영속을 허용하지 않는다.
