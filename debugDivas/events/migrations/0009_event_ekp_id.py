# Generated by Django 5.1.3 on 2024-11-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_event_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ekp_id',
            field=models.CharField(default=0, max_length=25, verbose_name='№ ЕКП'),
            preserve_default=False,
        ),
    ]
