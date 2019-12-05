# Generated by Django 2.2.6 on 2019-12-05 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20191205_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('founded', models.DateField()),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date_published', models.DateField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('published_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher')),
            ],
            options={
                'verbose_name': 'Edition',
                'verbose_name_plural': 'Editions',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
