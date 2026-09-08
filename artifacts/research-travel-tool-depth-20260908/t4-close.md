# T4.3 — C4: 다음 실험 기준 마감

## 결론

**`no-build/hold`를 유지한다.** 현재 문서 검토와 Red PASS는 실제 프로토타입, 사용자 효용, 재사용, 반복 사용, 직접 WTP, 가격 또는 출시의 증거가 아니다.

## 다음에 허용되는 최소 범위

별도 승인된 후속 Intent의 **합성·비식별·로컬 fixture lifecycle 검토**만 가능하다.

- 카드 2건 이상, 고정 3필드: `장면 → 유지/피함 → 다음 기준`
- 검색·태그·위치·지도·추천·AI·알림 없이 시간순 수동 목록만 사용
- `생성 → 목록 → 지정 카드 수동 열람 → 비식별 집계 export → 단일 삭제 후 목록/열람/export 부재 → 전체 삭제 후 fresh read 빈 상태`를 결정적으로 assertion
- 보존값은 fixture hash, 레코드 수, assertion별 pass/fail만; fixture 원문·개인 경험처럼 보이는 prose는 보존하지 않음

fixture PASS의 다음 단계도 **study-design review**일 뿐이며, 행동효용·재사용·WTP·출시 결론이나 실제 연구 실행의 승인으로 해석하지 않는다.

## Stop / hold

다음 중 하나라도 있으면 즉시 중단·삭제하고 `no-build/hold`를 유지한다.

1. 실제 또는 식별 가능한 데이터, 식별 자유 텍스트, 사진/EXIF/위치/예약·동행인 정보의 혼입
2. backup·sync·analytics·로그 영속, 계정·API·네트워크 동기화·텔레메트리·배포의 포함
3. lifecycle assertion 실패 또는 고정 3필드·시간순 수동 열람 계약의 사후 변경
4. 이후 승인된 연구에서 기존 자료 동등·우세, 저널/리스트/플래너 환원, 저장 기준 인용 부재 등 Stop/Discard 신호의 발생

## 승인 경계

참여자 모집·연락·실제 데이터 수집·결제·사전결제·외부 전송/발송과, 실제 선택의 동일 과업 비교는 fixture 검토와 별개의 명시적 승인 및 동의·최소수집·삭제 계약이 있는 후속 Intent 없이는 시작할 수 없다.

## 역할 수렴

- **Planner:** fixture lifecycle PASS 뒤에도 study-design review만 허용한다.
- **Developer:** hash·레코드 수·assertion 결과만 남기는 로컬 결정적 lifecycle을 요구한다.
- **Marketer:** fixture를 사용자 이해·행동 효용·WTP의 근거로 해석하지 않는다.
- **Operator:** 실제·식별 데이터나 외부 연결이 발견되면 중단·삭제하며 승인 경계를 분리한다.

## 검증

- T4.2 Red PASS와 fixture-only/no-build 계약을 재확인했다.
- 외부 모집·연락·실제 데이터 수집·결제·배포·발송은 수행하지 않았다.
