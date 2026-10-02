# promotion runtime·source discovery receipt

- 확인 시각: `2026-09-15T20:32:34Z`
- Infinity canonical: `eef528f067b4b01543151b3dfdc8d92c450854e5`
- Knowledge Lab source revision: `91826b078008e58e8eb2e69d067bfa96dae80faf` (`origin/main`과 동일)

## read-only 확인 결과

1. `source/openclaw-system/docs/PROMOTION_INDEX.md`는 `build_promotion_index.mjs`를 promotion-index의 생성 정본으로 지정합니다.
2. `source/openclaw-system/scripts/build_promotion_index.mjs`는 ingest manifest/index와 Agent Wiki outputs를 읽어 `data/promotion-index.json`을 생성합니다.
3. `source/openclaw-system/scripts/build_knowledge_loop.mjs`는 Knowledge Lab query log의 marker를 읽어 `data/knowledge-loop.json`을 생성합니다.
4. 사용자 crontab에서 확인된 관련 host job은 다음 둘뿐입니다: Infinity 10분 dispatcher와 6시간 `sync-ingest.sh`. promotion receipt/review를 실행하는 daily payload는 발견되지 않았습니다.

## 결론

T1.2 receipt schema를 구현하려면 **Knowledge Lab source tree의 generator와 실제 promotion runtime owner**가 같은 변경 범위에 들어와야 합니다. 현재 dispatcher 지시는 Infinity 파일만 commit/push하도록 제한하므로, generated `data/knowledge-loop.json`을 수동 편집하거나 새 schedule을 만들지 않습니다.

## 재개 조건

- runtime promotion payload 또는 그 owner가 read-only로 식별되고, 그리고
- Knowledge Lab source-tree 변경·검증·원격 반영이 이 Intent의 허용 범위로 명시될 것.

그 전까지 T1.2는 source artifact의 부재가 아닌 **generator/runtime ownership 미확정**으로 보류합니다.
