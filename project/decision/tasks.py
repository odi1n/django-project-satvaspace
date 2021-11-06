import django

from django_project.celery import app
from .service import increasing_counter_page

django.setup()


@app.task(queue='low')
def increasing_counter_page_task(page_id: int) -> None:
    increasing_counter_page(page_id)
