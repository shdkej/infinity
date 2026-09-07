# T5.1 배포·라이브 근거·시간 원장

## 검증 체인

| 구간 | 검증값 | 시각 |
| --- | --- | --- |
| Space 구현 커밋 | `caad68dd0048264e66d7fb093f8ef194a9ef4c4e` — evidence drawer 닫기 뒤 초점 복구 | 2026-09-07 14:34:23 UTC / 16:34:23 Europe/Rome (CEST) |
| 배포 CI | [GitHub Actions run 34133686917](https://github.com/shdkej/space/actions/runs/34133686917) — `success`, head SHA 일치 | 생성 14:34:27 UTC / 16:34:27 CEST; 완료 14:35:12 UTC / 16:35:12 CEST |
| live 관찰 | [safety-map-experiment-03](https://safety-map-experiment-03.aws.shdkej.com/) | 2026-09-07 14:42:44 UTC / 16:42:44 CEST |

마감은 2026-09-08 06:00 UTC / 08:00 Europe/Rome (CEST)이며, 위의 구현·배포·관찰은 모두 그 전이다. 현재 관찰된 HTTP 응답은 `200`, `Last-Modified: 2026-09-07 14:34:48 UTC`이다.

## 제한된 라이브 관찰

- live HTML에 `공개 경험`, `공식 맥락`, `NO SCORE`, `NO ROUTE`, `NO TRACKING` 문구가 있다.
- 기존 T3·T4의 실제 렌더 증거는 Termini 검색→넓은 허브 영역→근거 drawer, 390px drawer 닫기 초점 및 첫 출처 링크 도달을 확인했다.
- 이 관찰은 넓은 Roma Termini 환승 허브의 행동 보조 UI만 다룬다. 출처 진위·실시간성, 안전/위험 사실·발생률, 전체 네트워크 감사를 보증하지 않는다.

## 운영·rollback 경계

- 이번 leaf에서 새 배포·rollback·출처 수집·telemetry SDK/쿠키/저장/전송을 실행하지 않았다.
- rollback 판단 기준은 (1) live HTTP 실패, (2) Termini drawer 또는 출처 링크 누락, (3) 점수·경로·핀·안전 주장 경계 회귀다.
- 위 기준이 관찰되면 책임 있는 Space 배포 경로에서 직전 정상 SHA로 rollback한 뒤, HTTP·drawer·출처 링크·경계 문구를 다시 검증한다. 현재는 trigger가 없어 rollback하지 않았다.

## 역할 수렴

- **Planner:** SHA → 성공 run → live URL → UTC/CEST 관찰 순서를 재현 가능하게 남긴다.
- **Developer:** 구현 SHA와 CI head SHA 일치, live 200 및 static response headers를 확인했다.
- **Marketer:** 행동 문구·넓은 허브·출처/한계만 허용하며 위험/안전·실시간성 과장은 금지한다.
- **Operator:** rollback 조건과 재검증은 기록하되, 실패 trigger 없이 실행하지 않는다.
