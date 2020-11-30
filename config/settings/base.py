"""
Django settings for urbandata project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import sys
from os import getenv
from os.path import abspath, dirname, join
from typing import List


def root(*dirs: str):
    """
    Joins the `BASE_DIR` with any specified directory name(s).

    :param dirs: directories to be concatanted with the project root path.
    """
    base_dir = join(dirname(__file__), "..", "..")

    return abspath(join(base_dir, *dirs))


# GENERAL
# ------------------------------------------------------------------------------
# Project base directory.
BASE_DIR = root()

# Django apps directory.
APPS_DIR = root("urbandata")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", "override this key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS: List[str] = []

# https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# To support URL's not ending in a slash.
APPEND_SLASH = False


# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# https://docs.djangoproject.com/en/2.2/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-tz
USE_TZ = True


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "urbandata.assets.apps.AssetsConfig",
]
# https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("DB_DATABASE", "urbandata"),
        "USER": getenv("DB_USER", "postgres"),
        "PASSWORD": getenv("DB_PASS", "invalid-pass"),
        "HOST": getenv("DB_HOST", "localhost"),
        "PORT": getenv("DB_PORT", "5432"),
    },
}


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 9},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#logging
# See https://docs.djangoproject.com/en/2.2/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "format": "%(asctime)s [%(levelname)-8s] %(name)-15s %(module)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "custom",
            "level": "DEBUG",
        }
    },
    "loggers": {
        "urbandata": {
            "handlers": ["console"],
            "level": getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        }
    },
}


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-root
STATIC_ROOT = root("staticfiles")
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [root("static")]


# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_ROOT = root("media")
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-url
MEDIA_URL = "/media/"


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(APPS_DIR, "templates")],
        "APP_DIRS": False,
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

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Django REST framework
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}
