from django.db import models
from django.db.models.fields import DateTimeField


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name