from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("items/<int:id>", views.item_page, name="item_page"),
    path("register", views.register, name="register")
]
