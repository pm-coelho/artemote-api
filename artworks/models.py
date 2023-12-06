import os
from django.db import models

from users.models import Profile


def upload_to(instance, filename):
    return os.path.join("artworks", instance.artist.user.username, filename)


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    artist = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="artworks"
    )

    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"
        default_related_name = "artworks"
