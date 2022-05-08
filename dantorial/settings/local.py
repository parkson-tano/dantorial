from .base import *
import os


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {  
#     'default': {  
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': 'tantorial',  
#         'USER': 'root',  
#         'PASSWORD': 'danielTano123@',  
#         'HOST': '127.0.0.1',  
#         'PORT': '3306',  
#         'OPTIONS': {  
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
#         }  
#     }  
# }  