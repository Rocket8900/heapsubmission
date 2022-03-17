"""
Django settings for nashyseko project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-de^a9nt!y+xav@_hq@*xb^eo^t#(c+ozl_4t85$tic#o#3pg2g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hangrysloth.herokuapp.com', '127.0.0.1', 'www.hangrysloth.com', 'hangrysloth.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'food',
    'leaflet',
    'accounts',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nashyseko.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'nashyseko.wsgi.application'

GOOGLE_API_KEY = 'AIzaSyBEdIbqbG2UMbXcPLUVo8OiZzhdRdnkHyI'

RECAPTCHA_KEY = '6LfUIjoeAAAAABIDHagqxGUW9nKvHEm1kkfv3Cdn'

RECAPTCHA_SECRET_KEY = '6LfUIjoeAAAAAAj0a20CoX8NHgMrg3dAadi-RpHs'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'food',
#         'USER': 'foodadmin',
#         'PASSWORD': 'foodpass',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'd7fjd7ac4kij03',
        'USER': 'nojahymuajtoux',
        'PASSWORD': '90fb9895b3baf50e8e3cfa24dcdbc6819ee1ed002baa45f60dea3f6cd7099694',
        'HOST': 'ec2-3-208-121-149.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}




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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

LOGIN_URL = 'food:login'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (1.3521, 103.8198),
    'DEFAULT_ZOOM': 15,
    'MAX_ZOOM': 20,
    'MIN_ZOOM':12,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Inspired by Life in GIS'
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

BASE_COUNTRY = "SG"

LOGIN_REDIRECT_URL = 'accounts:profile'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SENDGRID_API_KEY = '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'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')


if os.getcwd() == '/app':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    DEBUG = False