from django.db import models
from django.db.models.fields import DateField

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    founded = models.DateField()  

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name

    # @property
    # def name(self):
    #     return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    