"""
Django settings for djangoTemp project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n5l1t$a3rvj_w*sh-c#p&(gatng5bbn+1@7llvlr-i%%03m2^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  #session
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mdjango',  #链接app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #session文件配置
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',   #跨站请求,安全性
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoTemp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "Template"),],    #添加网页路径
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

WSGI_APPLICATION = 'djangoTemp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {   #数据库配置
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    '''
    __init__中:
        import pymysql
        pymysql.install_as_MySQLdb()
    'sql':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名',
        'HOST': '数据库ip',
        'POST': '数据库端口',
        'USER': '用户名',
        'PASSWORD': '密码',
    }
    '''
}


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

LANGUAGE_CODE = 'zh-hans'     #切换Django语言界面

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/' #静态文件路径(前端用), 保证前端和后端分离

STATICFILES_DIRS = (    #静态文件路径(后端用)
    os.path.join(BASE_DIR, "Statics"),
)

#session配置文件

#session默认保存在数据库里

#文件
SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎
SESSION_FILE_PATH = None  # 缓存文件路径, 如果为None, 则使用tempfile模块获取一个临时地址tempfile.gettempdir()

#缓存 redis memcache
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'        # 引擎
#SESSION_CACHE_ALIAS= 'default'  #使用的缓存别名(CACHE={'default':{}}), 默认内存缓存

#缓存+数据库 读(先读内存, 内存没有读取数据库, 存到内存). 写(先写内存再写数据库)
#SESSION_ENGINE='django.contrib.sessions.backends.cached_db'        # 引擎

#浏览器(相当于没有用session, 又把敏感信息保存到客户端了)
#SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎

SESSION_COOKIE_NAME="sessionID"  # Session的cookie保存在浏览器上时的key, 即:sessionID＝随机字符串
SESSION_COOKIE_PATH="/"     # Session的cookie保存的路径
SESSION_COOKIE_DOMAIN = None    # Session的cookie保存的域名
SESSION_COOKIE_SECURE = False   # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True      # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 600000     # Session的cookie失效日期（2周） 默认1209600秒
SESSION_EXPIRE_AT_BROWSER_CLOSE =True   # 是否关闭浏览器使得Session过期

SESSION_SAVE_EVERY_REQUEST = True
#如果你设置了session的过期时间为30分钟:
# 是False时, 30分钟过后session准时失效
# 是True时, 在30分钟期间有请求服务端, 就不会过期