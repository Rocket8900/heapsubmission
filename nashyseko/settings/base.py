"""
Using Django 3.2.4.
"""
from pathlib import Path
import dj_database_url
from decouple import config
from dotenv import load_dotenv, find_dotenv


import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(find_dotenv())

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.environ.get('SECRET_KEY')

# 'gciza+eo*=ds*7m$koj2p%i%aee9=b6f$bk5v67@_-)wo(mgj7'
# SECRET_KEY = 'django-insecure-de^a9nt!y+xav@_hq@*xb^eo^t#(c+ozl_4t85$tic#o#3pg2g'

# AWS S3 SETTINGS
# AWS_ACCESS_KEY_ID = 'AKIA347MMUKRYJDRPN56'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'hangrysloth'
# AWS_S3_CUSTOM_DOMAIN = 'hangrysloth.s3.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_LOCATION = 'static'
# AWS_QUERYSTRING_AUTH = False
# AWS_HEADERS = {
#     'Access-Control-Allow-Origin':'*',
# }
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# AWS_S3_REGION = 'ap-southeast-1'
# AWS_S3_SIGNATURE_VERSION = 's3v4'

CKEDITOR_UPLOAD_PATH= f'https://hangrysloth.s3.amazonaws.com/uploads/'


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['hangrysloth.herokuapp.com', '127.0.0.1', 'www.hangrysloth.com', 'hangrysloth.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django.contrib.gis',
    'django_extensions',
    'food',
    'leaflet',
    'accounts',
    'taggit',
    'blog',
    'ckeditor',
    'ckeditor_uploader',
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

GOOGLE_API_KEY = 'AIzaSyDtaxDxZ7qrkLjgEp1x6zWP0MSdQiv64pU'

# RECAPTCHA_KEY = os.getenv("GOOGLE_RECAPTCHA_KEY")

# RECAPTCHA_SECRET_KEY = os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY")

# CACHES = {
#     "default": {
#         # Your default cache
#     },
#     "collectfast": {
#         # Your dedicated Collectfast cache
#     },
# }



# DATABASES = {'default': dj_database_url.config(default='sqlite3:///db.sqlite', conn_max_age=600)}

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': '5432'
    }
}

# DATABASES = {'default': dj_database_url.config(default='postgres://zvrtxfziizlabb:5c42dec16ee7e55a916fae3d387ec7874d70df868f99244cf1aa88836827af3b@localhost/dc5kpki60l67ka')}



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

# AWS SETTINGS





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


BASE_COUNTRY = "SG"

LOGIN_REDIRECT_URL = 'accounts:profile'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"



# SENDGRID SETTINGS

SENDGRID_API_KEY = 'SG.dP8Kp0SERrS7RC4XGyp6aA.LrNBB41SDJx21cMRK47YvFySRUUy6FcNvyirsfP4c7U'

DEFAULT_FROM_EMAIL = 'HangrySloth Admin <admin@hangrysloth.com>'


GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')


# if os.getcwd() == '/app':
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#     SECURE_SSL_REDIRECT = True
#     DEBUG = False



CKEDITOR_CONFIGS = {
    'default': {
     
        # 'skin': 'moono',
        # # 'skin': 'office2013',
        # 'toolbar_Basic': [
        #     ['Source', '-', 'Bold', 'Italic']
        # ],
        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 400,
        # 'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}