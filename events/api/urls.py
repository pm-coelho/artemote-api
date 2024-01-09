from rest_framework import routers

from events.api.views import EventViewSet

events_router = routers.SimpleRouter()
events_router.register(r"events", EventViewSet)
