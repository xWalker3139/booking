# Generated by Django 3.1.5 on 2022-05-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_desk_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birouri',
            name='date',
        ),
        migrations.RemoveField(
            model_name='birouri',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='birouri',
            name='user3',
        ),
        migrations.AddField(
            model_name='birouri',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='birouri',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]