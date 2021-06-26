from django.urls import reverse
from knox.models import AuthToken

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Account


class Pets(APITestCase):

    def test_create_new_user(self):
        """ Create a new user """
        url = reverse('auth-register')
        data = {
            'username': 'testuser',
            'password': 'kajsdkfjaksdncadsjj11342424',
            'first_name': 'Test user first name',
            'last_name': 'Test user last name',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Account.objects.all()), 1)

    def test_login_user(self):
        """ Test logging in an existing user."""
        # first create the user.
        _create_user(self)

        url = reverse('auth-login')
        data = {
            'username': 'testuser',
            'password': 'kajsdkfjaksdncadsjj11342424',
        }

        response = self.client.post(url, data, format='json')
        account = response.data.get('account')
        # 2 tokens - upon registration and login. 
        self.assertEqual(len(AuthToken.objects.all()), 2)
        self.assertEqual(account.get('first_name'), 'test-first-name')
        self.assertEqual(account.get('last_name'), 'test-last-name')


def _create_user(ref):
    """ Create a new user. """
    url = reverse('auth-register')
    data = {
        'username': 'testuser',
        'password': 'kajsdkfjaksdncadsjj11342424',
        'first_name': 'test-first-name',
        'last_name': 'test-last-name',
    }

    response = ref.client.post(url, data, format='json')
