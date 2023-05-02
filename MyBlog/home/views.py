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