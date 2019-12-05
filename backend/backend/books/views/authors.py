from rest_framework import generics

from books.models import Author, BookAuthor
from books.serializers import AuthorSerializer, BookAuthorSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ()

class BookAuthorList(generics.ListAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    permission_classes = ()