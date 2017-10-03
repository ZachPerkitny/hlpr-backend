from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    alliedmodders = models.CharField(max_length=25, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    github = models.CharField(max_length=39, blank=True)
    twitter = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
