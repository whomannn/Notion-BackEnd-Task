from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from post.models import Post
from rest_framework import status

class PostAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        response = self.client.post('/posts/create/', {'title': 'Test Title', 'content': 'Test Content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get('/posts/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)
        response = self.client.get(f'/posts/detail/{post.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)
        response = self.client.put(f'/posts/update/{post.id}', {'title': 'Updated Title', 'content': 'Updated Content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)
        response = self.client.delete(f'/posts/delete/{post.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class IsAuthenticatedPermissionTest(TestCase):
    def test_create_post_anonymous(self):
        response = self.client.post('/posts/create/', {'title': 'Test Title', 'content': 'Test Content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AuthorPermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_update_post(self):
        post = Post.objects.create(title='Test Title', content='Test Content', author=User.objects.create_user(username='author', password='testpassword'))
        response = self.client.put(f'/posts/update/{post.id}', {'title': 'Updated Title', 'content': 'Updated Content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post(self):
        post = Post.objects.create(title='Test Title', content='Test Content', author=User.objects.create_user(username='author', password='testpassword'))
        response = self.client.delete(f'/posts/delete/{post.id}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
