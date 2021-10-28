from django.db import models


class Video(models.Model):
    link = models.URLField(verbose_name="Ссылка на видео")
    link_subtitles = models.URLField(verbose_name="Ссылка на субтитры")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
