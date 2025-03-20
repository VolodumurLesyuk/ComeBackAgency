from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    current_year = timezone.now().year
    if value < 1800 or value > current_year:
        raise ValidationError(f'Published year must be between 1800 and {current_year}.')