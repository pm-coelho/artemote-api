from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    SerializerMethodField,
    ModelSerializer,
    ImageField,
)

from users.api.serializers import UserSerializer
from emotions.models import Emotion
from emotions.api.serializers import EmotionCountSerializer

from ..models import Artwork


User = get_user_model()


class ArtworkArtistSerializer(ModelSerializer):
    photo = ImageField(use_url=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "date_joined",
        )


class ArtworkSerializer(ModelSerializer):
    artist = ArtworkArtistSerializer()
    photo = ImageField(use_url=True)
    emotions = SerializerMethodField(method_name="get_emotions", read_only=True)

    class Meta:
        model = Artwork
        fields = (
            "id",
            "artist",
            "title",
            "description",
            "photo",
            "emotions",
        )

    def get_emotions(self, obj):
        qs = (
            obj.reactions.values("emotion__emotion")
            .annotate(count=Count("emotion"))
            .order_by("-count")
        )
        return EmotionCountSerializer(qs, many=True).data
