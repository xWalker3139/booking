# Generated by Django 3.1.5 on 2022-05-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_remove_question_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
