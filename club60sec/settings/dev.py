from __future__ import absolute_import, unicode_literals
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n3^*uv2eg@@*o2-z75vvi3q49)aml^8)x!coix4d146q)bwj-e'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
