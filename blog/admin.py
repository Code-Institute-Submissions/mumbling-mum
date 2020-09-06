from django.contrib import admin
from .models import Category, BlogEntry, Comments, Likes

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogEntry)
admin.site.register(Comments)
admin.site.register(Likes)