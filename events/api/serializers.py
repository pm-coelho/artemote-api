from rest_framework.serializers import (
    ModelSerializer,
    ImageField,
    SerializerMethodField,
)

from artworks.api.serializers import ArtworkSerializer

from events.models import Event

class EventSerializer(ModelSerializer):
    image = ImageField(use_url=True)
    artworks = ArtworkSerializer(many=True, read_only=True)
    location = SerializerMethodField()

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
            "location",
        )

    def get_location(self, obj):
        if obj.location:
            return [obj.location.y, obj.location.x]
        return None
