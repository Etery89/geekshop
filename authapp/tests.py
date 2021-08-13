from django.test import TestCase
from authapp.models import User
from django.test.client import Client
from django.conf import settings

# Create your tests here.


class UserManagementTestCase(TestCase):
    status_code_success = 200
    status_code_redirect = 302
    username = 'etery'
    email = 'etery@yandex.ru'
    password = 'password'

    new_user_data = {
        'username': 'natalia1',
        'email': 'natalia1@bk.ru',
        'first_name': 'Natalia',
        'last_name': 'Komarovica',
        'password1': 'geekbrains',
        'password2': 'geekbrains',
        'age': 33
    }

    def setUp(self):
        self.user = User.objects.create_superuser(
            self.username,
            email=self.email,
            password=self.password
        )
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/users/login/')
        # print(response.status_code)
        self.assertEqual(response.status_code, self.status_code_redirect)
        # self.assertFalse(response.context['user'].is_anonymous)

    def test_user_register(self):
        response = self.client.post('/users/register/', data=self.new_user_data)
        self.assertEqual(response.status_code, self.status_code_redirect)

        new_user = User.objects.get(username=self.new_user_data['username'])
        print(new_user)

        activation_url = f'{settings.DOMAIN_NAME}/users/verify/{new_user.email}/{new_user.activation_key}/'
        print(activation_url)

        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_success)

        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)
