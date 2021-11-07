from celery.schedules import crontab
from kombu import Exchange, Queue

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "is_secure": True,
}

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_DEFAULT_QUEUE = "default"

CELERY_QUEUES = (
    Queue("low", Exchange("low"), routing_key="low"),
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("high", Exchange("high"), routing_key="high"),
)
CELERY_BEAT_SCHEDULE = {}
