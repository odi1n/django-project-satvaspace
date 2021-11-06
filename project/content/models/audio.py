from django.db import models

from .base import Base


class Audio(Base):
    link = models.URLField(verbose_name="Ссылка на аудио")
    bitrate = models.PositiveBigIntegerField(verbose_name="Битрейт",
                                             help_text="Зависит от максимального битрейта, который попытаться добавить в бд. На вскидку: 1,4 Гбит - для 1080р несжатого, как говорит вики (а это 1400000000 бит). ",
                                             default=0)
    bit_in_second = models.IntegerField(verbose_name="Бит в секунду",
                                        default=0)

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"

    def __str__(self):
        return f'{self.title} - {self.counter}'
