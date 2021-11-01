from django.db import models

from .base import Base


class Page(Base):
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страница"