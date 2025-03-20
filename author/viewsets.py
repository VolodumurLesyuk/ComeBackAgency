from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from author.models import Author
from author.serializers import AuthorSerializer


@extend_schema_view(
    list=extend_schema(summary="Retrieve all authors"),
    retrieve=extend_schema(summary="Retrieve an author by ID"),
    create=extend_schema(summary="Create a new author"),
    update=extend_schema(summary="Update an author"),
    destroy=extend_schema(summary="Delete an author"),
)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

