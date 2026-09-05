# T3.1 독립 experiment-03 경로 생성

## 결과

`space/infra-aws-static-sites/sites/safety-map-experiment-03/`를 새로 만들었습니다. 기존 `sites/safety-map/**`는 수정하지 않았습니다.

## 생성 경로

- `README.md`: 목적, no-data 안전 경계, token/runtime/deploy 경계, 다음 검증 범위를 기록했습니다.
- `src/.gitkeep`, `dist/.gitkeep`: 다음 구현과 배포 산출물의 독립 경계를 고정했습니다.

## 검증

- e03 README·source·dist 경로 존재: 통과
- `git diff --name-only`에 `sites/safety-map/` 변경 없음: 통과
- `git diff --check`: 통과
- Space 원격 SHA: `23d5acef2a609b884f4ef490d071cf14b8d9cda6` (`HEAD == origin/main`)

## 경계와 다음 액션

새 domain, Terraform registry/apply, Mapbox origin allowlist, protected runtime config는 아직 변경하지 않았습니다. 다음 leaf T3.2에서 새 경로에 전체 화면 canvas와 Typography Rail만 구현합니다.
