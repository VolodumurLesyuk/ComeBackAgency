from rest_framework import viewsets, filters, pagination
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from book.models import Book
from book.paginations import StandardResultsSetPagination
from book.serializers import BookSerializer


@extend_schema_view(
    list=extend_schema(summary="Retrieve all books with optional filters"),
    retrieve=extend_schema(summary="Retrieve a book by ID"),
    create=extend_schema(summary="Create a new book"),
    update=extend_schema(summary="Update a book by ID"),
    destroy=extend_schema(summary="Delete a book by ID"),
)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'published_year', 'author']
    search_fields = ['title', 'author__name', 'genre']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
