from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    current_price = models.IntegerField()
    starting_bid = models.IntegerField()
    img_url = models.CharField(max_length=420)

    def __str__(self): 
        return self.title