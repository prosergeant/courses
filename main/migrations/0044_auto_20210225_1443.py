# Generated by Django 3.1.5 on 2021-02-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20210224_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(choices=[('rus', 'Русский'), ('kaz', 'Казахский'), ('eng', 'Английский'), ('mat', 'Математика')], max_length=3, verbose_name='Предмет'),
        ),
    ]
