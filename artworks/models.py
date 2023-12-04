from django.db import models

from users.models import Profile


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    artist = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="artworks"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    photo = models.ImageField(upload_to="media/artworks/", blank=True, null=True)

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"
        default_related_name = "artworks"

    def __str__(self):
        return self.title
