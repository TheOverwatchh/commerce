# Generated by Django 3.1.7 on 2021-05-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210514_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='creator',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]
