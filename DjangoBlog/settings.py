"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import sys
import os


def env_to_bool(env, default):
    str_val = os.environ.get(env)
    return default if str_val is None else str_val == 'True'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-07kezgx@x5dh1w^anq-1&ge3kfg^eo+un)z!f-m1cpd@78yzz1'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
# Application definition
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

INSTALLED_APPS = [
    'simpleui',
    # 'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'mdeditor',
    'haystack',
    'compressor',
    'password',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'servermanager',
    'owntracks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'blog.middleware.OnlineMiddleware'
]

ROOT_URLCONF = 'DjangoBlog.urls'

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
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'nxrobo',
        'HOST': '192.168.100.8',
        'POST': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# Automatically update searching index
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# Allow user login with username and password
AUTHENTICATION_BACKENDS = [
    'accounts.user_login_backend.EmailOrUsernameModelBackend']

STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

# bootstrap color styles
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# paginate
PAGINATE_BY = 10
# http cache timeout
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 10800,
        'LOCATION': 'unique-snowflake',
    }
}

SITE_ID = 1
BAIDU_NOTIFY_URL = os.environ.get('DJANGO_BAIDU_NOTIFY_URL') \
                   or 'http://data.zz.baidu.com/urls?site=https://www.lylinux.net&token=1uAOGrMsUm5syDGn'

# Email:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False  # 是否使用TLS安全传输协议
EMAIL_USE_SSL = True  # 是否使用SSL加密，qq企业邮箱要求使用
# SMTP地址
EMAIL_HOST = 'smtp.sina.com'
# SMTP端口
EMAIL_PORT = 465
# 自己的邮箱
EMAIL_HOST_USER = 'lzjpython@sina.com'
# 自己的邮箱授权码，非密码
EMAIL_HOST_PASSWORD = '1991630da76fdd8c'
EMAIL_SUBJECT_PREFIX = '[lzjpython的博客]'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Setting debug=false did NOT handle except email notifications
ADMINS = [('admin', os.environ.get('DJANGO_ADMIN_EMAIL') or 'admin@admin.com')]
# WX ADMIN password(Two times md5)
WXADMIN = os.environ.get(
    'DJANGO_WXADMIN_PASSWORD') or '995F03AC401D6CABABAEF756FC4D43C7'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'log_file'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'djangoblog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if os.environ.get('DJANGO_ELASTICSEARCH_HOST'):
    ELASTICSEARCH_DSL = {
        'default': {
            'hosts': os.environ.get('DJANGO_ELASTICSEARCH_HOST')
        },
    }
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'DjangoBlog.elasticsearch_backend.ElasticSearchEngine',
        },
    }
