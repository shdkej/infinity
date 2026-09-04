# Final pre-deadline live health check

- captured_at: `2026-09-04T05:54:00Z`
- Space `origin/master`: `face000372b6de4db43a6aa5770a524e7c2dc11c`
- scope: read-only live health and committed-dist parity; no deployment or token inspection

| Asset | HTTPS | Live SHA-256 | Committed `dist/` SHA-256 | Result |
| --- | --- | --- | --- | --- |
| `/` | 200 | `5c2bdb31aa012b1d9ee052b722c4bb745cf8d6b923b282c4e546612ab92e9435` | `5c2bdb31aa012b1d9ee052b722c4bb745cf8d6b923b282c4e546612ab92e9435` | match |
| `/app.js` | 200 | `4ff1fefd42bf51de92b49ba9e1a955072665919da3f1d43f66ceb62d40ca3934` | `4ff1fefd42bf51de92b49ba9e1a955072665919da3f1d43f66ceb62d40ca3934` | match |

This check preserves the prior M4 browser evidence and M6 Terraform proof. It is not a terminal receipt, Archive authorization, or Mapbox token inspection.
