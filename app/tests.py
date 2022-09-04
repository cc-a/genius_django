from django.test import TestCase

from .models import AccessRecord, UserInfo


class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_info(self):
        response = self.client.get("/info")
        self.assertEqual(response.status_code, 200)

    def test_info_post(self):
        data = dict(age=12, size=3)
        response = self.client.post("/info", data=data)
        self.assertEqual(response.status_code, 200)
        user_info = UserInfo.objects.get()
        self.assertEqual(user_info.age, data["age"])
        self.assertEqual(user_info.size, data["size"])

    def test_access(self):
        response = self.client.get("/access")
        self.assertEqual(response.status_code, 200)
        AccessRecord.objects.get()

    def test_stats(self):
        UserInfo.objects.create(age=1, size=1)
        response = self.client.get("/stats")
        self.assertEqual((1, 1, 1), response.context["age_stats"])
        self.assertEqual((1, 1, 1), response.context["size_stats"])
