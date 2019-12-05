# Generated by Django 2.2.6 on 2019-12-04 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20191204_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Genre')),
            ],
            options={
                'verbose_name': 'BookGenre',
                'verbose_name_plural': 'BookGenres',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
