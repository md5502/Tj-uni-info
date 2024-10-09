from .base import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# Email settings for local dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
