from rest_framework import serializers
from .models import Book, Genre

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'name', 'author', 'description', 'genre', 'created'
        )

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')