from django.db import models

from decision.models import Base


class Text(Base):
    page = models.ForeignKey("decision.Page",
                             verbose_name="Страница",
                             on_delete=models.CASCADE,
                             related_name="text")
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текст"