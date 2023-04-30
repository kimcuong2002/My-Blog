from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
        Data = {'Posts': Post.objects.all().order_by("-date")}
        return render(request, "pages/home.html", Data)
def contact(request):
        return render(request, "pages/contact.html")