import factory
from faker import Faker

from ..models import Page

fake = Faker()
title = factory.Sequence(lambda n: fake.sentence())


class PageFactories(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    title = title
