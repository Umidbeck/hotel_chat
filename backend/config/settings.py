import os
from pathlib import Path
from decouple import config

# Asosiy loyiha papkasi
BASE_DIR = Path(__file__).resolve().parent.parent

# Maxfiy kalit va debug rejimi
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me')
DEBUG = config('DEBUG', default=True, cast=bool)

# Ruxsat etilgan hostlar (server IP, domen va localhost)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# O'rnatilgan ilovalar (daphne va Channels zarur)
INSTALLED_APPS = [
    'daphne',  # ASGI server, Channels bilan ishlash uchun
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'channels',
    'corsheaders',

    'chat',
    'qr_auth',
    'qrcode',
]

# Middleware lar ketma-ketligi
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS uchun
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Shablon sozlamalari
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Zarur bo'lsa loyihaga shablon papka yo'li qo'shilsin
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

# URL konfiguratsiyasi
ROOT_URLCONF = 'config.urls'

# ASGI va WSGI ilovalari (Channels uchun ASGI kerak)
WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Ma'lumotlar bazasi - PostgreSQL, muhit o'zgaruvchilar orqali sozlanadi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST', default='localhost'),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

# Channels Redis konfiguratsiyasi
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # Redis konteyner nomi yoki IP manzil va port
            "hosts": [(config('REDIS_HOST', default='redis'), int(config('REDIS_PORT', default=6379)))],
        },
    },
}

# CORS sozlamalari
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default="http://localhost:3000,http://127.0.0.1:3000"
).split(',')

CORS_ALLOW_CREDENTIALS = True

# Xalqaro sozlamalar
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = True

# Statik fayllar URLi
STATIC_URL = '/static/'

# Django-ning avtomatik yaratiladigan primary key turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Maxsus foydalanuvchi modeli (agar ishlatilsa)
AUTH_USER_MODEL = 'qr_auth.User'
