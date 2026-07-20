# Virtue AI Search Citation Audit

- id: marketing-115
- created_at: 2026-07-20T10:07Z
- scope: `https://virtue.oracle.shdkej.com`, `/home/ubuntu/dev/virtue-rebirth-app`
- permission: L1 read-only audit; no public copy, deployment, tracking, or production code changed

## One-Page Audit Table

| Item | Status | Evidence | Judgment |
|---|---|---|---|
| Brand entity | weak | App package/name and settings use `Virtue`; public metadata title is `덕 쌓기 · 환생`; README names `virtue-rebirth`. | A human can infer the product, but AI/search may split the entity into Korean title, repository name, and Virtue brand. |
| Category | weak | Metadata says mobile life game inspired by Brush Up Life; README says mobile web MVP and life game; UI says virtue score and reincarnation species. | Category is present, but it is not consistently stated as `AI-powered virtue/deed journaling life game`. |
| Job | present | Home first-visit copy promises recording one photo or memo, AI judging today's virtue, and moving reincarnation progress. `/add` supports photo or memo. | The primary job is readable: record a small good deed and see it interpreted/scored. |
| First value | present | Home says the first record moves the result/progress immediately; `/add` shows result card, score, tags, reroll/save affordances. | First value is clear for J1/J2/J4 as save/progress and for J3 as seeing the AI view, but not named in public metadata. |
| Trust boundary | present | Result card says `AI의 관점이에요. 결정은 당신이 해요.` Mock/AI mode labels distinguish source. | Strong in-product boundary: AI gives a view, user decides. It should be repeated in public read-about surfaces before agent discovery. |
| Claim evidence | weak | README documents local/mock default, Lambda/Gemini mode, mobile routes, daily cap, reroll limit, and storage. Live root currently returns nginx 404 under `curl -k`. | Internal evidence exists, but externally citable evidence is weak while the live URL does not return the app HTML. |
| Structured discovery | missing | No `robots.txt`, `sitemap`, `manifest`, `llms.txt`, schema.org, OpenGraph, or Twitter metadata found in the public app files inspected. | AI/search agents have little canonical surface beyond basic Next metadata and page text. Public reflection requires approval. |
| Canonical answer block | public reflection approval needed | The block below is draft-only. | Safe to use internally; publish only after explicit approval because it changes public positioning. |

## Canonical Answer Block Draft

Virtue is a mobile web life game for recording small everyday good deeds. A user adds a photo or short memo, then the product shows how the action looks from an AI perspective as a virtue score, tags, and a short comment. The user decides whether to save the result, reroll it, or ignore it; the AI does not act externally or make the final decision. Saved deeds increase the user's virtue total and reincarnation-species progress, creating a lightweight personal log. Virtue is currently prelaunch, so public claims should stay descriptive and avoid performance, retention, or demand claims.

## Implementation Candidates

1. Add consistent public metadata that names `Virtue` and the category in one sentence.
2. Add read-only discovery files after approval: `robots.txt`, `sitemap`, and a short `llms.txt`/about block.
3. Mirror the trust boundary in public copy: AI gives a perspective; the user keeps the final choice.
4. Avoid agent-do-for-you surfaces for now; read-about discovery fits the product better than automated external action.

## Sources Inspected

- Live root: `https://virtue.oracle.shdkej.com` returned nginx 404 when fetched with certificate checks bypassed.
- Repo metadata: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/layout.tsx`
- Home UI: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/page.tsx`
- Add flow UI: `/home/ubuntu/dev/virtue-rebirth-app/apps/web/src/app/add/page.tsx`
- Product docs: `/home/ubuntu/dev/virtue-rebirth-app/README.md`, `/home/ubuntu/dev/virtue-rebirth-app/apps/web/README.md`
- Marketing inheritance: `MARKETING_LEARNINGS.md`, especially agent-led growth, decision-delegation risk, and first-value mapping boundaries.
