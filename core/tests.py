from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

class Pets(APITestCase):

    def test_create_pet(self):
        """ Create a pet instance """
        # TODO create authentication for tests. 
        url = ('http://127.0.0.1:8000/pets/')
        data = {
            'pet': {
                'name': 'Molly',
                "breed": "Lab",
                "bio": "Enjoys food."
            }
        }

        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.pop('name'), 'Molly')
