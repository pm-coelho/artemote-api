from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "start_date",
        "end_date",
        "created_at",
        "updated_at",
    )
    list_filter = ("start_date", "end_date", "created_at", "updated_at")
    search_fields = ("name", "location", "description")
