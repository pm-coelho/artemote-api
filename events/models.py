import os
from django.db import models

from shared.models import Address
from artworks.models import Artwork


def upload_to(instance, filename):
    return os.path.join("events", str(instance.id), filename)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events"
    )

    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    artworks = models.ManyToManyField(Artwork, blank=True)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        default_related_name = "events"

    def __str__(self):
        return self.name
