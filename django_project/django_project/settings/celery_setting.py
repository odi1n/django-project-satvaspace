from celery.schedules import crontab

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Europe/Moscow'

CELERY_BEAT_SCHEDULE = {
    "1_hours_discount_enabled": {
        "task": "decision.tasks.test_time",
        "schedule": crontab(minute=0, hour="*/1"),
    },
}

CELERY_TASK_ROUTES = {
    'decision.tasks.test_time': {'queue': 'test1', },
}

