#!/usr/bin/env python3
"""Three consecutive Slack callback continuations plus safety regressions."""
from __future__ import annotations
import json, subprocess, sys, tempfile, unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT = Path(__file__).with_name("process_slack_callbacks.py")
def future() -> str: return (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat().replace("+00:00", "Z")
class CallbackTest(unittest.TestCase):
 def setUp(self):
  self.dir = Path(tempfile.mkdtemp()); self.registry=self.dir/"registry.jsonl"; self.state=self.dir/"state.json"; self.outbox=self.dir/"outbox.jsonl"; self.intents=self.dir/"INTENTS.md"; self.artifacts=self.dir/"artifacts"
  entries=[]
  for n in range(1,4): entries.append(f"### [callback-test-{n}] 테스트 {n}\n- status: active\n- next_action: 대기\n")
  self.intents.write_text("# Intent Registry\n\n## Inbox\n\n## Active\n\n"+"\n".join(entries)+"## Waiting\n\n## Archive\n", encoding="utf-8")
 def event(self,n,value=None,thread="1788813179.680199",user="U1"):
  return {"event_id":f"evt-{n}","interactionType":"block_action","actionType":"button","signature_verified":True,"provider":"slack","workspace_id":"T1","channel_id":"C0BR41W31MM","message_ts":f"m-{n}","thread_ts":thread,"user_id":user,"value":value or f"continue-{n}","intent_id":f"callback-test-{n}","run_id":f"run-{n}","question_id":f"q-{n}"}
 def register(self,event,boundary="safe"):
  record={k:event[k] for k in ("provider","workspace_id","channel_id","message_ts","thread_ts","user_id","value","intent_id","run_id","question_id")}; record.update({"status":"sent","expires_at":future(),"label":"로컬 검증 시작","next_action":{"kind":"set_intent_next_action","next_action":f"후속 작업 {event['intent_id']}","approval_boundary":boundary,"approval_reason":"명시 승인 필요"}})
  with self.registry.open("a",encoding="utf-8") as h:h.write(json.dumps(record)+"\n")
  return record
 def invoke(self,event,fail_after_outbox=False,fail_after_dispatch=False):
  event_path=self.dir/(event["event_id"]+".json");event_path.write_text(json.dumps(event),encoding="utf-8")
  command=[sys.executable,str(SCRIPT),"--event",str(event_path),"--registry",str(self.registry),"--state",str(self.state),"--intents",str(self.intents),"--mock-outbox",str(self.outbox),"--artifacts",str(self.artifacts)]
  if fail_after_outbox: command.append("--test-fail-after-outbox")
  if fail_after_dispatch: command.append("--test-fail-after-dispatch")
  output=subprocess.check_output(command,text=True);return json.loads(output)
 def test_three_consecutive_callbacks_bind_dispatch_and_report_same_thread(self):
  for n in range(1,4):
   event=self.event(n);self.register(event);result=self.invoke(event);self.assertEqual(result["result"],"accepted");self.assertEqual(result["stages"], ["received","bound","claimed","dispatched","receipt_written","reported"])
   out=json.loads(self.outbox.read_text().splitlines()[-1]);self.assertEqual(out["destination"],{"channel":"slack","target":"C0BR41W31MM","reply_to":"1788813179.680199"});self.assertTrue(Path(result["report_path"]).is_file())
   duplicate=self.invoke(event);self.assertEqual(duplicate["result"],"duplicate_ignored")
  self.assertEqual(len(self.outbox.read_text().splitlines()),3); text=self.intents.read_text(); self.assertEqual(text.count("callback_last_event:"),3)
 def test_rejects_wrong_thread_and_requires_approval_without_dispatch(self):
  event=self.event(1);self.register(event);bad={**event,"event_id":"wrong-thread","thread_ts":"other"};self.assertEqual(self.invoke(bad)["result"],"rejected");self.assertNotIn("callback_last_event",self.intents.read_text())
  protected=self.event(2);self.register(protected,"public");result=self.invoke(protected);self.assertEqual(result["outcome"],"approval_required");self.assertNotIn("callback_last_event: evt-2",self.intents.read_text())
 def test_crash_after_outbox_keeps_durable_claim_and_never_replies_twice(self):
  event=self.event(3);self.register(event)
  with self.assertRaises(subprocess.CalledProcessError): self.invoke(event,True)
  self.assertEqual(len(self.outbox.read_text().splitlines()),1)
  replay=self.invoke(event);self.assertEqual(replay["result"],"delivery_unknown")
  self.assertEqual(len(self.outbox.read_text().splitlines()),1)
  self.assertIn("- status: waiting",self.intents.read_text());self.assertIn("delivery_unknown",self.intents.read_text())
 def test_crash_after_dispatch_becomes_waiting_without_delivery(self):
  event=self.event(3);self.register(event)
  with self.assertRaises(subprocess.CalledProcessError): self.invoke(event,fail_after_dispatch=True)
  self.assertFalse(self.outbox.exists())
  replay=self.invoke(event);self.assertEqual(replay["result"],"dispatch_uncertain")
  self.assertIn("dispatch_uncertain",self.intents.read_text())
 def test_outbound_registration_rejects_duplicate_binding(self):
  event=self.event(1); record=self.register(event); self.registry.unlink()
  source=self.dir/"outbound.json";source.write_text(json.dumps(record),encoding="utf-8")
  command=[sys.executable,str(SCRIPT),"--register",str(source),"--registry",str(self.registry)]
  self.assertEqual(json.loads(subprocess.check_output(command,text=True))["result"],"registered")
  self.assertEqual(json.loads(subprocess.check_output(command,text=True))["result"],"rejected")
if __name__=="__main__": unittest.main()
