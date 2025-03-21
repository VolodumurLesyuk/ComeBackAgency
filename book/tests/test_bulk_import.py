from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from customer.models import Customer
from rest_framework_simplejwt.tokens import RefreshToken
from author.models import Author


class BulkImportTest(APITestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(username='bulkuser', password='bulkpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.url = reverse('bulk_import_books')

    def test_bulk_import_valid_books(self):
        data = [
            {
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "published_year": 1937,
                "genre": "Fiction"
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "published_year": 1949,
                "genre": "Fiction"
            }
        ]
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bulk_import_with_missing_fields(self):
        data = [
            {
                "title": "",
                "author": "Some Author",
                "published_year": 2023,
                "genre": "Fiction"
            }
        ]
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
