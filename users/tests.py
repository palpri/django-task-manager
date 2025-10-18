from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class UserAuthTests(APITestCase):
    def test_user_registration(self):
        """POST /api/auth/register/ should create new user"""
        data = {"username": "newuser", "password": "newpass123"}
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_login(self):
        """POST /api/auth/login/ should return JWT tokens"""
        user = User.objects.create_user(username='loginuser', password='loginpass')
        data = {"username": "loginuser", "password": "loginpass"}
        response = self.client.post('/api/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
