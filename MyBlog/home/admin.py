from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(kimcuong)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title', 'id']
    
admin.site.register(Post, PostAdmin)
