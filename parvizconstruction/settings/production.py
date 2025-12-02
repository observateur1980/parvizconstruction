from .base import *

# ----------------------------------------------------------------------
# SECURITY
# ----------------------------------------------------------------------

DEBUG = False

SECRET_KEY = '-5v6wjxts6a_mqzjb5u^n_m*&%y7=^ej!&0f39fr%sro(1z1ko'

ALLOWED_HOSTS = [
    "parvizconstruction.com",
    "www.parvizconstruction.com",
    "127.0.0.1",
    "localhost",
]

# ----------------------------------------------------------------------
# PostgreSQL Database (production)
# ----------------------------------------------------------------------

if os.environ.get("USE_SQLITE_IN_LOCAL"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "parvizconstruction",
            "USER": "parviz",
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

# ----------------------------------------------------------------------
# Static & Media paths (for Nginx)
# ----------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

# ----------------------------------------------------------------------
# Email config
# ----------------------------------------------------------------------

EMAIL_HOST_USER = 'smtpforwebpages@gmail.com'
EMAIL_HOST_PASSWORD = 'qercfgriuwhlulte'

# ----------------------------------------------------------------------
# reCAPTCHA keys
# ----------------------------------------------------------------------

RECAPTCHA_PUBLIC_KEY = '6LeQ0mUqAAAAAOugpr5ComdF5DTwaiwnJGelR9k9'
RECAPTCHA_PRIVATE_KEY = '6LeQ0mUqAAAAAM1LrkO6Y-9__xDLpUTaDmEexLvZ'

# ----------------------------------------------------------------------
# Security Headers
# ----------------------------------------------------------------------

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
