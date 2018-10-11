# Generated by Django 2.1.1 on 2018-10-11 09:08

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]