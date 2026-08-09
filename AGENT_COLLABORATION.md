# Agent Collaboration Contract

Last updated: 2026-06-09

## Purpose

Agent-to-agent work should be visible and executable through Infinity, not hidden inside a source agent note.

The general pattern is:

`source agent -> target-agent Inbox intent -> target agent execution/report -> source intent update`

For normal user work, the target agent is `genie`. Genie owns the full execution path and must run Knowledge Lab plus Planner, Developer, Marketer, Operator, and Red validation even when the source request appears simple.

## Canonical Route

When one agent needs another agent to do real work, create or update a target-agent intent in Infinity.

Examples:

- 나래 / Naver Shopping Agent needs Marketer help -> create `marketing-*`.
- Research Agent needs Wiki compilation -> create `wiki-*`.
- Marketer needs product implementation -> create `product-*` or `build-*`.

The source intent may link to the target intent, but the target-agent intent is canonical.

## Required Fields

Every collaboration intent should include:

- `source_agent`
- `source_intent`
- `target_agent`
- `request_type`
- `question`
- `context`
- `evidence`
- `desired_output`
- `output_contract`
- `approval_boundary`
- `user_visible`

Use `user_visible: false` for routine internal collaboration. User-visible messages should be reserved for approval needs, blockers, or meaningful summaries.

## Visibility

`INTENTS.md` Inbox is the visible queue.

A source intent can include a one-line backlink such as:

```md
- collaboration: requested `marketing-48` for title/copy positioning; no user approval needed.
```

Do not rely on the backlink as the execution trigger. The target-agent intent must exist.

## Internal Inboxes

SAM internal inbox files such as `/home/ubuntu/workspace/knowledge-lab/source/openclaw-system/data/agent-inbox/marketing.jsonl` are supplementary.

They are useful for heartbeat, review, and lightweight status triage, but they do not replace Infinity Inbox intents for target-agent work.

## Completion

The target agent should:

1. read this contract and its own standing rules,
2. complete the requested work within normal approval boundaries,
3. write the required report/artifact,
4. archive the target intent,
5. update or link back to the source intent if the result changes the source stream.
