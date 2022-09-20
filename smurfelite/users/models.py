from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("Email Address"), unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.username
