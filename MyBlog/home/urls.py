from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact),
    path("aboutme/", views.aboutme),
    path("pages/", views.pages),
    path("search/", views.search, name="search"),
    path("<int:id>/", views.post),
    path("login/", views.login),
    path("register/", views.register),
]
