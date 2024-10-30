"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eya)b9v_e$x4&=r@99f@nk&*=w@-u!ohs9xgqb^*&==xp3_2wi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'libra',
    'corsheaders',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## django-alluthのapp
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    ## django-allauth-rest
    'rest_framework',
    'rest_framework.authtoken',  # Token認証用
    'dj_rest_auth.registration',
    'dj_rest_auth',  # REST API経由の認証
    # 'mysqlclient',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.middleware.common.CommonMiddleware',
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # デフォルトの認証バックエンド
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth用バックエンド
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'libra.serializers.CustomUserDetairlsSerializer',
}



SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # 'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
}

# CORS_ORIGINS_ALLOW_ALL = True
ROOT_URLCONF = 'config.urls'
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # フロントエンドのURL
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]
# SESSION_COOKIE_SECURE = False  # ローカル開発環境の場合
# CSRF_COOKIE_SECURE = False  # ローカル開発環境の場合
CORS_ALLOW_CREDENTIALS = True  # Cookieを許可する
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "tamplates")],
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

WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = "config.asgi.application"
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',
        'USER': 'takato',
        'PASSWORD': '0605',
        'HOST': 'db',  # MySQL コンテナのホスト名（docker-compose のサービス名）
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # collectstatic で収集される場所
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'frontend/dist')
# ]
# 開発中の静的ファイルを配置する場所
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
REST_USE_JWT = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "accounts.Customuser"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = "/accounts/login"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Eメールでログイン
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
APPEND_SLASH=False
