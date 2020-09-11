from django.contrib import admin
from .models import Category, BlogEntry, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogEntry)
admin.site.register(Comment)
