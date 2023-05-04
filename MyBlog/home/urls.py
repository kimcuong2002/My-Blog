from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('aboutme/', views.aboutme),
    path('pages/', views.pages),
    path('<int:id>/', views.post),
]
