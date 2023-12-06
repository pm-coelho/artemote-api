from django.contrib import admin

from .models import Emotion, Reaction


@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ("emotion",)


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ("emotion", "artwork", "author")
