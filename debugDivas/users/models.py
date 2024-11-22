from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from users.managers import CustomUserManager


class SportType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
    )
    full_name = models.CharField(max_length=255)
    tg_username = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    sport = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

