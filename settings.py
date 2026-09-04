import os
from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY", default="development-only-change-me" if DEBUG else None)
if not SECRET_KEY:
    raise ImproperlyConfigured("SECRET_KEY must be set when DEBUG=False")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"] if DEBUG else [])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions",
    "django.contrib.messages", "django.contrib.staticfiles", "apps.accounts", "apps.firms", "apps.matters",
    "apps.parties", "apps.events", "apps.jurisdictions", "apps.rules", "apps.deadlines", "apps.integrations",
    "apps.billing", "apps.communications", "apps.legal_updates", "apps.web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "apps.web.middleware.SecurityHeadersMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "apps.accounts.middleware.RequireMFAMiddleware",
    "apps.web.middleware.SearchIndexingMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True, "OPTIONS": {"context_processors": ["django.template.context_processors.request", "django.contrib.auth.context_processors.auth", "django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")}
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LANGUAGE_CODE = "en-ca"
TIME_ZONE = "America/Edmonton"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {"default": {"BACKEND": "django.core.files.storage.FileSystemStorage"}, "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
PUBLIC_SITE_URL = env("PUBLIC_SITE_URL", default="https://walrus-app-aebgn.ondigitalocean.app").rstrip("/")

INTEGRATION_TOKEN_ENCRYPTION_KEY = env("INTEGRATION_TOKEN_ENCRYPTION_KEY", default="")
CLIO_CLIENT_ID = env("CLIO_CLIENT_ID", default="")
CLIO_CLIENT_SECRET = env("CLIO_CLIENT_SECRET", default="")
CLIO_REDIRECT_URI = env("CLIO_REDIRECT_URI", default="")
CLIO_AUTH_BASE_URL = env("CLIO_AUTH_BASE_URL", default="https://ca.app.clio.com")
CLIO_API_BASE_URL = env("CLIO_API_BASE_URL", default="https://ca.app.clio.com/api/v4")
FILEVINE_CLIENT_ID = env("FILEVINE_CLIENT_ID", default="")
FILEVINE_CLIENT_SECRET = env("FILEVINE_CLIENT_SECRET", default="")
FILEVINE_REDIRECT_URI = env("FILEVINE_REDIRECT_URI", default="")
FILEVINE_AUTH_URL = env("FILEVINE_AUTH_URL", default="")
FILEVINE_TOKEN_URL = env("FILEVINE_TOKEN_URL", default="https://identity.filevine.com/connect/token")
FILEVINE_API_BASE_URL = env("FILEVINE_API_BASE_URL", default="https://api.filevineapp.com/fv-app/v2")
FILEVINE_PERSONAL_ACCESS_TOKEN = env("FILEVINE_PERSONAL_ACCESS_TOKEN", default="")
FILEVINE_ORG_ID = env("FILEVINE_ORG_ID", default="")
FILEVINE_USER_ID = env("FILEVINE_USER_ID", default="")
FILEVINE_PROJECTS_PATH = env("FILEVINE_PROJECTS_PATH", default="/Projects")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET", default="")
STRIPE_MONTHLY_PRICE_ID = env("STRIPE_MONTHLY_PRICE_ID", default="")
STRIPE_ANNUAL_PRICE_ID = env("STRIPE_ANNUAL_PRICE_ID", default="")
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID", default="")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET", default="")
GOOGLE_REDIRECT_URI = env("GOOGLE_REDIRECT_URI", default="")
MICROSOFT_CLIENT_ID = env("MICROSOFT_CLIENT_ID", default="")
MICROSOFT_CLIENT_SECRET = env("MICROSOFT_CLIENT_SECRET", default="")
MICROSOFT_REDIRECT_URI = env("MICROSOFT_REDIRECT_URI", default="")
MICROSOFT_TENANT_ID = env("MICROSOFT_TENANT_ID", default="common")
OPENAI_API_KEY = env("OPENAI_API_KEY", default="")
OPENAI_MODEL = env("OPENAI_MODEL", default="gpt-5.4-mini")
OPENAI_API_BASE_URL = env("OPENAI_API_BASE_URL", default="https://api.openai.com/v1")

EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
EMAIL_TIMEOUT = env.int("EMAIL_TIMEOUT", default=15)
EMAIL_REMINDER_DAYS_AHEAD = env.int("EMAIL_REMINDER_DAYS_AHEAD", default=30)
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="Formata <notifications@formata.ca>")
SERVER_EMAIL = env("SERVER_EMAIL", default="Formata Security <security@formata.ca>")

SESSION_COOKIE_NAME = "formata_sessionid"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = 60 * 60 * 8
SESSION_SAVE_EVERY_REQUEST = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
PASSWORD_RESET_TIMEOUT = 60 * 60
DATA_UPLOAD_MAX_MEMORY_SIZE = 1 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 1 * 1024 * 1024

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=86400)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False)
    SECURE_HSTS_PRELOAD = False
    X_FRAME_OPTIONS = "DENY"
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"


# Emit application errors to DigitalOcean Runtime Logs.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
