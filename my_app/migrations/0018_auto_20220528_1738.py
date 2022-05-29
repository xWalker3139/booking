# Generated by Django 3.1.5 on 2022-05-28 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0017_places_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='user',
        ),
        migrations.AddField(
            model_name='places',
            name='user',
            field=models.ManyToManyField(related_name='favorit', to=settings.AUTH_USER_MODEL),
        ),
    ]
