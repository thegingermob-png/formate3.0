import os
from contextlib import contextmanager

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()


@contextmanager
def _migration_lock():
    """Serialize startup migrations across Gunicorn workers in one container."""
    import fcntl

    with open("/tmp/formata-migrations.lock", "w", encoding="utf-8") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


# DigitalOcean's component run command can override the repository Procfile.
# Apply committed migrations before this worker begins accepting requests.
if os.environ.get("RUN_MIGRATIONS_ON_STARTUP", "1") == "1":
    with _migration_lock():
        call_command("migrate", interactive=False, verbosity=1)
