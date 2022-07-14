from app.conf.environ import env
from app.conf.timezone import TIME_ZONE

BROKER_URL = CELERY_BROKER_URL = env(
    'CELERY_BACKEND',
    cast=str,
    default='redis://redis:6379/0',
)

CELERY_ALWAYS_EAGER = env(
    'CELERY_ALWAYS_EAGER',
    cast=bool,
    default=env('DEBUG'),
)
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = False
