# Generated by Django 4.2.16 on 2024-10-31 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0002_book_isbn_10_book_isbn_13'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
    ]