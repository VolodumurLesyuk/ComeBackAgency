# Generated by Django 5.1.7 on 2025-03-20 13:14

import author.validators
import book.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('a0c37f21-74d6-490e-81f5-0792bab27d31'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, validators=[author.validators.validate_non_empty])),
                ('published_year', models.IntegerField(validators=[book.validators.validate_year])),
                ('genre', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Science', 'Science'), ('History', 'History')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='author.author')),
            ],
        ),
    ]
