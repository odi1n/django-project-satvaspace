import factory
from faker import Faker
from faker.generator import random

from decision.factory.page_factories import PageFactories
from .audio_factories import AudioFactories
from .text_factories import TextFactories
from .video_factories import VideoFactories
from ..models import Content

fake = Faker()


class ContentFactories(factory.django.DjangoModelFactory):
    class Meta:
        model = Content

    page = factory.SubFactory(PageFactories)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)

        content_model = random.randint(1, 3)
        if content_model == 1:
            kwargs["content_audio"] = AudioFactories()
        elif content_model == 2:
            kwargs["content_text"] = TextFactories()
        elif content_model == 3:
            kwargs["content_video"] = VideoFactories()

        return manager.create(*args, **kwargs)
