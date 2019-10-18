from django.db import models
from django.db.models.fields import DateTimeField

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)    

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'