# Generated by Django 2.1.1 on 2018-10-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20181011_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='uuid',
            new_name='id',
        ),
    ]
