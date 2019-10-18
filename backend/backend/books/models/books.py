from django.db import models
from django.db.models.fields import DateTimeField

from . import Genre, Author

ROLE_AUTHOR = [
    (0, 'Writer'),
    (1, 'Translator'),
    (2, 'Illustrator'),
    (3, 'Editor')
]

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(
        'Genre',
        related_name="books",
        on_delete=models.CASCADE,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(
        'Author',
        related_name='books',
        through='BookAuthor'
    )

    def __str__(self):
        return self.name
    
    @property
    def genre_name(self):
        return self.genre.name


class BookAuthor(models.Model):
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
    )
    role = models.IntegerField(choices=ROLE_AUTHOR, default=0)

    def __str__(self):
        return str((self.book, self.author))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'BookAuthor'
        verbose_name_plural = 'BookAuthors'