from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    name = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100)
