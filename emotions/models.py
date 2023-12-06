from django.db import models

from artworks.models import Artwork
from users.models import Profile


class Emotion(models.Model):
    emotion = models.CharField(max_length=100)


class Reaction(models.Model):
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        default_related_name = "reactions"
