from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from book.models import Book
from author.models import Author
from customer.models import Customer
from rest_framework_simplejwt.tokens import RefreshToken


class BookAPITest(APITestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(username='testuser', password='password123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(
            title='Harry Potter',
            author=self.author,
            published_year=1997,
            genre='Fiction'
        )

    def test_get_books_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_get_book_detail(self):
        response = self.client.get(reverse('book-detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter')

    def test_create_book(self):
        data = {
            "title": "1984",
            "author": str(self.author.uuid),
            "published_year": 1949,
            "genre": "Fiction"
        }
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {
            "title": "Harry Potter Updated",
            "author": str(self.author.uuid),
            "published_year": 1997,
            "genre": "Fiction"
        }
        response = self.client.put(reverse('book-detail', args=[self.book.pk]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter Updated")

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
