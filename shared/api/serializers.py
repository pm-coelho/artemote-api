from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shared.models import Address

class AddressSerializer(ModelSerializer):
    location = SerializerMethodField()

    class Meta:
        model = Address
        fields = (
            "city",
            "city_district",
            "county",
            "state",
            "country",
            "postcode",
            "road",
            "house_number",
            "suburb",
            "location",
        )

    def get_location(self, obj):
        if obj and obj.location:
            return [obj.location.y, obj.location.x]
        return None
