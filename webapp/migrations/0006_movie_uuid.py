# Generated by Django 2.1.1 on 2018-10-11 10:54

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    Movies = apps.get_model('webapp', 'Movie')
    for mov in Movies.objects.all():
        mov.uuid = uuid.uuid4()
        mov.save()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True)
        )
    ]