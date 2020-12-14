# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import environ
from common.environ import MyEnv

env = environ.Env(DEBUG=(bool, False))

PREFIX_ENVVARS = "DJANGO"
env = MyEnv(PREFIX_ENVVARS)

root = environ.Path(__file__) - 2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# DEBUG = env.bool('DEBUG', default=False)
DEBUG = False

# env.read_env(os.path.join(BASE_DIR, 'ellysium', '.env'))

SECRET_KEY = env('SECRET_KEY', default='xxx')

# DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3')}

DATABASES = {
    'default': env.db("DATABASE_URL"),
}

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 500

MEDIA_URL = env('MEDIA_URL', default='/media/')
STATIC_URL = env('STATIC_URL', default='/static/')

MEDIA_ROOT = env('MEDIA_LOCATION', default=os.path.join(BASE_DIR, 'media'))
STATIC_ROOT = env('STATIC_LOCATION', default=os.path.join(BASE_DIR, 'staticfiles'))

SHUUP_HOME_CURRENCY = env('SHOP_CURRENCY', default='EUR')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*').split(',')

EMAIL_FROM = env('EMAIL_FROM', default="info@kingdomwargames.com")
EMAIL_HOST = env('EMAIL_HOST', default="")
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default="")
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default="")
EMAIL_PORT = env('EMAIL_PORT', default="")
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)

# EMAIL_CONFIG = env.email_url('EMAIL_URL', default='smtp://localhost:25')
# vars().update(EMAIL_CONFIG)

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # external apps that needs to be loaded before Shuup
    'easy_thumbnails',
    'common',
    # shuup themes
    'shuup.themes.classic_gray',
    'kingdomtheme',
    'kingdom_search',
    'kingdom_front',
    'manufacturer_reports',
    # shuup
    'shuup.core',
    'shuup.admin',
    'shuup.addons',
    'shuup.default_tax',
    'shuup.front',
    'shuup.front.apps.auth',
    'shuup.front.apps.carousel',
    'shuup.front.apps.customer_information',
    'shuup.front.apps.personal_order_history',
    'shuup.front.apps.saved_carts',
    'shuup.front.apps.registration',
    'shuup.front.apps.simple_order_notification',
    # 'shuup.front.apps.simple_search',
    'shuup.front.apps.recently_viewed_products',
    'shuup.notify',
    'shuup.simple_cms',
    'shuup.customer_group_pricing',
    'shuup.campaigns',
    'shuup.simple_supplier',
    'shuup.order_printouts',
    'shuup.utils',
    'shuup.xtheme',
    'shuup.reports',
    'shuup.default_reports',
    'shuup.regions',
    'shuup.importer',
    'shuup.default_importer',
    'shuup.gdpr',
    'shuup.tasks',
    'shuup.discounts',
    'shuup_stripe',

    # external apps
    'bootstrap3',
    'django_countries',
    'django_jinja',
    'django_filters',
    'filer',
    'reversion',
    'registration',
    'rest_framework',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shuup.front.middleware.ProblemMiddleware',
    'shuup.core.middleware.ShuupMiddleware',
    'shuup.front.middleware.ShuupFrontMiddleware',
    'shuup.xtheme.middleware.XthemeMiddleware',
    'shuup.admin.middleware.ShuupAdminMiddleware'
]

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
LANGUAGE_CODE = env('LANGUAGE_CODE', default='es')
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
RAVEN_CONFIG = {'dsn': env('SENTRY_DSN')}

DEFAULT_FROM_EMAIL = env('EMAIL_FROM', default='info@kingdomwargames.com')

SITE_ID = env('SITE_ID', default=1)

LANGUAGE_CHOICES = [
    # ('en', 'English'),
    ('es', 'Spanish'),
]

selected_languages = env('LANGUAGES', default='es').split(',')
LANGUAGES = [(code, name) for code, name in LANGUAGE_CHOICES if code in selected_languages]

PARLER_DEFAULT_ACTIVATE = True
PARLER_DEFAULT_LANGUAGE_CODE = env('PARLER_DEFAULT_LANGUAGE_CODE', default='es')

PARLER_LANGUAGES = {
    None: [{'code': c, 'name': n} for (c, n) in LANGUAGES],
    'default': {
        'fallback': 'en',
        'hide_untranslated': False
    }
}

_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.request",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "shuup.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "debug": DEBUG
        }
    },
]

CACHES = {'default': env.cache(default='memcache://127.0.0.1:11211?key_prefix=project')}
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'kingdomwargames_cache'
#     }
# }

SHUUP_PRICING_MODULE = "customer_group_pricing"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'shuup.api.permissions.ShuupAPIPermission',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [
        "get"
    ]
}

# extend the submit methods only if DEBUG is True
if DEBUG:
    SWAGGER_SETTINGS["SUPPORTED_SUBMIT_METHODS"].extend(["post", "patch", "delete", "put"])

SHUUP_SETUP_WIZARD_PANE_SPEC = [
    "shuup.admin.modules.shops.views:ShopWizardPane",
    "shuup.admin.modules.service_providers.views.PaymentWizardPane",
    "shuup.admin.modules.service_providers.views.CarrierWizardPane",
    "shuup.xtheme.admin_module.views.ThemeWizardPane",
    "shuup.testing.modules.sample_data.views.SampleObjectsWizardPane" if DEBUG else "",
    "shuup.admin.modules.system.views.TelemetryWizardPane"
]

SHUUP_ERROR_PAGE_HANDLERS_SPEC = [
    "shuup.admin.error_handlers:AdminPageErrorHandler",
    "shuup.front.error_handlers:FrontPageErrorHandler"
]

SHUUP_SIMPLE_SEARCH_LIMIT = 150

# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SHUUP_ENABLED_ADDONS_FILE = os.getenv("SHUUP_ENABLED_ADDONS_FILE") or (
    os.path.join(BASE_DIR, "var", "enabled_addons"))

CREATE_SUPER_USER = env.bool('CREATE_SUPER_USER', default=False)
CREATE_DUMMY = env.bool('CREATE_DUMMY_DATA', default=False)
DEFAULT_SUPER_USER_EMAIL = env('DEFAULT_SUPER_USER_EMAIL', default='hispar@gmail.com')
DEFAULT_SUPER_USER_PASSWORD = env('DEFAULT_SUPER_USER_PASSWORD', default='as12345678')
SHUUP_ENABLE_MULTIPLE_SHOPS = env.bool('SHUUP_ENABLE_MULTIPLE_SHOPS', default=True)
SHUUP_ENABLE_MULTIPLE_SUPPLIERS = env.bool('SHUUP_ENABLE_MULTIPLE_SUPPLIERS', default=True)
SHUUP_ENABLE_ATTRIBUTES = env.bool('SHUUP_ENABLE_ATTRIBUTES', default=True)
