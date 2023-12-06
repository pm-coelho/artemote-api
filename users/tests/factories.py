from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker
from django.contrib.auth import get_user_model


from users.models import Profile

User = get_user_model()


class UserFactory(DjangoModelFactory):
    username = "testuser"

    class Meta:
        model = User
        django_get_or_create = ("username",)

    @classmethod
    def create_random(cls):
        return cls(username=Faker("name"))


class ProfileFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)

    class Meta:
        model = Profile
        django_get_or_create = ("user",)
