# Generated by Django 3.2.1 on 2022-08-13 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "first_name",
                    models.CharField(max_length=200, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=200, verbose_name="Last Name"),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]