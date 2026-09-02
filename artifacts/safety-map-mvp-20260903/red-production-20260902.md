# Safety Map production Red report — PASS

- reviewed_at: 2026-09-02T19:42Z
- scope: approved static production deployment only; live travel-safety data accuracy and demand/user-study validation excluded.
- live_url: https://safety-map.aws.shdkej.com/

## Gate results

1. **Live render:** HTTPS 200 for `/` and `/sources.html`; 1440px desktop and 390px mobile render evidence inspected. Gray/no-live default, synthetic Zone A/B/C, 10 city cards, separate advertising slot, and local-only input wording render without horizontal overflow.
2. **Safety and privacy:** published JS has no `fetch`, geolocation, storage, analytics, or cookie path. The executable PII regression covers URL, handle, phone, email, English/Korean address, decimal/DMS coordinates, Plus Code, and one benign observation.
3. **Deployment isolation:** the release uses `static-safety-map-aws-shdkej-com`, CloudFront `E17JBS3Q0EH0DQ`, and `safety-map.aws.shdkej.com`; Travel Ops remains on its own bucket/distribution. S3 public access blocks, SSE AES256, CloudFront OAC, HTTPS redirect, and TLS 1.2_2021 were confirmed.
4. **Asset parity:** live hashes match `sites/safety-map/dist/`: index `0be289b70adb3b92ce98adbb62d8338e9101dac0425fe4771f022f849d609ab7`, app `5a27fd94981425bd6a5335459addccba23a66e8240c51a2d5c0dadccc29c0f0e`, CSS `4ee0ffd39f010e9528cd14cb88b0b77967d01f4b89a9a88e547ac2a1550be351`, sources `dc4e1c8f43d989eae0eb8a33f49d9b54bc298fea4c4eb048ac253954980256d1`.
5. **IaC:** un-targeted post-apply Terraform plan exited 0 with `No changes. Your infrastructure matches the configuration.`

## Remediation before pass

The initial Red review found a 403 `README.md` footer link and target-only apply evidence. The footer now points to published `/sources.html` (HTTPS 200 and hash-verified); an un-targeted no-change Terraform plan closes the IaC evidence gap.

## Residual limits

This is a fixture-only travel-context MVP, not a real-time crime/safety service. It makes no street/block/incident/routing/safety-guarantee claim, and it does not establish demand validation.
