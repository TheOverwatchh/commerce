from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("items/<str:title>", views.item_page, name="item_page"),
    path("register", views.register, name="register"),
    path("items/<str:title>/making-a-bid", views.createBid, name="createBid"),
    path("comment/<str:title>", views.createComment, name="createComment"),
    path("create", views.createListing, name="createListing")
]
