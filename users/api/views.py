from django.contrib.auth import get_user_model
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response
from django.db.models import Count

from users.api.serializers import MeSerializer, ArtistSerializer

User = get_user_model()


class MeViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = MeSerializer

    def list(self, request, format=None):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ArtistViewSet(ReadOnlyModelViewSet):
    queryset = (
        User.objects
        .annotate(num_artworks=Count('profile__artworks'))
        .filter(num_artworks__gt=0)
        .all()
    )
    serializer_class = ArtistSerializer
    lookup_field = "username"
