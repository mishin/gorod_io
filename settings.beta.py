# -*- coding: utf-8 -*-

"""
Django settings for gorod_io beta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w1^2-jaji&(1h0n17_!d8-cqz4ot8^vjtv5qq%trq04pvm7li#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.beta.gorod.io', '.beta..gorod.io.fstest.ru']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'gorod',
    'ckeditor',
    'south',
    'mptt',
    'social.apps.django_app.default',
    'easy_thumbnails',
    #'captcha',
    'smart_selects',
    'django_mptt_admin',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'comments',
    'likes'
)

COMMENTS_APP = 'comments'
COMMENT_MAX_LENGTH = 1000

SITE_ID = 2

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'gorod.middleware.base.UserCityMiddleware',
    'gorod.middleware.base.RedirectOldCityUrlsMiddleware',
    'gorod.middleware.exceptions.RequestExceptionMiddleware'
)


TEMPLATE_DIRS = (
    BASE_DIR + '/templates'
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
    # Auth
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    # Gorod
    'gorod.context_processors.base.base_params',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gorodin',
        'USER': 'gorodin',
        'PASSWORD': 'barcelona1',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMINS = (('Igor', 'igorkarbachinsky@mail.ru'))

MANAGERS = (('Manager', 'hola@gorod.io'))

EMAIL_HOST = 'smtp.fullspace.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'system@gorod.io'
EMAIL_HOST_PASSWORD = 'f999ece7'
DEFAULT_FROM_EMAIL = 'system@gorod.io'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/home/g/gorodin/beta.gorod.io/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '/home/g/gorodin/beta.gorod.io/gorod/static',
    '/home/g/gorodin/beta.gorod.io/comments/static',
    '/home/g/gorodin/beta.gorod.io/likes/static',
    '/home/g/gorodin/.venv/lib/python2.7/site-packages/django/contrib/admin/static',
    '/home/g/gorodin/.venv/lib/python2.7/site-packages/ckeditor/static',
    '/home/g/gorodin/.venv/lib/python2.7/site-packages/django_mptt_admin/static'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

CKEDITOR_UPLOAD_PATH = "/home/g/gorodin/beta.gorod.io/media/uploads/"

MEDIA_ROOT = '/home/g/gorodin/beta.gorod.io/media/'
MEDIA_URL = '/media/'
#ADMIN_MEDIA_PREFIX = '/uploads_admin/'


CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser, wordcount, elementspath",
        "forcePasteAsPlainText": True,
        "ShiftEnterMode": 'p', 
        "pasteFromWordRemoveFontStyles": True,
        "removeFormatTag": "b,big,code,del,dfn,em,font,i,ins,kbd,q,samp,small,span,strike,strong,sub,sup,tt,u,var,br",
        "ignoreEmptyParagraph": True,
        "extraPlugins": "link,confighelper",
        'toolbar': [
            ['Bold', 'Link', 'NumberedList', 'BulletedList'],
        ],
        'width' : '100%',
        'height': '200',
        'resize_enabled' : False,
        'placeholder': u'Введите текст'
    }
}

DATE_FORMAT = 'd.m.Y'

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

# Social

# Social
AUTH_USER_MODEL = 'gorod.User'
LOGIN_REDIRECT_URL = 'profile'
SOCIAL_AUTH_CREATE_USERS = True

AUTH_PROFILE_MODULE = 'gorod.User'

SOCIAL_AUTH_VK_OAUTH2_KEY = '4377733'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'BCPF9FkSOGmjnC4zujpp'
SOCIAL_AUTH_VK_APP_USER_MODE = 2
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email', 'photos']

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = '1090274560'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = 'BD30F031F1E7D779694636B0'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = 'CBAGENPBEBABABABA'

SOCIAL_AUTH_FACEBOOK_KEY = '1520443171507198'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b11c387ef1dc5eea98b999d42c9425bf'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

# Authentication
AUTHENTICATION_BACKENDS = (
    'social.backends.vk.VKOAuth2',
    'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

GOROD_ARTICLE_MAX_ADD_IN_HOUR_CNT = 3
GOROD_COMMENT_MAX_ADD_IN_HOUR_CNT = 20
GOROD_HUBQUESTION_MAX_ADD_IN_HOUR_CNT = 10
GOROD_HUBANSWER_MAX_ADD_IN_HOUR_CNT = 20
GOROD_LIKE_MAX_ADD_IN_HOUR_CNT = 200

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    # Avatar saver
    'gorod.utils.auth_pipelines.save_avatar',
)


SOCIAL_AUTH_AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS

THUMBNAIL_ALIASES = {
    '': {
        'feed_image': {'size': (265, 0)},
    },
}

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/g/gorodin/logs/beta.django.log',
            'formatter': 'simple',
        },
        'exceptions-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/g/gorodin/logs/beta.exceptions.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'exceptions': {
            'handlers': ['exceptions-file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
