from django.contrib import admin


from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")
    search_fields = ("user",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
