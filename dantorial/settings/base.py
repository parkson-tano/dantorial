from imp import load_compiled
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 
SECRET_KEY = os.getenv('SECRET_KEY')

# with open('secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

# ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django',
    # 'channels',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'category',
    'mainapp',
    'mooc',
    'messaging',
    'review',
    'autoslug',
    'location',
    # 'cities_light',
    'crispy_forms',
    # 'crispy_tailwind',
    'dani',
    'smart_selects',
    'ckeditor',
    'flatpickr',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'api',
    'rest_framework',
    "corsheaders",
    # "translation_manager",
    'django.contrib.humanize',
    'mathfilters',
    'debug_toolbar',
    'django_browser_reload',
    'cookie_consent',
    'robots',
    # 'agora',
    # 'notifications',
    # 'multiselectfield',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django.core.cache.backends.filebased.FileBasedCache",
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "django.core.cache.backends.memcached.PyMemcacheCache",
]

ROOT_URLCONF = 'dantorial.urls'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache'
#     }
# }

# CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
# CACHE_MIDDLEWARE_SECONDS = '600'    # number of seconds to cache a page for (TTL)
# CACHE_MIDDLEWARE_KEY_PREFIX = ''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders': [
            # (
            #     'django.template.loaders.filesystem.Loader',
            #     [BASE_DIR / 'templates']
            # ),
            # ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'dani.dani_processor.carousel_slide',
                'location.location_processor.location_renderer',
                'category.category_processor.category_list',
            ],
        },
    },
]

WSGI_APPLICATION = 'dantorial.wsgi.application'

# ASGI_APPLICATION = 'dantorial.routing.application'

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': [
#             '172.19.26.240:11211',
#             '172.19.26.242:11212',
#             '172.19.26.244:11213',
#         ]
#     }
# }

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROBOTS_USE_SITEMAP = False
ROBOTS_USE_SCHEME_IN_HOST = True
ROBOTS_CACHE_TIMEOUT = 60*60*24
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

MESSAGES_TO_LOAD = 15

# In settings.py


# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }

CKEDITOR_CONFIGS = {
'default': {
    'toolbar': 'Custom', #You can change this based on your requirements.
    'toolbar_Custom': [
        ['Bold', 'Italic', 'Underline', 'Font', 'FontSize'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['Link', 'Unlink'],
        ['RemoveFormat']
        ],
    'width': 'auto !important'
          },
    }

BOOTSTRAP4 = {
    'include_jquery': True,
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    )

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


DJANGO_NOTIFICATIONS_CONFIG = { 'USE_JSONFIELD': True}


USE_DJANGO_JQUERY = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ASGI_APPLICATION = 'dantorial.asgi.application'

# ACCOUNT_FORMS = {
#     'login': 'mainapp.forms.UserLoginForm'
# }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# CITIES_LIGHT_APP_NAME = 'location'
# CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr', 'en']
# CITIES_LIGHT_INCLUDE_CONTINENTS = ['AF']
# CITIES_LIGHT_INCLUDE_COUNTRIES = ['CM']
# CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT',]

SITE_ID = 3

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'



ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_ADAPTER = "dantorial.adapter.MyAccountAdapter"
# SOCIALACCOUNT_ADAPTER = 'dantorial.adapter.MySocialAccountAdapter'
# LOGIN_URL = "/"
# LOGIN_REDIRECT_URL = "/users/{id}/mytags"

# DEFAULT_FROM_EMAIL = 'info@tantorial.com'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_HOST_USER='tanocoder237@gmail.com'
# EMAIL_HOST_PASSWORD='danielTano123@'
# EMAIL_PORT = 587 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST= os.getenv('EMAIL_HOST')

# server96.web-hosting.com
EMAIL_HOST_USER= os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SOCIALACCOUNT_PROVIDERS = {
        'google': 
        {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS' : {
                'access_type': 'online'
            }
        },
            'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v7.0',
    }
        }

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')


GOOGLE_APPLICATION_CREDENTIALS = os.path.join(BASE_DIR, 'dantorial-bdef7-9833c8c7d45c.json')


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
# ]
CORS_ALLOW_ALL_ORIGINS = True
# django_heroku.settings(locals())
