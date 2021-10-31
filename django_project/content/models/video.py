from django.db import models


class Video(models.Model):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=255)
    page = models.ForeignKey("decision.Page",
                             verbose_name="Страница",
                             on_delete=models.CASCADE,
                             related_name="video")
    link = models.URLField(verbose_name="Ссылка на видео")
    link_subtitles = models.URLField(verbose_name="Ссылка на субтитры")
    counter = models.IntegerField(verbose_name="Счетчик",
                                  default=0)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f'{self.title} - {self.counter}'
