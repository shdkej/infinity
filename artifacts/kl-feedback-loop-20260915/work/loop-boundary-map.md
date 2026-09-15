# 승격 피드백루프 읽기 모델 경계 감사

## 결론

현재 `promotion-index`는 **승격 상태를 보여 주는 파생 읽기 모델**이고, `knowledge-loop`는 **이벤트를 집계하는 비어 있는 원장**입니다. 둘 다 후속 Intent 재사용이나 7–30일 결과 재평가를 아직 표현하지 않습니다. 따라서 다음 구현은 두 모델을 섞지 않고, 기존 `knowledge-loop.events`에만 append-only receipt를 추가하는 방식이 안전합니다.

## 검증한 source revision과 현재 계약

이 문서의 generator·문서 경로는 Infinity clean checkout이 아니라 read-only Knowledge Lab source tree에서 확인했습니다: `knowledge-lab@91826b078008e58e8eb2e69d067bfa96dae80faf` (원격 `origin/main`과 동일). Infinity `eef528f`에는 이 source tree가 포함되지 않으므로, 아래 경로는 Infinity 내부 구현 파일이라고 주장하지 않습니다.

| 표면 | 생성 정본 | 입력 | 현재 보장 | 이번 단계의 금지 |
|---|---|---|---|---|
| `data/promotion-index.json` | `source/openclaw-system/scripts/build_promotion_index.mjs` | `ingest/manifest.jsonl`, `ingest/INDEX.md`, Agent Wiki outputs | 원본 ↔ 명시적 outputs 연결과 `promotion_state` | 이름/문장 유사도로 재사용 관계 추론, 실행 receipt 저장 |
| `data/knowledge-loop.json` | `source/openclaw-system/scripts/build_knowledge_loop.mjs` | `logs/agent-wiki-query.md` 및 archive logs의 `knowledge-loop` marker | 이벤트 수와 7일 ingest/query/lint/open/resolved 집계 | historical metric 의미 변경, promotion index 덮어쓰기 |
| Archive 판정 | `scripts/check_knowledge_promotion.py` | KL archive, ingest index, Context Pack receipt | Archive 시 knowledge decision/receipt 일치 확인 | promotion 생성·재평가 실행 |
| Dispatcher | `scripts/run_dispatcher_cycle.sh` | 기존 단일 10분 host-owned watcher | clean checkout, lock, dispatch 준비 | 새 cron·systemd·외부 알림 경로 |

## 최소 추가 계약 (다음 leaf의 구현 범위)

`knowledge-loop.events`에 다음 필드만 추가합니다. 과거 event와 기존 `metrics` 키는 보존합니다.

```json
{
  "type": "promotion_receipt",
  "promotion_id": "stable-id",
  "source": "ingest source path",
  "targets": ["/docs/outputs/..."],
  "downstream_intent_id": "optional Infinity intent id",
  "outcome": "unknown|used|not_used|superseded",
  "review_due_at": "ISO-8601 UTC",
  "loop_state": "open|resolved"
}
```

`promotion-index`는 실제 승격 연결의 증거로 계속 읽고, receipt의 `downstream_intent_id`와 outcome은 별도 파생 지표로만 집계합니다. `review_due_at`은 기존 실행 경로가 확인된 뒤 그 **기존 경로**에서만 재평가합니다.

## 검증·운영 경계

- T1.2 전에는 `data/`와 cron/권한/외부 발송을 바꾸지 않습니다.
- 현재 crontab에서 확인된 것은 Infinity 10분 dispatcher와 6시간 ingest sync뿐이며, daily promotion job은 확인되지 않았습니다. T1.3에서 runtime payload를 read-only로 식별하기 전에는 dispatcher를 promotion job으로 가정하지 않습니다.
- fixture seam은 `build_knowledge_loop.mjs --output <temp-file>`와 marker가 든 임시 로그입니다. production output을 직접 생성하지 않습니다.
- 다음 검증 기본선: `python3 scripts/test_check_knowledge_promotion.py`, JSON parse, 그리고 새 순수 helper/fixture test입니다.

## 근거

- `source/openclaw-system/docs/PROMOTION_INDEX.md`
- `source/openclaw-system/scripts/build_promotion_index.mjs`
- `source/openclaw-system/scripts/build_knowledge_loop.mjs`
- `scripts/run_dispatcher_cycle.sh`
- `scripts/check_knowledge_promotion.py`

## 다음 결정

T1.2는 receipt schema와 derived metrics를 additively 구현하되, runtime promotion payload가 식별되지 않으면 T1.3은 구현 대신 정확한 runtime-owner blocker를 기록합니다.
