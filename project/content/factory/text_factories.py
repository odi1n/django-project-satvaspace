import factory
from faker import Faker

from ..models import Text

fake = Faker()


class TextFactories(factory.django.DjangoModelFactory):
    class Meta:
        model = Text

    title = fake.sentence()
    text = fake.text()
    counter = 0
