from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, tg_username, full_name, password=None, **extra_fields):
        if not tg_username:
            raise ValueError('The Telegram username must be set')
        if not full_name:
            raise ValueError('The full name must be set')
        user = self.model(tg_username=tg_username, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, tg_username, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(tg_username, full_name, password, **extra_fields)

class SportType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    tg_username = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    sport = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

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

    objects = UserManager()

    USERNAME_FIELD = 'tg_username'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name
    

class Event(models.Model):
    following_user = models.ForeignKey(User, related_name='events_as_following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='events_as_followed', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sex = models.BooleanField()  # True for male, False for female
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    seats = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self):
        return f"{self.name} (ID: {self.id})"