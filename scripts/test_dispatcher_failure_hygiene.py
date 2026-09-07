#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, tempfile, unittest
from pathlib import Path
SCRIPT = Path(__file__).with_name("safe_failure_alert.py")
class FailureHygieneTest(unittest.TestCase):
 def test_raw_bash_failure_becomes_safe_korean_thread_message(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory); detail=root/"detail.log"; outbox=root/"outbox.jsonl"
   raw="Bash failed: bash -lc deploy --token secret\nstderr: Traceback (most recent call last)"
   detail.write_text(raw)
   result=subprocess.run(["python3",str(SCRIPT),"--stage","terminal","--detail-file",str(detail),"--mock-outbox",str(outbox),"--channel","slack","--target","C0BR41W31MM","--reply-to","1788813179.680199"],check=True,capture_output=True,text=True)
   payload=json.loads(result.stdout); sent=json.loads(outbox.read_text())
   self.assertEqual(sent["destination"]["reply_to"],"1788813179.680199")
   self.assertEqual(sent["message"],payload["user_message"])
   for forbidden in ("Bash failed","bash -lc","stderr","Traceback","secret","exit="): self.assertNotIn(forbidden,sent["message"])
   self.assertIn("상태 보고",sent["message"])
 def test_bootstrap_failure_does_not_print_raw_git_error(self):
  script=Path(__file__).with_name("run_dispatcher_cycle.sh")
  # ROOT is fixed by the production script; exercise its early safe path by
  # replacing the git executable with a failing fixture instead.
  fake=Path(tempfile.mkdtemp()); (fake/"git").write_text("#!/bin/sh\necho 'Bash failed: secret command' >&2\nexit 1\n"); (fake/"git").chmod(0o755)
  env={"PATH":str(fake)+":/usr/bin:/bin","INFINITY_DISPATCHER_STATE_DIR":tempfile.mkdtemp(),"INFINITY_DISPATCHER_LOCK_FILE":str(fake/"lock")}
  result=subprocess.run(["bash",str(script)],env=env,capture_output=True,text=True)
  self.assertEqual(result.returncode,0)
  self.assertIn("Infinity 점검을 시작하지 못했습니다",result.stdout)
  self.assertNotIn("Bash failed",result.stdout+result.stderr)
 def test_prepare_failure_does_not_print_raw_error(self):
  fake=Path(tempfile.mkdtemp()); prepare=fake/"prepare.py"
  prepare.write_text("import sys\nprint('Bash failed: command --secret', file=sys.stderr)\nraise SystemExit(1)\n")
  env={"PATH":"/usr/bin:/bin","INFINITY_DISPATCHER_STATE_DIR":tempfile.mkdtemp(),"INFINITY_DISPATCHER_LOCK_FILE":str(fake/"lock"),"INFINITY_DISPATCH_PREPARE_SCRIPT":str(prepare)}
  result=subprocess.run(["bash",str(Path(__file__).with_name("run_dispatcher_cycle.sh"))],env=env,capture_output=True,text=True)
  self.assertEqual(result.returncode,0)
  self.assertIn("Infinity 점검을 시작하지 못했습니다",result.stdout)
  self.assertNotIn("Bash failed",result.stdout+result.stderr)
if __name__ == "__main__": unittest.main()
