# Generated by Django 3.1.5 on 2021-02-04 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_remove_course_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024, verbose_name='Вопрос')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Questcourse', to='main.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Tests',
        ),
        migrations.AddField(
            model_name='qanda',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quest'),
        ),
        migrations.AddField(
            model_name='qanda',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quest'),
        ),
    ]