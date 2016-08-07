from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()
    
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# AWS S3
AWS_ACCESS_KEY_ID=env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=env['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME=env['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_CUSTOM_DOMAIN = '%s.s3-website-eu-west-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = 's3-eu-west-1.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

try:
    from .local import *
except ImportError:
    pass
