from .base import *

# ----------------------------------------------------------------------
# SECURITY
# ----------------------------------------------------------------------

DEBUG = False

SECRET_KEY = 'REPLACE_ME_WITH_A_NEW_SECURE_KEY'

ALLOWED_HOSTS = [
    'parvizconstruction.com',
    'www.parvizconstruction.com',
]

# ----------------------------------------------------------------------
# PostgreSQL Database (production)
# ----------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parvizconstruction',
        'USER': 'parviz',
        'PASSWORD': 'REPLACE_DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
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
