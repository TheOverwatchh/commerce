# Generated by Django 3.1.7 on 2021-05-27 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='user',
            new_name='username',
        ),
    ]
