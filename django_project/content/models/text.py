from django.db import models


class Text(models.Model):
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текст"
