from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker

from users.tests.factories import ProfileFactory
from artworks.tests.factories import ArtworkFactory
from emotions.models import Emotion, Reaction


class EmotionFactory(DjangoModelFactory):
    emotion = Faker("word")

    class Meta:
        model = Emotion
        django_get_or_create = ["emotion"]


class ReactionFactory(DjangoModelFactory):
    emotion = SubFactory(EmotionFactory)
    artwork = SubFactory(ArtworkFactory)
    author = SubFactory(ProfileFactory)

    class Meta:
        model = Reaction
