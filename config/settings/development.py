from .base import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]

# INSTALLED_APPS.append("debug_toolbar")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
# Email settings for local dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
