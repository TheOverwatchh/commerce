# Generated by Django 3.1.7 on 2021-05-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
