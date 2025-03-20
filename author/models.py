from django.db import models

from author.validators import validate_non_empty


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[validate_non_empty])

    def __str__(self):
        return self.name
