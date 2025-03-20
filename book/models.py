from django.db import models

from author.models import Author
from author.validators import validate_non_empty
from book.validators import validate_year
import uuid

GENRE_CHOICES = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science', 'Science'),
    ('History', 'History'),
]

class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, validators=[validate_non_empty])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=False, blank=False)
    published_year = models.IntegerField(validators=[validate_year])
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.published_year}) - {self.genre}"
