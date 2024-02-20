from rest_framework import routers

from users.api.views import ArtistViewSet

users_router = routers.SimpleRouter()
users_router.register(r"artists", ArtistViewSet)
