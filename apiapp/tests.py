from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status

from apiapp.models import Dog
from apiapp.serializers import DogSerializer

import json


class AddDogTestCase(RequestsClient):
    def __init__(self):
        self.client = RequestsClient()
        self.client = APITestCase()
    
    def test_add_dog(self):
        data = {
            "name": "fluffly",
            "description": "likes to play",
            "image": "image location",
            "location": "kalyan west"
        }
        response = self.client.post("api-auth/add/", data, format='')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)