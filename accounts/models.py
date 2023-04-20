from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# creating the custom user model with a custom field.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
