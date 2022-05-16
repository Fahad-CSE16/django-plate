from searchlight.settings import DEBUG, REDIS_HOST, RABBITMQ_URL

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'searchlight.apis.renderers.DefaultRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PAGINATION_CLASS': 'base.helpers.CustomPagination',
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    )
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] + (
        'searchlight.apis.renderers.OnlyRawBrowsableAPIRenderer',
    )
if not DEBUG:
    REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'base.exceptions.custom_exception_handler'


CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_ALLOW_HEADER = [
    'username',
    'group',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOW_HEADERS = '*'
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:6379/1".format(REDIS_HOST),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
            "IGNORE_EXCEPTIONS": True,
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            "MASTER_CACHE": f"redis://{REDIS_HOST}:6379",
            "DB": 4,
        },
        "KEY_PREFIX": "searchlight",
    }
}

CACHEOPS_REDIS = "redis://{}:6379/1".format(REDIS_HOST)

CACHEOPS_DEGRADE_ON_FAILURE = True
CACHEOPS_ENABLED = True

CACHEOPS = {
    'catalog.ProductGroup': {'ops': 'all', 'timeout': 60},
    'catalog.ProductCategory': {'ops': 'all', 'timeout': 60},
    'catalog.ProductSubCategory': {'ops': 'all', 'timeout': 60},
    'catalog.ProductVariant': {'ops': 'all', 'timeout': 60},
}

# 5 minutes cache
CACHE_MIDDLEWARE_SECONDS = 300

# celery
CELERY_BROKER_URL = RABBITMQ_URL
CELERY_RESULT_BACKEND = "redis://{}:6379/".format(REDIS_HOST)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_TASK_DEFAULT_QUEUE = 'searchlight.celery'

