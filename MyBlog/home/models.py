from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(null=True)
    content = models.TextField()
    author = models.TextField(max_length=100, null=True)
    avatar = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title
class Contact(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length= 11)
    email = models.EmailField("")
    content = models.CharField(max_length=1000)