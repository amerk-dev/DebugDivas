# Generated by Django 5.1.3 on 2024-11-23 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_options_alter_event_location_and_more'),
        ('users', '0005_alter_customuser_options_alter_location_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='gender',
        ),
        migrations.AddField(
            model_name='event',
            name='gender',
            field=models.BooleanField(choices=[(None, '...'), (1, 'Мужчины'), (2, 'Женщины'), (0, 'Мужчины и женщины')], default=None, verbose_name='пол'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='ended_at',
            field=models.DateTimeField(verbose_name='дата конца'),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_age',
            field=models.IntegerField(verbose_name='максимальный возраст'),
        ),
        migrations.AlterField(
            model_name='event',
            name='min_age',
            field=models.IntegerField(verbose_name='минимальный возраст'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.IntegerField(verbose_name='количество участников'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sport_type', to='users.sporttype', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='event',
            name='started_at',
            field=models.DateTimeField(verbose_name='дата начала'),
        ),
    ]
