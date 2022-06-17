# Generated by Django 3.1.5 on 2021-02-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='video',
            new_name='video_file',
        ),
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.CharField(blank=True, help_text='Видео url', max_length=250, null=True, verbose_name='video_url'),
        ),
    ]
