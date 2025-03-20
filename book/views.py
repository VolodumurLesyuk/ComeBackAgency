from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from author.serializers import AuthorSerializer
from .models import Book, Author
from .serializers import BookSerializer

class BulkImportBooksView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=BookSerializer(many=True),
        responses={201: BookSerializer(many=True)},
        summary="Bulk import books",
        description="Imports multiple books from a JSON array",
        examples=[
            OpenApiExample(
                "Example Request",
                summary="Import multiple books",
                description="Send a list of books to import",
                value=[
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
                ],
                request_only=True,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        books_data = request.data

        if not isinstance(books_data, list):
            return Response({"error": "Invalid data format, expected a list of books."},
                            status=status.HTTP_400_BAD_REQUEST)

        errors = []
        created_books = []

        for index, book_data in enumerate(books_data):
            if not isinstance(book_data, dict):
                errors.append({f"Book {index}": "Expected an object, but got a list or invalid format."})
                continue

            title = book_data.get("title", "").strip()
            author_name = book_data.get("author", "").strip()
            published_year = book_data.get("published_year")
            genre = book_data.get("genre", "").strip()

            if not title:
                errors.append({f"Book {index}": "Title cannot be empty."})
                continue
            if not author_name:
                errors.append({f"Book {index}": "Author cannot be empty."})
                continue

            # Отримуємо або створюємо автора
            author, _ = Author.objects.get_or_create(name=author_name)

            # Перевіряємо, чи існує книга з таким же заголовком, автором і роком публікації
            book_exists = Book.objects.filter(
                title=title,
                author=author,
                published_year=published_year
            ).exists()

            if book_exists:
                errors.append({f"Book {index}": "Book with this title, author, and year already exists."})
                continue

            # Створюємо книгу без дублікатів
            book = Book.objects.create(
                title=title,
                author=author,
                published_year=published_year,
                genre=genre
            )
            created_books.append(book)

        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Books imported successfully!"}, status=status.HTTP_201_CREATED)