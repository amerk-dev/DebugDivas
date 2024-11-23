from django.db import models


class Gender(models.IntegerChoices):
    MALE = 1, "мужчины"
    FAMEALE = 2, "женщины"
    BOTH = 0, "мужчины, женщины"

    __empty__ = "..."


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    sport_type = models.CharField(max_length=255, verbose_name='вид спорта')
    gender = models.BooleanField(verbose_name='пол',choices=Gender.choices)
    min_age = models.IntegerField(verbose_name='минимальный возраст')
    max_age = models.IntegerField(verbose_name='максимальный возраст')
    location = models.CharField(max_length=255, verbose_name='локация')
    started_at = models.DateTimeField(verbose_name='дата начала')
    ended_at = models.DateTimeField(verbose_name='дата конца')
    seats = models.IntegerField(verbose_name='количество участников')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    
    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'
    