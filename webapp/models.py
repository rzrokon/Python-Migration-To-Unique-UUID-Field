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

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(null=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



