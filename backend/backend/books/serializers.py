from django.db import transaction
from rest_framework import serializers
from books.models import (Book, Genre, Author, BookAuthor, BookGenre, Edition, Publisher)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'name', 'authors', 'description',
            'genres', 'genre_names', 'author_names', 'created', 'pages'
        )
    
    @transaction.atomic
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        if "authors" in self.initial_data:
            authors = self.initial_data.get("authors")
            for author in authors:
                author_id = author.get("author")
                role = author.get("role")
                author_instance = Author.objects.get(pk=author_id)
                BookAuthor(book=book, author=author_instance, role=role).save()
        book.save()
        return book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name', 'last_name')


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'price', 'date_published', 'published_by', 'book')


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ('id', 'book', 'author', 'role')


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ('id', 'book', 'genre', 'namebook', 'namegenre')

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'location', 'description', 'founded')