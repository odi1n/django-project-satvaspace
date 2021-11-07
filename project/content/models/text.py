from django.db import models

from .base import Base


class Text(Base):
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текст"