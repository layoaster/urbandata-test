"""
Django settings for local/dev environments.
"""
from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True

ALLOWED_HOSTS = ["*"]

# django-extensions
# ------------------------------------------------------------------------------
SHELL_PLUS = "ipython"
