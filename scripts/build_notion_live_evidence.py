#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
src = Path(sys.argv[1]); out = Path(sys.argv[2]); payload = json.loads(src.read_text()); rows = payload.get('results', [])
def text(prop): return ''.join(x.get('plain_text', '') for x in (prop or {}).get('rich_text', []))
def title(prop): return ''.join(x.get('plain_text', '') for x in (prop or {}).get('title', []))
with out.open('w') as f:
    for row in rows:
        p = row.get('properties', {})
        record = {'page_id': row.get('id'), 'title': title(p.get('후보명')), 'source_url': (p.get('출처') or {}).get('url'), 'rating': (p.get('별점') or {}).get('number'), 'rating_evidence': text(p.get('별점 근거/출처')), 'fit_comment': text(p.get('사용자 맞춤 코멘트')), 'judgment': text(p.get('판단 상태/신뢰도')), 'marker': text(p.get('플랫폼')), 'checked': (p.get('최종 확인') or {}).get('date', {}).get('start')}
        f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
print(json.dumps({'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'ledger_sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'rows': len(rows), 'has_more': payload.get('has_more'), 'ledger': str(out)}, ensure_ascii=False))
