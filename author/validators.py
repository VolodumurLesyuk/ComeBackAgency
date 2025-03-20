from django.core.exceptions import ValidationError


def validate_non_empty(value):
    if not value.strip():
        raise ValidationError('This field cannot be empty.')