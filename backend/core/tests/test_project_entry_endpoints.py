from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestProjectEntryNoUser(APITestCase):
    # NOTE: While the payloads are invalid (missing)
    # but we still expect things to fail due to authorisation denied
    def setUp(self) -> None:
        self.list_url = reverse("project-entry-list")
        self.detail_url = reverse("project-entry-detail", kwargs={"pk": 1})

    def test_no_auth_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 401)

    def test_no_auth_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 401)

    def test_no_auth_create(self):
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 401)

    def test_no_auth_replace(self):
        response = self.client.put(self.detail_url)
        self.assertEquals(response.status_code, 401)

    def test_no_auth_update(self):
        response = self.client.patch(self.detail_url)
        self.assertEquals(response.status_code, 401)

    def test_no_auth_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEquals(response.status_code, 401)


class TestProjectEntryEndpontsAdmin(APITestCase):
    fixtures = ["users.json", "project_entries.json"]

    def setUp(self) -> None:
        UserModel = get_user_model()  # noqa
        self.user = UserModel.objects.get(username="superadmin")
        token = Token.objects.get_or_create(user=self.user)[0]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        self.list_url = reverse("project-entry-list")

    def test_get_list(self):
        response = self.client.get(self.list_url, data={"ordering": "-id"})
        self.assertEquals(response.status_code, 200)
        results = response.data.get("results")
        self.assertEquals(len(results), 10)
        self.assertEquals(results[0].get("name"), "Dummy entry 5123")

    def test_get_detail(self):
        response = self.client.get(reverse("project-entry-detail", kwargs={"pk": 10}))
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        response = self.client.post(
            self.list_url,
            data={
                "name": "Test entry 001",
                "link": "https://github.com/diomepa/",
                "rating": 1,
            },
        )
        self.assertEquals(response.status_code, 201)
        data = response.data
        self.assertEquals(data.get("name"), "Test entry 001")
        self.assertEquals(data.get("rating"), 1)

    def test_replace(self):
        response = self.client.put(
            reverse("project-entry-detail", kwargs={"pk": 10}),
            data={
                "name": "Test Entry 212",
                "link": "https://github.com/diomepa/GitKiosk",
                "rating": 5,
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data.get("name"), "Test Entry 212")

    def test_update(self):
        response = self.client.patch(
            reverse("project-entry-detail", kwargs={"pk": 10}),
            data={
                "rating": 3,
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data.get("rating"), 3)

    def test_delete(self):
        response = self.client.delete(
            reverse("project-entry-detail", kwargs={"pk": 10})
        )
        self.assertEquals(response.status_code, 204)


# TODO: Write tests checking edit/delete access denied if not owner !
