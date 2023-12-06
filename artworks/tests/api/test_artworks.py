from django.urls import reverse
from rest_framework.test import APITestCase


from emotions.models import Emotion, Reaction
from artworks.tests.factories import ArtworkFactory
from emotions.tests.factories import EmotionFactory, ReactionFactory


class ArtworkAPIListTestCase(APITestCase):
    def setUp(self):
        self.artwork = ArtworkFactory()
        self.url = reverse("artwork-list")

    def test_list_artworks_calculates_emotions(self):
        [emotion_1, emotion_2] = EmotionFactory.create_batch(2)
        ReactionFactory(artwork=self.artwork, emotion=emotion_1)
        ReactionFactory(artwork=self.artwork, emotion=emotion_1)
        ReactionFactory(artwork=self.artwork, emotion=emotion_2)

        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["count"], 1)

        results = res.json()["results"]

        self.assertEqual(results[0]["emotions"][0]["emotion"], emotion_1.emotion)
        self.assertEqual(results[0]["emotions"][0]["count"], 2)
        self.assertEqual(results[0]["emotions"][1]["emotion"], emotion_2.emotion)
        self.assertEqual(results[0]["emotions"][1]["count"], 1)


class ArtworkEmotionsAPICreateTestCase(APITestCase):
    def setUp(self):
        self.artwork = ArtworkFactory()
        self.url = reverse("artwork-emotions", kwargs={"pk": self.artwork.id})

    def test_create_emotion(self):
        emotion = EmotionFactory(emotion="happy")
        ReactionFactory(artwork=self.artwork, emotion=emotion)
        data = {"emotion": "sad"}

        self.assertEqual(Emotion.objects.count(), 1)

        res = self.client.post(self.url, data=data)

        self.assertEqual(res.status_code, 200)
        res_json = res.json()
        self.assertEqual(res_json["emotions"][0]["emotion"], "happy")
        self.assertEqual(res_json["emotions"][0]["count"], 1)
        self.assertEqual(res_json["emotions"][1]["emotion"], "sad")
        self.assertEqual(res_json["emotions"][1]["count"], 1)

        self.assertEqual(Emotion.objects.count(), 2)
        created_emotion = Emotion.objects.get(emotion="sad")
        self.assertEqual(created_emotion.emotion, data["emotion"])

    def test_create_associates_existing_emotion(self):
        emotion = EmotionFactory(emotion="happy")
        ReactionFactory(artwork=self.artwork, emotion=emotion)
        data = {"emotion": "happy"}

        self.assertEqual(Emotion.objects.count(), 1)

        res = self.client.post(self.url, data=data)

        self.assertEqual(res.status_code, 200)
        res_json = res.json()
        self.assertEqual(res_json["emotions"][0]["emotion"], "happy")
        self.assertEqual(res_json["emotions"][0]["count"], 2)

        self.assertEqual(Emotion.objects.count(), 1)
        reactions = Reaction.objects.filter(emotion=emotion, artwork=self.artwork)
        self.assertEqual(reactions.count(), 2)

    def test_create_considers_90_pct_accuracy(self):
        emotion = EmotionFactory(emotion="happy")
        ReactionFactory(artwork=self.artwork, emotion=emotion)
        data = {"emotion": "happi"}

        self.assertEqual(Emotion.objects.count(), 1)

        res = self.client.post(self.url, data=data)

        self.assertEqual(res.status_code, 200)
        res_json = res.json()
        self.assertEqual(res_json["emotions"][0]["emotion"], "happy")
        self.assertEqual(res_json["emotions"][0]["count"], 2)

        self.assertEqual(Emotion.objects.count(), 1)
        reactions = Reaction.objects.filter(emotion=emotion, artwork=self.artwork)
        self.assertEqual(reactions.count(), 2)
