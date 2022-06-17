# Generated by Django 3.1.5 on 2021-01-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_course_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='course',
            name='anons_kz',
            field=models.CharField(max_length=50, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='course',
            name='anons_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='course',
            name='direction_kz',
            field=models.CharField(choices=[('nis', 'НИШ'), ('ktl', 'КТЛ'), ('165', '165 Лицей'), ('rfm', 'РФМШ')], max_length=3, null=True, verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='course',
            name='direction_ru',
            field=models.CharField(choices=[('nis', 'НИШ'), ('ktl', 'КТЛ'), ('165', '165 Лицей'), ('rfm', 'РФМШ')], max_length=3, null=True, verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_kz',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='course',
            name='quest_kz',
            field=models.TextField(null=True, verbose_name='Текст задачи'),
        ),
        migrations.AddField(
            model_name='course',
            name='quest_ru',
            field=models.TextField(null=True, verbose_name='Текст задачи'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject_kz',
            field=models.CharField(blank=True, choices=[('rus', 'Русский'), ('kaz', 'Казахский'), ('eng', 'Английский'), ('mat', 'Математика')], max_length=3, null=True, verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject_ru',
            field=models.CharField(blank=True, choices=[('rus', 'Русский'), ('kaz', 'Казахский'), ('eng', 'Английский'), ('mat', 'Математика')], max_length=3, null=True, verbose_name='Предмет'),
        ),
    ]