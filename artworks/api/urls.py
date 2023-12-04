from rest_framework import routers

from artworks.api.views import ArtworkViewSet

artworks_router = routers.SimpleRouter()
artworks_router.register(r"artworks", ArtworkViewSet)
