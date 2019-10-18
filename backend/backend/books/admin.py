from django.contrib import admin

from .models import Author, Book, BookAuthor, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Genre)