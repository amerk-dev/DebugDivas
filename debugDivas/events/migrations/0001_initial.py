# Generated by Django 5.1.3 on 2024-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.BooleanField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField()),
                ('seats', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
