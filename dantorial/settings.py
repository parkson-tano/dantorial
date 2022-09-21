from imp import load_compiled
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY')


INTERNAL_IPS = [
    '127.0.0.1',
]


DEBUG = True


ALLOWED_HOSTS = ["*"]

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Application definition

INSTALLED_APPS = [
    # Django cleanup to remove unused media files
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',
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
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'category',
    'mainapp',
    'notificate',
    'mooc',
    'messaging',
    'review',
    'autoslug',
    'location',
    'payments',
    'crispy_forms',
    'dani',
    'smart_selects',
    'ckeditor',
    'flatpickr',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'api',
    "corsheaders",
    'rest_framework',
    'django.contrib.humanize',
    'mathfilters',
    'debug_toolbar',
    'django_browser_reload',
    'cookie_consent',
    'robots',
    'notifications',
    "pwa",
    'rest_framework.authtoken',
    'webpush',
    'chat',
    # "channels",
]

MIDDLEWARE = [
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'dantorial.urls'

CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
# number of seconds to cache a page for (TTL)
CACHE_MIDDLEWARE_SECONDS = 60*60*24
CACHE_MIDDLEWARE_KEY_PREFIX = ''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',

                ]),
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

# WSGI_APPLICATION = 'dantorial.wsgi.application'

# ASGI_APPLICATION = 'dantorial.routing.application'

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BCqIQ7dMD6j7xe9-gVcHhkG2ID6nzak8owscKsHP4Bghj6dW4ZZ5Bw5dW8W2BdQe9XUOM917Vm371-Cvwok_dF4",
    "VAPID_PRIVATE_KEY": "G7wdzuixpCTlIHhjUZ1d__lc7PEzN1c5EoJhGa0EvyQ",
    "VAPID_ADMIN_EMAIL": "tanoparksonsilencer@gmail.com"
}


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

}


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


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # You can change this based on your requirements.
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Font', 'FontSize'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
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

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

TIME_ZONE = 'Africa/Libreville'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True}


USE_DJANGO_JQUERY = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


CORS_ORIGIN_WHITELIST = [
    'http://localhost:19000',
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

SITE_ID = 3

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = os.getenv('EMAIL_HOST')

# server96.web-hosting.com
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SOCIALACCOUNT_PROVIDERS = {
    'google':
        {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
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


GOOGLE_APPLICATION_CREDENTIALS = os.path.join(
    BASE_DIR, 'dantorial-bdef7-9833c8c7d45c.json')


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
# ]
CORS_ALLOW_ALL_ORIGINS = True
# django_heroku.settings(locals())


PWA_APP_NAME = 'Tantorial'
PWA_APP_DESCRIPTION = "Tantorial is a platform for people to share their knowledge and experience with each other."
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': 'static/images/my_apple_icon.png',
        'sizes': '150x150'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/images/my_apple_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/images/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(
    BASE_DIR, 'static/js', 'serviceworker.js')


AUTH_USER_MODEL = 'mainapp.User'
