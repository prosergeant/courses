# Generated by Django 3.1.5 on 2021-01-30 08:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_course_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]