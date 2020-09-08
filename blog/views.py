from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogEntry

# Create your views here.
class BlogList(ListView):
    model = BlogEntry
    template_name = 'blog/blog_list.html'
