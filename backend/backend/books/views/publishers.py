from rest_framework import generics

from books.models import Publisher
from books.serializers import PublisherSerializer


class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = ()