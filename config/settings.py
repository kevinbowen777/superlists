"""Settings for superlists TDD project"""
from pathlib import Path

# from environs import Env

# env = Env()
# env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "SECRET_KEY"
# SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True
# DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["165.232.131.115", "localhost"]
CSRF_TRUSTED_ORIGINS = ["http://165.232.131.115"]

# Application definition
INSTALLED_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "lists",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path.joinpath(BASE_DIR, "../database/db.sqlite3"),
    }
}
"""
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL", default="postgres://postgres@db/postgres"
    )
}
"""
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa:E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa:E501
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Vancouver"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR.joinpath("../static"))
# STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
