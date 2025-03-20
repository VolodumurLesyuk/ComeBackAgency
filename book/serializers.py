from rest_framework import serializers

from author.models import Author
from author.serializers import AuthorSerializer
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)
    author_name = serializers.SerializerMethodField(read_only=True)  # Додаємо ім'я автора у відповідь

    class Meta:
        model = Book
        fields = '__all__'

    def get_author_name(self, obj):
        """Отримуємо ім'я автора для відображення у відповіді"""
        return obj.author.name if obj.author else None

    def validate_title(self, value):
        """Перевіряємо, що title не є пустим"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_author(self, value):
        """Перевіряємо, що author не є пустим"""
        if not value:
            raise serializers.ValidationError("Author cannot be empty.")
        return value
