# Generated by Django 3.1.5 on 2022-05-27 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('prenume', models.CharField(max_length=264, null=True)),
                ('mesaj', models.TextField(max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tara', models.CharField(max_length=264, null=True)),
                ('oras', models.CharField(max_length=264, null=True)),
                ('strada', models.CharField(max_length=264, null=True)),
                ('etaj', models.FloatField(max_length=264, null=True)),
                ('desk', models.IntegerField(max_length=264, null=True)),
                ('favorit', models.ManyToManyField(related_name='favourite', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
