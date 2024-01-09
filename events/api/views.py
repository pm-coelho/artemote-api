from rest_framework import viewsets

from events.models import Event

from events.api.serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.order_by("-created_at").all()
    serializer_class = EventSerializer
