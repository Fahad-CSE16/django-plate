import os
from dotenv import load_dotenv
load_dotenv()

# django vars
AUTH_USER_MODEL = 'user.User'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True
APPEND_SLASH = False
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# env
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))

REDIS_HOST = os.environ.get('REDIS_HOST')
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
# request setup
REQUEST_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 8))

# Email
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
FROM_EMAIL = os.environ.get('FROM_EMAIL')


# AWS s3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.environ.get('SECRET_ACCESS_KEY')
S3_BUCKET = os.environ.get('S3_BUCKET')

# SSL ECOMMERCE PAYMENT
SSL_STORE_ID = os.environ.get('SSL_STORE_ID')
SSL_STORE_PASSWORD = os.environ.get('SSL_STORE_PASSWORD')
SSL_BASE_URL = os.environ.get('SSL_BASE_URL')

# Frontend
FRONTEND_BASE_URL = os.environ.get('FRONTEND_BASE_URL')

# NGORK
NGORK_URL = os.environ.get('NGORK_URL')

# METABASE
METABASE_SITE_URL = os.environ.get('METABASE_SITE_URL')
METABASE_SECRET_KEY = os.environ.get('METABASE_SECRET_KEY')