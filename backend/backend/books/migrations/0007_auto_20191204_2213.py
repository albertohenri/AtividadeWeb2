# Generated by Django 2.2.6 on 2019-12-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='role',
            field=models.IntegerField(choices=[(0, 'Escritor'), (1, 'Tradutor'), (2, 'Ilustrador'), (3, 'Editor')], default=0),
        ),
    ]
