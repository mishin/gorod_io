"""
Django settings for gorod_io project.

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

ALLOWED_HOSTS = ['.gorod.io','gorod.io','.gorod.io.fstest.ru','gorod.in.fstest.ru']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gorod',
    'ckeditor',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'gorod_io.urls'

WSGI_APPLICATION = 'gorod_io.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gorod_in',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMINS = (('Igor', 'igorkarbachinsky@mail.ru'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/home/igor/git/working_copy/gorod.in/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '/home/igor/git/working_copy/gorod.in/gorod/static',
    '/usr/local/lib/python2.7/dist-packages/django/contrib/admin/static',
    '/usr/local/lib/python2.7/dist-packages/ckeditor/static'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

CKEDITOR_UPLOAD_PATH = "uploads/"

MEDIA_ROOT = '/home/igor/git/working_copy/gorod.in/media/'
MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
    }
}
