# Generated by Django 3.1.7 on 2021-05-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210506_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='current_price',
            field=models.IntegerField(blank=True),
        ),
    ]
