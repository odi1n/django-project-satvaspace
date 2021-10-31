from django.db import models


class Text(models.Model):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=255)
    page = models.ForeignKey("decision.Page",
                             verbose_name="Страница",
                             on_delete=models.CASCADE,
                             related_name="text")
    text = models.TextField(verbose_name="Текст")
    counter = models.IntegerField(verbose_name="Счетчик",
                                  default=0)

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текст"

    def __str__(self):
        return f'{self.title} - {self.counter}'
