from django.test import TestCase
import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apiapp.serializers import PersonSerializer
from apiapp.models import Person
# Create your tests here.

BASE_DIR = 'http://127.0.0.1:8000/api-auth'

class AddTestCase(APITestCase):
    
    def test_add1(self):
        data = {"name": "Jean", "age": 28}
        response = self.client.post(f'{BASE_DIR}/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_add2(self):
        data = {"name": "Chinaswamy muthu swamy venu Gopal Iyer", "age": 43}
        response = self.client.post(f'{BASE_DIR}/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_add3(self):
        data = {"name": "Dwayne", "age": 33}
        response = self.client.post(f'{BASE_DIR}/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_add4(self):
        data = {"name": "Binod", "age": 56}
        response = self.client.post(f'{BASE_DIR}/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ViewPersonTestCase(APITestCase):
    
    def test_view1(self):
        response = self.client.get(f'{BASE_DIR}/view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    