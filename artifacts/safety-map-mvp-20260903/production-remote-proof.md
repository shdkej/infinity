# Safety Map production remote proof

- checked_at: 2026-09-02T19:42:17Z
- site: https://safety-map.aws.shdkej.com/
- method_page: https://safety-map.aws.shdkej.com/sources.html
- HTTP: `/` = 200; `/sources.html` = 200.
- cache invalidation: `I9Z6TNKCEGPXHVYAC9M1GNYC1` completed.
- release asset hashes match remote bytes:
  - index: `0be289b70adb3b92ce98adbb62d8338e9101dac0425fe4771f022f849d609ab7`
  - app: `5a27fd94981425bd6a5335459addccba23a66e8240c51a2d5c0dadccc29c0f0e`
  - css: `4ee0ffd39f010e9528cd14cb88b0b77967d01f4b89a9a88e547ac2a1550be351`
  - sources: `dc4e1c8f43d989eae0eb8a33f49d9b54bc298fea4c4eb048ac253954980256d1`
- infrastructure: private encrypted S3 `static-safety-map-aws-shdkej-com`; CloudFront `E17JBS3Q0EH0DQ`; OAC `E1PMYI8608YUT9`; HTTPS redirect; TLS `TLSv1.2_2021`.
- isolation: Travel Ops bucket/distribution were not modified; full un-targeted Terraform post-apply plan exited 0 with no changes.
- source remote: Space release commits `2e35b192fdbe9f17b96a45b5720fb64f5a6f708d` and `1a9da8c89b6c956e68286d9ae0a5f5ebf41d7698`; latest `HEAD` equals `origin/master` after push.
