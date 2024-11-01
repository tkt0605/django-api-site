# Generated by Django 4.2.16 on 2024-11-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0008_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='価格'),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='在庫数'),
        ),
    ]