from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from book.models import Book
from author.models import Author
from customer.models import Customer
from rest_framework_simplejwt.tokens import RefreshToken


class ExportBooksAPITestCase(APITestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            published_year=2020,
            genre='Fiction'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_export_books(self):
        url = reverse('export_books')  # переконайся, що name='export_books' у urls.py
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

        book_data = response.data[0]
        self.assertIn('title', book_data)
        self.assertIn('author_name', book_data)
        self.assertIn('published_year', book_data)
        self.assertIn('genre', book_data)

        self.assertEqual(book_data['author_name'], self.author.name)
