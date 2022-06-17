# Generated by Django 3.1.5 on 2021-03-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_quizdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizdata',
            name='answer',
        ),
        migrations.AlterField(
            model_name='quizdata',
            name='option_one',
            field=models.CharField(max_length=255, verbose_name='Правильный вариант'),
        ),
    ]
