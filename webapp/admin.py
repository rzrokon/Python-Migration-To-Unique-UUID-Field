from django.contrib import admin
from . models import Books, Movie, Category, Author, Post

admin.site.register(Books)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
