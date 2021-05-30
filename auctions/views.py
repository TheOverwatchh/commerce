from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import random
import string
from .models import User, Auction, Bid, Comment, WatchList


def index(request):
    all_auctions = Auction.objects.all()
    return render(request, "auctions/index.html", {
        "auctions": all_auctions
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if username == '': 
            return render(request, "auctions/index.html", {
                "message": "You need to fill the required camps."
            })
        elif password == '':
            return render(request, "auctions/index.html", {
                "message": "You need to fill the required camps"
            })    

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/index.html", {
                "message": "Invalid username and/or password."
            })
    # else:
    #     return render(request, "auctions/login.html")

def seeWatchList(request, username):
            w = WatchList.objects.filter(username=username)
            items = []
            for i in w:
                items.append(Auction.objects.filter(title=i.listing))
                w = WatchList.objects.filter(username=request.user.username)
            return render(request,"auctions/watch-list.html",{
                "items":items,
            })
     
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html", {
        "logged": False
        })

def item_page(request, title):
     item = Auction.objects.get(title=title)
     comments = Comment.objects.filter(listing=title)
     w = WatchList.objects.filter(listing=title)
     if w:
        return render(request, "auctions/item_page.html", {
            "i": item,
            "comments":comments,
            "inWatch": True
        })
     else: 
          return render(request, "auctions/item_page.html", {
            "i": item,
            "comments":comments,
            "inWatch": False
        })   

def createBid(request, title):
    # pegar o item de acordo com o titulo
    item = Auction.objects.get(title=title)
    # alterar o current_price do item
    item.current_price = request.POST["bid"]
    item.save()
    # retornar para a página do item, com o current price alterado
    return render(request, "auctions/item_page.html", {
        "i":item
    })

def createComment(request, title):
    if request.method == "POST":
        c = Comment()
        c.comment = request.POST.get('content')
        c.creator = request.POST["creator"]
        c.listing = title
        c.save()
        return redirect('item_page',title=title)
    else :
        return redirect('index')
        
def addWatchList(request, title):
    item = Auction.objects.get(title=title)
    comments = Comment.objects.filter(listing=title)
    userName = request.user.username
    randomic = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(24)])

    # if len(WatchList.objects.get(listing=title, username=request.user.username)) >= 1:   
    #     return render(request, "auctions/item_page.html", {
    #         "i": item,
    #         "comments":comments,
    #         "inWatch": False
    #     })     
    # else:    
    w = WatchList(randomic, userName, title)
    w.save()
    return render(request, "auctions/item_page.html", {
            "i": item,
            "comments":comments,
            "inWatch": True
        })

def removeWatchList(request, title):
    item = Auction.objects.get(title=title)
    comments = Comment.objects.filter(listing=title)
    w = WatchList.objects.get(listing=title, username=request.user.username)
    w.delete()
    return render(request, "auctions/item_page.html", {
        "i": item,
        "comments":comments,
        "inWatch": False
    })    
    
def createListing(request):

    if request.method == "POST":
        all_listings = Auction.objects.all()
        creator = request.POST["creator"]
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        img_url = request.POST["img_url"]
        # listings = Auction.objects.all()
        # listingsLength = len(listings)
        #  Attempt to create 
        listing = Auction(creator, title, description, starting_bid ,starting_bid, img_url)
        listing.save()
        return render(request, "auctions/index.html", {
            "auctions": all_listings
        })
       

    else: 
        return render(request, "auctions/createlisting.html")