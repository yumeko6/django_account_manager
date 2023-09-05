from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, verbose_name='Username')
    email = models.EmailField(verbose_name='Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
