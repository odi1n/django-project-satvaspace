from django.db import models


class Page(models.Model):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=255)
    counter = models.IntegerField(verbose_name="Счетчик",
                                  default=0)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страница"

    def __str__(self):
        return f'{self.title} - счет: {self.counter}'
