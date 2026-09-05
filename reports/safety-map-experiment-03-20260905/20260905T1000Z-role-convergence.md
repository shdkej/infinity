# Experiment-03 역할 수렴 — 2026-09-05 10:00 UTC

## 실행 계약

Inbox의 `waiting` 표기는 role delegation 불가라는 과거 blocker와 충돌했습니다. 이번 dispatcher cycle에서 네 역할을 별도 세션으로 실제 실행했고, intent를 Active로 승격했습니다.

| 역할 | 세션 | 판단 | 채택 |
|---|---|---|---|
| Planner | `/root/role_safety03_planner` | experiment-02와 독립된 전역 지도 경험, 구현 전 T2.5 수렴 필요 | 독립 경로·명확한 leaf 순서 |
| Developer | `/root/role_safety03_developer` | 기존 `sites/safety-map/**`는 dirty legacy이며 재사용 불가 | `sites/safety-map-experiment-03/`만 생성 |
| Marketer | `/root/role_safety03_marketer` | 위험 점수 지도 대신 장소 탐색과 데이터 한계를 5초 안에 전달 | 검색 하나를 첫 행동으로, no-data 문장 유지 |
| Operator | `/root/role_safety03_operator` | 신규 domain/registry/Terraform/runtime config를 완전히 분리 | apply·origin allowlist·토큰 보호를 배포 전 게이트로 설정 |

## 수렴한 구현 계약

1. 새 앱은 `space/infra-aws-static-sites/sites/safety-map-experiment-03/`에만 만듭니다. legacy `sites/safety-map/**`는 읽기 전용입니다.
2. 전체화면 Mapbox canvas, 장소/도로 검색, zoom/pan, basemap layer만 제공합니다. 안전 점수·안전 경로·실시간 사건·위치 수집·개인정보 전송은 제외합니다.
3. 라이트 기본 Spatial Type에서 목적·첫 행동·no-data 경계를 Typography Rail로 제시합니다. 한국어 카피는 안전을 단정하지 않습니다.
4. 신규 도메인, Terraform apply, Mapbox origin allowlist와 protected runtime config는 배포 전에 명시적으로 재검증합니다. 토큰 값은 어떤 artifact·로그·커밋에도 기록하지 않습니다.
5. 다음 구현 leaf의 완료 증거는 새 경로만의 diff, legacy 경로 무변경 검사, README의 운영/토큰 경계입니다.

## 기각한 선택

- experiment-02 코드 복사 또는 기존 도메인 덮어쓰기: legacy 보호·독립 실험 계약 위반.
- 치안 점수/위험도/실시간 사건을 넣는 확장: 근거 없는 안전 판단 금지 경계 위반.
- role delegation 없이 단일 구현으로 하향: `multi_subagent_roles` 계약 위반.

## 다음 액션

T2.5 수렴 내용을 task plan에 상태로 기록한 뒤, T3.1 `독립 experiment-03 정적 사이트 경로 생성`을 명시적으로 Active로 전이하고 실행합니다.
