from pathlib import Path
import environ
from datetime import timedelta
import os

# ======================
# PATHS
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ======================
# Usuario personalizado
# ======================
AUTH_USER_MODEL = 'usuarios.Usuario'

# ======================
# ENV
# ======================
env = environ.Env(
    DEBUG=(bool, False)
)
# ======================
# DJANGO ENV (DEL SISTEMA)
# ======================
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

# ======================
# LOAD .ENV SEGÚN ENTORNO
# ======================
if DJANGO_ENV == 'production':
    env_file = BASE_DIR / '.env.production'
else:
    env_file = BASE_DIR / '.env.development'

environ.Env.read_env(env_file)

# ======================
# SECURITY
# ======================
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

# ======================
# APPS
# ======================
INSTALLED_APPS = [
    # Django default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'drf_spectacular',
    # Cuando activas blacklist:
    #     Django guarda tokens en base de datos
    #     Puedes “bloquear” refresh tokens
    #     Permite logout real en JWT (que normalmente no existe)
    'rest_framework_simplejwt.token_blacklist', 
    'corsheaders',

    # Local apps (ejemplo)
    'apps.auditoria',
    'apps.core',
    'apps.personas',
    'apps.usuarios',
    'apps.catalogo',
    'apps.caja',
    'apps.locaciones',
    'apps.inventario',
    'apps.traslado',
    'apps.compras',
    # 'apps.products',
]

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Middleware de CORS sirve para permitir que tu frontend (React, Angular, etc.) haga peticiones a tu backend (Django) desde un dominio diferente. Esto es útil cuando tu frontend y backend están en dominios distintos.
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ======================
# CORS CONFIG
# ======================

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[ # CORS controla qué frontend puede hablar con tu backend.
    'http://localhost:3000'
])
# CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[]) SE USA EN PRODUCCIÓN.
CORS_ALLOW_CREDENTIALS = True  # permite cookies / auth

# ======================
# URL / WSGI
# ======================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# ======================
# TEMPLATES
# ======================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# ======================
# DATABASE POSTGRESQL
# ======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ======================
# INTERNATIONALIZATION
# ======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ======================
# STATIC
# ======================
STATIC_URL = 'static/'

# ======================
# DEFAULT FIELD
# ======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ======================
# DRF CONFIG
# ======================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.usuarios.authentication.jwt.CookieJWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': ( # Para generar documentación automática con drf-spectacular
        'drf_spectacular.openapi.AutoSchema'
    ),
}

# ======================
# SIMPLE JWT
# ======================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),

    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# ======================
# MEDIA
# ======================
MEDIA_ROOT = BASE_DIR / "archivos"
MEDIA_URL = "/archivos/"