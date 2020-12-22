"""
Django settings for oxfordconsultants project.


For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
from urllib import parse

import dj_database_url
import django_heroku
from decouple import config

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

ENVIRONMENT = config('ENVIRONMENT', default='local')

if ENVIRONMENT != 'local':
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://8c8adf80a7f743199bfb87345e3234fe@o224520.ingest.sentry.io/5271343",
        integrations=[DjangoIntegration()],
        send_default_pii=True

    )
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
    s.strip() for s in v.split(',')], default='*')

INSTALLED_APPS = [
    'frontend',
    'search',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',

    'wagtail.contrib.styleguide',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'storages'
]

SITE_ID = 1
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'oxfordconsultants.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oxfordconsultants.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'oxfordconsultants.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DEFAULT_DATABASE = parse.urlparse(config('DATABASE_URL'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DEFAULT_DATABASE.path[1:],
        'USER': DEFAULT_DATABASE.username,
        'PASSWORD': DEFAULT_DATABASE.password,
        'HOST': DEFAULT_DATABASE.hostname,
        'PORT': DEFAULT_DATABASE.port,
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000
# Wagtail settings

WAGTAIL_SITE_NAME = "oxfordconsultants"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = config('BASE_URL', default='BASE_URL')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

if ENVIRONMENT != 'local':
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    X_FRAME_OPTIONS = 'DENY'

USER_AGENTS_CACHE = None

MAILGUN_API_KEY = config('MAILGUN_API_KEY', default='MAILGUN_API_KEY')
MAILGUN_API_BASE_URL = config('MAILGUN_API_BASE_URL', default='MAILGUN_API_BASE_URL')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# media
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'oxfordconsultants.storage_backends.PublicMediaStorage'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'oxfordconsultants.storage_backends.PrivateMediaStorage'
AWS_DEFAULT_ACL = "public-read"
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN,
                                AWS_PUBLIC_MEDIA_LOCATION)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
