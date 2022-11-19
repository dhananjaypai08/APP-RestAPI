from rest_framework.test import APITestCase
from rest_framework import status

from apiapp.models import Dog
from apiapp.serializers import DogSerializer

from django.http.request import QueryDict

class AddDogTestCase(APITestCase):
    
    def test_add_dog(self):
        data = {
            "name": "fluffly",
            "description": "likes to play",
            "image": "image location",
            "location": "kalyan west"
        }
        response = self.client.post("api-auth/add/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)