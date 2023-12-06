from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker

from users.tests.factories import ProfileFactory
from artworks.models import Artwork


class ArtworkFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=2)
    description = Faker("text")
    artist = SubFactory(ProfileFactory)

    class Meta:
        model = Artwork
        django_get_or_create = ["title"]
