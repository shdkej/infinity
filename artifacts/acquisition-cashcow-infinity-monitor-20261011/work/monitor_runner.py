#!/usr/bin/env python3
"""Manual public listing monitor. No scheduler, Notion schema mutation, or seller action."""
import argparse, datetime as dt, hashlib, json, sys, urllib.request
from pathlib import Path

SOURCES={"fello":"https://www.fello.io/products","listing":"https://listing.co/","sellernet":"https://sellernet.kr/products","flippa":"https://flippa.com/search","empire_flippers":"https://empireflippers.com/marketplace/digital-product-businesses-for-sale/","quiet_light":"https://quietlight.com/listings/","acquire":"https://app.acquire.com/all-listing"}
ROOT=Path(__file__).resolve().parents[3]
STATE=ROOT/"data/acquisition-cashcow-infinity-monitor-20261011/fingerprints.json"
LOG=ROOT/"data/acquisition-cashcow-infinity-monitor-20261011/runs.jsonl"

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--deadline",required=True); ap.add_argument("--dry-run",action="store_true"); a=ap.parse_args()
 now=dt.datetime.now(dt.timezone.utc); deadline=dt.datetime.fromisoformat(a.deadline.replace("Z","+00:00"))
 if now>=deadline: print(json.dumps({"status":"blocked","reason":"deadline_elapsed"})); return 2
 try: known=json.loads(STATE.read_text()).get("fingerprints",[]) if STATE.exists() else []
 except (OSError,json.JSONDecodeError): known=[]
 results={}; new=[]
 for site,url in SOURCES.items():
  try:
   req=urllib.request.Request(url,headers={"User-Agent":"infinity-acquisition-monitor/1.0"})
   with urllib.request.urlopen(req,timeout=20) as res: body=res.read(); status=res.status
   fp=hashlib.sha256(f"{site}|{url}".encode()).hexdigest(); dup=fp in known
   results[site]={"status":"ok","http":status,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),"fingerprint":fp,"duplicate":dup}
   if not dup:new.append(fp)
  except Exception as e: results[site]={"status":"error","error":str(e)[:240]}
 record={"checked_at":now.isoformat(),"deadline":deadline.isoformat(),"dry_run":a.dry_run,"sources":results,"new_fingerprints":len(new)}
 LOG.parent.mkdir(parents=True,exist_ok=True); LOG.open("a",encoding="utf-8").write(json.dumps(record,ensure_ascii=False)+"\n")
 if new: STATE.write_text(json.dumps({"fingerprints":known+new},ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":"ok","new_fingerprints":len(new),"errors":sum(v["status"]=="error" for v in results.values()),"log":str(LOG)})); return 0
if __name__=="__main__": sys.exit(main())
