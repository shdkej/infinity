#!/usr/bin/env python3
"""Append conservative, evidence-linked service descriptions to Notion pages.

Only page body blocks are appended. Database properties/schema are never patched.
"""
import argparse, hashlib, json, os, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

DB = "3f517bf7-599f-8176-8e1a-cddf002cf70b"
VERSION = "2022-06-28"
MARKER = "서비스 설명"

LAST_REQUEST = 0.0

def api(method, path, payload=None):
    global LAST_REQUEST
    # Notion's public API is rate limited; keep a conservative request cadence.
    wait = 0.38 - (time.monotonic() - LAST_REQUEST)
    if wait > 0: time.sleep(wait)
    data = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
    req = Request("https://api.notion.com" + path, data=data, method=method, headers={
        "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
        "Notion-Version": VERSION, "Content-Type": "application/json",
    })
    try:
        with urlopen(req, timeout=60) as resp:
            LAST_REQUEST = time.monotonic()
            body = resp.read().decode()
            return json.loads(body) if body else {}
    except HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        if exc.code == 429:
            try: retry = max(5, int(json.loads(detail).get("additional_data", {}).get("retry_after", 30)))
            except Exception: retry = 30
            time.sleep(retry)
            return api(method, path, payload)
        raise RuntimeError(f"{method} {path} -> {exc.code}: {detail[:500]}")

def plain(items):
    return "".join(x.get("plain_text", x.get("text", {}).get("content", "")) for x in (items or []))

def pages():
    out, cursor = [], None
    while True:
        payload = {"page_size": 100}
        if cursor: payload["start_cursor"] = cursor
        got = api("POST", f"/v1/databases/{DB}/query", payload)
        out.extend(got.get("results", []))
        if not got.get("has_more"): return out
        cursor = got["next_cursor"]

def title_of(page):
    for prop in page.get("properties", {}).values():
        if prop.get("type") == "title": return plain(prop.get("title"))
    return ""

def rich(page, name):
    prop = page.get("properties", {}).get(name, {})
    return plain(prop.get("rich_text"))

def source_url(page):
    prop = page.get("properties", {}).get("출처", {})
    return prop.get("url") or "미확인"

def audience(title):
    t = title.lower()
    if "amazon" in t or "fba" in t or "shopify" in t: return "온라인 쇼핑 고객을 대상으로 하는 것으로 보임"
    if "saas" in t or "software" in t or "technology" in t: return "해당 업무를 수행하는 기업·팀을 대상으로 하는 것으로 보임"
    if "app" in t or "ai" in t or "mobile" in t or "keyboard" in t: return "앱 사용자를 대상으로 하는 것으로 보임"
    if "blog" in t or "site" in t or "media" in t: return "온라인 콘텐츠 이용자·광고주 가능성이 있으나 구체 고객은 미확인"
    return "구체적인 고객군은 원문 상세 확인 전 미확인"

def model(title):
    t = title.lower()
    if "amazon" in t or "fba" in t or "shopify" in t: return "상품 판매·전자상거래 수익 모델로 보이나 가격·마진·반복매출 구조는 미확인"
    if "saas" in t or "software" in t: return "소프트웨어 구독 또는 사용료 모델 가능성이 있으나 과금 주기는 미확인"
    if "app" in t or "ai" in t or "mobile" in t: return "앱 판매·구독·광고·인앱결제 중 어느 방식인지 미확인"
    if "blog" in t or "site" in t or "media" in t: return "광고·제휴·콘텐츠 판매 가능성이 있으나 실제 수익원은 미확인"
    return "수익 방식은 공개 근거만으로 미확인"

def description(row):
    title = row.get("title") or "제목 미확인"
    url = row.get("source_url") or "미확인"
    fit = row.get("fit_comment") or "미확인"
    # Preserve the original evidence verbatim but cap length for a compact page block.
    fit = re.sub(r"\s+", " ", fit).strip()[:520]
    return (f"{MARKER}\n"
            f"무엇을 하는지: 원문 제목상 ‘{title}’ 사업·서비스를 제공하거나 운영하는 후보로 보입니다.\n"
            f"대상 고객: {audience(title)}.\n"
            f"수익 방식: {model(title)}.\n"
            f"인수 후 운영: 기존 서비스·판매·콘텐츠 운영을 이어가는 형태로 보이지만, 인수 후 필요한 운영 인력·업무·이전 범위는 미확인입니다.\n"
            f"원문 근거: 제목 ‘{title}’; source_url {url}; 기존 적합성 근거 ‘{fit}’.\n"
            f"미확인: 상세 기능, 실제 고객군, 확정 수익원, 운영 이전 가능 여부는 원문 상세 확인 전 미확인.")

def block(text):
    return {"object":"block", "type":"paragraph", "paragraph":{"rich_text":[{"type":"text", "text":{"content":text}}]}}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    ledger = [json.loads(line) for line in Path(args.ledger).read_text().splitlines() if line.strip()]
    by_id = {r["page_id"]: r for r in ledger}
    live = pages()
    before = {p["id"]: hashlib.sha256(json.dumps(p.get("properties",{}), sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in live}
    if len(live) != len(ledger): raise RuntimeError(f"ledger/live mismatch: {len(ledger)} vs {len(live)}")
    writes = skips = 0
    events = []
    for i, page in enumerate(live, 1):
        pid = page["id"]
        row = by_id.get(pid)
        if not row: raise RuntimeError(f"page absent from ledger: {pid}")
        existing = rich(page, "사용자 맞춤 코멘트")
        if MARKER in existing:
            skips += 1; events.append({"page_id":pid,"action":"skip_existing"}); continue
        text = description(row)
        target = (existing + "\n\n" + text).strip() if existing else text
        if args.write:
            api("PATCH", f"/v1/pages/{pid}", {"properties":{"사용자 맞춤 코멘트":{"rich_text":[{"type":"text","text":{"content":target[:2000]}}]}}})
            writes += 1; events.append({"page_id":pid,"action":"append","sha256":hashlib.sha256(text.encode()).hexdigest()})
            time.sleep(0.35)
        else:
            events.append({"page_id":pid,"action":"would_append","sha256":hashlib.sha256(text.encode()).hexdigest()})
    after = pages()
    after_props = {p["id"]: hashlib.sha256(json.dumps(p.get("properties",{}), sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in after}
    changed = [pid for pid in before if before[pid] != after_props.get(pid)]
    result = {"database_id":DB,"ledger_rows":len(ledger),"live_rows_before":len(live),"live_rows_after":len(after),"write_mode":args.write,"writes":writes,"skips":skips,"property_changes":changed,"events":events}
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("ledger_rows","live_rows_before","live_rows_after","write_mode","writes","skips","property_changes")}, ensure_ascii=False))
    if changed: raise SystemExit("FAIL: database properties changed")
    if len(after) != 382: raise SystemExit("FAIL: live row count changed")

if __name__ == "__main__": main()
