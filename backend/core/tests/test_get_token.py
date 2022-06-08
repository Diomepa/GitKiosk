from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse


class TestGetTokens(APITestCase):
    fixtures = ["users.json"]

    def test_users(self):
        """Sanity check for fixtures"""
        UserModel = get_user_model()  # noqa
        users = UserModel.objects.all()
        self.assertEquals(len(users), 2)

    def test_login(self):
        response = self.client.post(
            reverse("get-token"),
            data={"username": "superadmin", "password": "bananapaper"},
        )
        self.assertEquals(response.status_code, 200)
        response = self.client.post(
            reverse("get-token"),
            data={"username": "superadmin", "password": "bananapaper"},
        )
        self.assertEquals(response.status_code, 200)
