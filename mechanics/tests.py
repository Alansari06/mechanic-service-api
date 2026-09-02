from django.test import TestCase
from rest_framework.test import APIClient

from .models import Mechanic


class MechanicAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        Mechanic.objects.create(
            name="Test Mechanic",
            phone="9876543210",
            location="Noida",
            rating=4.5,
            is_open=True,
            services="Oil Change"
        )

    def test_get_mechanics(self):
        response = self.client.get('/api/mechanics/')

        self.assertEqual(response.status_code, 200)

    def test_get_mechanic_by_id(self):
        response = self.client.get('/api/mechanics/1/')

        self.assertEqual(response.status_code, 200)