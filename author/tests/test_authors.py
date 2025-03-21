from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from customer.models import Customer
from author.models import Author


class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

        self.author_data = {"name": "J.K. Rowling"}
        self.author = Author.objects.create(**self.author_data)

    def test_list_authors(self):
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        url = reverse('author-list')
        data = {"name": "George Orwell"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_author(self):
        url = reverse('author-detail', args=[str(self.author.uuid)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_author(self):
        url = reverse('author-detail', args=[str(self.author.uuid)])
        data = {"name": "New Name"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        url = reverse('author-detail', args=[str(self.author.uuid)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
