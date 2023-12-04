from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from users.api.serializers import MeSerializer

User = get_user_model()


class MeViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = MeSerializer

    def list(self, request, format=None):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
