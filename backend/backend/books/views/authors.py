from rest_framework import generics

from books.models import Author
from books.serializers import AuthorSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ()