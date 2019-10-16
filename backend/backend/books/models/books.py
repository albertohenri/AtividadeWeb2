from django.db import models
from django.db.models.fields import DateTimeField

from . import Genre

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(
        'Genre',
        related_name="books",
        on_delete=models.CASCADE,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def genre_name(self):
        return self.genre.name
