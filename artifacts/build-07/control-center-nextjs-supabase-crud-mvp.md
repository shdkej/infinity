# Control Center Next.js Supabase CRUD MVP

## Summary

Control Center CMS를 사용자가 직접 웹에서 데이터를 만들고 고칠 수 있는 앱으로 전환했다. 이번 단계는 Supabase scratch data CRUD이며, 실제 공개 페이지 정본 반영은 다음 단계로 남겼다.

## Deployed Surface

- URL: `https://cms.oracle.shdkej.com`
- Repo: `/home/ubuntu/workspace/space`
- App: `apps/control-center-cms`
- Platform: Next.js 15 on Kubernetes through ArgoCD-managed manifests
- Commits:
  - `c1a168e Add control center CMS app`
  - `8abc407 Pin CMS pnpm runtime`

## Data Model

Supabase table: `public.control_center_items`

- `id uuid`
- `surface text`
- `field_key text`
- `value text`
- `status text` with `draft`, `ready`, `published`
- `created_at timestamptz`
- `updated_at timestamptz`

RLS is enabled. The public browser does not receive Supabase service credentials. The Next.js server route uses `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` from Kubernetes Secret `control-center-cms-env`.

## API

- `GET /api/items`
- `POST /api/items`
- `PATCH /api/items/:id`
- `DELETE /api/items/:id`

The API is intentionally small. It validates required fields and keeps the write surface scoped to scratch CMS records.

## Browser Verification

The public UI was tested from `https://cms.oracle.shdkej.com`.

- Created a test record from the form.
- Edited the same record through the `Edit` flow.
- Deleted the test record through the `Delete` flow and confirmation dialog.
- Final visible state returned to 1 ready sample record.

Persistent sample record:

- id: `66061087-4ce3-4586-b223-f1eb50620d2d`
- surface: `family-wedding`
- field_key: `notice`
- status: `ready`
- value: `가족식 안내장 NOTICE 문구는 양해를 구하는 톤으로 관리합니다. 실제 공개 반영은 별도 승인 후 진행합니다.`

## Boundary

Done:

- Web app.
- Supabase table.
- Server-side CRUD.
- Kubernetes deploy.
- Browser data manipulation.

Not done:

- Write to Family Wedding source file.
- Commit/push from UI.
- Production deploy button.
- Auth/permission model.
- Audit log.
- Rollback.

Next: `build-08` for authenticated publish pipeline.
