from rest_framework import serializers
from books.models import (Book, Genre, Author)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'name', 'authors', 'description',
            'genre', 'genre_name', 'created'
        )

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name', 'last_name')