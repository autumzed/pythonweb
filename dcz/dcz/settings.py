"""
Django settings for dcz project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import configparser
# 读取配置文件
config = configparser.ConfigParser()
config.read("config.ini")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(vc@$k$@th(6+(whlh^5ecpv*iech5v^++t50x#6x=cf+$as&9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get("system", "DEBUG")
# DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dc',
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

ROOT_URLCONF = 'dcz.urls'
# 若关闭网页，删除session
SESSION_EXPIRE_AT_BROWSER_CLOSE = config.get("session", "SESSION_EXPIRE_AT_BROWSER_CLOSE")
# session 有效时间 60秒*30 = 30分钟
SESSION_COOKIE_AGE = int(config.get("session", "SESSION_COOKIE_AGE"))
# SESSION_COOKIE_AGE = 60
APPEND_SLASH = config.get("session", "APPEND_SLASH")
# APPEND_SLASH = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/dcz/templates",],
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

WSGI_APPLICATION = 'dcz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.get("database", "db_name"),
        'USER': config.get("database", "user"),
        'PASSWORD': config.get("database", "password"),
        'HOST': config.get("database", "host"),
        'PORT': config.get("database", "port"),
    }
}
"""
        'NAME': config.get("database", "db_name"),
        'USER': config.get("database", "user"),
        'PASSWORD': config.get("database", "password"),
        'HOST': config.get("database", "host"),
        'PORT': config.get("database", "port"),
        'NAME': 'dc',
        'USER': 'root',
        'PASSWORD': '1234qwer',
        'HOST': '127.0.0.1',
        'PORT': '3306',
"""

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'CCT'
TIME_ZONE = 'Asia/BeiJing'
# Asia/Shanghai

USE_I18N = True

USE_L10N = True
# 时区切换为本地时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS =(
    os.path.join(BASE_DIR,"static"),
)

STATIC_ROOT='/var/dcz/staticfiles'
MEDIA_ROOT='/var/dcz/media'
MEDIA_URL='/media/'
