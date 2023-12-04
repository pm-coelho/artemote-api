from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from users.api.serializers import UserSerializer

from ..models import Artwork


class ArtworkSerializer(ModelSerializer):
    artist = UserSerializer()

    class Meta:
        model = Artwork
        fields = (
            "id",
            "artist",
            "title",
            "description",
        )
