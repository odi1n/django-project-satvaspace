import factory
from faker import Faker

from ..models import Video

fake = Faker()


class VideoFactories(factory.django.DjangoModelFactory):
    class Meta:
        model = Video

    title = fake.sentence()
    link = fake.url(),
    link_subtitles = fake.url()
    counter = 0
