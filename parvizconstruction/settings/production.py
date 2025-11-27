
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = False
ALLOWED_HOSTS = ['www.parvizconstruction.com', 'parvizconstruction.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')



RECAPTCHA_PUBLIC_KEY ='6LeQ0mUqAAAAAOugpr5ComdF5DTwaiwnJGelR9k9'
RECAPTCHA_PRIVATE_KEY ='6LeQ0mUqAAAAAM1LrkO6Y-9__xDLpUTaDmEexLvZ'