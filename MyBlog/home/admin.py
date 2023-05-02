from django.contrib import admin
from .models import Post
from .models import Contact

# Register your models here.
# admin.site.register(kimcuong)

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_filter = ["date"]
    search_fields = ["title", "id"]

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["address", "phone", "email", "content"]
    list_filter = ["phone"]

admin.site.register(Contact, ContactAdmin)
