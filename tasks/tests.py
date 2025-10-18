from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from tasks.models import Task
from rest_framework_simplejwt.tokens import RefreshToken


class TaskAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

        # Create a sample task
        self.task = Task.objects.create(
            title="Initial Task",
            description="Initial description",
            completed=False
        )

    def test_list_tasks(self):
        """GET /api/tasks/ should return all tasks"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_task(self):
        """GET /api/tasks/{id}/ should return one task"""
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_create_task_requires_auth(self):
        """POST without auth should fail"""
        data = {"title": "New Task", "description": "desc"}
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_with_auth(self):
        """POST with JWT token should create task"""
        data = {"title": "New Task", "description": "desc"}
        response = self.client.post('/api/tasks/', data, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        """PUT /api/tasks/{id}/ should update task"""
        data = {"title": "Updated", "description": "updated", "completed": True}
        response = self.client.put(f'/api/tasks/{self.task.id}/', data, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
        self.assertEqual(self.task.title, "Updated")

    def test_delete_task(self):
        """DELETE /api/tasks/{id}/ should delete task"""
        response = self.client.delete(f'/api/tasks/{self.task.id}/', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
