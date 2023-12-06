from rest_framework.serializers import ModelSerializer, IntegerField, CharField


from emotions.models import Emotion


class EmotionCountSerializer(ModelSerializer):
    emotion = CharField(source="emotion__emotion")
    count = IntegerField(default=-1)

    class Meta:
        model = Emotion
        fields = ("emotion", "count")
        ordering = ["-count"]


class EmotionSerializer(ModelSerializer):
    class Meta:
        model = Emotion
        fields = "emotion"
