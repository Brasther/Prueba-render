"""
Django settings for aulatrack project.
Optimizado para Deploy en Render con WhiteNoise.
"""

from pathlib import Path
import os

# ============================
# BASE
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-i0zs+wbc0rtgz)&-5a!ft(=slfrh29@5n5vxg3+#m@ra9dquf1'

# En producción: siempre en False
DEBUG = False

ALLOWED_HOSTS = [
    'prueba-render-0fd9.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]

# ============================
# APPS
# ============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
]

AUTH_USER_MODEL = 'usuarios.Usuario'

# ============================
# ARCHIVOS ESTÁTICOS (CSS, JS)
# ============================

STATIC_URL = '/static/'

# Carpeta donde Django juntará todo para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Carpetas donde tienes tus archivos estáticos reales
STATICFILES_DIRS = [
    BASE_DIR / 'static',               # carpeta principal de estáticos
    BASE_DIR / 'usuarios' / 'static',  # si tienes estáticos dentro de la app usuarios
]

# WhiteNoise para servir archivos estáticos en producción
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ============================
# MIDDLEWARE (incluye WhiteNoise)
# ============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 🔥 obligatorio para Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================
# LOGIN Y REDIRECCIONES
# ============================
LOGIN_URL = 'usuarios:login'
LOGIN_REDIRECT_URL = 'usuarios:home_page'
LOGOUT_REDIRECT_URL = 'usuarios:login'


# ============================
# TEMPLATES
# ============================
ROOT_URLCONF = 'aulatrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta templates global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aulatrack.wsgi.application'


# ============================
# BASE DE DATOS
# ============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================
# PASSWORDS
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================
# IDIOMA / ZONA HORARIA
# ============================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'

USE_I18N = True
USE_TZ = True


# ============================
# DEFAULTS
# ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
