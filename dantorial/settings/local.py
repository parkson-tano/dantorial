from .base import *
import os


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}