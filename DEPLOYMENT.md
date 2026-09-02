# Formata 3.0 DigitalOcean deployment

Formata 3.0 must be deployed as a separate DigitalOcean App Platform application. Do not repoint, edit, reuse, or attach resources from Formata 1.0 or 2.0.

## Source

- Repository: `AshleyKirkland/Formata-3.0`
- Production branch: `main`
- Runtime: Python 3.12
- HTTP port: 8080
- Health endpoint: `/health/`
- First preview: DigitalOcean starter hostname only

## Required production resources

1. A NEW App Platform app dedicated to Formata 3.0.
2. A NEW PostgreSQL database dedicated to Formata 3.0.
3. A unique `SECRET_KEY` stored as an encrypted/secret environment variable.
4. `DATABASE_URL` injected only from the Formata 3.0 PostgreSQL resource.

## Required environment variables

- `DEBUG=False`
- `SECRET_KEY=<new Formata 3.0 secret>`
- `DATABASE_URL=<new Formata 3.0 PostgreSQL connection string>`
- `ALLOWED_HOSTS=<DigitalOcean starter hostname>`
- `CSRF_TRUSTED_ORIGINS=https://<DigitalOcean starter hostname>`
- `SECURE_SSL_REDIRECT=True`
- `SECURE_HSTS_SECONDS=3600`

## Build, deploy, and run

Build command:

`pip install . && python manage.py collectstatic --noinput`

Pre-deploy command/job:

`python manage.py migrate --noinput && python manage.py seed_jurisdictions`

The web process must only start Gunicorn. Database migrations are intentionally separated from web startup so multiple web instances do not race migrations during restarts.

Run command (also defined in `Procfile`):

`gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2 --timeout 120`

## Controlled first owner bootstrap

After the first successful deployment, set these values temporarily as encrypted environment variables:

- `FORMATA_OWNER_EMAIL=<owner email>`
- `FORMATA_OWNER_PASSWORD=<temporary strong password, minimum 12 characters>`
- `FORMATA_OWNER_FIRST_NAME=<first name>`
- `FORMATA_OWNER_LAST_NAME=<last name>`
- `FORMATA_FIRM_NAME=<preview firm name>`

Run once:

`python manage.py bootstrap_preview`

Then remove `FORMATA_OWNER_PASSWORD` from the environment. The command is idempotent for the same owner/firm and stops safely if the firm already has a different active owner.

## First launch sequence

1. Merge only after the final CI workflow passes.
2. Create a NEW DigitalOcean app from `AshleyKirkland/Formata-3.0` and `main`.
3. Attach a NEW PostgreSQL database.
4. Configure production environment variables.
5. Use the build, pre-deploy, and run commands above.
6. Configure an HTTP health check at `/health/` on port 8080.
7. Deploy to the DigitalOcean starter domain first.
8. Verify `/health/`, HTTPS, static files, database persistence, and login.
9. Run the controlled owner bootstrap once and log into the preview.
10. Keep Formata 1.0 and 2.0 unchanged while 3.0 is tested side by side.
11. Add a separate 3.0 hostname only after the starter deployment is stable. Do not change existing Formata DNS during the initial preview launch.

## Launch gate

A successful preview deployment is not authorization to rely on Formata 3.0 for legal deadlines. Substantive legal rules remain disabled/unverified until their current primary legal sources, effective dates, exceptions, calculation treatment, and approved test cases have been reviewed.
