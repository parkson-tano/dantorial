from .base import *
import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = False

ALLOWED_HOSTS = ['tantorial.com', 'www.tantorial.com']

DATABASES = {
    'default': {
        'ENGINE': os.gewtenv('ENGINE'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 248000
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True