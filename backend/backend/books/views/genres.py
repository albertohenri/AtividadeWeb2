from rest_framework import generics

from books.models import Genre, BookGenre
from books.serializers import GenreSerializer, BookGenreSerializer


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = ()


class BookGenreList(generics.ListAPIView):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permission_classes = ()