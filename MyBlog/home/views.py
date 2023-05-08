from django.shortcuts import render
from .models import Post
from .models import Contact

# Create your views here.
def index(request):
        Data = {'Posts': Post.objects.all().order_by("-date")}
        return render(request, "pages/home.html", Data)
def contact(request):
        Data = {'Contact': Contact.objects.all()}
        return render(request, "pages/contact.html", Data)
def aboutme(request):
        return render(request, "pages/aboutme.html")
def pages(request):
        return render(request, "pages/pages.html")
def post(request, id):
        post = Post.objects.get(id = id)
        return render(request, 'pages/post.html', {'post': post})
def error(request, exception):
        return render(request, 'pages/error.html', {})