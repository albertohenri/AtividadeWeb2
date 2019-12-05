from django.contrib import admin

from .models import Author, Book, BookAuthor, Genre, BookGenre, Edition, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(BookGenre)
admin.site.register(Genre)
admin.site.register(Edition)
admin.site.register(Publisher)