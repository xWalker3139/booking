# Generated by Django 3.1.5 on 2022-05-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20220528_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
