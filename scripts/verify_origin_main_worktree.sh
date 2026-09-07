#!/usr/bin/env bash
# Run a read-only verification command in a clean origin/main detached worktree.
set -euo pipefail
ROOT="${1:?Infinity repository path required}"; shift
WORKTREE="$(mktemp -d /tmp/infinity-origin-main-verify-XXXXXX)"
cleanup() { git -C "$ROOT" worktree remove --force "$WORKTREE" >/dev/null 2>&1 || true; }
trap cleanup EXIT
git -C "$ROOT" fetch origin main >/dev/null
git -C "$ROOT" worktree add --detach "$WORKTREE" origin/main >/dev/null
test -z "$(git -C "$WORKTREE" status --porcelain)"
(cd "$WORKTREE" && "$@")
test -z "$(git -C "$WORKTREE" status --porcelain)"
