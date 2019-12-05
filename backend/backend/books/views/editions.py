from rest_framework import generics

from books.models import Edition
from books.serializers import EditionSerializer


class EditionList(generics.ListAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = ()