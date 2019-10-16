from rest_framework import generics

from books.models import Genre
from books.serializers import GenreSerializer


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = ()