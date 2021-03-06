"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)^-rj63rp2d9@z()vjzqmwzh+p!p=$=skl@$c+mct)qv(h+qdw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
VERIFY_SSL = False

ADMIN_USERNAME='root'
SESSION_PROTECTION = 'weak'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0','zrealtycorp.com', 'www.zrealtycorp.com']
AUTH_USER_MODEL = 'users.User'

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'admin_auto_filters',
    'admin_tools',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'adminsortable',
    'django_extensions',
    'encrypted_fields',
    'imagekit',
    'redis',
    'redis_cache',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_bulk',
    'rest_framework_jwt',
    'rest_framework_oauth',
    'rest_framework_extensions',
    'rest_framework_filters',
    'rest_framework_swagger',
    'django_filters',
    'custom.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zrealtydb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# A list of hex-encoded 32 byte keys
# You only need one unless/until rotating keys
FIELD_ENCRYPTION_KEYS = [
    "f164ec6bd6fbc4aef5647abc15199da0f9badcc1d2127bde2087ae0d794a9a0b"
]

STATICFILES_DIRS = (
  './static_files',
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),
                    os.path.join(BASE_DIR, 'static_files/js'), 
                    os.path.join(BASE_DIR, 'static_files/html'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static', )
STATIC_URL = '/static/'
REGISTRATION_API_ACTIVATION_SUCCESS_URL = '/'
ACTIVATION_HOST = ''
MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'

