from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ImageField

from ..models import Profile
from artworks.models import Artwork

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
        fields = ("id", "username", "first_name", "last_name", "email", "photo")


class MeSerializer(UserSerializer):
    pass


class ArtistArtworkSerializer(ModelSerializer):
    photo = ImageField(use_url=True)

    class Meta:
        model = Artwork
        fields = (
            "id",
            "title",
            "description",
            "photo",
        )

class ArtistSerializer(UserSerializer):
    artworks = ArtistArtworkSerializer(many=True, read_only=True, source="profile.artworks")
    photo = ImageField(use_url=True, source="profile.photo")

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "artworks",
            "photo",
            "date_joined",
        )
