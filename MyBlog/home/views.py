from django.shortcuts import render
from .models import Post
from .models import Contact
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .form import RegistrationForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    Data = {"Posts": Post.objects.all().order_by("-date")}
    return render(request, "pages/home.html", Data)


def contact(request):
    Data = {"Contact": Contact.objects.all()}
    return render(request, "pages/contact.html", Data)


def aboutme(request):
    return render(request, "pages/aboutme.html")


def pages(request):
    return render(request, "pages/pages.html")


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "pages/post.html", {"post": post})


def error_404(request, exception):
    context = {}
    return render(request, "pages/error.html", context)


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Post.objects.filter(title__contains=searched)
    return render(request, "pages/search.html", {"searched": searched, "keys": keys})



def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, "pages/register.html", {"form": form})
