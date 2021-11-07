from django.core.exceptions import ValidationError
from django.db import models

from . import Base, Audio, Text, Video


class Content(models.Model):
    custom_id = models.PositiveIntegerField(default=0,
                                            blank=False,
                                            null=False)
    page = models.ForeignKey("decision.Page",
                             verbose_name="Страница",
                             on_delete=models.CASCADE,
                             related_name="contents")
    content_audio = models.ForeignKey(Audio,
                                      verbose_name="Аудио",
                                      related_name="contents",
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE)
    content_text = models.ForeignKey(Text,
                                     verbose_name="Текст",
                                     related_name="contents",
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE)
    content_video = models.ForeignKey(Video,
                                      verbose_name="Видео",
                                      related_name="contents",
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контент"
        ordering = ['custom_id']

    def __str__(self):
        return f'Контент - {self.id}'


    @classmethod
    def get_content_fields(cls) -> list:
        return [x for x in cls._meta.fields if x.name.startswith("content_")]

    @classmethod
    def get_content_class_models(cls) -> list[Base]:
        """Список моделей данных"""
        return [x.related_model for x in cls.get_content_fields()]

    def clean_content(self):
        content_fields = [x.name for x in self.get_content_fields()]
        content_type = None
        errors = {}
        for field in content_fields:
            value = getattr(self, field)
            if not value:
                continue

            if content_type:
                errors[field] = ValidationError("Выберите только один вид контента")
            else:
                content_type = field

        if not content_type:
            errors = {x: ValidationError("Выберите хотя бы один вид контента.") for x in content_fields}

        if errors:
            raise ValidationError(errors)

    def full_clean(self, exclude=None, validate_unique: bool = True):
        self.clean_content()
        return super().full_clean(exclude, validate_unique)
