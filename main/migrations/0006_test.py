# Generated by Django 3.1.5 on 2021-01-14 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210114_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('lessons_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.lessons')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            bases=('main.lessons',),
        ),
    ]
