from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from account.views import RegisterUserView
class RegisterUserViewTest(TestCase):
    def test_register_user_view(self):
        factory = APIRequestFactory()
        request_data = {'username': 'testuser', 'password': 'testpassword', 'password1' : 'testpassword'}
        request = factory.post('/register/', data=request_data, format='json')
        view = RegisterUserView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(username='testuser').exists(), True)
    def test_register_erorrs_user_view(self):
        factory = APIRequestFactory()
        request_data = {'username': 'testuser', 'password': 'testpassword111', 'password1' : 'testpassword222'}
        request = factory.post('/register/', data=request_data, format='json')
        view = RegisterUserView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

