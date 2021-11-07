from model_utils.models import TimeStampedModel
from django.db import models


class Base(TimeStampedModel):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=200)
    counter = models.PositiveIntegerField(verbose_name="Счетчик",
                                          default=0)

    def __str__(self):
        return f"{self.title} - кол-во: {self.counter}"

    class Meta:
        abstract = True
