from django.db import models
import uuid

from author.validators import validate_non_empty


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, validators=[validate_non_empty])

    def __str__(self):
        return self.name
