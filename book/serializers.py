from rest_framework import serializers

from author.serializers import AuthorSerializer
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'