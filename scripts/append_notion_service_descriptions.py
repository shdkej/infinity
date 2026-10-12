#!/usr/bin/env python3
"""Append conservative, evidence-linked service descriptions to Notion pages.

Only the existing `사용자 맞춤 코멘트` property is rewritten. Database properties/schema are never patched.
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

def props_without_comment(page):
    props = dict(page.get("properties", {}))
    props.pop("사용자 맞춤 코멘트", None)
    return props

def source_url(page):
    prop = page.get("properties", {}).get("출처", {})
    return prop.get("url") or "미확인"

def audience(title):
    t = title.lower()
    if any(x in t for x in ("amazon", "fba", "shopify", "apparel", "accessories", "food", "beverage", "beauty", "personal care")):
        return "상품을 찾고 구매하는 일반 소비자"
    if any(x in t for x in ("saas", "software", "technology", "crm", "workflow", "business")):
        return "반복 업무를 줄이려는 기업·팀"
    if any(x in t for x in ("app", "ai", "mobile", "keyboard", "gaming")):
        return "해당 기능을 직접 쓰려는 앱·모바일 사용자"
    if any(x in t for x in ("blog", "site", "media", "news", "education", "content")):
        return "정보·콘텐츠를 찾는 방문자와 광고주/제휴사"
    if any(x in t for x in ("home", "bed & bath", "romance", "lifestyle")):
        return "관련 제품이나 정보를 찾는 생활 소비자"
    return "정확한 고객군은 원문 상세 확인 필요"

def category(title):
    """Turn marketplace taxonomy into a plain-language service description."""
    t = title.lower()
    if "차량 출입관리" in title: return "차량의 출입을 기록하고 관리하는 시스템"
    if "amazon" in t or "fba" in t: return "아마존 상품 판매·재고·주문을 운영하는 온라인 사업"
    if "shopify" in t or "ecommerce" in t: return "온라인 쇼핑몰에서 상품을 판매하는 사업"
    if "personal care" in t or "beauty" in t: return "미용·개인관리 상품이나 서비스를 판매하는 사업"
    if "food" in t or "beverage" in t: return "식음료 상품을 판매하거나 관련 정보를 제공하는 사업"
    if "apparel" in t or "accessories" in t or "gifts" in t: return "의류·액세서리·선물 상품을 판매하는 사업"
    if "bed & bath" in t or "home" in t: return "집 안에서 쓰는 생활용품을 판매하는 사업"
    if "app" in t or "mobile" in t: return "모바일에서 특정 문제를 해결하는 앱"
    if "ai" in t: return "AI를 이용해 특정 작업을 자동화하거나 보조하는 소프트웨어"
    if "software" in t or "saas" in t or "technology" in t: return "웹에서 반복 업무를 처리하게 돕는 소프트웨어"
    if "gaming" in t: return "게임을 제공하거나 게임 이용자를 대상으로 하는 서비스"
    if any(x in t for x in ("blog", "media", "news", "education", "content")): return "특정 주제의 글·정보·콘텐츠를 제공하는 웹사이트"
    if "romance" in t or "lifestyle" in t: return "생활·관심사 관련 제품이나 정보를 제공하는 온라인 사업"
    return "서비스의 정확한 기능은 원문 상세 확인 필요"

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
    kind = category(title)
    return (f"{MARKER}\n"
            f"한줄 설명: {kind}입니다.\n"
            f"주 사용자는 {audience(title)}입니다. 실제로는 관련 상품을 사거나, 정보를 읽거나, 반복 업무를 처리할 때 이용합니다.\n"
            f"돈을 버는 방식: {model(title)}.\n"
            f"인수 후 운영: 먼저 상품·콘텐츠·앱이 실제로 계속 작동하는지와 고객 유입 경로를 확인해야 합니다. 운영 인력, 공급처·코드·계정 이전 범위는 원문 상세 확인 필요입니다.\n"
            f"근거와 한계: 제목 ‘{title}’, 출처 {url}. 제목과 공개 목록만으로 분류한 설명이므로 세부 기능·고객·수익원은 원문 상세 확인이 필요합니다.")

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
    before = {p["id"]: hashlib.sha256(json.dumps(props_without_comment(p), sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in live}
    if len(live) != len(ledger): raise RuntimeError(f"ledger/live mismatch: {len(ledger)} vs {len(live)}")
    writes = skips = 0
    events = []
    for i, page in enumerate(live, 1):
        pid = page["id"]
        row = by_id.get(pid)
        if not row: raise RuntimeError(f"page absent from ledger: {pid}")
        existing = rich(page, "사용자 맞춤 코멘트")
        # Replace the prior generic block instead of appending another one.
        if MARKER in existing:
            # Handle both the first-generation `서비스 설명:` block and the
            # newer `서비스 설명` block, including a previous rewrite.
            existing = re.split(r"서비스 설명(?::|\n)", existing, maxsplit=1)[0].rstrip()
        text = description(row)
        target = (existing + "\n\n" + text).strip() if existing else text
        if args.write:
            api("PATCH", f"/v1/pages/{pid}", {"properties":{"사용자 맞춤 코멘트":{"rich_text":[{"type":"text","text":{"content":target[:2000]}}]}}})
            writes += 1; events.append({"page_id":pid,"action":"rewrite","sha256":hashlib.sha256(text.encode()).hexdigest()})
            time.sleep(0.35)
        else:
            events.append({"page_id":pid,"action":"would_rewrite","sha256":hashlib.sha256(text.encode()).hexdigest()})
    after = pages()
    after_props = {p["id"]: hashlib.sha256(json.dumps(props_without_comment(p), sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in after}
    changed = [pid for pid in before if before[pid] != after_props.get(pid)]
    result = {"database_id":DB,"ledger_rows":len(ledger),"live_rows_before":len(live),"live_rows_after":len(after),"write_mode":args.write,"writes":writes,"skips":skips,"non_comment_property_changes":changed,"events":events}
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("ledger_rows","live_rows_before","live_rows_after","write_mode","writes","skips","non_comment_property_changes")}, ensure_ascii=False))
    if changed: raise SystemExit("FAIL: non-comment database properties changed")
    if len(after) != 382: raise SystemExit("FAIL: live row count changed")

if __name__ == "__main__": main()
