# 온톨로지의 Knowledge Lab 적용 가능성

**권고:** 지금은 RDF/OWL 온톨로지나 그래프 DB를 도입하지 마십시오. 대신 공개 컴파일 문서만 대상으로 하는 **read-only 관계 레지스트리 v0**를 20개 assertion 또는 2주 동안 파일럿하고, 실제 검색·인계 효용이 입증될 때만 확대하십시오.

## 왜 이 결론인가

KL의 핵심은 `source → ingest 판정 → Agent Wiki 컴파일 → 공개 검색`의 출처·공개 경계입니다. OWL은 클래스·개체·속성·제약을 통한 정밀한 추론 모델이고, SKOS는 taxonomy·controlled vocabulary 같은 반정형 개념 체계에 맞습니다. 현재 KL에는 전자에 필요한 교차 도메인 추론 요구가 확인되지 않았고, 후자의 제한된 관계 표현만으로도 검색 회수성 가설을 검증할 수 있습니다.

| 선택지 | 효과 | 위험 | 판정 |
|---|---|---|---|
| 현행 유지 | 무위험 | 관계 기반 탐색 개선을 검증하지 못함 | 파일럿 전 기준선 |
| 관계 레지스트리 v0 | 명시 링크·근거 기반 관련 문서 탐색/감사 | 수동 검토 부채 | 권고 |
| full ontology/graph | 복잡 관계·추론 가능 | 이중 정본·drift·공개 경계 침범 | 보류 |

## 파일럿 계약

- 범위: 공개 컴파일 문서 20개 assertion, 2주 이내. raw/queued/private 경로는 금지.
- 레코드: `relation_id, subject_ref, predicate, object_ref, evidence_ref, source_revision, asserted_at, reviewer, review_state, deprecated, schema_version`.
- predicate(방향 고정): `addresses, supports, derived_from, contradicts, same_as_candidate, requires_review`. 자동 추론·자동 write-back은 금지.
- 정합성: 모든 assertion은 stable anchor 1개 이상; 표본 독립 검토 일치율 ≥90%; anchor 유효율 ≥95%.
- 효용: 실제 질의 3개 중 2개 이상에서 기존 경로 검색보다 탐색 단축 또는 누락 근거 발견이 있어야 합니다.
- 중단: anchor 소실, 정합성/효용 기준 미달, 소유자 부재, private/raw 노출, 재현 불가, 외부 SaaS·권한·스케줄 필요 중 하나라도 발생하면 소비를 중지하고 회고합니다.

## 사용자의 언어

‘온톨로지’가 아니라 **연결 지도**: “기록을 더 잘 분류하는 기능이 아니라, 지금 하는 일과 이어지는 예전 기록을 다시 보여주는 지도.” 자동 정답이 아닌 관련 기록 후보 제안으로 표현합니다.

## 근거와 한계

- [W3C OWL 2 Primer](https://www.w3.org/TR/owl2-primer/original.html): OWL은 classes, individuals, properties 및 정밀한 관계 모델을 제공.
- [W3C SKOS](https://www.w3.org/2004/02/skos/specs): taxonomy·thesaurus·controlled vocabulary를 위한 가벼운 모델.
- [W3C PROV](https://www.w3.org/ns/prov): provenance 교환 모델.
- KL `README.md`, `DOCUMENT_SEARCH_PIPELINE.md`: raw source·ingest·컴파일 공개 검색의 경계를 확인.

**한계:** 파일럿 전에는 관계 레지스트리가 실제 질의 품질을 개선한다는 증거가 없습니다. 따라서 구현/마이그레이션은 이 결정의 범위 밖입니다.
