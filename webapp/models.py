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
