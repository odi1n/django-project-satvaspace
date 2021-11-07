from django.db.models import F

from content.models import Content


def increasing_counter_page(page_id: int) -> None:
    """Увеличение счетчика данных на странице"""
    content_models = Content.get_content_class_models()
    for model in content_models:
        model.objects.filter(contents__page_id=page_id).distinct("pk").update(counter=F("counter") + 1)
