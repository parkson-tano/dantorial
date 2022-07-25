from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "tantwexs_db",
        'USER': "tantwexs_tantorialadmin",
        'PASSWORD':  os.getenv('PASSWORD'),
        'HOST':  "localhost",
        'PORT': 3306,
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 248000
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
