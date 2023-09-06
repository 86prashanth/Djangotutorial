"""
Django settings for Django project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)wqrvsg+o&!2p88d*0gt-@ha#*+*#=^3ow*gqphqh3@itn-0%t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'Basic_Application',
    'core',
    'multiapplication',
    'dynamicapp',
    'templates_app',
    'formapp',
    'crudapp',
    'messageframe',
    'usercreationform',
    'pagecounter.apps.PagecounterConfig',
    'querysetapi',
    'model_inheritance',
    'manager_app',
    'model_relationship',
    'class_based_view',
    'TemplateView',
    'Redirectview',
    'generic_listview',
    'genericdetailview',
    'formview',
    'modelformmixin',
    'pagination',
    'Captchapp',
    'captcha',
    'rest_framework',
    'routersViewsets',
    'payment_Gateway',
    'createCardbutton',
    
    # for this you have to install django rest framework
]
# auth user


# razor pay..
RAZOR_KEY_ID='razor_pay key id'
RAZOR_KEY_SECRET='razor_pay secret key'

# twilio account
TWILIO_ACCOUNT_SID = 'twilio account sid'
TWILIO_AUTH_TOKEN = 'twilio auth token'
TWILIO_PHONE_NUMBER = 'twilio account specify number'

# middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', # caches
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript', # livereload
    # 'core.middleware.my_middleware' ,#middleware,
    'core.middleware.Brothermiddleware',#middleware
    'core.middleware.Mothermiddleware', #middleware
    'core.middleware.Fathermiddleware', # middleware
    'core.middleware.Myprocessmiddleware', # middleware
    'core.middleware.MyExceptionmiddleware', # middleware
    'core.middleware.MyTemplatemiddleware', #middleware 
    'core.middleware.UnderConstructionMiddleware',#middlewware
]

ROOT_URLCONF = 'Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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


WSGI_APPLICATION = 'Django.wsgi.application'
# caches 


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djapyngoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False
# file based session
SESSION_ENGINE='django.contrib.sessions.backends.file'
SESSION_FILE_PATH=os.path.join(BASE_DIR,'session')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
MEDIA_URL='images/'
APPEND_SLASH=False
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE=120
# SESSION_COOKIE_NAME='sessionname'
# SESSION_COOKIE_PATH='/home'
# SESSION_EXPIRE_AT_BROWSER_CLOSE=True
# SESSION_FILE_PATH=''
# SESSION_SAVE_EVERY_REQUEST='' 

CACHE_MIDDLEWARE_SECONDS=20
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'pagecounter_cache',
    }
}

# LOGIN_REDIRECT_URL='/accounts/dashboard/'

# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


 # email settings 
 
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=True 
EMAIL_PORT=587
EMAIL_HOST_USER='prashanthambala6@gmail.com'
EMAIL_HOST_PASSWORD='xiogygmypxwgsvlx'

