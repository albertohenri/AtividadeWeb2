from django.db import models
from django.db.models.fields import DateField
# from . import Publisher, Book

class Edition(models.Model):
    price = models.FloatField()
    # review = models.TextField()
    date_published = models.DateField()
    published_by = models.OneToOneField(
        "Publisher",
        on_delete=models.CASCADE
    )
    book = models.OneToOneField(
        "Book",
        on_delete=models.CASCADE
    )

    @property
    def author_names(self):
        anames = []
        for author in self.authors.all():
            anames.append(author.name)
        return anames

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'

    def __str__(self):
        return "{}".format(self.date_published)


    