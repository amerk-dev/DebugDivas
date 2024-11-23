from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class SportType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'спорт'
        verbose_name_plural = 'спорт'


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'локации'
        verbose_name_plural = 'локации'



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    tg_username = models.CharField(max_length=255, unique=True, verbose_name="Telegram username")
    sport_type = models.ForeignKey(
        SportType,
        on_delete=models.SET_NULL,
        null=True, 
        verbose_name='Вид спорта'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    

