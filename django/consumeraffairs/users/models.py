from django.db import models
from django.contrib.auth.models import AbstractUser


class Reviewer(AbstractUser):
    # reviewer metadata
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True)
