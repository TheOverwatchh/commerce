from django.contrib import admin
from .models import User, Auction, Bid, Comment, WatchList, ClosedBid
# Register your models here.
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(WatchList)
admin.site.register(Comment)
admin.site.register(ClosedBid)

# superuser id: Miks password: micael123
# superuser id: Micael password: micael123