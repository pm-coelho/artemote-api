from rest_framework.serializers import (
    ModelSerializer,
    ImageField,
)

from artworks.api.serializers import ArtworkSerializer

from shared.api.serializers import AddressSerializer
from events.models import Event

class EventSerializer(ModelSerializer):
    image = ImageField(use_url=True)
    artworks = ArtworkSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
            "image",
            "artworks",
            "address",
        )
