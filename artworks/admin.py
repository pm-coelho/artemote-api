from django.contrib import admin

from .models import Artwork


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "artist", "created_at", "updated_at")
    search_fields = ("title", "artist")
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
