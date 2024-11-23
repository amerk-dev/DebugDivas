from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    tg_username = models.CharField(max_length=255, unique=True, verbose_name="Telegram username")
    sport_type = models.CharField(max_length=255, null=True, verbose_name='Вид спорта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    

