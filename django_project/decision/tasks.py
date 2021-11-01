import datetime

import django
from celery.utils.log import get_task_logger
from django.utils.timezone import make_aware

from django_project.django_project.celery import app

django.setup()

logger = get_task_logger(__name__)


def get_time() -> datetime.datetime:
    """Получить текущее время"""
    return make_aware(datetime.datetime.now())


@app.task
def test_time() -> dict:
    """Включение/выключение скидок"""
    time = get_time()
    return {"status": True, "time": time}
