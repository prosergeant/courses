# Generated by Django 3.1.5 on 2021-01-15 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210115_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('someInt1', models.IntegerField(verbose_name='some int 1')),
                ('someInt2', models.IntegerField(verbose_name='some int 2')),
                ('someInt3', models.IntegerField(verbose_name='some int 3')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Propertytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='EEG',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.commoninfo')),
                ('number', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('main.commoninfo',),
        ),
        migrations.DeleteModel(
            name='qqq',
        ),
        migrations.AddField(
            model_name='property',
            name='propertytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.propertytype'),
        ),
        migrations.AddField(
            model_name='property',
            name='EEG',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.eeg'),
        ),
    ]