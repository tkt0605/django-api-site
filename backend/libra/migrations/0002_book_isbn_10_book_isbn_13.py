# Generated by Django 4.2.16 on 2024-10-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn_10',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
