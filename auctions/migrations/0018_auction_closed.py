# Generated by Django 3.1.7 on 2021-06-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210610_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='closed',
            field=models.CharField(default='False', max_length=20),
        ),
    ]
