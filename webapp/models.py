# HOW TO URL : https://docs.djangoproject.com/en/2.1/howto/writing-migrations/#migrations-that-add-unique-fields

from django.db import migrations, models
import uuid

class Books(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published = models.DateField(null=False)

    def __str__(self):
        return '%s by %s' % (self.name, self.author)


class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    rating = models.CharField(max_length=4)
    release = models.DateField(null=False)

    def __str__(self):
        return '%s - %s' % (self.name, self.year)

