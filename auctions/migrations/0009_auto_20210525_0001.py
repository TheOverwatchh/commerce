# Generated by Django 3.1.7 on 2021-05-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='auctionReferent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='creator',
        ),
        migrations.AddField(
            model_name='comment',
            name='listingid',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='UnknownUser', max_length=64),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
