# Generated by Django 2.2.6 on 2019-10-10 13:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20191010_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]