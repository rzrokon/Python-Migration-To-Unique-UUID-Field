# Generated by Django 2.1.1 on 2018-10-11 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_author_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='uuid',
        ),
    ]
