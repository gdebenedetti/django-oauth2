# -*- coding: utf-8 -*-
"""
Django settings for oauth_toolkit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gg@u3)qmi1nob96$a^)xh)gjl7)2ehic%!18lqdm)+27g1il6g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sslserver',
    'oauth2_provider',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

#CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
        #'sparl.v2',
        #'sparl.local',
        'sparl.hcdn.gob.ar',
        'hcdn.gob.ar',
        'spd.hcdn.gob.ar',
)


ROOT_URLCONF = 'oauth_toolkit.urls'

WSGI_APPLICATION = 'oauth_toolkit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('es', gettext_noop('Spanish')),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
     # Token duration :  12hs 
    'ACCESS_TOKEN_EXPIRE_SECONDS': 43200,
}

# Email setting
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.hcdn.gob.ar'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no_responder.dsdp@hcdn.gob.ar'
EMAIL_HOST_PASSWORD = 'UhbIjn93'
DEFAULT_FROM_EMAIL = 'no_responder.dsdp@hcdn.gob.ar'
EMAIL_SUBJECT="Recuperación de contraseña - Sistema Parlamentario Digital"
EMAIL_MESSAGE="Para recuperar su contraseña ingrese al siguiente link:  http://sparl-desa.hcdn.gob.ar/#/cambiarPassword?token={0} \n\nEn caso de no haber solicitado este email, por favor ignórelo.\n\nSaludos cordiales. \n\nSistema Parlamentario Digital \nDirección de Servicios Digitales Parlamentarios"
EMAIL_MESSAGE_EXCEPTION="Hay una excepción para el usuario: \nCUIL: {0} \nNombre: {1} \nApellido: {2} \nEmail-bd: {3} \nEmail-nuevo: {4}"
# Email recovery exception responsible
EMAIL_RECOVERY_RESPONSIBLE="info.dsdp@hcdn.gob.ar"
