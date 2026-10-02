# GitHub 리서치 스킬 후보 — 최종 비교 브리프

## 결론

- **기본 도입: 0개.** 현재 `deep-research` + `agent-reach` + Infinity의 plan/trace/Red/HTML report 계약을 유지한다.
- **조건부 보류: Kang-chen의 문헌검토 하위 기능.** 저장소 라이선스, 실제 의존성·외부 호출·데이터 전송 경로를 재확인하고 별도 승인을 받기 전에는 설치 후보가 아니다.
- 이 결론은 2026-09-12의 commit 고정 관찰 스냅샷이며, 설치 적합성·호환성·성능을 증명하지 않는다.

## 비교 결정

| 후보 | 결정 | 근거 요약 | 재개/변경 조건 |
|---|---|---|---|
| PracticalSwan/agent-skills | 비도입 | 1차 출처·fallback은 `deep-research`와 중복하고 background-agent 지시가 Infinity 역할/trace 계약과 충돌 가능 | 현재 계약을 해치지 않는 별도 기능이 commit 고정 근거로 확인될 때 |
| pbi-agent/skills | 비도입 | repo 라이선스 부재, 별도 `research/<slug>` 상태 원장 요구 | 명시적 라이선스와 Infinity와 공존 가능한 상태 경계가 확인될 때 |
| drader/researcher_agent | 비도입 | CC BY-NC 4.0 표면 및 human-approval 운영 모델 | 사용 범위·라이선스·승인 모델이 현재 dispatcher와 양립할 때 |
| CODE-SAURABH/OpenSkills | 비도입 | `SKILL.md` 시작 구분 형식 불확실, primary/secondary validation은 기존 연구 흐름과 중복 | 호환 형식과 독립적인 검증 가치를 확인할 때 |
| Kang-chen/Agent-skills | **hold** | DOI 중복 제거·screening·citation traversal은 문헌검토에 한해 비중복 가능성이 있으나 repo-level 라이선스와 외부 의존성이 미확인 | 아래 승인 전 파일럿 설계의 모든 시작 조건이 충족될 때 |
| krzysztofdudek/ResearcherSkill | 비도입 | `.lab/`·branch·반복 코드 실험 중심으로 현재 공개자료 조사와 범위·운영 비용이 다름 | 연구 대상이 코드 최적화 실험으로 명확히 전환될 때 |

각 후보의 commit 고정 README·실제 `SKILL.md`·LICENSE/명시적 부재·default-branch HEAD 동치는 [근거표](../work/github-candidate-evidence.md#t12a-재현-레코드--같은-commit에서-직접-다시-연-표면)에 있다.

## 비도입·보류의 세 가지 이유

1. **중복:** primary-source 조사, 출처 비교, 한계 보고는 기존 `deep-research`·`agent-reach`와 Infinity 계약이 이미 제공한다.
2. **권리·형식 불확실성:** 라이선스 부재·비상업 라이선스·비표준 frontmatter는 기본 도입의 근거가 되지 않는다.
3. **운영 비용:** 별도 상태 원장, background agent, write/branch, sync, 외부 API·도식 생성 요구는 현재의 안전·감사 경계와 충돌하거나 확인되지 않았다.

## 승인 전 파일럿 설계 — 실행하지 않음

**목적:** Kang-chen의 문헌 검색·DOI dedupe·screening·citation traversal 중 필요한 부분이 Infinity의 근거 추적을 실제로 보완하는지 판단한다. 실제 환경·설치·클론·네트워크 연결을 만들지 않는 설계 문서다.

### 시작 전 필수 승인·증빙

1. 사용하려는 하위 파일과 저장소의 라이선스가 재사용 범위에 맞는지 확인한다.
2. 특정 하위 `SKILL.md`, 연결 스크립트, GitHub Actions, 의존성 목록, 외부 API/DB/telemetry·egress 목적지, 기록 데이터가 commit 고정 근거로 확인된다.
3. 사용자가 단일 학술 질문 1건과 격리 검증 실행을 별도로 승인한다.
4. 격리 환경은 no-secret, egress deny-by-default이며 계정 연결·유료 API·개인 데이터 반입을 허용하지 않는다.

### 승인 뒤에만 가능한 제한 범위

- 단일 학술 질문 1건에서 DOI dedupe, screening rubric, citation traversal의 **부분 기능**만 관찰한다.
- 성공은 ‘후보를 더 많이 모음’이 아니라, Infinity의 claim/source/limit 기록보다 출처 추적이나 제외 사유를 검증 가능하게 추가하는 경우다.
- 생성물이 있다면 읽기 전용 fixture 1건과 폐기 가능한 임시 격리 경로 안에만 두며, 로그·해시·삭제 확인만 남긴다. 기존 Infinity 원장·스킬·설정은 수정하지 않는다.

### 재현성 계약 — 실제 승인 뒤에만 사용

- 임시 경로는 실행 시점에 새로 만든 단일 디렉터리로 한정하고, 기존 workspace·skill registry 밖에 둔다. 결과 기록에는 생성 경로, 파일 목록, 각 파일 해시, 삭제 확인을 남긴다.
- fixture manifest는 질문 ID, 공개 출처 URL, 허용된 입력 파일 해시만 담는다. 사용자 데이터·계정 데이터·시크릿은 포함하지 않는다.
- 비교표는 기존 Infinity와 부분 기능 결과를 `claim`, `source`, `limit`, `exclusion_reason` 네 필드로만 대조한다. “더 많은 결과”는 성공 지표가 아니다.
- cleanup 검증은 임시 경로가 비어 있거나 제거됐다는 확인을 증거로 남기는 것으로 끝난다. workspace·전역 스킬·설정에는 어떤 변경도 남기지 않는다.

### 즉시 중단·보류 조건

- 라이선스·의존성·외부 호출·데이터 전송 중 하나라도 확인되지 않음
- 네트워크 허용, 계정 연결, 시크릿 입력, 유료 API, 자동 설치·sync·스크립트 실행 요구
- 기존 근거 추적보다 검증 가능한 차이가 없음

중단 시 생성물을 삭제하거나 격리 환경 자체를 폐기하고, 설치·전역 설정·기존 스킬에는 변경을 남기지 않는다.

## 다음 판단

현재는 도구를 추가하지 않는 것이 결론이다. 파일럿을 실제로 검토하려면 위 시작 조건을 증빙한 뒤, 사용자 승인 경계에서 별도 intent로 다룬다.
