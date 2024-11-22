from django.db import models

from users.models import CustomUser, Location, SportType


class Event(models.Model):
    following_user = models.ForeignKey(CustomUser, related_name='events_as_following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(CustomUser, related_name='events_as_followed', on_delete=models.CASCADE)
    sport_type = models.ForeignKey(SportType, related_name='sport_type', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sex = models.BooleanField()  # True for male, False for female
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    