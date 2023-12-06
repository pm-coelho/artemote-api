from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField

from ..models import Profile

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        )


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "username", "first_name", "last_name", "email")


class MeSerializer(UserSerializer):
    pass
