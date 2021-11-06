from django.db import models
from .base import Base


class Video(Base):
    link = models.URLField(verbose_name="Ссылка на видео")
    link_subtitles = models.URLField(verbose_name="Ссылка на субтитры")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f'{self.title} - {self.counter}'
