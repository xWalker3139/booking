# Generated by Django 3.1.5 on 2022-05-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0023_places_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(choices=[('Da', 'Da'), ('Nu', 'Nu')], max_length=264, null=True)),
                ('option2', models.CharField(choices=[('Da', 'Da'), ('Nu', 'Nu')], max_length=264, null=True)),
                ('option3', models.CharField(choices=[('Da', 'Da'), ('Nu', 'Nu')], max_length=264, null=True)),
                ('option4', models.CharField(choices=[('Da', 'Da'), ('Nu', 'Nu')], max_length=264, null=True)),
            ],
        ),
    ]
