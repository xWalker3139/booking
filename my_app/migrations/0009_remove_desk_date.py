# Generated by Django 3.1.5 on 2022-05-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_desk_imagine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desk',
            name='date',
        ),
    ]
