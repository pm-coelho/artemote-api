from difflib import SequenceMatcher
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from emotions.models import Emotion, Reaction
from ..models import Artwork

from .serializers import ArtworkSerializer


class ArtworkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artwork.objects.order_by("-created_at").all()
    serializer_class = ArtworkSerializer

    @action(detail=True, methods=["POST"], url_path="emotions")
    def emotions(self, request, pk=None):
        artwork = Artwork.objects.get(pk=pk)
        emotion_name = request.data.get("emotion")

        emotion = None
        for e in Emotion.objects.all():
            ratio = SequenceMatcher(
                None, e.emotion.lower(), emotion_name.lower()
            ).ratio()
            if ratio >= 0.8:
                emotion = e
                break

        if not emotion:
            emotion = Emotion.objects.create(emotion=emotion_name)

        Reaction.objects.create(artwork=artwork, emotion=emotion)
        artwork.refresh_from_db()

        return Response(ArtworkSerializer(artwork).data)


    @action(detail=False, methods=["GET"], url_path="random")
    def random(self, request):
        artwork = Artwork.objects.order_by("?").first()
        return Response(self.get_serializer(artwork).data)
