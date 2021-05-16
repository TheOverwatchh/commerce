from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    creator = models.CharField(max_length=20, default="Unknown")
    title = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=128)
    current_price = models.IntegerField(blank=True)
    starting_bid = models.IntegerField()
    img_url = models.CharField(max_length=420)

    def __str__(self): 
        return self.title


class Bid(models.Model):
    creator = models.CharField(max_length=20, default="Unknown")
    price = models.IntegerField()

    def __str__(self): 
        return f"{self.creator} made a bit of ${self.price}."

class Comment(models.Model):
    creator = models.CharField(max_length=20, default="Unknown")
    comment = models.CharField(max_length=980)
    auctionReferent = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.creator}: {self.comment} in {self.auctionReferent}"