# Generated by Django 3.1.5 on 2021-03-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_customuser_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchased',
            name='until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
