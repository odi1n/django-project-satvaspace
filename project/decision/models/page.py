from django.db import models


class Page(models.Model):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=255)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страница"
        ordering = ['-id']

    def __str__(self):
        return self.title
