from django.db import models

from users.models import Location, SportType


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport_type = models.ForeignKey(SportType, related_name='sport_type', on_delete=models.CASCADE, verbose_name='спорт')
    sex = models.BooleanField()  # True for male, False for female
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE, verbose_name='локация')
    seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    
    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'
    