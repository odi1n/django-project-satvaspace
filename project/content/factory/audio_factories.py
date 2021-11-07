import factory
from faker import Faker
from faker.generator import random

from ..models import Audio

fake = Faker()


class AudioFactories(factory.django.DjangoModelFactory):
    class Meta:
        model = Audio

    title = fake.sentence()
    bitrate = random.randint(10000, 100000)
    bit_in_second = random.randint(1000, 1000000)
    link = fake.url()
    counter = 0
