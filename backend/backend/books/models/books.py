from django.db import models
from django.db.models.fields import DateTimeField

from . import Genre, Author

ROLE_AUTHOR = [
    (0, 'Escritor'),
    (1, 'Tradutor'),
    (2, 'Ilustrador'),
    (3, 'Editor')
]

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField()
    pages = models.IntegerField()
    authors = models.ManyToManyField(
        'Author',
        related_name='books',
        through='BookAuthor'
    )
    genres = models.ManyToManyField(
        'Genre',
        related_name='books',
        through='BookGenre'
    )

    def __str__(self):
        return self.name
    
    @property
    def genre_names(self):
        gnames = []
        for genre in self.genres.all():
            gnames.append(genre.name)
        return gnames

    
    @property
    def author_names(self):
        anames = []
        for author in self.authors.all():
            anames.append(author.name)
        return anames


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


class BookGenre(models.Model):
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
    )

    @property
    def namebook(self):
        return self.book.name

    @property
    def namegenre(self):
        return self.genre.name

    def __str__(self):
        return str((self.book, self.genre))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'BookGenre'
        verbose_name_plural = 'BookGenres'